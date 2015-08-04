from django.shortcuts import render
from django.http import HttpResponse
from forms import UserForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from forms import MediaForm
from wsgiref.util import FileWrapper
from models import Media

def index(request):
    return render(request, 'djangosnap/cover.html')

def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(form)
            login(new_user)
    else:
        form = UserForm()
    return HttpResponse("success")


@csrf_exempt
def test(request):
    if request.method == 'POST':
        user = request.POST['user']
        password = request.POST['password']
        print user, password
        return HttpResponse("you did it")

def video_response(request):
    file = FileWrapper(open('path/to/video.mp4', 'rb'))
    response = HttpResponse(file, content_type='video/mp4')
    response['Content-Disposition'] = 'attachment; filename=filename.mp4'
    return response
 
def handle_uploaded_file(f):
    with open('some/file/name', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def video_test(request):
    form = MediaForm()
    return render(request, 'djangosnap/videotest.html', {'form':form})

def upload_it(request):
    form = MediaForm()
    return render(request, 'djangosnap/upload.html', {'form': form})

def upload_file(request):
    if request.method == 'POST':
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Saved")
    else:
        form = MediaForm()
    return HttpResponse()

def watch_videos(request):
    #mediafiles = list(Media.objects.filter(approved=True).values('mediafile'))
    mediafiles = Media.objects.filter(approved=True)
    print type(mediafiles)
    return render(request, 'djangosnap/play_video.html', {'mediafiles': mediafiles})