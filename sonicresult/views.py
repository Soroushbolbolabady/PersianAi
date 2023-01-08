from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from .services import main
from .forms import SearchArticleForm


# Create your views here

class SearchArticleView(FormView):
    template_name = 'sonicresult/search_article.html'
    form_class = SearchArticleForm
    success_url = reverse_lazy('sonicresult:result')

    def form_valid(self, form):
        form.send_to_ai()
        return super().form_valid(form)


class ResultView(TemplateView):
    template_name = 'sonicresult/result.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'result': main
        }
        return context
