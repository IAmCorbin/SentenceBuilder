from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
  if request.user.is_authenticated():
    return HttpResponse("Welcome to my Chinese sentence builder %s!<br /><a href='/accounts/logout'>logout</a>" % request.user.username)
  else:
    return HttpResponse("Welcome to my Chinese sentence builder, please <a href='/accounts/login'>login</a> or <a href='accounts/register'>signup</a>!")

def userlogin(request):
  if request.user.is_authenticated():
    return HttpResponseRedirect("/")
  else:
    if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(username=username, password=password)
      if user is not None:
        if user.is_active:
          login(request, user)
          return HttpResponseRedirect("/")
      return HttpResponse("There was an error logging you in")
    else:
      return render_to_response("registration/login.html", 
                                 context_instance=RequestContext(request))
 
def userlogout(request):
  logout(request)
  return HttpResponseRedirect("/")
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render_to_response("registration/register.html", {'form': form}, 
                               context_instance=RequestContext(request))
                               
