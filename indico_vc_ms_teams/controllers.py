from __future__ import unicode_literals

import flask
from indico.web.rh import RH

from indico_vc_ms_teams.config import *
from indico_vc_ms_teams.msgraph import msgraph
from indico.web.flask.util import url_for
from indico.modules.events import Event
from indico.modules.vc.models.vc_rooms import VCRoomEventAssociation
from sqlalchemy.orm.attributes import flag_modified

import json
import uuid

def format_date(date):
    return 'T'.join(str(date).split(' '))

class RHAuthorized(RH):
    def _process(self):
        MSGRAPH = msgraph()
        json_state = json.loads(flask.request.args['state'])
        event = Event.get(int(json_state['event_id']))
        room_event_assocs = VCRoomEventAssociation.find_for_event(event).all()
        event_vc_rooms = [event_vc_room for event_vc_room in room_event_assocs if event_vc_room.vc_room.name == json_state['vc_room_name']]

        if len(event_vc_rooms) <= 0:
            raise Exception('no videoconference room found!')

        vc_room = event_vc_rooms[0].vc_room

        if str(vc_room.data['state']) != str(flask.request.args['state']):
            raise Exception('state returned to redirect URL does not match!')

        authorized_response = MSGRAPH.authorized_response()
        flask.session['access_token'] = authorized_response['access_token']

        endpoint = 'me/onlineMeetings'
        headers = {'SdkVersion': 'Indico-Teams-Plugin',
                'x-client-SKU': 'Indico-Teams-Plugin',
                'client-request-id': str(uuid.uuid4()),
                'return-client-request-id': 'true'}
        
        meeting = {"endDateTime": format_date(event.end_dt),
                "startDateTime": format_date(event.start_dt),
                "subject": str(vc_room.name)}        
        
        response = MSGRAPH.post(endpoint, headers=headers, data=json.dumps(meeting), format='json', content_type='application/json')
        graphdata = response.data

        vc_room.data['authorized'] = True
        vc_room.data['join_URL'] = graphdata['joinWebUrl']
        vc_room.data['online_meeting_id'] = graphdata['id']
        flag_modified(vc_room, 'data')

        redirect_url = url_for('vc.manage_vc_rooms', confId=json_state['event_id'])
        return flask.redirect(redirect_url)
