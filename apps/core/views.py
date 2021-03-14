from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from apps.cake.models import Cake
from apps.userprofile.models import Userprofile


# Create your views here.

def frontpage(request):
    cakes=Cake.objects.all()
    count=Cake.objects.count()
    return render(request,'core/frontpage.html',{'cakes':cakes,'count':count})

def signup(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            account_type = request.POST.get('account_type','reviewer')

            if account_type =='user':
                userprofile = Userprofile.objects.create(user=user,is_user=True)
                userprofile.save()
            else:
                userprofile = Userprofile.objects.create(user=user)
                userprofile.save()


            login(request,user)
            return redirect('dashboard')

    else:
        form = UserCreationForm()

    



    

    context={'form':form}
    return render(request,'core/signup.html',context)
