from .models import Feedback
from rest_framework import serializers


class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Feedback
