from rest_framework import serializers
from base.models import AP_Payment

class AP_PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AP_Payment
        fields = '__all__'