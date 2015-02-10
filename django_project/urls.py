from django.conf.urls import patterns, include, url
from djangosnap import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from djangosnap.api import MediaResource
admin.autodiscover()

media_resource = MediaResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.index, name='index'),
    url(r'^test/', views.video_test, name='test'),
    url(r'^upload/', views.upload_file, name='upload'),
    url(r'^watch/', views.watch_videos, name='watch'),

    url(r'^api/', include(media_resource.urls)),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
