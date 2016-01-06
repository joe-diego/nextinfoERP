from django.conf.urls import patterns, include, url
from nextinfoERP.bands.views import *

from django.contrib import admin

urlpatterns = patterns('nextinfoERP.bands.views',


    url(r'^$', Home.as_view(), name='home'),
    url(r'^bands/$', BandList.as_view(), name='bands'),
    url(r'^bands/(?P<pk>\d+)/$', 'band_detail', name='band_detail'),
    url(r'^bandform/$', BandForm.as_view(), name='band_form'),
    url(r'^memberform/$', MemberForm.as_view(), name='member_form'),
    url(r'^contact/$', 'band_contact', name='contact'),
    url(r'^protected/$', 'protected_view', name='protected'),
    url(r'^accounts/login/$', 'message'),
    url(r'^admin/', include(admin.site.urls), name='admin'),

)
