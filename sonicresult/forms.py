from django import forms
from .services import main


class SearchArticleForm(forms.Form):
    text = forms.CharField()

    def send_to_ai(self):
        main(self.data['text'])
