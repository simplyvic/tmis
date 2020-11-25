from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings #for file uploads
from django.conf.urls.static import static #for file uploads
# from uimsapp.views import settings
# from taskmis.views import settings


urlpatterns = [


################################## BACK END #####################################
    
    # url(r'^amis/', include("amis.urls", namespace='amis')),
    url(r'^tmis/', include("tmis.urls", namespace='tmis')),
    # url(r'^uimsapp/', include("uimsapp.urls", namespace='uimsapp')),
    # url(r'^cug/', include("cug.urls", namespace='cug')),
    # url(r'^cmis/', include("cmis.urls", namespace='cmis')),

  
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    

    # Admin and login:
    url(r'^$', 'tmis.views.home', name='home'),
    url(r'^login$', 'tmis.views.login', name='login'),
    # url(r'^frontadmin/$', 'uimsapp.views.frontadmin', name='frontadmin'),

    url(r'^settings/$', 'tmis.views.admin_settings', name='settings'),
    # url(r'^fixassetsettings/$', fixassetsettings, name='fixassetsettings'),
    # url(r'^storesettings/$', storesettings, name='storesettings'),

]
# if settings.DEBUG:
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)