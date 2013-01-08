from django.shortcuts import render_to_response
from apps.data.models import Entry

def index(request):
	entries = Entry.objects.published_entries().order_by('-id')
	ctx = { 'entries':entries }
	return render_to_response('homepage/index.html', ctx)
