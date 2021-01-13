# This file is part of the Indico plugins.
# Copyright (C) 2002 - 2020 CERN
#
# The Indico plugins are free software; you can redistribute
# them and/or modify them under the terms of the MIT License;
# see the LICENSE file for more details.

from __future__ import unicode_literals

from flask import session
from sqlalchemy.orm.attributes import flag_modified

from indico.core.plugins import IndicoPlugin, IndicoPluginBlueprint, url_for_plugin
from indico.modules.vc import VCPluginMixin

from indico_vc_ms_teams.blueprint import blueprint
from indico_vc_ms_teams.msgraph import msgraph
from indico_vc_ms_teams.forms import VCRoomForm, VCRoomAttachForm
from indico_vc_ms_teams.config import *

import uuid
import json


class MsTeamsPlugin(VCPluginMixin, IndicoPlugin):
    """Microsoft Teams

    Microsoft Teams videoconferencing plugin
    """
    configurable = True
    vc_room_form = VCRoomForm
    vc_room_attach_form = VCRoomAttachForm
    friendly_name = "Microsoft Teams"

    @property
    def logo_url(self):
        return url_for_plugin(self.name + '.static', filename='images/msteams_logo.svg')

    @property
    def icon_url(self):
        return url_for_plugin(self.name + '.static', filename='images/msteams_logo.svg')

    @property
    def default_settings(self):
        return dict(VCPluginMixin.default_settings, **{
            'auth_URL': None,
            'state': None,
            'authorized': False,
            'online_meeting_id': ''
        })

    def get_blueprints(self):
        return blueprint

    def create_room(self, vc_room, event):
        self.create_authorization_url(vc_room, event)
    
    def delete_room(self, vc_room, event):
        pass

    def update_room(self, vc_room, event):
        if not vc_room.data['authorized']:
            self.create_authorization_url(vc_room, event)

    def refresh_room(self, vc_room, event):
        pass

    def create_authorization_url(self, vc_room, event):
        MSGRAPH = msgraph()
        state = json.dumps({ 'random_id': str(uuid.uuid4()), 'event_id': event.id, 'vc_room_name': vc_room.name })
        authorize = MSGRAPH.authorize(callback=REDIRECT_URI, state=state)
        authorization_url = authorize.location
        vc_room.data['state'] = state
        vc_room.data['auth_URL'] = authorization_url
        vc_room.data['authorized'] = False
        flag_modified(vc_room, 'data')
