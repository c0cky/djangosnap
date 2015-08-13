from django.conf.urls import patterns, include, url
from djangosnap import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from djangosnap.api import MediaResource
from tastypie.api import Api
admin.autodiscover()


tagalong_api = Api('')
tagalong_api.register(MediaResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django_comments.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^test/', views.video_test, name='test'),
    url(r'^uploadit/', views.upload_it, name='uploadit'),
    url(r'^upload/', views.upload_file, name='upload'),
    url(r'^watch/', views.watch_videos, name='watch'),
    url(r'^cusr/', views.add_user, name='adduser'),
    url(r'^lusr/', views.login_user, name='login_user'),
    url(r'^map/', views.map_pick, name='map'),
    url(r'^api', include(tagalong_api.urls)),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
