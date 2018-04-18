from django.urls import path
from . import views

urlpatterns = [
    path('sip/',views.sip),
    path('sip/fillForm',views.fillForm)

]

