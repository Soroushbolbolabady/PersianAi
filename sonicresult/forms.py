from django.forms import ModelForm
from .services import main
from .models import AiData


class SearchArticleForm(ModelForm):
    class Meta:
        model = AiData
        fields = ('to_ai',)

    def send_to_ai(self):
        main(self.data['to_ai'])
