from django.contrib import admin
from board.models import PersonD

class AdminPerson(admin.ModelAdmin):
    pass
admin.site.register(PersonD, AdminPerson)
