from django.contrib import admin
from django.conf.urls import patterns, include, url

from apps.apis import urls as apis_urls
from django.views.decorators.csrf import ensure_csrf_cookie

from django.views.generic.base import TemplateView


# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()


# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns('',
    # Admin panel and documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # REST API URLs
    url(r'^api/', include(apis_urls)),
    url(r'^$', ensure_csrf_cookie(TemplateView.as_view(template_name="home.html")))
)
