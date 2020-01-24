from visiting_card_data.models import VisitingCardCompanyData,EmailMaster,SMSMaster
from bootstrap_modal_forms.forms import BSModalForm

class SMSForm(BSModalForm):
    class Meta:
        model = SMSMaster
        fields = ['SMS_Subject', 'SMS_Message' ]

class EmailForm(BSModalForm):
    class Meta:
        model = EmailMaster
        fields = ['Email_Subject', 'Email_Message' ]