from django.shortcuts import render, redirect # type: ignore
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
		selected_meetup = Meetup.objects.get(slug=meetup_slug)
		if request.method == 'GET':
			registration_form = RegisterationForm()
		else:
			registration_form = RegisterationForm(request.POST)
		if registration_form.is_valid():
			participant = registration_form.save()
			selected_meetup.participant.add(participant)
			return redirect("confirm-registration")
		return render(request, "meetups/meetups-details.html", {
		'meetup_found': True,
		'meetup': selected_meetup,
		'form': registration_form
		})
	except Exception as exc:
		return render(request,"meetups/meetups-details.html", {
		'meetup_found': False
		})

def confirm_registration(request):
	return render(request, "meetups/registration-success.html")
