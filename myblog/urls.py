from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('blog.urls', namespace='blog', app_name='blog')),

    url(r'^admin/', include(admin.site.urls)),
)
