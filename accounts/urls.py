from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.accounts, name='login'),
    path('quan_ly_hs/', views.login_accept, name='quan_ly_hs')
]
