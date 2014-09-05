from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^$', views.home_page, name='home_page'),
    url(r'(?P<post_id>\d+)/', views.post, name='post'),
    url(r'^add_comment/(?P<pk>\d+)/&', views.add_comment, name='add_comment'),
    url(r'^publications/$', views.publications, name='publications'),
    url(r'^contacts/$', views.contacts, name='contacts'),


)
