from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login/', 'rest_framework.authtoken.views.obtain_auth_token')
)
