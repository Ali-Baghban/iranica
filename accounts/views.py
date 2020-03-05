from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import auth, messages
from .models import User
from product.models import Product,Delivery,Order

def dashboard_view(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = get_object_or_404(User,id=user_id)
        if request.method == 'GET' and 'option' in request.GET:
            r = request.GET['option']
            if r == '1':
                pass
            elif r == '2':
                return redirect('logout')
            else:
                return redirect('edit_profile')
        orders = Order.objects.all().filter(customer=user).order_by('-register_time')
        context = { 'orders': orders,}
        return render(request, 'accounts/dashboard.html', context=context)
    else:
        return redirect('login')

def order_details(request,order_id):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = get_object_or_404(User,id=user_id)
        order = get_object_or_404(Order,id=order_id,customer=user)
        context = { 'order': order,}
        return render(request, 'accounts/order_details.html',context=context)
    else:
        return redirect('login')

def dashboard_profile_edit(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = get_object_or_404(User, id=user_id)
        if request.method == 'POST' and 'edit_me' in request.POST:
            first_name = request.POST['firstname']
            last_name = request.POST['lastname']
            email = request.POST['email']
            #username = request.POST['username']
            password = request.POST['password']
            repassword = request.POST['repassword']
            address = request.POST['address']
            phone = request.POST['phone']

            if (password not in 'last_passX') and (repassword not in 'last_passX'):
                if len(password) | len(repassword) < 8 :
                    #messages.error(request, 'Your password is short, it must be greater than 8 characters !')
                    return redirect('edit_profile')
                else:
                    if password != repassword : 
                        #messages.error(request, 'Password does not match !')
                        return redirect('edit_profile')
                    else:
                        user.set_password(password)

                        #messages.success(request, 'Congratulation, you are successfully registered !')
                        

            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.address=address
            user.phone=phone
            user.save()

        user = get_object_or_404(User, id=user_id)
        context = { 'user': user, }
        return render(request, 'accounts/edit_profile.html', context=context)
    else:
        return redirect('login')
def dashboard_login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            return redirect('login')
    return render(request, 'accounts/login.html')

def dashboard_register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']
        address = request.POST['address']
        phone = request.POST['phone']

        if len(password) | len(repassword) < 8 :
            #messages.error(request, 'Your password is short, it must be greater than 8 characters !')
            return redirect('register')
        else:
            if password != repassword : 
                #messages.error(request, 'Password does not match !')
                return redirect('register')
            else:
                if  User.objects.filter(username=username).exists():
                    #messages.error(request, 'The username is token !')
                    return redirect('register')
                else:
                    if User.objects.filter(email=email).exists():
                        #messages.error(request, 'The email has registered before !')
                        return redirect('register')
                    else:
                        user = User.objects.create_user(
                            username=username, password=password, email=email, first_name=first_name,
                            last_name=last_name, address=address, phone=phone
                        )
                        user.save()
                        #messages.success(request, 'Congratulation, you are successfully registered !')
                        return redirect('login')
                        
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def dashboard_logout(request):
    #if request.method == 'POST':
    auth.logout(request)
        #messages.success(request, 'You have logged out !')
    return redirect('index')
def card_view(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        delivery = Delivery.objects.all()
        
        if request.method == 'POST':
            card = request.session.get('card', {})
            if request.POST['add']:
                pid = request.POST['item_id']
                pc = request.POST['count']
                card[pid] = pc
                request.session['card'] = card
                items = {}
                card = request.session['card']
                for key in card:

                    items[key] = get_object_or_404(Product, id=key)
                    items[key].price_2nd = int(items[key].price)*int(card[key])
                    items[key].count = card[key]

                context = { 'items': items, 'user':user, 'delivery':delivery, }

                return render(request, 'accounts/card.html', context=context)

        items = {}
        card = request.session.get('card', {})
        for key in card:  
            items[key] = get_object_or_404(Product, id=key)    
            items[key].price_2nd = int(items[key].price)*int(card[key])
            items[key].count = card[key]

        context = { 'items': items, 'user':user,'delivery':delivery, }
        return render(request, 'accounts/card.html', context=context)
    else:
        return redirect('login')
    

def card_remove(request,item_id_remove):
    
    card = request.session['card']
    
    del card[str(item_id_remove)]
    request.session['card'] = card
    return redirect('card')

