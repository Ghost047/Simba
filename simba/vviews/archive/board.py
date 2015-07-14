from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from simba.models import UserProfile, Role
from simba.vviews.actions.user_actions import is_sec
from simba.forms import RoleForm
import unicodedata

@login_required
@user_passes_test(is_sec, login_url='/simba/dashboard/?action=perm_denied')
def board(request):
	roled = False
	context_dict = {}

	n_waiting = UserProfile.objects.filter(status=False).count()

	##TODO Access allowed at board members only
	if request.method == 'POST':
		form = RoleForm(data=request.POST)

		if form.is_valid():
			form.cleaned_data.get('lab')
			role = form.save(commit=False)

			role.save()
			roled = True

			context_dict['test'] = str(role.label)			

	else:
		form = RoleForm()

	board_list = UserProfile.objects.filter(role__label="Board")
	role_list = Role.objects.all()
	context_dict['tab_title'] = "Board List"
	context_dict ['form'] = form

	render_page = 'simba/archive/board.html'

		
	paginator = Paginator(board_list, 25)

	page = request.GET.get('page')
	try:
		boardies = paginator.page(page)
	except PageNotAnInteger:
		boardies = paginator.page(1)
	except EmptyPage:
		boardies = pagintor.page(paginator.num_pages)	
		
	context_dict ['boardies'] = boardies	
	context_dict ['roles'] = role_list
	
	if n_waiting > 0:
		context_dict ['n_waiting'] = n_waiting

	return render(request, render_page, context_dict)

@login_required
def indvitations(request):
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

