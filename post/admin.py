from django.contrib import admin
from .models import PostAttachment, Reserve, Specialty, Doctor, Date, Services

admin.site.register(Reserve)
admin.site.register(PostAttachment)
admin.site.register(Specialty)

class ServicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug']
admin.site.register(Services, ServicesAdmin)


class DateAdmin(admin.ModelAdmin):
    list_display  = ['name', 'id', 'slug', 'email', 'phone', 'date_at', ]
admin.site.register(Date, DateAdmin)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
admin.site.register(Doctor, DoctorAdmin)