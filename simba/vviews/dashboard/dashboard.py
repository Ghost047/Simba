from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from simba.models import UserProfile

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

	
