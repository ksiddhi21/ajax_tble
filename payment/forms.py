from django import forms
from payment.models import Groupdescription, AirTicketsQuatation, VisaCostQuatation, HotelQuatation, RestaurantQuatation, EntrancesQuatation, SapSanQuatation, Client, Vendor, Service, CustomUser,Guide,Transport,AllServices,VisitingCardAgencyData,VisitingCardCompanyData,Chefservice
from bootstrap_modal_forms.forms import BSModalForm

class GroupdescriptionForm(forms.ModelForm):
    class Meta:
        model= Groupdescription
        fields= ('groupdescription_vtrefNo',
        'groupdescription_client_Name',
        'groupdescription_number_of_passengers_paid',
        'groupdescription_number_of_passengers_free',
        'groupdescription_number_of_days',
        'groupdescription_volshebny_handle_person',
        'groupdescription_client_handle_person',
        'groupdescription_booking_date',
        'groupdescription_confirmation_date',
        'groupdescription_amount',
        'groupdescription_start_date',
        'groupdescription_end_date',
        'groupdescription_destination',
        'groupdescription_payment_method',
        'groupdescription_payment_status',
        'groupdescription_client_id',
        'groupdescription_remark')

class CustomUserForm(BSModalForm):
    class Meta:
        model = CustomUser
        fields = ['user_role','username','email']


class GroupdescriptionForm_UpdateForm(BSModalForm):
    class Meta:
        model = Groupdescription
        fields = ('groupdescription_destination',
        'groupdescription_start_date',
        'groupdescription_end_date',
        'groupdescription_amount',
        'groupdescription_payment_status',
        'groupdescription_payment_method',
        'groupdescription_booking_date',
        'groupdescription_client_id',
        'groupdescription_volshebny_handle_person',
        'groupdescription_client_handle_person',
        'group_description_service_calculation_type',
        'groupdescription_remark')

class ServiceForm_UpdateForm(BSModalForm):
    class Meta:
        model = Service
        fields = ('service_vendor_id',
        'service_number_of_passengers',
        'service_quote_per_head',
        'service_roe',
        'service_gst',
        'service_total_amount',
        'service_vendor_payment_status',
        'service_payment_method',
        'service_id')

class Client_UpdateForm(BSModalForm):
    class Meta:
        model = Client
        fields= ('client_company_name',
        'client_name',
        'client_address',
        'client_email',
        'client_telephone',
        'client_website')

class Vendor_UpdateForm(BSModalForm):
    class Meta:
        model = Vendor
        fields=('vendor_name',
        'vendor_address',
        'vendor_type',
        'vendor_mobile',
        'vendor_email',
        'vendor_remark')

class AddAirticket(BSModalForm):
    class Meta:
        model = AirTicketsQuatation
        fields=('airticket_airline_name',
        'airticket_date_and_time_of_depature',
        'airticket_date_and_time_of_arrival',
        'airticket_departure_from',
        'airticket_arrival_at',
        'airticket_booked_from',
        'service_roe',
        'service_gst',
        'service_quote_per_head',
        'service_number_of_passengers',
        'service_total_amount',
        'service_payment_method',
        'service_vendor_payment_status')

class AddVisacost(BSModalForm):
    class Meta:
        model = VisaCostQuatation
        fields=('visacost_type_of_Visa',
        'visacost_time_period',
        'visacost_service_cost',
        'service_roe',
        'service_gst',
        'service_quote_per_head',
        'service_number_of_passengers',
        'service_total_amount',
        'service_payment_method',
        'service_vendor_payment_status')

class AddHotel(BSModalForm):
    class Meta:
        model = HotelQuatation
        fields=('hotelquatation_hotel_name',
        'hotelquatation_number_of_rooms',
        'hotelquatation_type_of_room',
        'hotelquatation_breakfast_provided',
        'service_roe',
        'service_gst',
        'service_quote_per_head',
        'service_number_of_passengers',
        'service_total_amount',
        'service_payment_method',
        'service_vendor_payment_status')

