
from django.urls import re_path
from django.urls import path, include
from wallet_app import views
urlpatterns = [
    re_path(r'^/create$', views.create_wallet.as_view()),
    re_path(r'^/activate$', views.activate_wallet.as_view()),
    re_path(r'^/add-money$', views.add_money.as_view()),
    re_path(r'^/withdraw-money$', views.withdrawal.as_view()),
    re_path(r'^/transaction$', views.transactions.as_view()),
]

