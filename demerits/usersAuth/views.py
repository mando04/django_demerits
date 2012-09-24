from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from usersAuth.forms import RegisterForm, loginUserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from usersAuth.models import userAccount


def usersRegister(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        REFERER = request.META['HTTP_REFERER']

        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], \
                                            email=form.cleaned_data['email'], \
                                            password=form.cleaned_data['password'])
            user.save()
            
            USER_P = userAccount(user=user, name=form.cleaned_data['name'], \
                                 bday=form.cleaned_data['bday'], \
                                 email=form.cleaned_data['email'])
            USER_P.save()
            performLogin(request)
            return HttpResponseRedirect(REFERER)
        else:
            return render_to_response('register.html', { 'form':form }, context_instance=RequestContext(request))    
    else:
        """ user is not submitting a form Show blank form"""
        form = RegisterForm()
        context = {'form': form }
        return render_to_response('register.html', context, context_instance=RequestContext(request))

def performLogin(request):
    form = loginUserForm(request.POST)
    if form.is_valid():
        user = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=user, \
                            password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return 1
            else:
                error = "Account is diabled please email the Site Administrator"
                #return a 'disabled account' error message
                contexte({'error':error})
                return render_to_response('login.html', context, context_instance=RequestContext(request))
        else:
            error = "Username or password was incorrect!"
            context = {'error':error, 'form':form }
           # return an 'invalid login' error page
            return render_to_response('login.html', context, context_instance=RequestContext(request))
    else:
        return render_to_response('login.html', { 'form':form }, context_instance=RequestContext(request))

def loginUser(request):
    context = {'form': loginUserForm}

    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        # Login the user
        performLogin(request)

    return render_to_response('login.html', context, context_instance=RequestContext(request))

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def userprofile(request, username):
    print username
    if request.user.is_authenticated:
        print "User %s is authenticated show editable profile"%username
        profile = usersAuth.objects.get(name=username)
    return render_to_response('profile.html', { 'profile' : profile }, context_instance=RequestContext(request))

