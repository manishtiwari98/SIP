from django.db import models


    
class Applicants(models.Model):
    name=models.CharField(max_length=50)
    roll=models.CharField(max_length=10)
    phone=models.IntegerField(max_length=15)
    email=models.EmailField(max_length=100)
    position= models.CharField(max_length=50)
    company_name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    statement_of_purpose=models.CharField(max_length=5000)
    resume_link=models.CharField(max_length=500)

class Company(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=1000)
    location=models.CharField(max_length=50)
    no_of_position=models.IntegerField()
    stipend= models.CharField(max_length=50)
    position= models.CharField(max_length=50)
    def calculateApp(self):
        return len(Applicants.objects.filter(company_name=self.name))
    appCount=property(calculateApp)

    def __str__(self):
        return self.name
    
