from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from forms import UploadFileForm
from wsgiref.util import FileWrapper

def index(request):
    return HttpResponse("WORK IN PROGRESS BY CAMRON GODBOUT AND JARED PIEDT")

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
    response['Content-Disposition'] = 'attachment; filename=filenam3.mp4'
    return response
 
def handle_uploaded_file(f):
    with open('some/file/name', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_file(request): 
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = ModelWithFileField(file_field=request.FILES['file']
            instance.save()
            return HttpResponse("Saved")
    else:
        form = UploadFileForm()
    return HttpResponse()
