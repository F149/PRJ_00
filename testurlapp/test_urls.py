from django.urls import path
from testurlapp import views


urlpatterns = [
    path('user/<int:month>/<int:year>/', views.home, name='home'),
]

