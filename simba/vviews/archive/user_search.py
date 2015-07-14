from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from simba.models import UserProfile
from simba.vviews.actions.user_actions import is_sec

@login_required
@user_passes_test(is_sec, login_url='/simba/dashboard/?action=perm_denied')
def search(request):
	context_dict = {}

	n_waiting = UserProfile.objects.filter(status=False).count()

	k = request.GET.get('key');

	profile_list = UserProfile.objects.filter(user__username__contains=k)
	context_dict['tab_title'] = "Search keyword: "
	context_dict['key'] = k
	render_page = 'simba/archive/search.html'

		
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
