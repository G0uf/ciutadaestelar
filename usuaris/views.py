# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import csrf_protect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from .forms import LoginForm, RegistreForm, CanviarContrasenyaForm
from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404
from usuaris.models import Hangar
from naus.models import Nau

@csrf_protect
def vista_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('ciutadaestelar:inici'))
    else:
        if request.method=='POST':
            form=LoginForm(request.POST)
            if form.is_valid():
                username=form.cleaned_data['usuari']
                password=form.cleaned_data['contrasenya']
                seguent=request.GET.get('next',default=None)
                user=authenticate(username=username,password=password)
                if user is not None:
                    if user.is_active:
                        login(request,user)
                        if bool(seguent):
                            return HttpResponseRedirect(seguent)
                        else:
                            #messages.error(request,'Usuari desactivat')
                            return HttpResponseRedirect(reverse('ciutadaestelar:inici'))
                    else:
                        messages.error(request,'Error, usuari i/o contrasenya són/és incorrectes/e/a')
                        return HttpResponseRedirect(reverse('login'))
                else:
                    messages.error(request,'Hi ha errors en el formulari')
                    return HttpResponseRedirect(reverse('login'))
        else:
            form=LoginForm()
        
    form.helper=FormHelper()
    form.helper.form_class='form-horizontal'
    form.helper.add_input(Submit('submit','Login'))
    return render (request, 'formularis/login.html', {'form':form})

@csrf_protect
def vista_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('ciutadaestelar:inici'))

@csrf_protect
def vista_registre(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('ciutadaestelar:inici'))
    else:
        if request.method=='POST':
            form=RegistreForm(request.POST)
            if form.is_valid():
                cleaned_data=form.cleaned_data
                username=cleaned_data.get('usuari')
                password=cleaned_data.get('contrasenya')
                email=cleaned_data.get('correu')
                User.objects.create_user(username=username,password=password,email=email)
                messages.success(request,'Usuari registrat correctament')
                return HttpResponseRedirect(reverse('login'))
            else:
                messages.error(request,"Hi ha errors en el formulari")
        else:
            form=RegistreForm()
            
    form.helper=FormHelper()
    form.helper.form_class='form-horizontal'
    form.helper.add_input(Submit('submit','Registrar-se'))
    
    return render(request,'formularis/registre.html',{'form':form})
    
@user_passes_test(lambda u:u.is_authenticated(), login_url='/login/')
def vista_perfil(request):
    user=request.user
    context={'user':user}
    return render(request,'perfil.html',context)
    
@user_passes_test(lambda u:u.is_authenticated(), login_url='/login/')
def vista_reset(request):
    if request.method=='POST':
        form = CanviarContrasenyaForm(request.POST)
        if form.is_valid():
            cleaned_data=form.cleaned_data
            password=cleaned_data.get('password')
            user=request.user
            user.set_password(password)
            user.save()
            logout(request)
            messages.success(request,'La clau s\'ha modificat correctament')
            return HttpResponseRedirect(reverse('login'))
        else:
            messages.error(request,"Hi ha errors en el formulari")
    else:
        form=CanviarContrasenyaForm()

    form.helper=FormHelper()
    form.helper.form_class='form-horizontal'
    form.helper.add_input(Submit('submit','Desar'))

    return render(request,'formularis/registre.html',{'form':form})

@user_passes_test(lambda u:u.is_authenticated(), login_url='/login/')
def vista_hangar(request):
    hangar = Hangar.objects.get(usuari = request.user)
    naus_hangar=hangar.naus.all().order_by('nom')
    context= {'naus_hangar':naus_hangar}
    return render(request, 'usuaris/hangar.html', context)

@user_passes_test(lambda u:u.is_authenticated(), login_url='/login/')    
def modifica_nau(request,nau_id = None):
    esNau = (nau_id!=None)
    formModificaNau = modelform_factory(Nau,exclude=('nom','imatge','silueta','descripcio',
                                                    'fabricant','video','salut','escuts',
                                                    'velocitat','disipaciocalor','numarmes',
                                                    'nummisils','preucredits','preu'
                                                    ))
    if esNau:
        nau = get_object_or_404(Nau, pk = nau_id)
    else:
        messages.error(request,'No tens cap nau')
        return HttpResponseRedirect(reverse('usuaris:hangar'))
    if request.method=='POST':
        form = formModificaNau(request.POST,request.FILES,instance=nau)
        if form.is_valid():
            nau=form.save()
            messages.success(request,'La nau s\'ha desat correctament')
            return HttpResponseRedirect(reverse('usuaris:hangar'))
        else:
            messages.error(request,'Hi ha errors en el formulari')
    else:
        form=formModificaNau(instance=nau)

    form.helper=FormHelper()
    form.helper.form_class='blueForms'
    form.helper.label_class='col-lg-2'
    form.helper.field_class='col-lg-10'
    form.helper.add_input(Submit('submit','Desar'))
    return render(request,'formularis/form.html',{'form':form})

@user_passes_test(lambda u:u.is_authenticated(), login_url='/login/')
def ven_nau(request,nau_id):
    nau=get_object_or_404(Nau,pk=nau_id)
    hangar = Hangar.objects.get(usuari = request.user)
    hangar.credits += nau.credits
    hangar.save()
    nau.delete()
    messages.success(request,'El producte s\'ha eliminat correctament')
    return HttpResponseRedirect(reverse('items:items'))