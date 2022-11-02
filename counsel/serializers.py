from rest_framework import serializers
from .models import *


class BusinessscheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Businessschedule
        fields = '__all__'


class CounselingmanualSerializer(serializers.ModelSerializer):
    class Meta:
        model = CounselingManual
        fields = '__all__'


class CounselingmanualcommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CounselingManualComment
        fields = '__all__'


class CounselingtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counselingtype
        fields = '__all__'


class SoftwareproductfamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftwareProductFamily
        fields = '__all__'
