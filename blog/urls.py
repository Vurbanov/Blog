from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^$', views.home_page, name='home'),
    url(r'about/', views.about, name='about'),
    url(r'contacts/', views.contacts, name='contacts'),
    url(r'publications/', views.publications, name='publications'),
)
