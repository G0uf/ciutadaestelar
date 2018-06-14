from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import ensure_csrf_cookie
from django.forms import modelform_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from django.contrib import messages
from naus.models import Nau, Arma, Misil, Fabricant
import json

@ensure_csrf_cookie
def inici(request):
     return render(request, 'naus/index.html')

def wiki(request):
    lista_naus=Nau.objects.all().order_by('nom')
    lista_armes=Arma.objects.all().order_by('nom')
    lista_misils=Misil.objects.all().order_by('nom')
    lista_fabricants=Fabricant.objects.all().order_by('nom')
    context= {'lista_naus':lista_naus,'lista_armes':lista_armes,'lista_misils':lista_misils,'lista_fabricants':lista_fabricants}
    return render(request,'naus/wiki.html',context)
    
def botiga(request):
    lista_naus=Nau.objects.all().order_by('nom')
    context= {'lista_naus':lista_naus}
    return render(request,'naus/botiga.html',context)

def joc(request):
    return render(request, 'naus/descarga.html')

#VISTES DE NAU

@user_passes_test(lambda u:u.is_staff, login_url='/login/') 
def naus(request):
    lista_naus=Nau.objects.all().order_by('nom')
    context= {'lista_naus':lista_naus}
    return render(request, 'naus/nau/naus.html', context)
    
def infonau(request):
    info=json.loads(request.body)
    nau=Nau.objects.get(pk=info['id'])
    infoitem={'nom':nau.nom,'resum':nau.descripcio,'video':nau.video}
    resposta=json.dumps({'resposta':infoitem});
    return HttpResponse(resposta,content_type='application/json'); 

def nau(request,idNau):
    nau= get_object_or_404(Nau, pk = idNau)
    return render(request, 'naus/nau/nau.html', {"Nau":nau})

@user_passes_test(lambda u:u.is_staff, login_url='/login/')    
def editanau(request, idNau = None):
    esModificacio = (idNau!=None)
    formCreaNau = modelform_factory(Nau,exclude=())
    if esModificacio:
        nau = get_object_or_404(Nau, pk = idNau)
    else:
        nau = Nau()
    if request.method=='POST':
        form = formCreaNau(request.POST,request.FILES,instance=nau)
        if form.is_valid():
            nau=form.save()
            messages.success(request,'La nau s\'ha desat correctament')
            return HttpResponseRedirect(reverse('ciutadaestelar:naus'))
        else:
            messages.error(request,'Hi ha errors en el formulari')
    else:
        form = formCreaNau(instance=nau)
    form.helper=FormHelper()
    form.helper.form_class='blueForms'
    form.helper.label_class='col-lg-2'
    form.helper.field_class='col-lg-10'
    form.helper.add_input(Submit('submit','Desar'))
    return render(request,'formularis/form.html',{'form':form})
    
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def eliminanau(request,idNau):
    nau=get_object_or_404(Nau,pk = idNau)
    nau.delete()
    messages.success(request,'La nau s\'ha eliminat correctament')

    return HttpResponseRedirect(reverse('ciutadaestelar:naus'))
    
#VISTES DE ARMA

@user_passes_test(lambda u:u.is_staff, login_url='/login/') 
def armes(request):
    lista_armes=Arma.objects.all().order_by('nom')
    context= {'lista_armes':lista_armes}
    return render(request, 'naus/arma/armes.html', context)
    
def arma(request,idArma):
    arma= get_object_or_404(Arma, nom = idArma)
    return render(request, 'naus/arma/arma.html', {"Arma":arma})

@user_passes_test(lambda u:u.is_staff, login_url='/login/')    
def editaarma(request, idArma = None):
    esModificacio = (idArma!=None)
    formCreaArma = modelform_factory(Arma,exclude=())
    if esModificacio:
        arma = get_object_or_404(Arma, pk = idArma)
    else:
        arma = Arma()
    if request.method=='POST':
        form = formCreaArma(request.POST,request.FILES,instance=arma)
        if form.is_valid():
            arma=form.save()
            messages.success(request,'L\'arma s\'ha desat correctament')
            return HttpResponseRedirect(reverse('ciutadaestelar:armes'))
        else:
            messages.error(request,'Hi ha errors en el formulari')
    else:
        form = formCreaArma(instance=arma)
    
    form.helper=FormHelper()
    form.helper.form_class='blueForms'
    form.helper.label_class='col-lg-2'
    form.helper.field_class='col-lg-10'
    form.helper.add_input(Submit('submit','Desar'))
    return render(request,'formularis/form.html',{'form':form})
    
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def eliminaarma(request,idArma):
    arma=get_object_or_404(Arma, pk = idArma)
    arma.delete()
    messages.success(request,'L\'arma s\'ha eliminat correctament')

    return HttpResponseRedirect(reverse('ciutadaestelar:armes'))
    
