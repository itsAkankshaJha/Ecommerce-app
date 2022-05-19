# from telnetlib import LOGOUT
# from auth import settings
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
# from telnetlib import LOGOUT
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from shopkaro.forms import RegisterForm, MyLoginForm


# Create your views here.


# Create your views here.
def index(request):
    return render(request, 'index.html')


# def login(request):
#     return render(request, 'login.html')


# def register(request):
#     return render(request, 'register.html')
#

class myregister(SuccessMessageMixin, CreateView):
    form_class = RegisterForm  # this will be used in register.html as table
    template_name = 'register.html'
    success_url = reverse_lazy('myregister')
    success_message = "Your account has been created successfully"

    def dispatch(self, *args, **kwargs):
        return super(myregister, self).dispatch(*args, **kwargs)


def my_login(request):
    myloginform = MyLoginForm(request.POST or None)
    if myloginform.is_valid():
        username = myloginform.cleaned_data.get("uname")  # got username from login form
        redirect_to = request.POST.get('next')

        userobj = User.objects.get(username__iexact=username)  # return userobj with help of username

        login(request, userobj)  # session create

        request.session["myname"] = username  # variable stored in session
        if redirect_to:
            return redirect(redirect_to)
        else:
            return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "login.html", {"meraloginform": myloginform})
