from django.conf.urls.static import static
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from usuaris import views as logins

urlpatterns = (
    [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('naus.urls', namespace="ciutadaestelar")),
    url(r'^carret/', include('carrets.urls', namespace="carrets")),
    url(r'^perfil/$', logins.vista_perfil, name="perfil"),
    url(r'^perfil/restaurar/$', logins.vista_reset, name="restaurarContrasenya"),
    url(r'^backups/', include('backups.urls', namespace="backups")),
    url(r'^login/$', logins.vista_login, name="login"),
    url(r'^logout/$', logins.vista_logout, name="logout"),
    url(r'^registre/$', logins.vista_registre, name="registre"),
    url(r'^hangar/$', logins.vista_hangar, name="hangar"),
    url(r'^taller/$', logins.modifica_nau, name="taller"),
    url(r'^venta/$', logins.ven_nau, name="venta")
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
