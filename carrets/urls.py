from django.conf.urls import url
from carrets import views

urlpatterns = [
    url(r'^actualitzar_carret/(?P<idNau>[0-9]+)/$', views.actualitzar_carret, name='actualitzarCarret'),
    url(r'^veure_comanda/$', views.veure_comanda, name='veureComanda'),
    url(r'^veure_comanda/confirmar_carret/$', views.confirmar_carret, name='confirmarCarret'),
    url(r'^veure_comanda/esborrar_linia/(?P<idNau>[0-9]+)/$', views.esborrar_linia, name='esborrarLinia'),
    url(r'^veure_comanda/esborrar_comanda/$', views.esborrar_comanda, name='esborrarComanda'),
    url(r'^llista_comandes/$', views.llista_comandes, name='llistaComandes'),
    url(r'^llista_comandes/detall/(?P<comanda_id>[0-9]+)/$', views.detall_comanda, name='detallComanda')
]