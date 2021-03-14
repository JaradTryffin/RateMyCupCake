from django.shortcuts import render,redirect
from .forms import AddCakeForm,RateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Cake
from apps.notification.utilities import create_notification






def cake_detail(request,cake_id):
    cake = Cake.objects.get(pk=cake_id)
    return render(request,'cake/cake_detail.html',{'cake':cake})

@login_required
def  rate_cake(request,cake_id):
    cake = Cake.objects.get(pk=cake_id)

    if request.method == 'POST':
        form = RateForm(request.POST)

        if form.is_valid():
            rate = form.save(commit=False)
            rate.cake =cake 
            rate.created_by = request.user
            rate.save()


            create_notification(request,cake.created_by,'rate',extra_id=rate.id)

            return redirect('dashboard')
    
    else:
        form = RateForm()
    
    return render(request,'cake/rate_cake.html',{'form':form,'cake':cake})


@login_required
def add_cake(request):
    if request.method =='POST':
        form = AddCakeForm(request.POST,request.FILES)

        if form.is_valid():
            
            cake = form.save(commit=False)
            cake.created_by=request.user
            cake.save()

            return redirect('dashboard')
    
    else:
        form = AddCakeForm()
    
    return render(request,'cake/add_cake.html',{'form':form})

