from django.views import generic
from django.shortcuts import render, HttpResponseRedirect
import urllib.request
import urllib.parse
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from visiting_card_data.models import VisitingCardCompanyData,EmailMaster,SMSMaster
from visiting_card_data.send_sms import sendSMS
from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)
from visiting_card_data.forms import SMSForm,EmailForm
from django.views.generic import TemplateView, View, DeleteView
from django.core import serializers
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='/user_login')
def visiting_card_data_list(request):
    all_visiting_cards_data = VisitingCardCompanyData.objects.all()
    sms_master = SMSMaster.objects.all()
    email_master = EmailMaster.objects.all()
    user_role = request.user.user_role
    data = {'all_visiting_cards_data':all_visiting_cards_data,'user_role':user_role,'sms_master':sms_master,'email_master':email_master}
    return render(request,'visiting_card_data/visiting_card_data_list.html',data)

#Convert visitors to Client page
@login_required(login_url='/user_login')
def send_welcome_sms(request,pk):
    user_role = request.user.user_role
    visitor_list = VisitingCardCompanyData.objects.all()
    visitor = VisitingCardCompanyData.objects.get(pk=pk)
    client_telephone=visitor.visitingcardcompanydata_tel_number1
    resp =  sendSMS('G6LdbDUMrL4-yUFYrUvHH5a0xhLBJVOLN1NGj0gxws', '91'+client_telephone,'TXTLCL', 'Thank you for visiting us. To Know more About Volshebny Tours visit http://www.volshebnyholidays.com')
    print(resp)
    visitor.visitingcardcompanydata_welcome_sms_sent = True
    visitor.save()
    return HttpResponseRedirect(reverse('visiting_card_data:visiting_card_data_list'))

#SMS Master
@login_required(login_url='/user_login')
def sms_master(request):
    sms_master = SMSMaster.objects.all()
    user_role = request.user.user_role
    data = {'sms_master':sms_master,'user_role':user_role}
    return render(request,'visiting_card_data/sms_master_django.html',data)

@login_required(login_url='/user_login')
def email_master(request):
    email_master = EmailMaster.objects.all()
    user_role = request.user.user_role
    data = {'email_master':email_master,'user_role':user_role}
    return render(request,'visiting_card_data/email_master_django.html',data)


# Create
class SMSCreateView(BSModalCreateView):
    model = SMSMaster
    template_name = 'visiting_card_data/sms_curd_templates/create_sms.html'
    form_class = SMSForm
    success_message = 'Success: SMS was created.'
    success_url = reverse_lazy('visiting_card_data:sms_master')

# Update
class SMSUpdateView(BSModalUpdateView):
    model = SMSMaster
    template_name = 'visiting_card_data/sms_curd_templates/update_sms.html'
    form_class = SMSForm
    success_message = 'Success: SMS was updated.'
    success_url = reverse_lazy('visiting_card_data:sms_master')

# Read
class SMSReadView(BSModalReadView):
    model = SMSMaster
    template_name = 'visiting_card_data/sms_curd_templates/read_sms.html'

# Delete
class SMSDeleteView(BSModalDeleteView):
    model = SMSMaster
    template_name = 'visiting_card_data/sms_curd_templates/delete_sms.html'
    success_message = 'Success: SMS was deleted.'
    success_url = reverse_lazy('visiting_card_data:sms_master')

# Create
class EmailCreateView(BSModalCreateView):
    model = EmailMaster
    template_name = 'visiting_card_data/email_curd_templates/create_email.html'
    form_class = EmailForm
    success_message = 'Success: SMS was created.'
    success_url = reverse_lazy('visiting_card_data:email_master')

# Update
class EmailUpdateView(BSModalUpdateView):
    model = EmailMaster
    template_name = 'visiting_card_data/email_curd_templates/update_email.html'
    form_class = EmailForm
    success_message = 'Success: SMS was updated.'
    success_url = reverse_lazy('visiting_card_data:email_master')

# Read
class EmailReadView(BSModalReadView):
    model = EmailMaster
    template_name = 'visiting_card_data/email_curd_templates/email_email.html'

