from django.shortcuts import render
from .models import Meetup
from .forms import RegisterationForm
# Create your views here.

def index(request):
	meetups = Meetup.objects.all()
	return render(request, "meetups/index.html", {
		"meetups": meetups
		})

def meetup_details(request, meetup_slug):
	try:
		if request.method == 'GET':
			selected_meetup = Meetup.objects.get(slug=meetup_slug)
			registration_form = RegisterationForm()
			return render(request, "meetups/meetups-details.html", {
			'meetup_found': True,
			'meetup': selected_meetup,
			'form': registration_form
			})
		else:
			registration_form = RegisterationForm(request.POST) 
	except Exception as exc:
		return render(request,"meetups/meetups-details.html", {
		'meetup_found': False
		})