from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect
from .models import Userprofile,ConversationMessage
from apps.cake.models import Cake,Rate

from apps.notification.utilities import create_notification

# Create your views here.
@login_required
def dashboard(request):
    return render(request,'userprofile/dashboard.html',{'userprofile':request.user.userprofile})

@login_required()
def view_rating(request,rate_id):
    # if request.user.userprofile.is_user:
    #     rate = get_object_or_404(Rate,pk=rate_id,cake__created_by=request.user)
    # else:
    #     rate = get_object_or_404(Rate,pk=rate_id,created_by=request.user)
    rate = Rate.objects.get(pk=rate_id)

    if request.user.userprofile.is_user:
        to_user = rate.created_by
    else:
        to_user = rate.cake.created_by
  
  
   
    
    if request.method =='POST':
        content = request.POST.get('content')

        if content:
            conversation = ConversationMessage.objects.create(rate=rate,content=content,created_by=request.user)

            # create_notification(request,rate.created_by,'message',extra_id=rate.id)
            create_notification(request,to_user,'message',extra_id=rate.id)
         

            return redirect('view_rating',rate_id=rate_id)

        
    
    return render(request,'userprofile/view_rating.html',{'rate':rate})

@login_required
def view_dashboard_cake(request,cake_id):
    cake = get_object_or_404(Cake,pk=cake_id,created_by=request.user)

    return render(request,'userprofile/view_dashboard_cake.html',{'cake':cake})

