from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	meetups = [
	{
		"title": "A First Meetup",
		"location": "New York",
		"slug": "a-first-meetup"
	},
	{
		"title": "A Second Meetup",
		"location": "Paris",
		"slug": "a-second-meetup"
	},
	]
	return render(request, "meetups/index.html", {
		"show_meeting" : False,
		"meetups": meetups
		})

def meetup_details(request, meetup_slug):
	selected_meetup = {'title': "A First Meetup", "description": 'This is the first meetup!'}
	return render(request, "meetups/meetups-details.html", {
	'meetup_title': selected_meetup["title"],
	'meetup_description': selected_meetup["description"]
	})
