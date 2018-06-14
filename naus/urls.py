from django.conf.urls import url, include
from naus import views

urlpatterns = [
    #seccio pagina
    url(r'^$', views.inici, name="inici"),
    url(r'^wiki/$', views.wiki, name='wiki'),
    url(r'^botiga/$', views.botiga, name='botiga'),
    #seccio naus
    url(r'^naus/$', views.naus, name='naus'),
    url(r'^nau/', views.infonau, name='infoNau'),
    url(r'^nau/(?P<idNau>.+)/$', views.nau, name="nau"),
    url(r'^afegir_nau/$', views.editanau, name='afegirnau'),
    url(r'^editar_nau/(?P<idNau>.+)/$', views.editanau, name='editarnau'),
    url(r'^eliminar_nau/(?P<idNau>.+)/$', views.eliminanau, name='eliminarnau'),
    #seccio armes
    url(r'^armes/$', views.armes, name='armes'),
    url(r'^arma/(?P<idArma>.+)/$', views.arma, name="arma"),
    url(r'^afegir_arma/$', views.editaarma, name='afegirarma'),
    url(r'^editar_arma/(?P<idArma>.+)/$', views.editaarma, name='editararma'),
    url(r'^eliminar_arma/(?P<idArma>.+)/$', views.eliminaarma, name='eliminararma'),
    #seccio misils
    url(r'^misils/$', views.misils, name='misils'),
    url(r'^misil/(?P<idMisil>.+)/$', views.misil, name='misil'),
    url(r'^afegir_misil/$', views.editamisil, name='afegirmisil'),
    url(r'^editar_misil/(?P<idMisil>.+)/$', views.editamisil, name='editarmisil'),
    url(r'^eliminar_misil/(?P<idMisil>.+)/$', views.eliminamisil, name='eliminarmisil'),
    #seccio fabricants
    url(r'^fabricants/$', views.fabricants, name='fabricants'),
    url(r'^afegir_fabricant/$', views.editafabricant, name='afegirfabricant'),
    url(r'^editar_fabricant/(?P<idFabricant>.+)/$', views.editafabricant, name='editarfabricant'),
    url(r'^eliminar_fabricant/(?P<idFabricant>.+)/$', views.eliminafabricant, name='eliminarfabricant')
    
    
]