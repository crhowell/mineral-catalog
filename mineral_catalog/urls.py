from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin

from core import views


urlpatterns = [
    url(r'^random/$', views.MineralRandomView.as_view(), name='random_mineral'),
    url(r'^detail/(?P<pk>([\d]+))/$', views.MineralDetailView.as_view(), name='detail'),
    url(r'^search/?(?P<term>[\w]+)?/$', views.MineralSearchForView.as_view(), name='search_for'),
    url(r'^by-letter/(?P<name>[\w])/$', views.MineralByLetterListView.as_view(), name='by_letter'),
    url(r'^by-group/(?P<group>[\w-]+)/$', views.MineralByGroupListView.as_view(), name='by_group'),
    url(r'^by-color/(?P<color>[\w-]+)/$', views.MineralByColorListView.as_view(), name='by_color'),
    url(r'^$', views.MineralListView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

