from django.db import models
import datetime


class DomainNameServer(models.Model):
    address = models.CharField(primary_key=True, max_length=40, blank=True) #адрес ДНС сервера


class Client(models.Model):
    login = models.CharField(primary_key=True, max_length=30,unique=True, null=False, blank=True)
    password = models.CharField(max_length=30, null=False, blank=True)
    dns_server = models.ManyToManyField(DomainNameServer, blank=True) # доступные ДНС серверы


class Website(models.Model):
    name = models.CharField(primary_key=True,  max_length=50, null=False, blank=True) # адрес сайта
    address = models.CharField(max_length=40, null=False, blank=True) # IP-адрес сайта
    owner = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='website') # связь с владельцем
    expires = models.DateTimeField(default=datetime.datetime.today() + datetime.timedelta(days=30)) # дата и время окончания аренды
