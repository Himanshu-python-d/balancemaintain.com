from django.contrib import admin
from .models import Signup, Transaction
# Register your models here.

@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    class Meta:
        model = Signup
        fields = '__all__'

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    class Meta:
        model = Transaction
        fields = '__all__'  
