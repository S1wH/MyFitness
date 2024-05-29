from django.contrib import admin
from .models import Coach, Client, User, ActivationCode


admin.site.register(Coach)
admin.site.register(Client)
admin.site.register(User)
admin.site.register(ActivationCode)
