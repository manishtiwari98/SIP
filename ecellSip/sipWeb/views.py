from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def sip(request):
    companies=Company.objects.all()
    return render(request,'index.html',{'companySet':companies})
@csrf_exempt
def fillForm(request):
    company=Company.objects.get(id=request.POST['formNum'])
    return HttpResponse(company.name)


# Create your views here.
