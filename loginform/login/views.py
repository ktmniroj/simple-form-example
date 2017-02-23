from django.http import HttpResponse
from django.shortcuts import render


from .forms import PersonalInfoForm
from .models import PersonalInfo



def personalInfoView(request):
	
	if request.method == 'POST':
		form = PersonalInfoForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponse("form submitted")
	else:
		#template_name = "login.html"
		form = PersonalInfoForm()
	
	context ={'form':form}
	return render(request, 'login.html', context)





