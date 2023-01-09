from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from .models import AiData
from .forms import SearchArticleForm
from django.contrib.auth.models import User


# Create your views here

class SearchArticleView(FormView):
    template_name = 'sonicresult/search_article.html'
    form_class = SearchArticleForm
    success_url = reverse_lazy('sonicresult:result')

    def form_valid(self, form):
        search = form.save(commit=False)
        search.user = User.objects.get(username=self.request.user)
        form.save()
        return super().form_valid(form)


class ResultView(TemplateView):
    template_name = 'sonicresult/result.html'

    def get_context_data(self, **kwargs):
        context = {
            'result': AiData.objects.latest('pk')

        }
        return context
