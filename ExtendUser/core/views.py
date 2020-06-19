from django.shortcuts import render,redirect
from django.http import HttpResponse

# USER
from django.contrib.auth.forms import UserCreationForm
from ExtendUser.account.forms import UserCustomCreateForm
from ExtendUser.account.models import User
# Create your views here.


def base(request):
    template_name = 'base.html'
    return render(request,template_name,{})

def index(request):
    template_name = 'index.html'
    #return HttpResponse("Teste")
    count = User.objects.count()    
    return render(request,template_name,{'count':count})

def signup(request):
    if request.method == 'POST':
        form = UserCustomCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCustomCreateForm()
       
    return render(request, 'registration/signup.html',{'form': form})