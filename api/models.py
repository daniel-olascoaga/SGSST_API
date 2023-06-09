from django.db import models

# Create your models here.

class Risk(models.Model):

  environment = models.CharField(max_length=150)
  levelRisk = models.CharField(max_length=150)
  probablity = models.PositiveSmallIntegerField(default=1)
  gravity = models.PositiveSmallIntegerField(default=1)
  description = models.TextField()
  actions = models.TextField()

  def __str__(self):
    return self.environment

class Worker(models.Model):
  name = models.CharField(max_length=100)
  lastname = models.CharField(max_length=100)
  age = models.IntegerField()
  sex = models.CharField(max_length=100)
  email = models.EmailField(unique=True)
  phone = models.IntegerField(unique=True)
  address = models.CharField(max_length=100)
  profession = models.CharField(max_length=100)
  roleInCompany = models.CharField(max_length=100)
  risks = models.ManyToManyField(Risk)
  created_at = models.DateTimeField(auto_now_add = True)

  def __str__(self):
    return self.name

class Company(models.Model):
  nit = models.CharField(max_length=20, unique=True)
  name = models.CharField(max_length=150)
  email = models.EmailField(unique=True)
  phone = models.IntegerField(unique=True)
  address = models.CharField(max_length=100, unique=True)
  password = models.CharField(max_length=100)
  workers = models.ForeignKey(Worker, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add = True)

  def __str__(self):
    return self.nit