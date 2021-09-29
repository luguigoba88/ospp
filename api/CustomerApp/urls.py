from django.conf.urls import url
from CustomerApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^catalog/$',views.statuscatalogsApi),
    url(r'^catalog/([0-9]+)$',views.statuscatalogsApi),

    url(r'^customer/$',views.customerApi),
    url(r'^customer/([0-9]+)$',views.customerApi),

    url(r'^group/$', views.groupApi),
    url(r'^group/([0-9]+)$', views.groupApi),

    url(r'^SaveFile/$', views.SaveFile),
    url(r'^checkBC/$', views.checkBC),
    url(r'^checkPLD/$', views.checkPLD),
    url(r'^checkWL/$', views.checkWL),
    url(r'^leadToCustomer/$', views.leadToCustomer),
    url(r'^leadToCustomer/([0-9]+)$', views.leadToCustomer),
    url(r'^validateLead/$', views.validateLead),
    url(r'^validateLead/([0-9]+)$', views.validateLead),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)