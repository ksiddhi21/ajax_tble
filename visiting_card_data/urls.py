from django.contrib import admin
from django.urls import path,re_path
from django.urls import reverse_lazy
from visiting_card_data import views

app_name = 'visiting_card_data'

urlpatterns = [
# Add new Visiting Card Company Data
path('visitingcard', views.visiting_card_data_list, name='visiting_card_data_list'),

path('send_welcome_sms/<int:pk>', views.send_welcome_sms, name='send_welcome_sms'),

path('sms_master', views.sms_master, name='sms_master'),

path('email_master', views.email_master, name='email_master'),

path('sms/create/', views.SMSCreateView.as_view(), name='create_sms'),
path('sms/update/<int:pk>', views.SMSUpdateView.as_view(), name='update_sms'),
path('sms/read/<int:pk>', views.SMSReadView.as_view(), name='read_sms'),
path('sms/delete/<int:pk>', views.SMSDeleteView.as_view(), name='delete_sms'),

path('email/create/', views.EmailCreateView.as_view(), name='create_email'),
path('email/update/<int:pk>', views.EmailUpdateView.as_view(), name='update_email'),
path('email/read/<int:pk>', views.EmailReadView.as_view(), name='read_email'),
path('email/delete/<int:pk>', views.EmailDeleteView.as_view(), name='delete_email'),

path('all_data',views.CrudView.as_view(),name='all_data'),

path('all_data/crud_ajax_delete',views.DeleteCrudUser.as_view(),name='crud_ajax_delete'),

path('all_data/crud_ajax_create',views.CreateCrudUser.as_view(),name='crud_ajax_create'),

path('all_data/crud_ajax_update',views.UpdateCrudUser.as_view(),name='crud_ajax_update'),

]