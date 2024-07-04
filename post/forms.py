from django.forms import ModelForm 
from .models import Reserve, Date, Services, Specialty, Doctor

class ReserveForm(ModelForm):
    class Meta:
        model = Reserve
        fields = (
            'body',
                        
            )
        
class DateForm(ModelForm):
    class Meta:
        model = Date 
        fields = (
            'name',
            'email',
            'phone',
            'date_at',
    )

class SpecialtyForm(ModelForm):
    class Meta:
        model = Specialty 
        fields = (
            'name',
    )

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor 
        fields = (
            'specialty',
            'image',
            'name',
            'description',
    )


class ServicesForm(ModelForm):
    class Meta:
        model = Services 
        fields = (
            'title',
            'description',
            'thumbnails',
            
    )