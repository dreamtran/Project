from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AddRecordForm, AddDealForm
from .models import Record, Deal




def home(request):
    records = Record.objects.all()
    deals = Deal.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in!")
            return redirect('home')
        else:
            messages.success(request, "Error. Please try again.")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records, 'deals':deals})


def logout_user(request):
    logout(request)
    messages.success(request, "Logged out...")
    return redirect('home')


def contact(request):
    records = Record.objects.all()
    if request.user.is_authenticated:
        return render(request, 'contact.html', {'records':records})
    else:
        messages.success(request, "You must be logged in to view records.")
        return redirect('home')



def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You must be logged in to view records.")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Deleted.")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to delete records.")
        return redirect('home')
    

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Added")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in.")
        return redirect('home')
    

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated.")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in.")
        return redirect('home')
    

def deal(request):
    deals = Deal.objects.all()
    if request.user.is_authenticated:
        return render(request, 'deal.html', {'deals':deals})
    else:
        messages.success(request, "You must be logged in to view deals.")
        return redirect('home')
    

def add_deal(request):
    form1 = AddDealForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form1.is_valid():
                add_deal = form1.save()
                messages.success(request, "Added")
                return redirect('deal')
        return render(request, 'add_deal.html', {'form1':form1})
    else:
        messages.success(request, "You must be logged in.")
        return redirect('home')