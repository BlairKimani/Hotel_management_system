from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.http import HttpResponse, JsonResponse
from .form import UserCreationForm as Form
import datetime as dt
from . import models
import json


# Create your views here.
User = get_user_model()
#funtion loads the home page
def index(request):
    return render(request, 'index.HTML')

#function loads the Sign up page and sign in user
def Register(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data['username'] = data['first_name'] + data['last_name']
        data['password1'], data['password2'] = data['password'],data['password']
        User = get_user_model()
        user = User(username=data['username'], first_name=data['first_name'], last_name=data['last_name'], email=data['email'], contact=data['contact'], id_no=data['id'], gender=data['gender'])
        user.set_password(data['password'])
        user.save()
        return redirect('login')

    else:
        return render(request, 'Register.HTML', {'message': {'msgbool': 0}})

#function loads the login page
def Login(request):
    if request.method == 'POST':
        Uuser = get_user_model()

        user = authenticate(request, email=request.POST['email'], password=request.POST['password'])
        print('hello', request.POST['email'], request.POST['password'])
        if user != None:
            print('hello')
            login(request, user)
            if user.is_staff:
                return redirect('staff')
            else:
                return redirect('client')
        return render(request, 'Login.HTML', {'message': {'msgbool': 1}})
    else:
        return render(request, 'Login.HTML', {'message': {'msgbool': 0}})

#function loads the forgot password page
def Forgot_password(request):
    if request.POST:
        code = request.POST['code']
        password = request.POST['password']
        
        user=User.objects.get(id_no=code)
        user.set_password(password)
        user.save()
        return redirect('login')
    else:
        return render(request, 'forgot_pass.html')
#function loads the staff page
def Staff_fun(request):

    services = models.ServiceRequest.objects.filter(service=request.user.service.service_id)
    content = {
        'services':services
    }
    return render(request, 'staff.html', content)

#function loads the client page
def Client_fun(request):
    foods = models.Inventory.objects.all()
    rooms = models.Room.objects.filter(availabilty_status=1)
    content = {
        'foods':foods,
        'rooms':rooms
    }
    return render(request, 'client.HTML', content)


def process_data(request):
    if request.method == 'POST':
        data = dict(json.loads(request.body))
        user = models.AppCustomuser.objects.get(id=request.user.id)
        service = models.Service.objects.get(service_id=int(data['service']))
        if data['type'] == 'room':
            room = models.Room.objects.get(room_id=data['id'])
            checkout = str(dt.date.today + dt.timedelta(days=data['days']))
            booking = models.Booking(user=user, room=room, check_out_date=checkout, number_of_guests=1, total_price=data['price'])
            booking.save()

            request = models.ServiceRequest(user=user, booking=booking, service=service)
            request.save()
            payment = models.Payment(user=user, booking=booking, service=service, amount=data['price'], payment_mode=data['payment'])
            payment.save()
        else:
            request = models.ServiceRequest(user=user, service=service)
            request.save()
            payment = models.Payment(user=user, service=service, amount=data['price'], payment_mode=data['payment'])
            payment.save()
        
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})