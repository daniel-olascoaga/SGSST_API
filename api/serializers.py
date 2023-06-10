from rest_framework import serializers
from .models import Risk, Worker, Company

class RiskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Risk
    fields = ['id', 'environment', 'levelRisk', 'probablity', 'gravity', 'description', 'actions']

class WorkerSerializer(serializers.ModelSerializer):
  risks = serializers.SerializerMethodField()

  class Meta:
    model = Worker
    fields = ['id','name', 'lastname', 'age', 'sex', 'email', 'phone', 'address', 'profession', 'risks', 'roleInCompany', 'created_at']

    def get_risks(self, obj):
      risks = obj.risks.all()
      return RiskSerializer(risks, many=True).data 

class CompanySerializer(serializers.ModelSerializer):
  workers = WorkerSerializer()

  class Meta:
    model = Company
    fields = ['id', 'nit', 'name', 'email', 'phone', 'address', 'password', 'workers', 'created_at'] 