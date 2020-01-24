from payment.models import Groupdescription, AirTicketsQuatation, VisaCostQuatation, HotelQuatation, RestaurantQuatation, EntrancesQuatation, SapSanQuatation, Client, Vendor, Service, CustomUser,Guide,Transport, AllServices

def client_status_count(a,client_payment_status):
    count = Groupdescription.objects.filter(groupdescription_client_id=a[0],groupdescription_payment_status=client_payment_status).all().count()
    return count

def vendor_status_count(a,vendor_payment_status):
    count = Service.objects.filter(service_vendor_id=a[0],service_vendor_payment_status=vendor_payment_status).all().count()
    return count

def vendor_payment_count(a,vendor_payment_status_one):
    if vendor_payment_status_one == 'Pending':
        count = Service.objects.filter(service_vendor_id=Vendor.objects.get(pk=int(a[0])),service_vendor_payment_status='Pending').all().count()
        return count
    elif vendor_payment_status_one == 'Done':
        count = Service.objects.filter(service_vendor_id=Vendor.objects.get(pk=int(a[0])),service_vendor_payment_status='Done').all().count()
        return count
    elif vendor_payment_status_one == 'Payment_Pending_Amonut':
        all_services_of_one_tour  = Service.objects.filter(service_vendor_id=Vendor.objects.get(pk=int(a[0])),service_vendor_payment_status='Pending')
        service_cost_list=[]
        for service in all_services_of_one_tour:
            service_cost_list.append(service.service_total_amount)
        cost = 0
        for num in service_cost_list:
            cost+=num
        return cost
    elif vendor_payment_status_one == 'Payment_Done_Amount':
        all_services_of_one_tour  = Service.objects.filter(service_vendor_id=Vendor.objects.get(pk=int(a[0])),service_vendor_payment_status='Done')
        service_cost_list = []
        for service in all_services_of_one_tour:
            service_cost_list.append(service.service_total_amount)
        cost = 0
        for num in service_cost_list:
            cost+=num
        return cost
    
def all_vendor_services_status_payment_count(vendor_id,payment_status_one):
    count = Service.objects.filter(service_vendor_id = vendor_id,service_vendor_payment_status=payment_status_one).all().count()
    return count

def all_vendor_services_status_payment_amountpending_count(vendor_id,payment_amount_one):
        all_pending_services_of_one_tour  = Service.objects.filter(service_vendor_id= vendor_id,service_vendor_payment_status=payment_amount_one)
        service_cost_list = []
        for service in all_pending_services_of_one_tour:
            service_cost_list.append(service.service_total_amount)
        cost_pending = 0
        for num in service_cost_list:
            cost_pending+=num
        return cost_pending    
def all_vendor_services_status_payment_amountpaid_count(vendor_id,payment_amount_one):       
        all_paid_services_of_one_tour  = Service.objects.filter(service_vendor_id= vendor_id,service_vendor_payment_status=payment_amount_one)
        service_cost_list = []
        for service in all_paid_services_of_one_tour:
            service_cost_list.append(service.service_total_amount)
        cost_done = 0
        for num in service_cost_list:
            cost_done+=num
        return cost_done
        


