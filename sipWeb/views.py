from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from channels import Group

def sip(request):
    companies=Company.objects.all()
    return render(request,'index.html',{'companySet':companies})

def fillForm(request):
    company=Company.objects.get(id=request.POST['formNum'])
    return render(request,'form.html',{'name':company.name,'location':company.location ,'position':company.position})
def addApplicant(request):
    try:
        new_applicant= Applicants(
            name=request.POST['name'],
            roll=request.POST['roll'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            position=request.POST['position'],
            company_name=request.POST['company_name'],
            location=request.POST['location'],
            statement_of_purpose=request.POST['statement_of_purpose'],
            resume_link=request.POST['resume_link']

        )
        new_applicant.save()
        return HttpResponse(status=200,content="Registerd Successfully.")
    except:
        return HttpResponse(status=350)
def comparyForm(request):
    return render(request,'newCompany.html')

def addCompany(request):
    try:
        new_company=Company(
            name=request.POST['name'],
            description=request.POST['description'],
            location=request.POST['location'],
            no_of_position=request.POST['no_of_position'],
            stipend=request.POST['stipend'],
            position=request.POST['position']

        )
        new_company.save()
        return render(request,'registered.html')
    except:
        return render(request,'registered.html')
        return HttpResponse(status=350)

def analysis(request):
    applicants=Applicants.objects.all()
    tot=len(applicants)
    company=Company.objects.all()
    
    return render(request,'analysis.html',{'total':tot,'companyData':company})



# Create your views here.