#VISTES DE MISIL

@user_passes_test(lambda u:u.is_staff, login_url='/login/') 
def misils(request):
    lista_misils=Misil.objects.all().order_by('nom')
    context= {'lista_misils':lista_misils}
    return render(request, 'naus/misil/misils.html', context)
    
def misil(request,idMisil):
    misil= get_object_or_404(Misil, pk = idMisil)
    return render(request, 'naus/misil/misil.html', {"Misil":misil})

@user_passes_test(lambda u:u.is_staff, login_url='/login/')    
def editamisil(request, idMisil = None):
    esModificacio = (idMisil!=None)
    formCreaMisil = modelform_factory(Misil,exclude=())
    if esModificacio:
        misil = get_object_or_404(Misil, pk = idMisil)
    else:
        misil = Misil()
    if request.method=='POST':
        form = formCreaMisil(request.POST,request.FILES,instance=misil)
        if form.is_valid():
            misil=form.save()
            messages.success(request,'El misil s\'ha desat correctament')
            return HttpResponseRedirect(reverse('ciutadaestelar:misils'))
        else:
            messages.error(request,'Hi ha errors en el formulari')
    else:
        form = formCreaMisil(instance=misil)
    
    form.helper=FormHelper()
    form.helper.form_class='blueForms'
    form.helper.label_class='col-lg-2'
    form.helper.field_class='col-lg-10'
    form.helper.add_input(Submit('submit','Desar'))
    return render(request,'formularis/form.html',{'form':form})
    
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def eliminamisil(request,idMisil):
    misil=get_object_or_404(Misil,pk = idMisil)
    misil.delete()
    messages.success(request,'El misil s\'ha eliminat correctament')

    return HttpResponseRedirect(reverse('nau:misils'))
        
#VISTES DE FABRICANT

@user_passes_test(lambda u:u.is_staff, login_url='/login/') 
def fabricants(request):
    lista_fabricants=Fabricant.objects.all().order_by('nom')
    context= {'lista_fabricants':lista_fabricants}
    return render(request, 'naus/fabricant/fabricants.html', context)
    
def fabricant(request,idFabricant):
    fabricant= get_object_or_404(Fabricant, pk = idFabricant)
    return render(request, 'naus/fabricant/fabricant.html', {"Fabricant":fabricant})

@user_passes_test(lambda u:u.is_staff, login_url='/login/')    
def editafabricant(request, idFabricant = None):
    esModificacio = (idFabricant!=None)
    formCreaFabricant = modelform_factory(Fabricant,exclude=())
    if esModificacio:
        fabricant = get_object_or_404(Fabricant, pk = idFabricant)
    else:
        fabricant = Fabricant()
    if request.method=='POST':
        form = formCreaFabricant(request.POST,request.FILES,instance=fabricant)
        if form.is_valid():
            fabricant=form.save()
            messages.success(request,'El fabricant s\'ha desat correctament')
            return HttpResponseRedirect(reverse('ciutadaestelar:fabricants'))
        else:
            messages.error(request,'Hi ha errors en el formulari')
    else:
        form = formCreaFabricant(instance=fabricant)
    
    form.helper=FormHelper()
    form.helper.form_class='blueForms'
    form.helper.label_class='col-lg-2'
    form.helper.field_class='col-lg-10'
    form.helper.add_input(Submit('submit','Desar'))
    return render(request,'formularis/form.html',{'form':form})
    
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def eliminafabricant(request,idFabricant):
    fabricant=get_object_or_404(Fabricant,pk = idFabricant)
    fabricant.delete()
    messages.success(request,'El fabricant s\'ha eliminat correctament')

    return HttpResponseRedirect(reverse('nau:fabricants'))