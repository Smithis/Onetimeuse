from django.shortcuts import render,redirect
from django.http import request
from .models import FilesAdmin
import os
import random,string
from django.contrib import messages


# Create your views here.

def home(request):
    if request.method=='POST':
        file=request.FILES['fil']
        rand=''.join(random.choices(string.ascii_letters+string.digits,k=5))
        nm=FilesAdmin.objects.create(name=rand,fil=file)
        
        
        context={
            'key':rand,
        }
        messages.success(request,"uploaded")
        return render(request,"index.html",context)
    return render(request,"index.html")




def downl(request):
    text=request.POST['game']
    
    if(FilesAdmin.objects.filter(name=text).exists()): 
        print(text)
        gg=FilesAdmin.objects.get(name=text).fil
        context={
            'img':gg,
        }
        return render(request,"index.html",context)

    else:
        messages.info(request,"enter correct code")
        return redirect('home')

         
        
        
    return render(request,"download.html")



def download(request,file_name):
    file_path = settings.MEDIA_ROOT +'/'+ file_name
    file_wrapper = FileWrapper(file(file_path,'rb'))
    file_mimetype = mimetypes.guess_type(file_path)
    response = HttpResponse(file_wrapper, content_type=file_mimetype )
    response['X-Sendfile'] = file_path
    response['Content-Length'] = os.stat(file_path).st_size
    response['Content-Disposition'] = 'attachment; filename=%s/' % smart_str(file_name) 
    return response