def filtering_vendors(vendor_type_parameter):
    vendor_payment_status = ['Pending','Done','Payment_Pending_Amonut','Payment_Done_Amount']
    x = list(set(list(Vendor.objects.filter(vendor_type=vendor_type_parameter).values_list('pk','vendor_name'))))
    vendor_status_list = [vendor_payment_count(a,vendor_payment_status_one) for a in x for vendor_payment_status_one in vendor_payment_status ]
    final = [vendor_status_list[i * 4:(i + 1) * 4] for i in range((len(vendor_status_list) + 4 - 1) // 4 )]
    vendor_dict = dict(zip(x,final))
    return vendor_dict

#---this is the function for getting the paid and pending of AirticketQuataion 
def vendor_airticket_status_count(a,service_vendor_payment_status):
    count = AirTicketsQuatation.objects.filter(service_vendor_id=a[0],service_vendor_payment_status=service_vendor_payment_status).all().count()
    return count
#-----------

#---this is the function for getting the paid and pending of VisaCostQuatation 
def vendor_visacost_status_count(a,service_vendor_payment_status):
    count = VisaCostQuatation.objects.filter(service_vendor_id=a[0],service_vendor_payment_status=service_vendor_payment_status).all().count()
    return count
#-----------

#---this is the function for getting the paid and pending of HotelQuatation 
def vendor_hotel_status_count(a,service_vendor_payment_status):
    count = HotelQuatation.objects.filter(service_vendor_id=a[0],service_vendor_payment_status=service_vendor_payment_status).all().count()
    return count
#-----------

#---this is the function for getting the paid and pending of RestaurantQuatation 
def vendor_restaurant_status_count(a,service_vendor_payment_status):
    count = RestaurantQuatation.objects.filter(service_vendor_id=a[0],service_vendor_payment_status=service_vendor_payment_status).all().count()
    return count
#-----------

#---this is the function for getting the paid and pending of EntrancesQuatation 
def vendor_entrances_status_count(a,service_vendor_payment_status):
    count = EntrancesQuatation.objects.filter(service_vendor_id=a[0],service_vendor_payment_status=service_vendor_payment_status).all().count()
    return count
#-----------

#---this is the function for getting the paid and pending of SapSanQuatation 
def vendor_sapsan_status_count(a,service_vendor_payment_status):
    count = SapSanQuatation.objects.filter(service_vendor_id=a[0],service_vendor_payment_status=service_vendor_payment_status).all().count()
    return count
#-----------

def client_payment_recieved(Paid):
    """Function to give count of client payment done
    Parameters: client id
    Returns : count of all the payments made by client"""
    count = Groupdescription.objects.filter(groupdescription_payment_status="Paid").all().count()
    return count

def client_payment_pending(Pending):
    """Function to give count of client payment done
    Parameters: client id
    Returns : count of all the payments made by client"""
    count = Groupdescription.objects.filter(groupdescription_payment_status="Pending").all().count()
    return count

def vendor_payment_done():
    """Function to give count of client payment done
    Parameters: vendor id
    Returns : count of all the payments made by client"""
    
    return count

def vendor_payment_pending():
    """Function to give count of client payment done
    Parameters: vendor id
    Returns : count of all the payments made by client"""
    return count

def group_cost_list_generator(one_tour_detials):
    group_object = Groupdescription.objects.get(pk=one_tour_detials[0])
    air_tickets = list(AirTicketsQuatation.objects.all().filter(service_id=group_object.pk))
    visa_costs = list(VisaCostQuatation.objects.all().filter(service_id=group_object.pk))
    hotel_quatations = list(HotelQuatation.objects.all().filter(service_id=group_object.pk))
    restaurant_quatations = list(RestaurantQuatation.objects.all().filter(service_id=group_object.pk))
    entrances_quatations = list(EntrancesQuatation.objects.all().filter(service_id=group_object.pk))
    sapsan_quatations = list(SapSanQuatation.objects.all().filter(service_id=group_object.pk))
    guide_names = list(Guide.objects.all().filter(service_id=group_object.pk))
    transport_names = list(Transport.objects.all().filter(service_id=group_object.pk))
    sum=0
    if group_object.group_description_service_calculation_type=="INCLUSIVE":
        for airticket in air_tickets:
            sum = sum + airticket.service_total_amount
        for visacost in visa_costs:
            sum = sum + visacost.service_total_amount
        for hotel in hotel_quatations:
            sum = sum + hotel.service_total_amount
        for restaurant in restaurant_quatations:
            sum = sum + restaurant.service_total_amount
        for entrance in entrances_quatations:
            sum = sum + entrance.service_total_amount
        for sapsan in sapsan_quatations:
            sum = sum + sapsan.service_total_amount
        for guide in guide_names:
            sum = sum + guide.service_total_amount
        for transport in transport_names:
            sum = sum + transport.service_total_amount
        payment_total = sum
    elif group_object.group_description_service_calculation_type=="EXCLUSIVE":
        for hotel in hotel_quatations:
            sum = sum + hotel.service_total_amount
        for restaurant in restaurant_quatations:
            sum = sum + restaurant.service_total_amount
        for entrance in entrances_quatations:
            sum = sum + entrance.service_total_amount
        for sapsan in sapsan_quatations:
            sum = sum + sapsan.service_total_amount
        for guide in guide_names:
            sum = sum + guide.service_total_amount
        for transport in transport_names:
            sum = sum + transport.service_total_amount
        payment_total = sum
    return payment_total
 

def client_list():
    clients = Client.objects.all()
    client_payment_status = ['Paid','Pending']
    x = list(set(list(Client.objects.values_list('pk','client_name'))))
    client_status_list = [client_status_count(a,client_payment_status_one) for a in x for client_payment_status_one in client_payment_status ]
    final = [client_status_list[i * 2:(i + 1) * 2] for i in range((len(client_status_list) + 2 - 1) // 2 )]
    client_dict = dict(zip(x,final))
    return client_dict

def airticket_list():
    airticketobjects = AirTicketsQuatation.objects.all()
    vendors = Vendor.objects.all()
    vendor_payment_status = ['Pending','Done']
    x = list(set(list(Vendor.objects.values_list('pk','vendor_name'))))
    vendor_status_list = [vendor_airticket_status_count(a,vendor_payment_status_one) for a in x for vendor_payment_status_one in vendor_payment_status ]
    final = [vendor_status_list[i * 2:(i + 1) * 2] for i in range((len(vendor_status_list) + 2 - 1) // 2 )]
    airticket_dict = dict(zip(x,final))
    return airticket_dict

def visacost_list():
    visacosttobjects = VisaCostQuatation.objects.all()
    vendors = Vendor.objects.all()
    vendor_payment_status = ['Pending','Done']
    x = list(set(list(Vendor.objects.values_list('pk','vendor_name'))))
    vendor_status_list = [vendor_visacost_status_count(a,vendor_payment_status_one) for a in x for vendor_payment_status_one in vendor_payment_status ]
    final = [vendor_status_list[i * 2:(i + 1) * 2] for i in range((len(vendor_status_list) + 2 - 1) // 2 )]
    visacost_dict = dict(zip(x,final))
    return visacost_dict

def hotel_list():
    hotelquatationobjects = HotelQuatation.objects.all()
    vendors = Vendor.objects.all()
    vendor_payment_status = ['Pending','Done']
    x = list(set(list(Vendor.objects.values_list('pk','vendor_name'))))
    vendor_status_list = [vendor_hotel_status_count(a,vendor_payment_status_one) for a in x for vendor_payment_status_one in vendor_payment_status ]
    final = [vendor_status_list[i * 2:(i + 1) * 2] for i in range((len(vendor_status_list) + 2 - 1) // 2 )]
    hotel_dict = dict(zip(x,final))
    return hotel_dict

def restaurant_list():
    restaurantquatationobjects = RestaurantQuatation.objects.all()
    vendors = Vendor.objects.all()
    vendor_payment_status = ['Pending','Done']
    x = list(set(list(Vendor.objects.values_list('pk','vendor_name'))))
    vendor_status_list = [vendor_restaurant_status_count(a,vendor_payment_status_one) for a in x for vendor_payment_status_one in vendor_payment_status ]
    final = [vendor_status_list[i * 2:(i + 1) * 2] for i in range((len(vendor_status_list) + 2 - 1) // 2 )]
    restaurant_dict = dict(zip(x,final))
    return restaurant_dict

def entrances_list():
    entrancesquatationobjects = EntrancesQuatation.objects.all()
    vendors = Vendor.objects.all()
    vendor_payment_status = ['Pending','Done']
    x = list(set(list(Vendor.objects.values_list('pk','vendor_name'))))
    vendor_status_list = [vendor_entrances_status_count(a,vendor_payment_status_one) for a in x for vendor_payment_status_one in vendor_payment_status ]
    final = [vendor_status_list[i * 2:(i + 1) * 2] for i in range((len(vendor_status_list) + 2 - 1) // 2 )]
    entrances_dict = dict(zip(x,final))
    return entrances_dict

def sapsan_list():
    sapsanquatationobjects = SapSanQuatation.objects.all()
    vendors = Vendor.objects.all()
    vendor_payment_status = ['Pending','Done']
    x = list(set(list(Vendor.objects.values_list('pk','vendor_name'))))
    vendor_status_list = [vendor_sapsan_status_count(a,vendor_payment_status_one) for a in x for vendor_payment_status_one in vendor_payment_status ]
    final = [vendor_status_list[i * 2:(i + 1) * 2] for i in range((len(vendor_status_list) + 2 - 1) // 2 )]
    sapsan_dict = dict(zip(x,final))
    return sapsan_dict


def all_service_dictionary_generator():
    allservices = AllServices.objects.all()
    all_service_dict = {}
    services_list = []
    for all_service in allservices:
        services_list = []
        if all_service.allservices_airticket == True:
            services_list.append("Air Ticket Service,")
        if all_service.allservices_visacost == True:
            services_list.append("Visa Cost Service,")
        if all_service.allservices_hotel == True:
            services_list.append("Hotel Service,")
        if all_service.allservices_restaurant == True:
            services_list.append("Restaurant Service,")
        if all_service.allservices_entrances == True:
            services_list.append("Entrances Service,")
        if all_service.allservices_sapsan == True:
            services_list.append("SapSan Service,")
        if all_service.allservices_guide == True:
            services_list.append("Guide Service,")
        if all_service.allservices_transport == True:
            services_list.append("Transport Service")
        all_service_dict[all_service.pk]=services_list
    return all_service_dict