from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import Vehicle
from .forms import VehicleForm

# Create your views here.

def home(request):
    return render(request, "home.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('vehicle_list')
        else:
            messages.info(request, "Invalid username or password")
            return redirect('login')
    return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']


        if not username or not password or not password1:
            messages.error(request, "Your registration is not completed")
            return redirect('register')

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('register')
    return render(request, "register.html")
def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicle_list.html', {'vehicles': vehicles})

def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm()
    return render(request, 'vehicle_form.html', {'form': form})

def edit_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'vehicle_form.html', {'form': form})

def delete_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('vehicle_list')
    return render(request, 'vehicle_confirm_delete.html', {'vehicle': vehicle})

def logout_view(request):
    logout(request)
    return redirect('home')