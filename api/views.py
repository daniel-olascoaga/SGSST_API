from rest_framework import viewsets
from .models import Risk, Worker, Company
from .serializers import RiskSerializer, WorkerSerializer, CompanySerializer

# Create your views here.
class RiskViewSet(viewsets.ModelViewSet):
  queryset = Risk.objects.all()
  serializer_class = RiskSerializer

class WorkerViewSet(viewsets.ModelViewSet):
  queryset = Worker.objects.all()
  serializer_class = WorkerSerializer

class CompanyViewset(viewsets.ModelViewSet):
  queryset = Company.objects.all()
  serializer_class = CompanySerializer
