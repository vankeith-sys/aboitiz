from django.urls import path
from . import views

urlpatterns = [
    path('',views.AP_PaymentView.as_view()),
]
