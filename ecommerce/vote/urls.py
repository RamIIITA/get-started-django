from django.urls import path, reverse
from . import views

#app_name= 'vote'
urlpatterns=[
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:pk>/voting/', views.voting, name='voting'),
]
