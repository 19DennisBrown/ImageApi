

from rest_framework import serializers
from .models import Data

class dataSerializer(serializers.ModelSerializer):
  class Meta:
    model = Data
    fields = ['id', 'title', 'date_posted']