class AddRestaurant(BSModalForm):
    class Meta:
        model = RestaurantQuatation
        fields=('restaurantquatation_resturant_name',
        'restaurantquatation_For',
        'service_roe',
        'service_gst',
        'service_quote_per_head',
        'service_number_of_passengers',
        'service_total_amount',
        'service_payment_method',
        'service_vendor_payment_status')

class AddEntrances(BSModalForm):
    class Meta:
        model = EntrancesQuatation
        fields=('entrancesquatation_name',
        'service_roe',
        'service_gst',
        'service_quote_per_head',
        'service_number_of_passengers',
        'service_total_amount',
        'service_payment_method',
        'service_vendor_payment_status')

class AddSapsan(BSModalForm):
    class Meta:
        model = SapSanQuatation
        fields=('sapsanquatation_From_Station',
        'sapsanquatation_To_Station',
        'service_roe',
        'service_gst',
        'service_quote_per_head',
        'service_number_of_passengers',
        'service_total_amount',
        'service_payment_method',
        'service_vendor_payment_status')

class AddGuide(BSModalForm):
    class Meta:
        model = Guide
        fields=('Guide_Name',
        'Guide_Destination',
        'service_roe',
        'service_gst',
        'service_quote_per_head',
        'service_number_of_passengers',
        'service_total_amount',
        'service_payment_method',
        'service_vendor_payment_status')

class AddTransport(BSModalForm):
    class Meta:
        model = Transport
        fields=('transport_type_of_vehicle',
        'service_roe',
        'service_gst',
        'service_quote_per_head',
        'service_number_of_passengers',
        'service_total_amount',
        'service_payment_method',
        'service_vendor_payment_status')

class AddChef(BSModalForm):
    class Meta:
        model = Chefservice
        fields=('chefservice_chef_name',
        'chefservice_chef_destination',
        'service_roe',
        'service_gst',
        'service_quote_per_head',
        'service_number_of_passengers',
        'service_total_amount',
        'service_payment_method',
        'service_vendor_payment_status')

class AddAllservices(BSModalForm):
    class Meta:
        model = AllServices
        fields=('allservices_airticket',
        'allservices_visacost',
        'allservices_hotel',
        'allservices_restaurant',
        'allservices_entrances',
        'allservices_sapsan',
        'allservices_guide',
        'allservices_transport',
        'service_roe',
        'service_gst',
        'service_quote_per_head',
        'service_number_of_passengers',
        'service_total_amount',
        'service_payment_method',
        'service_vendor_payment_status')

class AddVisitingCard(BSModalForm):
    class Meta:
        model = VisitingCardAgencyData
        fields=('visitingcardagencydata_agency_name',
        'visitingcardagencydata_agent_name',
        'visitingcardagencydata_agent_designation',
        'visitingcardagencydata_agency_address',
        'visitingcardagencydata_agency_city',
        'visitingcardagencydata_tel_numbers',
        'visitingcardagencydata_mobile_numbers',
        'visitingcardagencydata_email_address',
        'visitingcardagencydata_agency_website')

class AddCompanyVisitingCard(BSModalForm):
    class Meta:
        model = VisitingCardCompanyData
        fields=('visitingcardcompanydata_company_name',
        'visitingcardcompanydata_agent_name',
        'visitingcardcompanydata_agent_designation',
        'visitingcardcompanydata_company_address1',
        'visitingcardcompanydata_company_address2',
        'visitingcardcompanydata_tel_number1',
        'visitingcardcompanydata_tel_number2',
        'visitingcardcompanydata_mobile_number1',
        'visitingcardcompanydata_mobile_number2',
        'visitingcardcompanydata_email_id1',
        'visitingcardcompanydata_email_id2',
        'visitingcardcompanydata_company_website')

class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%Y/%m/%d %H:%M:%S'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': ['#datetimepicker1','#datetimepicker2']   
        })
    )

