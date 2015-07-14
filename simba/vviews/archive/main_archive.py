from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from simba.models import UserProfile
from simba.vviews.actions.user_actions import is_sec
import datetime 



@login_required
@user_passes_test(is_sec, login_url='/simba/dashboard/?action=perm_denied') #Only sec can access this
def archive(request, type="all"):
	context_dict = {}
	n_waiting = UserProfile.objects.filter(status=False).count()
	date = datetime.datetime.now() + datetime.timedelta(days=90)
	
	
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
		#profile_list = UserProfile.objects.filter(wifi_pending=True)
		profile_list = UserProfile.objects.filter(user__date_joined__gte=date, wifi_access=0)
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
