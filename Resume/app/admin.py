from django.contrib import admin
from .models import ResumeModel

# Register your models here.
@admin.register(ResumeModel)
class ResumeAdmin(admin.ModelAdmin):
    list_display=['id','name','address','email','phone','education','skills','photo','projects']
