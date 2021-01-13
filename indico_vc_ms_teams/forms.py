from wtforms.fields.core import StringField, DateTimeField, BooleanField
from indico.modules.vc.forms import VCRoomAttachFormBase, VCRoomFormBase
from indico.web.forms.widgets import SwitchWidget
from indico.web.forms.fields import IndicoDateTimeField

class VCRoomForm(VCRoomFormBase):
    pass

class VCRoomAttachForm(VCRoomAttachFormBase):
    pass
