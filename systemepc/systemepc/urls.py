from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from companies.views import Novo_compromisso

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),
    (r'^novo_compromisso/', Novo_compromisso.as_view()),
    # Examples:
    # url(r'^$', 'systemepc.views.home', name='home'),
    # url(r'^systemepc/', include('systemepc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
