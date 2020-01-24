from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from payment.models import Groupdescription,AirTicketsQuatation,VisaCostQuatation,HotelQuatation,RestaurantQuatation,EntrancesQuatation,SapSanQuatation,CustomUser,Vendor,Client,Service,Guide,Transport,AllServices,VisitingCardAgencyData,VisitingCardCompanyData

# Register your models here.

class VendorAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "vendor_name",
        "vendor_type",
    ]

class AirTicketsQuatationAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "service_type",
    ]

class VisaCostQuatationAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "service_type",
    ]
class HotelQuatationAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "service_type",
    ]
class RestaurantQuatationAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "service_type",
    ]
class EntrancesQuatationAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "service_type",
    ]
class SapSanQuatationAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "service_type",
    ]

class TransportAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "service_type",
    ]
class ClientAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "client_name",
    ]

class GuideAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "service_type",
    ]

class AllServicesAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "allservices_airticket",
        "allservices_visacost",
        "allservices_hotel",
        "allservices_restaurant",
        "allservices_entrances",
        "allservices_sapsan",
        "allservices_guide",
        "allservices_transport",
    ]

class VisitingCardAgencyDataAdmin(ImportExportModelAdmin):
    list_display = [
        "pk",
        "visitingcardagencydata_agency_name",
        "visitingcardagencydata_agent_name",
        "visitingcardagencydata_agent_designation",
        "visitingcardagencydata_agency_address",
        "visitingcardagencydata_agency_city",
        "visitingcardagencydata_tel_numbers",
        "visitingcardagencydata_mobile_numbers",
        "visitingcardagencydata_email_address",
        "visitingcardagencydata_agency_website"
    ]

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
        "visitingcardcompanydata_company_website"
    ]
class GroupdescriptionAdmin(admin.ModelAdmin):
    search_fields = ["groupdescription_vtrefNo", "groupdescription_client_id"]
    list_filter = ["groupdescription_client_id", "groupdescription_payment_status"]
    list_display = [
        "pk",
        "groupdescription_vtrefNo",
        "groupdescription_client_id",
        "groupdescription_date_time_added",
        "groupdescription_payment_status",
        ]
    list_editable = ["groupdescription_payment_status"]
    

admin.site.register(Groupdescription,GroupdescriptionAdmin)
admin.site.register(AirTicketsQuatation,AirTicketsQuatationAdmin)
admin.site.register(VisaCostQuatation,VisaCostQuatationAdmin)
admin.site.register(HotelQuatation,HotelQuatationAdmin)
admin.site.register(RestaurantQuatation,RestaurantQuatationAdmin)
admin.site.register(EntrancesQuatation,EntrancesQuatationAdmin)
admin.site.register(SapSanQuatation,SapSanQuatationAdmin)
admin.site.register(Transport,TransportAdmin)
admin.site.register(Guide,GuideAdmin)
admin.site.register(CustomUser)
admin.site.register(Vendor,VendorAdmin)
admin.site.register(Client,ClientAdmin)
admin.site.register(AllServices,AllServicesAdmin)
admin.site.register(Service)
admin.site.register(VisitingCardAgencyData,VisitingCardAgencyDataAdmin)
admin.site.register(VisitingCardCompanyData,VisitingCardCompanyDataAdmin)
