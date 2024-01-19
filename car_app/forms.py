from django import forms 
from car_app.models import Car, Comment,Job_seeker 

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

class jobsekeerFrom(forms.ModelForm):
    class Meta:
        model=Job_seeker
        fields='__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'text']

  