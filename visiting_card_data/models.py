from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
class VisitingCardCompanyData(models.Model):
    HIGH=1
    MEDIUM=2
    LOW=3
    NOT_DECIDED=4
    IMPORTANCE_LEVEL=(('HIGH',HIGH),('MEDIUM',MEDIUM),('LOW',LOW))
    visitingcardcompanydata_company_name = models.CharField(max_length=920)
    visitingcardcompanydata_agent_name = models.CharField(max_length=920)
    visitingcardcompanydata_agent_designation = models.CharField(max_length=920,blank=True)
    visitingcardcompanydata_company_address1 = models.TextField(max_length=920)
    visitingcardcompanydata_company_address2 = models.TextField(max_length=920,blank=True)
    visitingcardcompanydata_tel_number1 = models.CharField(max_length=920)
    visitingcardcompanydata_tel_number2 = models.CharField(max_length=920,blank=True)
    visitingcardcompanydata_mobile_number1 = models.CharField(max_length=920)
    visitingcardcompanydata_mobile_number2 = models.CharField(max_length=920,blank=True)
    visitingcardcompanydata_email_id1 = models.CharField(max_length=920)
    visitingcardcompanydata_email_id2 = models.CharField(max_length=920,blank=True)
    visitingcardcompanydata_company_website = models.CharField(max_length=920,blank=True)
    visitingcardcompanydata_date_of_entry = models.DateTimeField(default=timezone.now)
    visitingcardcompanydata_convert_to_client = models.BooleanField(default=False)
    visitingcardcompanydata_importance = models.CharField(choices=IMPORTANCE_LEVEL,max_length=920,default=NOT_DECIDED)
    visitingcardcompanydata_welcome_sms_sent=models.BooleanField(default=False)
    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = "VisitingCardCompanyData"
        verbose_name = "Compony Data"

class SMSMaster(models.Model):
    SMS_Subject = models.CharField(max_length=100)
    SMS_Message = models.CharField(max_length=150)
    SMS_Date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = "SMS Template"
        verbose_name = "SMS Templates"

class EmailMaster(models.Model):
    Email_Subject = models.CharField(max_length=900)
    Email_Message = models.CharField(max_length=1600)
    Email_Date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = "Email Template"
        verbose_name = "Email Templates"