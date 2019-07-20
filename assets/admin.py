from django.contrib import admin
from .models import *


# Register your models here.
class AcAdmin(admin.ModelAdmin):
    readonly_fields = ['pk', 'user', 'amount', 'category', 'description', 'budget', 'income', 'date']

    def has_view_permission(self, request, obj=None):


        if Expense.objects.filter(pk=2) :
                return True
        else:
            return False


admin.site.register(Budget)
admin.site.register(Category)
admin.site.register(Expense, AcAdmin)
