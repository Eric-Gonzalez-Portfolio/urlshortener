from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request, 'index.html')

def create(request):
	if request.method == 'POST':
		link = request.POST['urllink']
		uid = str(uuid.uuid4())[:5]
		new_url = Url(urllink=link,uuid=uid)
		new_url.save()
		return HttpResponse(uid)

def directurl(request, pk):
	url_info = Url.objects.get(uuid=pk)
	if ( (url_info.urllink.startswith('http://')) or (url_info.urllink.startswith('https://')) ):
		return redirect(url_info.urllink)
	else:
		return redirect('https://' + url_info.urllink)