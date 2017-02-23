
from django import forms

from .models import PersonalInfo

class PersonalInfoForm(forms.ModelForm):
	class Meta:
		model = PersonalInfo
		fields = ('name','address','phone_num','profile_picture')
