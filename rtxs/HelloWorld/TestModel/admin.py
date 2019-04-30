# Register your models here.
from django.contrib import admin
from TestModel.models import Test, Contact, Tag

admin.site.register([Test, Contact, Tag])


class ContactAdmin(admin.ModelAdmin):
    fields = ('name', 'email')

admin.site.register(Contact, ContactAdmin)
admin.site.register([Test, Tag])


