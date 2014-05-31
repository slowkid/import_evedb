from django.db import models
from django.contrib import admin

from models import Invtypes, Invtypematerials, Dgmeffects

class InvtypematerialsAdmin(admin.ModelAdmin):
    list_display = ('typeid','materialtypeid','quantity')

admin.site.register(Invtypes)
admin.site.register(Invtypematerials, InvtypematerialsAdmin)
admin.site.register(Dgmeffects)
