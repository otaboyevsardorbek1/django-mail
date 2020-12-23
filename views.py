from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

def home(request):
	return render(request, 'home_page.html')



def sendMail(request):
	if request.method == 'POST':
		sender = settings.EMAIL_HOST_USER
		receiver = request.POST['receiver']
		subject = request.POST['sub']
		content = request.POST['content']

		mail = send_mail(subject, content, sender, [receiver], fail_silently=False)
		if mail:
			messages.success(request, 'Email has been sent.')
			return redirect('home')
		else:
			return HttpResponse('message not sent')
	else:
		return redirect('home')