from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from visiting_card_data.models import VisitingCardCompanyData, SMSMaster, EmailMaster
# Register your models here.
class VisitingCardCompanyDataAdmin(ImportExportModelAdmin):
    list_display = [
        "pk",
        "visitingcardcompanydata_company_name",
        "visitingcardcompanydata_agent_name",
        "visitingcardcompanydata_agent_designation",
        "visitingcardcompanydata_company_address1",
        "visitingcardcompanydata_company_address2",
        "visitingcardcompanydata_tel_number1",
        "visitingcardcompanydata_tel_number2",
        "visitingcardcompanydata_mobile_number1",
        "visitingcardcompanydata_mobile_number2",
        "visitingcardcompanydata_email_id1",
        "visitingcardcompanydata_email_id2",
        "visitingcardcompanydata_company_website",
        "visitingcardcompanydata_importance",
        "visitingcardcompanydata_welcome_sms_sent"
    ]

class SMSMasterAdmin(ImportExportModelAdmin):
    list_display = [
        "pk",
        "SMS_Subject",
        "SMS_Message",
    ]

class EmailMasterAdmin(ImportExportModelAdmin):
    list_display = [
        "pk",
        "Email_Subject",
        "Email_Message",
    ]

admin.site.register(VisitingCardCompanyData,VisitingCardCompanyDataAdmin)
admin.site.register(SMSMaster,SMSMasterAdmin)
admin.site.register(EmailMaster,EmailMasterAdmin)