# Delete
class EmailDeleteView(BSModalDeleteView):
    model = EmailMaster
    template_name = 'visiting_card_data/email_curd_templates/delete_email.html'
    success_message = 'Success: SMS was deleted.'
    success_url = reverse_lazy('visiting_card_data:email_master')

class CrudView(TemplateView):
    template_name = 'visiting_card_data/all_data.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_visiting_cards_data'] = VisitingCardCompanyData.objects.all()
        return context    

class DeleteCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        VisitingCardCompanyData.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

class CreateCrudUser(View):
    def  get(self, request):
        cname1 = request.GET.get('cname', None)
        aname1 = request.GET.get('aname', None)
        designation1 = request.GET.get('designation', None)
        mobile_no21 = request.GET.get('mobile_no2', None)
        mobile_no11 = request.GET.get('mobile_no1', None)
        email_id11 = request.GET.get('email_id1', None)
        email_id21 = request.GET.get('email_id2', None)

        obj = VisitingCardCompanyData.objects.create(
            visitingcardcompanydata_company_name = cname1,
            visitingcardcompanydata_agent_name = aname1,
            visitingcardcompanydata_agent_designation = designation1,
            visitingcardcompanydata_mobile_number1=mobile_no21,
            visitingcardcompanydata_mobile_number2=mobile_no11,
            visitingcardcompanydata_email_id1=email_id11,
            visitingcardcompanydata_email_id2 =email_id21
        )

        user = {'id':obj.id,'visitingcardcompanydata_company_name':obj.visitingcardcompanydata_company_name,'visitingcardcompanydata_agent_name':obj.visitingcardcompanydata_agent_name,'visitingcardcompanydata_agent_designation':obj.visitingcardcompanydata_agent_designation,'visitingcardcompanydata_mobile_number1':obj.visitingcardcompanydata_mobile_number1,'visitingcardcompanydata_mobile_number2':obj.visitingcardcompanydata_mobile_number2,'visitingcardcompanydata_email_id1':obj.visitingcardcompanydata_email_id1,'visitingcardcompanydata_email_id2':obj.visitingcardcompanydata_email_id2}

        data = {
            'visiting_card': user
        }
        return JsonResponse(data)

class UpdateCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        cname1 = request.GET.get('visitingcardcompanydata_company_name', None)
        aname1 = request.GET.get('visitingcardcompanydata_agent_name', None)
        designation1 = request.GET.get('visitingcardcompanydata_agent_designation', None)
        mobile_no11 = request.GET.get('visitingcardcompanydata_mobile_number1', None)
        mobile_no21 = request.GET.get('visitingcardcompanydata_mobile_number2', None)
        email_id11 = request.GET.get('visitingcardcompanydata_email_id1', None)
        email_id21 = request.GET.get('visitingcardcompanydata_email_id2', None)

        obj = VisitingCardCompanyData.objects.get(id=id1)
        obj.visitingcardcompanydata_company_name = cname1
        obj.visitingcardcompanydata_agent_name = aname1
        obj.visitingcardcompanydata_agent_designation = designation1
        obj.visitingcardcompanydata_mobile_number1 = mobile_no11
        obj.visitingcardcompanydata_mobile_number2 = mobile_no21
        obj.visitingcardcompanydata_email_id1 = email_id11
        obj.visitingcardcompanydata_email_id2 = email_id21
        obj.save()

        user = {'id':obj.id,'visitingcardcompanydata_company_name':obj.visitingcardcompanydata_company_name,'visitingcardcompanydata_agent_name':obj.visitingcardcompanydata_agent_name,'visitingcardcompanydata_agent_designation':obj.visitingcardcompanydata_agent_designation,'visitingcardcompanydata_mobile_number1':obj.visitingcardcompanydata_mobile_number1,'visitingcardcompanydata_mobile_number2':obj.visitingcardcompanydata_mobile_number2,'visitingcardcompanydata_email_id1':obj.visitingcardcompanydata_email_id1,'visitingcardcompanydata_email_id2':obj.visitingcardcompanydata_email_id2}

        data = {
            'visiting_card': user
        }
        return JsonResponse(data)