from django.urls import path
from . import views

urlpatterns = [
    path('news', views.NewsListView.as_view()),
    path('types', views.TypeListView.as_view()),
    path('create/type', views.TypeCreateView.as_view()),
    path('create/news', views.NewsCreateView.as_view()),
    path('news/<int:pk>', views.NewsUpdateView.as_view()),
    path('news/<int:pk>/delete', views.NewsDeleteView.as_view()),
    path('types/<str:pk>', views.TypeUpdateView.as_view()),
    path('types/<str:pk>/delete', views.TypeDeleteView.as_view()),
]