from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from core import views

urlpatterns = [
    url(r'^random/$', views.MineralRandomView.as_view(), name='random_mineral'),
    url(r'^detail/(?P<pk>([\d]+))/$', views.MineralDetailView.as_view(), name='detail'),
    url(r'^$', views.MineralListView.as_view(), name='home'),
    #url(r'^$', views.HomepageView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
