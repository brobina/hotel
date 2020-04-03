from django.shortcuts import render
from django.http import HttpResponse
from staffs.models import Staff
# Create your views here.
def index(request):
	return render(request,'pages/index.html')

def about(request):
	staffs=Staff.objects.all()
	context={
		'staffs':staffs
	}
	return render(request,'pages/about.html',context)