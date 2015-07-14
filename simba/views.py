from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from simba.forms import CourseForm, UserForm, UserProfileForm
from simba.models import Course, UserProfile
from reportlab.pdfgen import canvas

current_simba_version = "0.9 Beta - Unstable"

'''
@login_required
def dash(request):
	context_dict = {}

	if request.user.is_authenticated():
		context_dict['user_name'] = request.user.username

		try:
			profile = UserProfile.objects.get(user = request.user)	
			context_dict['profile'] = profile			

		except UserProfile.DoesNotExist:
			pass
	else:
		return HttpResponseRedirect('/simba/')

	
	return render(request, 'simba/dashboard/dashboard.html', context_dict)
'''
def index(request):
	context_dict = {}

	
	if request.user.is_authenticated():
		return HttpResponseRedirect('dashboard/')
	else:

		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(username=username, password=password)

			if user:
				if user.is_active:
					login(request,user)
					return HttpResponseRedirect('/simba/')
				else:
					return HttpResponse("Your Account is disabled");

			else:
				print "Invalid login details: {0}, {1}".format(username, password)
				return HttpResponse("invalid login details supplied")	
		else:
			return render(request, 'simba/index.html', context_dict)

	return render(request, 'simba/index.html', context_dict)

def about(request):
	context_dict = {}
	
	context_dict['version'] = current_simba_version
	
	return render(request, 'simba/about.html', context_dict)

def course(request, course_name_slug):
	context_dict = {}

	try:
		course = Course.objects.get(slug=course_name_slug)
		context_dict['course_name'] = course.name
		
		users = UserProfile.objects.filter(course=course)
		
		context_dict ['users'] = users
		context_dict['course'] = course
		

	except Course.DoesNotExist:
		pass
	return render(request, 'simba/course.html', context_dict)

@login_required
def add_course(request):
	if request.method == 'POST':
		form = CourseForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print form.errors

	else:
		form = CourseForm()

	return render(request, 'simba/add_course.html', {'form':form})
'''
def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		course_form = CourseForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			profile.save()
			registered = True

		else:
			print user_form.errors, profile_form.errors

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request, 'simba/register.html', 
			{'user_form':user_form, 'profile_form':profile_form, 'registered': registered})


def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect('/simba/')
			else:
				return HttpResponse("Your Account is disabled");

		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("invalid login details supplied")	
	else:
		return render(request, 'simba/login.html', {})


@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/simba/')


def is_sec(user):
    return user.groups.filter(name='Secretary').exists()

@login_required
@user_passes_test(is_sec, login_url='/simba/dashboard/?action=error')
def archive(request, type="all"):
	context_dict = {}
	n_waiting = UserProfile.objects.filter(status=False).count()
	
	##TODO Access allowed at board members only
	if type == "all":
		profile_list = UserProfile.objects.all()
		context_dict['tab_title'] = "Soci registrati"
		render_page = 'simba/archive/archive_all.html'
	elif type == "active":
		profile_list = UserProfile.objects.filter(status=True)
		context_dict['tab_title'] = "Soci attivi"
		render_page = 'simba/archive/archive_active.html'
	elif type == "pending":
		profile_list = UserProfile.objects.filter(status=False)
		context_dict['tab_title'] = "Soci in attesa di attivazione"
		render_page = 'simba/archive/archive_pending.html'
	
	elif type == "wifi":
		profile_list = UserProfile.objects.filter(wifi_pending=True)
		context_dict['tab_title'] = "Soci in attesa del Wi-Fi"
		render_page = 'simba/archive/archive_w_pending.html'
		
	paginator = Paginator(profile_list, 25)

	page = request.GET.get('page')
	try:
		profiles = paginator.page(page)
	except PageNotAnInteger:
		profiles = paginator.page(1)
	except EmptyPage:
		profiles = pagintor.page(paginator.num_pages)	
		
	context_dict ['profiles'] = profiles	
	context_dict ['feedback'] = request.GET.get('action')
	
	if n_waiting > 0:
		context_dict ['n_waiting'] = n_waiting

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

   

# Create your views here.

