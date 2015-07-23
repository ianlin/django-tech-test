from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^apply_loan/$', views.apply_loan, name='apply_loan'),
    url(r'^apply_complete/$', views.apply_complete, name='apply_complete'),
    url(r'^display_loan/$', views.display_loan, name='display_loan'),
]
