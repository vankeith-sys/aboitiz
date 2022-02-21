from django.urls import path
from . import views

urlpatterns = [
    path('payment/',views.AP_PaymentView.as_view()),
    path('daily-report/', views.DailyCollectionReport.as_view(), name='Daily Collection Report'),
]
