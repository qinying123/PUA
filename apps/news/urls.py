from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('<int:news_id>/',views.news_detail,name='news_detail'),
    path('list/',views.news_list,name='news_list')
]