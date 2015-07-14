from django.conf.urls import patterns, url
from simba import views
from simba.vviews.dashboard import dashboard
from simba.vviews.archive import main_archive, user_act, user_search, board
from simba.vviews.actions import user_actions as ua

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^add_course/$', views.add_course, name='add_course'), 
	url(r'^register/$', ua.register, name='register'),
	url(r'^register/(?P<code>[\w\-]+)/$', ua.register, name='register'),
    	url(r'^course/(?P<course_name_slug>[\w\-]+)/$', views.course, name='course'),
	url(r'^login/$', ua.user_login, name='auth_login'),
	url(r'^logout/$', ua.user_logout, name='auth_logout'),
	url(r'^dashboard/$', dashboard.dash, name='dashboard'),
	url(r'^archive/$', main_archive.archive, name='archive'),
	url(r'^archive/(?P<type>[\w\-]+)/$', main_archive.archive, name='archive'),
	url(r'^activate/(?P<user_no>[\w\-]+)/$', user_act.activate, name='activate'),
	url(r'^unarm/(?P<user_no>[\w\-]+)/$', user_act.unarm, name='unarm'),
	url(r'^delete/(?P<user_no>[\w\-]+)/$', user_act.kill, name='kill'),
	url(r'^module/(?P<user_no>[\w\-]+)/$', user_act.modulo, name='modulo'),
	url(r'^search/$', user_search.search, name='search'),
	url(r'^board/$', board.board, name='board'),
	url(r'^invitations/$', user_act.invitations, name='invitations'),

	
)

'''
#old
urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^add_course/$', views.add_course, name='add_course'), 
	url(r'^register/$', views.register, name='register'),
    	url(r'^course/(?P<course_name_slug>[\w\-]+)/$', views.course, name='course'),
	url(r'^login/$', views.user_login, name='auth_login'),
	url(r'^logout/$', views.user_logout, name='auth_logout'),
	#url(r'^dashboard/$', views.dash, name='dashboard'),
	url(r'^dashboard/$', dashboard.dash, name='dashboard'),
	#url(r'^archive/$', views.archive, name='archive'),
	url(r'^archive/$', main_archive.archive, name='archive'),
	url(r'^archive/(?P<type>[\w\-]+)/$', main_archive.archive, name='archive'),
	#url(r'^archive/(?P<type>[\w\-]+)/$', views.archive, name='archive'),
	url(r'^activate/(?P<user_no>[\w\-]+)/$', user_act.activate, name='activate'),
	url(r'^unarm/(?P<user_no>[\w\-]+)/$', user_act.unarm, name='unarm'),
	url(r'^delete/(?P<user_no>[\w\-]+)/$', user_act.kill, name='kill'),
	url(r'^module/(?P<user_no>[\w\-]+)/$', user_act.modulo, name='modulo'),
	#url(r'^activate/(?P<user_no>[\w\-]+)/$', views.activate, name='activate'),
	#url(r'^unarm/(?P<user_no>[\w\-]+)/$', views.unarm, name='unarm'),
	#url(r'^delete/(?P<user_no>[\w\-]+)/$', views.kill, name='kill'),
	#url(r'^module/(?P<user_no>[\w\-]+)/$', views.modulo, name='modulo'),
	
)
'''
