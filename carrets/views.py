from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.forms import modelform_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import user_passes_test
from naus.models import Nau
from carrets.models import Comanda, Linia
from usuaris.models import Hangar
from .forms import edit_carret

def actualitzar_carret(request,idNau):
    nau = get_object_or_404(Nau,pk=idNau)
    if request.method=='POST':
        form = edit_carret(request.POST)
        if form.is_valid():
            if 'carret' not in request.session:
                request.session['carret']={}
            quantitat=form.cleaned_data['quantitat']
            request.session['carret'].update({idNau:quantitat})
            messages.add_message(request,messages.SUCCESS,'El producte s\'ha afegit dins el carret')
            return HttpResponseRedirect(reverse('ciutadaestelar:botiga'))
        else:
            messages.error(request,'Hi ha errors en el formulari')
    else:
        form=edit_carret()

    form.helper=FormHelper()
    return render(request,'carrets/editarcarret.html',{'form':form,'nau':nau})

def veure_comanda(request):
    if 'carret' not in request.session:
        request.session['carret']={}
    cistella=[]
    totDiners=0
    totCredits=0
    for id in request.session['carret']:
        nau=Nau.objects.get(id=id)
        quantitat=request.session['carret'][id]
        preu=nau.preu*quantitat
        totDiners+=preu
        preuCredits=nau.preucredits*quantitat
        totCredits+=preuCredits
        cistella.append({'nau':nau,
                        'quantitat':quantitat,
                        'preu':preu,
                        'preucredits':preuCredits
                        })
    return render(request,'carrets/carret.html',{'cistella':cistella,'totalDiners':totDiners, 'totalCredits':totCredits})

def esborrar_linia(request,idNau):
    request.session.modified=True
    producte=request.session['carret']
    if idNau in producte:
        del producte[idNau]
    return HttpResponseRedirect(reverse('carrets:veureComanda'))
    
def esborrar_comanda(request):
    if 'carret' in request.session:
        request.session['carret']={}
    return HttpResponseRedirect(reverse('carrets:veureComanda'))

@user_passes_test(lambda u:u.is_authenticated(), login_url='/login/')
def confirmar_carret(request):
    formConfirmarCarret = modelform_factory(Comanda,exclude=('comanda_id','usuari','data'))
    comanda=Comanda()
    if request.method == 'POST':
        form=formConfirmarCarret(request.POST,request.FILES,instance=comanda)
        if form.is_valid():
            carrer=form.cleaned_data['carrer']
            poblacio=form.cleaned_data['poblacio']
            codi_postal=form.cleaned_data['codi_postal']
            provincia=form.cleaned_data['provincia']
            pagament=form.cleaned_data['pagament']
            total_credits=0
            if 'carret' in request.session:
                if request.session['carret']:
                    comanda.carrer=carrer
                    comanda.poblacio=poblacio
                    comanda.codi_postal=codi_postal
                    comanda.provincia=provincia
                    comanda.usuari=request.user
                    comanda.pagament=pagament
                    comanda.save()
                    carret=request.session['carret']
                    
                    for id in carret:
                        producte=Nau.objects.get(id=id)
                        quantitat=carret[id]
                        linia=Linia()
                        linia.comanda_id=comanda
                        linia.producte_id=producte
                        linia.quantitat=quantitat
                        linia.preu=producte.preu
                        linia.pagament=pagament
                        linia.save()
                        total_credits+=producte.preu*quantitat
                        request.session['carret']={}
                    if pagament is 'CRE':
                        usuari=request.user
                        hangar=Hangar.objects.get(usuari=usuari)
                        if total_credits < hangar.credits :
                            messages.error(request,'No tens suficients credits')
                            return HttpResponseRedirect(reverse('carrets:veureComanda'))
                    return HttpResponseRedirect(reverse('carrets:llistaComandes'))
                else:
                    messages.error(request,'No hi ha cap producte al carret')
            else:
                return HttpResponseRedirect(reverse('ciutadaestelar:botiga'))
        else:
            messages.error(request,'Hi ha errors en el formulari')
    else:
        form= formConfirmarCarret(instance=comanda)
        
    form.helper=FormHelper()
    form.helper.form_class='blueForms'
    form.helper.label_class='col-lg-2'
    form.helper.field_class='col-lg-10'
    form.helper.add_input(Submit('submit','Finalitzar compra'))
    return render(request,'carrets/confirmar-carret.html',{'form':form})
    
@user_passes_test(lambda u:u.is_authenticated(), login_url='/login/')
def llista_comandes(request):
    comandes=Comanda.objects.filter(usuari=request.user)
    return render(request, 'carrets/llista_comandes.html',{'comandes':comandes})
    
@user_passes_test(lambda u:u.is_authenticated(), login_url='/login/')
def detall_comanda(request,comanda_id):
    preu_comanda=0
    pagament = None
    comanda=[]
    linias =Linia.objects.filter(comanda_id=comanda_id)
    for linia in linias.all():
        nau=Nau.objects.get(id=linia.producte_id.id)
        quantitat=linia.quantitat
        preu=linia.preu*quantitat
        preu_comanda+=preu
        pagament=linia.pagament
        comanda.append({'nau':nau,
                        'quantitat':quantitat,
                        'preu':preu
                        })
    return render(request,'carrets/detall.html',{'comanda':comanda,'preu_comanda':preu_comanda,'pagament':pagament})