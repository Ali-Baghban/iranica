from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from zeep import Client
from .models import *
from accounts.models import User
from hashlib import md5
from datetime import datetime

#############################
# Static values

MERCHANT = '5763ceee-1bd0-11ea-ad6b-000c295eb8fc'
client = Client('https://sandbox.zarinpal.com/pg/services/WebGate/wsdl')
description = "کد تخفیفی اعمال نشده است"  # Required
email = 'email@example.com'  # Optional
mobile = '09335138159'  # Optional
#############################
def product_view(request):
    category = Category.objects.all()
    products = Product.objects.filter(status=1).order_by('-register_time')
    context = {'category':category, 'products': products,}
    return render(request, 'products/index.html', context=context)

def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    products_recent = Product.objects.filter(status=1).order_by('-register_time')[:8]
    for p in products_recent:
        p.caption = p.caption[:100]
    context = {'product': product, 'products_recent':products_recent, }
    return render(request, 'products/product.html', context=context)

def order(request):
    if request.method == 'POST' and 'buy' in request.POST and 'final_address' in request.POST and 'final_details' in request.POST and 'delivery_type' in request.POST:
        card = request.session.get('card', {})
        if bool(card):
            
            address = request.POST['final_address']
            details = request.POST['final_details']
            deliver_id = request.POST['delivery_type']
            deliver_with = get_object_or_404(Delivery,id=deliver_id)
            user_id = request.user.id
            user = get_object_or_404(User, id=user_id)
            ordering = ""
            total_cost = 0
            counter = 0
            for key in card:
                product = get_object_or_404(Product, id=key)
                counter += 1
                ordering = ordering +str(counter)+" - نام محصول  : "+product.title+" ( "+product.sub_title+" ) "+" به تعداد : "+card[key]+"\n"
                total_cost += int(product.price)*int(card[key])
            salt = str(user_id)+str(datetime.now())
            bill_id = md5(bytes(salt,encoding='utf-8')).hexdigest()
            orders = Order.objects.create(customer = user, products_ordered = ordering ,products_type_count=counter, address=address,
             details=details, total_cost=total_cost,bill_id=bill_id,deliver_with=deliver_with,)
            orders.save()
            #######################
            # Payment
            #######################
            
            CallbackURL = 'http://127.0.0.1:8000/products/verify/'+bill_id+"/"  # Important: need to edit for realy server.
            delivery_cost = deliver_with.cost
            total_price = total_cost+delivery_cost
            result = client.service.PaymentRequest(MERCHANT, total_price, description, email, mobile, CallbackURL)
            if result.Status == 100:
                return redirect('https://sandbox.zarinpal.com/pg/StartPay/' + str(result.Authority))
            else:
                return HttpResponse('متاسفانه درگاه پرداخت آماده نیست' + str(result.Status))
        else:
            return redirect('products')
    
    return redirect('products')

def verify(request,bill_id):
    if request.GET.get('Status') == 'OK':
        try:
            order = get_object_or_404(Order, bill_id=str(bill_id))
            products_cost = order.total_cost
            delivery = get_object_or_404(Delivery, id=order.deliver_with.id)
            delivery_cost = delivery.cost
            total_cost = int(products_cost)+int(delivery_cost)
            print(total_cost)
            products_type_count = order.products_type_count
            result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], total_cost)
            
            #print("result -> "+str(result.Status))
            if result.Status == 100:	
                order.status = 1
                order.save()
                del request.session['card']
                context = {'success':True, 'total_cost': total_cost,'products_cost':products_cost,
                'delivery_cost': delivery_cost, 'products_type_count':products_type_count}
                return render(request,'accounts/verify.html',context)
            elif result.Status == 101:
                context = {'success': False,}
                return render(request, 'accounts/verify.html', context)
            else:
                context = {'success': False,}
                return render(request, 'accounts/verify.html', context)
        except:
            print("OK->execption")
            return HttpResponse(request)
    else:
        return redirect('card')