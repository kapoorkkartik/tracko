from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import SignUpForm,ContactForm

# Create your views here.

def home(request):
	title = "Search Instantly"
	context = {
		'title' : title,
	}
	return render(request,"home.html",context)


def contact(request):
	contact = 'Contact Us'
	form = ContactForm(request.POST or None)
	if form.is_valid():
		email =  form.cleaned_data.get("email")
		full_name =  form.cleaned_data.get("full_name")
		message =  form.cleaned_data.get("message")
		subject = 'Welcome to tracko'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email]
		contact_message = "%s:%s via %s" %(full_name,
			message,
			from_email)
		send_mail(subject,
			contact_message,
			from_email,
			to_email,
			fail_silently=True)

	context = {'form':form,'title':contact}
	return render(request,"forms.html",context)