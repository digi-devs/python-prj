from rest_framework import serializers
from companyAPI.models import CompanyModel

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = "__all__"