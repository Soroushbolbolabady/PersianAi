from django.urls import path
from .views import ResultView , SearchArticleView

app_name = 'sonicresult'


urlpatterns=[
    path('', SearchArticleView.as_view() , name = 'search_form'),
    path('result/', ResultView.as_view() , name = 'result'),

]