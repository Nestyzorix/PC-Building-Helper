from rest_framework import serializers
from .models import Processor


class ProcessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processor
        fields = ['name', 'firm', 'frequency', 'socket', 'core_number', 'price']
