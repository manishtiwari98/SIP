from django.urls import path
from . import views

urlpatterns = [
    path('sip/',views.sip),
    path('sip/fillForm',views.fillForm),
    path('companyForm',views.comparyForm),
    path('addCompany',views.addCompany),
    path('sip/addApplicant',views.addApplicant)

]

