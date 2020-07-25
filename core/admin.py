from django.contrib import admin
from core.models import Attack

# Register your models here.

class AttackInsert(admin.ModelAdmin):
    list_display = ('nameAttack', 'descritionAttack', 'featureAttack')
    list_filter = ('nameAttack',)

admin.site.register(Attack, AttackInsert)