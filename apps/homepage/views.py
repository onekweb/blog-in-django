from django.shortcuts import render_to_response
from apps.data.models import Entry
from django.template import RequestContext
from apps.homepage.forms import ContactForm
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail, mail_admins
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def index(request):
	entries = Entry.objects.published_entries().order_by('-id')
	paginator = Paginator(entries, 2)
	page_num= request.GET.get('page', 1)
	page = paginator.page(page_num)
	ctx = {
		'page':page
		}
	return render_to_response('homepage/index.html', ctx, context_instance=RequestContext(request))

def about(request):
	return render_to_response('homepage/about.html', context_instance=RequestContext(request))

def archive(request):
	return render_to_response('homepage/archive.html', context_instance=RequestContext(request))

def contact(request):
	
	success = False
	email = ""
	title = ""
	text = ""
	
	if request.method == "POST":
		contact_form = ContactForm(request.POST)
		
		if contact_form.is_valid():
			success = True
			email = contact_form.cleaned_data['email']
			title = contact_form.cleaned_data['title']
			text = contact_form.cleaned_data['text']
			send_mail("Your subjtect", "Your text message! Data send:%s %s %s" % (title, text, email), 'mail.from@server.com', ['mario.onekanda@hotmail.com'], fail_silently=True)
			mail_admins("Other subject", "some text", fail_silently = True)
	else:
		contact_form = ContactForm()
	ctx = {'contact_form':contact_form,'email':email, 'title': title, 'text':title, 'success':success}
	return render_to_response('homepage/contact.html', ctx, context_instance=RequestContext(request))

@login_required	
def profile(request):
	ctx = {}
	return render_to_response('homepage/profile.html', ctx, context_instance=RequestContext(request))