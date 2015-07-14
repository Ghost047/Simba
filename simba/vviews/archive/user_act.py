from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from simba.forms import CourseForm, UserForm, UserProfileForm, BetaCodeForm
from simba.models import Course, UserProfile, BetaCode
from reportlab.pdfgen import canvas
import string
import random
from io import BytesIO, StringIO
from django.template.loader import render_to_string
from django.template import RequestContext


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

@login_required
def invitations(request):
	context_dict = {}
	invited = False
	code = id_generator()
	invite_list = BetaCode.objects.all()[:10]

	link = 'http://127.0.0.1:8000/register/'+code
	mess = 'Link registrazione best Napoli '+link
	
	##TODO Access allowed at board members only
	if request.method == 'POST':
		form = BetaCodeForm(data=request.POST)

		if form.is_valid():
			invite = form.save(commit=False)
			invite.code = code
			invite.save()
			invited = True
			send_mail('[Simba]RegLink', mess, 'best@cos.com',[invite.email], fail_silently=False)
			context_dict['feedback'] = "success"
			context_dict['msg'] = code

		else:
			print form.errors 
			context_dict['feedback'] = "error"

	else:
		form = BetaCodeForm()


	render_page = "simba/archive/beta.html" 
	context_dict ['form'] = form
	context_dict ['list'] = invite_list
	return render(request, render_page, context_dict)

@login_required
def activate(request, user_no):
	context_dict = {}
	
	##TODO Access allowed at board members only
	user = User.objects.get(id = user_no)
	user_profile = UserProfile.objects.get(user=user)
	user_profile.status = 1
	user.is_active = 1
	user.save()
	user_profile.save()
	
	return HttpResponseRedirect('/simba/archive/pending?action=success')

@login_required
def unarm(request, user_no):
	context_dict = {}
	
	##TODO Access allowed at board members only
	user = User.objects.get(id = user_no)
	user_profile = UserProfile.objects.get(user=user)
	if user_profile.user == request.user :
		return HttpResponseRedirect('/simba/archive/active?action=noaction')
		
	user_profile.status = 0
	user.is_active = 0
	user.save()
	user_profile.save()
	
	return HttpResponseRedirect('/simba/archive/active?action=success')

@login_required
def kill(request, user_no):
	context_dict = {}
	
	##TODO Access allowed at board members only
	user = User.objects.get(id = user_no)
	user.delete()
	
	return HttpResponseRedirect('/simba/archive/pending?action=success')


@login_required
def modulo(request, user_no):
	context_dict = {}

	user = User.objects.get(id = user_no)
	user_profile = UserProfile.objects.get(user=user)
	course = user_profile.course
	
	context_dict ['profile'] = user_profile
	context_dict ['course'] = user_profile.course
	
    	robaccia = render(request, 'simba/documents/model.html', context_dict)

    	myfile = StringIO.StringIO()
    	pisa.CreatePDF(robaccia, myfile)
    	myfile.seek(0)
    	response =  HttpResponse(myfile, mimetype='application/pdf')
    	response['Content-Disposition'] = 'attachment; filename=coupon.pdf'
    	return response
'''
@login_requred
@user_passes_test(is_sec, login_url='/simba/dashboard/?action=perm_denied') #Only sec can access this
def invite(request):
	context_dict={}
	
	request.POST.

	'''
