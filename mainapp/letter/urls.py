from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('letters', views.AllLettersView.as_view(), name='letters'),
    path('letter', views.LetterCreate.as_view(), name='write'),
    path('letters/<int:pk>', views.LetterDetailView.as_view(), name='letter-detail')
]
