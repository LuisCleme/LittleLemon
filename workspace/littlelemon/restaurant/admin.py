from django.contrib import admin
from .models import Booking, MenuItem
# Register your models here.
models = [Booking, MenuItem]
for model in models:
    admin.site.register(model)