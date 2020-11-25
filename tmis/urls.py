from django.conf.urls import include, url
from django.contrib import admin
from .views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'uimsproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'tmis.views.home', name='home'),
    url(r'^user_task_list/$', user_task_list, name='user_task_list'), #list items
    url(r'^user_task_entry/$', user_task_entry, name='user_task_entry'), #list items
    url(r'^user_task_completed_list/$', user_task_completed_list, name='user_task_completed_list'), #list items
    url(r'^all_task_list/$', all_task_list, name='all_task_list'), #list items
    url(r'^all_task_completed_list/$', all_task_completed_list, name='all_task_completed_list'), #list items
    url(r'^task_ext_list/$', task_ext_list, name='task_ext_list'), #list items
    url(r'^task_rev_list/$', task_rev_list, name='task_rev_list'), #list items
    # url(r'^unit_one_task_list/$', unit_one_task_list, name='unit_one_task_list'), #list items
    # url(r'^unit_two_task_list/$', unit_two_task_list, name='unit_two_task_list'), #list items
    # url(r'^unit_three_task_list/$', unit_three_task_list, name='unit_three_task_list'), #list items
    # url(r'^unit_four_task_list/$', unit_four_task_list, name='unit_four_task_list'), #list items
    # url(r'^unit_five_task_list/$', unit_five_task_list, name='unit_five_task_list'), #list items
    # url(r'^unit_six_task_list/$', unit_six_task_list, name='unit_six_task_list'), #list items
    # # url(r'^unit_specific_task/$', unit_specific_task, name='unit_specific_task'), #list items
    # url(r'^unit_one_task_list_completed/$', unit_one_task_list_completed, name='unit_one_task_list_completed'), #list items
    # url(r'^unit_two_task_list_completed/$', unit_two_task_list_completed, name='unit_two_task_list_completed'), #list items
    # url(r'^unit_three_task_list_completed/$', unit_three_task_list_completed, name='unit_three_task_list_completed'), #list items
    # url(r'^unit_four_task_list_completed/$', unit_four_task_list_completed, name='unit_four_task_list_completed'), #list items
    # url(r'^unit_five_task_list_completed/$', unit_five_task_list_completed, name='unit_five_task_list_completed'), #list items
    # url(r'^unit_six_task_list_completed/$', unit_six_task_list_completed, name='unit_six_task_list_completed'), #list items
    # url(r'^user_task_edit/$', user_task_edit, name='user_task_edit'), #list items
    url(r'^user_task_edit/(?P<id>\d+)/edit$', user_task_edit, name='user_task_edit'),
    url(r'^user_task_progress/(?P<id>\d+)/progress$', user_task_progress, name='user_task_progress'), #list items
    url(r'^user_task_comment/(?P<id>\d+)/comment$', user_task_comment, name='user_task_comment'), #list items
    url(r'^task_ext_edit/(?P<id>\d+)/edit$', task_ext_edit, name='task_ext_edit'),
    url(r'^task_rev_edit/(?P<id>\d+)/edit$', task_rev_edit, name='task_rev_edit'),
    # url(r'^task_delete/(?P<id>\d+)/delete$', task_delete, name='task_delete'),
    url(r'^assigned_task_completed_list/$', assigned_task_completed_list, name='assigned_task_completed_list'), #list items
    # url(r'^annual_plan_list/$', annual_plan_list, name='annual_plan_list'), #list items
    
    # url(r'^start_activity/(?P<id>\d+)/start_activity$', start_activity, name='start_activity'),
    # url(r'^end_activity/(?P<id>\d+)/end_activity$', end_activity, name='end_activity'),
    # url(r'^annual_plan_edit/(?P<id>\d+)/edit$', annual_plan_edit, name='annual_plan_edit'),

    url(r'^admin_settings/$', admin_settings, name='admin_settings'),
]