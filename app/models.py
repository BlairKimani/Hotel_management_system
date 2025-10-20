from django.db import models
from django.contrib.auth.models import AbstractUser
import random
import datetime as dt
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=200)
    service_description = models.TextField(blank=True, null=True, max_length=200)
    service_price = models.FloatField(blank=True, null=True, max_length=200)

    class Meta:
        db_table = 'Service'

class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_type = models.CharField( max_length=200)
    bed_type = models.CharField(max_length=200)
    price_per_night = models.FloatField( max_length=200)
    availabilty_status = models.IntegerField()
    max_occupation = models.IntegerField()

    class Meta:
        db_table = 'Room'

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    contact = models.CharField(max_length=15, blank=True)
    gender = models.TextField(max_length=200)
    salary = models.FloatField(blank=True, null=True, max_length=200)
    role = models.CharField(blank=True, null=True, max_length=200)
    service = models.ForeignKey('Service', models.DO_NOTHING, blank=True, null=True)
    id_no = models.IntegerField(unique=True, blank=True, null=True)  

    USERNAME_FIELD = 'email'         # Use email to log in
    REQUIRED_FIELDS = ['username']   # Required when creating superuser

    def __str__(self):
        return self.email

class AppCustomuser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField()
    date_joined = models.DateTimeField(default=str(dt.datetime.now()))
    email = models.CharField(unique=True, max_length=254)
    contact = models.CharField(max_length=15)
    gender = models.TextField()
    salary = models.FloatField(blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    id_no = models.IntegerField(unique=True)
    service = models.ForeignKey(Service, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_customuser'


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(AppCustomuser, models.DO_NOTHING, blank=True, null=True)
    room = models.ForeignKey(Room, models.DO_NOTHING, blank=True, null=True)
    check_in_date = models.TextField(blank=True, null=True, max_length=10)
    check_out_date = models.DateField(blank=True, null=True, max_length=10)
    number_of_guests = models.IntegerField(blank=True, null=True)
    total_price = models.FloatField(blank=True, null=True, max_length=200)
    booking_status = models.TextField( max_length=200, default='active')

    class Meta:
        db_table = 'Booking'

class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    item_name = models.CharField(blank=True, null=True, max_length=200)
    category = models.CharField(blank=True, null=True, max_length=200)
    service_time = models.TextField(blank=True, null=True, max_length=20)
    item_description = models.TextField(blank=True, null=True, max_length=200)
    quantity = models.IntegerField(blank=True, null=True)
    price_per_unit = models.FloatField(blank=True, null=True, max_length=200)

    class Meta:
        db_table = 'Inventory'



class ServiceRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(AppCustomuser, models.DO_NOTHING, blank=True, null=True)
    booking = models.ForeignKey(Booking, models.DO_NOTHING, blank=True, null=True)
    service = models.ForeignKey(Service, models.DO_NOTHING, blank=True, null=True)
    request_time = models.DateTimeField(blank=True, null=True, max_length=50, default=str(dt.datetime.now()))
    request_status = models.TextField(max_length=200, default='pending')

    class Meta:
        db_table = 'Service_request'


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(AppCustomuser, models.DO_NOTHING, blank=True, null=True)
    booking = models.ForeignKey(Booking, models.DO_NOTHING, blank=True, null=True)
    service = models.ForeignKey(Service, models.DO_NOTHING, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True, max_length=200)
    payment_time = models.DateTimeField(blank=True, null=True, max_length=50, default=str(dt.datetime.now()))
    payment_mode = models.TextField( max_length=200)
    account = models.IntegerField(null=True, blank=True)
    payment_status = models.TextField( max_length=200, default='paid')

    class Meta:
        db_table = 'payment'

