from __future__ import unicode_literals

from indico.core.plugins import IndicoPluginBlueprint
from indico_vc_ms_teams.controllers import RHAuthorized

blueprint = IndicoPluginBlueprint('vc_ms_teams', 'indico_vc_ms_teams')
blueprint.add_url_rule('/vc_ms_teams_authorized', 'vc_ms_teams_authorized', RHAuthorized)
