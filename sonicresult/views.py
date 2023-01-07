from django.shortcuts import render
from django.views.generic import TemplateView
from .services import main


# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {
            'result': main()
        }
        return context
