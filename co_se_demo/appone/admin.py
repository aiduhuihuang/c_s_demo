from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id",'username',"password","createtime","isDelete"]

    list_filter = ['username','isDelete','createtime']
    list_per_page = 5