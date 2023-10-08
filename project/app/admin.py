from django.contrib import admin
from app.models import User,Message,PrivateMessage

# Register your models here.
admin.site.register(User)
admin.site.register(PrivateMessage)