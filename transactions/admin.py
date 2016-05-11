from django.contrib import admin

from .models import Fund, Fpayment, Adult


class FpaymentInline(admin.TabularInline):
    model = Fpayment
    extra = 3
    
    
class FundAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['adult_id','kid_id']}),
        ('Promise of Faith', {'fields': ['Promise_of_Faith_No_of_Seats','Promise_of_Faith_Period','Promise_of_Faith_Total'], 'classes': ['collapse']}),
    ]
    inlines = [FpaymentInline]
    list_per_page = 20
    search_fields = ("adult_id", "kid_id",)
    list_filter = ('adult_id','kid_id','Promise_of_Faith_No_of_Seats','Promise_of_Faith_Period','Promise_of_Faith_Total')
    list_display = ('id','adult_id', 'kid_id','Promise_of_Faith_No_of_Seats','Promise_of_Faith_Period','Promise_of_Faith_Total')


class FpaymentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['fund_id']}),
        ('Commitment', {'fields': ['Payment_of_period','Payment_of_value'], 'classes': ['collapse']}),
    ]
    list_display = ('adult_name','kid_name','Payment_of_period','Payment_of_value')
    list_per_page = 20
    raw_id_fields = ('fund_id',)
    list_filter = ('fund_id','Payment_of_period')
    search_fields = ("Payment_of_period",)


admin.site.register(Fund, FundAdmin)
admin.site.register(Fpayment,FpaymentAdmin)