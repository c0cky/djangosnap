from django.conf.urls import patterns, include, url
from djangosnap import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^test/', views.video_test, name='test'),
    url(r'^upload', views.upload_file, name='upload'),
)
