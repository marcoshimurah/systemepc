from django.views.generic import ListView
from compromisso.models import Compromisso


class CompromissoListView(ListView):
	model = Compromisso