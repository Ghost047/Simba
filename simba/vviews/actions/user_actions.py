import string
import random
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from simba.forms import UserForm, UserProfileForm
from simba.models import UserProfile, BetaCode



def is_sec(user):
    return user.groups.filter(name='Secretary').exists()

def register(request, code=0):
	registered = False
	context_dict = {}
		
	if code == 0:
			print "You need an activation code to access the beta version"
			return HttpResponse("You need an activation code to access the beta version")

	try:
		code = BetaCode.objects.get(code=code)

	except BetaCode.DoesNotExist:
			return HttpResponse("Nice try, code you submitted does not exists")

	if code.valid == 0:
			return HttpResponse("Nice try, code you submitted is not valid anymore")

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

	context_dict ['user_email'] = code.email
	context_dict ['user_form' ] = user_form
	context_dict ['profile_form'] = profile_form
	context_dict ['registered'] = registered

	return render(request, 'simba/register.html', context_dict)


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

