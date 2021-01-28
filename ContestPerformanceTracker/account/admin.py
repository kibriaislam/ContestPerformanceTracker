from django.contrib import admin
#from django.contrib.auth import get_user_model
from .models import Account,AccountManager
# Register your models here.
admin.site.register(Account)