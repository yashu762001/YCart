from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt
from Paytm import Checksum
MERCHANT_KEY = 'cW3WR55G8mkpsNZf'

def home(request):
    list = set([])
    products = Product.objects.all()
    x = slice(25, len(products))
    for product in products[x]:
       list.add(product.category)
    print(list)
    temp = {'list': list, 'product': products}
    return render(request,'shop/home.html', temp)


def index(request):
    products = Product.objects.all()
    x = slice(0, 25)
    numberOfSlides = 5
    list = []
    for product in products[x]:
        list.append(product)
    params = {'product': list, 'numberOfSlides': numberOfSlides, 'range1': range(1, numberOfSlides)}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request,'shop/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        mobile = request.POST.get('mobile', '')
        whatsapp = request.POST.get('whatsapp', '')
        desc = request.POST.get('desc', '')
        print(name, email)
        obj = Contact(Name=name, Email=email, MobileNumber=mobile, WhatsappNumber=whatsapp, description=desc)
        obj.save()
        return render(request, 'shop/greeting.html')

    else:
        return render(request, 'shop/contact.html')

def tracker(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        orderId = request.POST.get('orderId', '')

        try:
            order = Order.objects.filter(email=email, order_id=orderId)
            if(len(order)>0):
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.time})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse("{}")

        except Exception as e:
            print(e)
            return HttpResponse("{}")
    else:
        return render(request, 'shop/tracker.html')

# def search(request):
#     return HttpResponse("We are At Search")


def product(request, id):
    # Fetch The product using the id
    product = Product.objects.filter(id=id)
    print(product)
    return render(request, 'shop/product.html', {'product': product[0]})


def checkout(request):
    if(request.method=='POST'):
        name = request.POST.get('name', '')
        totalAmount = int(request.POST.get('totalAmount', ''))
        email = request.POST.get('email', '')
        mobile = request.POST.get('mobile', '')
        whatsapp = request.POST.get('whatsapp', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2', '')
        zip = request.POST.get('zip', '')
        items_json = request.POST.get('itemsJson', '')

        obj = Order(name=name, email=email, mobile=mobile, whatsapp=whatsapp, city=city, state=state, address1=address1, address2=address2, zip_code=zip, items_json=items_json, amount=totalAmount)
        obj.save()
        thank = True
        id = obj.order_id
        update = OrderUpdate(order_id=obj.order_id, update_desc="The Order Has Been Placed.")
        update.save()
        # Requesting paytm to transfer the provided amount to my account after successful payment by user.
        param_dict = {
            'MID': 'dBIYIr12520508923551',
            'ORDER_ID': str(obj.order_id),
            'TXN_AMOUNT': str(totalAmount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/shop/handlerequest/',
        }
        temp = id
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'shop/paytm.html', {'param_dict': param_dict})
        # return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
    else:
        return render(request, 'shop/checkout.html')

#paytm will send you post request here and so you will need to allow it without any csrf check.

@csrf_exempt
def handlerequest(request):
    return HttpResponse('done')




