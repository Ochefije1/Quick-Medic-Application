from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import CreateView, DetailView, DeleteView, ListView
from django.views.generic.edit import DeleteView, UpdateView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from .models import Appointment


from .models import(
    Doctor,
    RequestConsultation,
    Symptoms,
    Drugs,
    MedicalHistory,
    Specialization
)

# Create your views here.

class Home(View):
    def get(self, request):
        return HttpResponse("This is Home Page")
    
    
   #DOCTOR VIEWS
class CreateDoctor(CreateView):
    model = Doctor
    fields= "__all__"
    exclude = ['is_verified', 'is_booked']
    success_url = "/"
    
class DoctorDetail(DetailView):
    model = Doctor
    
class DoctorList(ListView):
    model = Doctor
    
    
class RemoveDoctor(LoginRequiredMixin, DeleteView):
    model = Doctor
    login_url = "/"
    
    
class UpdateDoctor(UpdateView):
    model = Doctor
    fields = "__all__"
    
    
    #REQUEST VIEWS
class CreateRequest(CreateView):
    model = RequestConsultation
    fieelds= "__all__"

    
class RequestDetail(PermissionRequiredMixin, DetailView):
    model = RequestConsultation
    
class RequestList(ListView):
    model = RequestConsultation
    
    
class RemoveRequest(LoginRequiredMixin, DeleteView):
    model = RequestConsultation
    login_url = "/"
    
    
class UpdateRequest(UpdateView):
    model = RequestConsultation
    fields = "__all__"
    
    
    #APPOINTMENT VIEWS
class CreateAppointment(CreateView):
    model = Appointment
    fieelds= "__all__"

    
class AppointmentDetail(PermissionRequiredMixin, DetailView):
    model = Appointment
    
class AppointmentList(ListView):
    model = Appointment
    
    
class RemoveAppointment(LoginRequiredMixin, DeleteView):
    model = Appointment
    login_url = "/"
    
    
class UpdateAppointment(UpdateView):
    model = Appointment
    fields = "__all__"
    
    #SPECIALIZATION VIEWS
class CreateSpecialization(CreateView):
    model = Specialization
    fieelds= "__all__"

    
class SpecializationDetail(PermissionRequiredMixin, DetailView):
    model = Specialization
    
class SpecializationList(ListView):
    model = Specialization
    
    
class RemoveSpecialization(LoginRequiredMixin, DeleteView):
    model = Specialization
    login_url = "/"
    
    
class UpdateSpecialization(UpdateView):
    model = Specialization
    fields = "__all__"
    