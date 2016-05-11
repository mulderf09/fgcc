from django.contrib import admin

from .models import Cell, Role, Kelas, Ministry, Adult, Kid

class AdultAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['first_name','last_name','gender', 'role','cell_group', 'mobile_no','email', 'city','postcode','state','country','is_active']}),
        ('Date information', {'fields': ['date_joined','date_left'], 'classes': ['collapse']}),
        ('Others information', {'fields': ['line1','line2','line3'], 'classes': ['collapse']}),
    ]
    list_filter = ('gender','role','cell_group','country')
    list_per_page = 20
    search_fields = ('first_name',)
    list_display = ('first_name','last_name','gender', 'role', 'cell_group','mobile_no','email', 'city','postcode','state','country', 'date_joined', 'date_left','is_active')
    


class KidAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['first_name','last_name','gender', 'adult_id', 'role_id','cell_id', 'mobile_no','email']}),
        ('Date information', {'fields': ['date_joined','date_left'], 'classes': ['collapse']}),
    ]
    list_filter = ('adult_id','gender','role_id','cell_id')
    list_per_page = 20
    search_fields = ('first_name',)
    list_display = ('first_name','last_name','gender', 'adult_id', 'role_id','cell_id', 'mobile_no','email', 'date_joined', 'date_left')



class CellAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name','area']}),
    ]
    search_fields = ('name',)

class KelasAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['ministry','name','description']}),
    ]
    search_fields = ('name',)
    list_display = ('ministry', 'name', 'description')
    list_filter = ('ministry',)

class MinistryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name','description']}),
    ]
    search_fields = ('name',)
    list_display = ('name', 'description')


admin.site.register(Ministry, MinistryAdmin)
admin.site.register(Adult, AdultAdmin)
admin.site.register(Kid, KidAdmin)
admin.site.register(Kelas, KelasAdmin)
admin.site.register(Cell, CellAdmin)
admin.site.register(Role)