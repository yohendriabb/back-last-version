from django.contrib import admin
from .models import PostAttachment, Reserve, Specialty, Doctor, Date, Services

admin.site.register(Reserve)
admin.site.register(PostAttachment)
admin.site.register(Doctor)
admin.site.register(Specialty)
admin.site.register(Services)

class DateAdmin(admin.ModelAdmin):
    list_display  = ['name', 'id', 'email', 'phone', 'date_at',]



admin.site.register(Date, DateAdmin)