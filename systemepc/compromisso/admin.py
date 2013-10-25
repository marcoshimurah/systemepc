from django.contrib import admin
from compromisso.models import Status, Projeto, Reuniao, Compromisso

admin.site.register(Status)
admin.site.register(Projeto)
admin.site.register(Reuniao)
admin.site.register(Compromisso)
