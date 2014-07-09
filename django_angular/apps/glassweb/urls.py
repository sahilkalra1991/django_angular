from django.conf.urls import patterns, url
from django.views.decorators.csrf import ensure_csrf_cookie

from .views import HomeView

urlpatterns = patterns(
    '',
    (r'^$', ensure_csrf_cookie(HomeView.as_view())),
)

