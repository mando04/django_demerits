from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, Context
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from board.models import PersonD
import datetime

@login_required
def index(request):
    person = PersonD.objects.all().order_by('name')[:]
    return render_to_response('index.html', { 'person' : person }, context_instance=RequestContext(request))

def my_404(request):
    back = request.META['HTTP_REFERER']
    return render_to_response('404.html', { 'back' : back }, context_instance=RequestContext(request))

@login_required
def updateDemerit(request):
    if request.method == 'POST':
        demerit = request.POST['demerit']
        if demerit == 'bigot':
            p = PersonD.objects.get(id=request.POST['person'])
            d = p.demerits[request.POST['demerit']]
            p.demerits.update(bigot=d+1)
            p.save()
        elif demerit == 'shoboating':
            p = PersonD.objects.get(id=request.POST['person'])
            d = p.demerits[request.POST['demerit']]
            p.demerits.update(shoboating=d+1)
            p.save()
        elif demerit == 'sassin':
            p = PersonD.objects.get(id=request.POST['person'])
            d = p.demerits[request.POST['demerit']]
            p.demerits.update(sassin=d+1)
            p.save()
        elif demerit == 'ignuntz':
            p = PersonD.objects.get(id=request.POST['person'])
            d = p.demerits[request.POST['demerit']]
            p.demerits.update(ignuntz=d+1)
            p.save()
        elif demerit == 'insurrection':
            p = PersonD.objects.get(id=request.POST['person'])
            d = p.demerits[request.POST['demerit']]
            p.demerits.update(insurrection=d+1)
            p.save()
        elif demerit == 'isolationism':
            p = PersonD.objects.get(id=request.POST['person'])
            d = p.demerits[request.POST['demerit']]
            p.demerits.update(isolationism=d+1)
            p.save()
        elif demerit == 'demilitarization':
            p = PersonD.objects.get(id=request.POST['person'])
            d = p.demerits[request.POST['demerit']]
            p.demerits.update(demilitarization=d+1)
            p.save()
    return HttpResponseRedirect('/')

@login_required
def removeD(request):
    return HttpResponseRedirect('/')

@login_required
def addUser(request):
    if request.method == 'POST':
        pname = request.POST['pname']
        if pname == "":
	    return HttpResponseRedirect('/')
        adduser = PersonD(name=pname)
        dd=['demilitarization','isolationism','insurrection','ignuntz','sassin','shoboating','bigot']
        adduser.demerits.update(demilitarization=0)
        adduser.demerits.update(isolationism=0)
        adduser.demerits.update(insurrection=0)
        adduser.demerits.update(ignuntz=0)
        adduser.demerits.update(sassin=0)
        adduser.demerits.update(shoboating=0)
        adduser.demerits.update(bigot=0)
        adduser.save()
    return HttpResponseRedirect('/')

