from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# from django.contrib.gis.models import models

# Create your models here.
STATUS = (('pending', 'Pending'), ('accepted', 'Accepted'), ('declined', 'Declined'),)


class Location(models.Model):
    pass


class Specialization(models.Model):
    name = models.CharField(max_length=200)
    
    # def get_absolute_url(self):
    #     return reverse("specialization_detail", kwargs={"pk": self.pk})
    
    
class Doctor(models.Model):
    photo = models.ImageField(upload_to="media", null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    speaciality = models.CharField(max_length=255, default=Specialization, null=True)
    portfolio_number = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    is_verified = models.BooleanField(default=False)
    is_booked = models.BooleanField(default=False)
    
    
    def get_absolute_url(self):
        return reverse("doctor_detail", kwargs={"pk": self.pk})
                             

    def __str__(self) ->str:
        return f"{self.first_name} {self.last_name}"

class Patient(models.Model):
    pass

class RequestConsultation(models.Model):
    # Patience request consultation with available doctor, the doctor sets appointmentif consultation is accepted
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="request")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="consultation", verbose_name="Request for consultation")
    Symptoms = models.TextField()
    status = models.CharField(max_length=100, choices=STATUS)

    def __str__(self) ->str:
        return f"{self.patient}-{self.status}"

class Appointment(models.Model):
    consult = models.ForeignKey(RequestConsultation, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=(('virtual', 'virtual'), ('physical', 'physical'), ('private', 'private')))
    date = models.DateTimeField(verbose_name="Date and Time for appointment")
    
    def __str__(self) ->str:
        return f"{self.type}-{self.date}"

class Symptoms(models.Model):
    name = models.CharField(max_length=200, verbose_name="Symptoms")
    
    def __str__(self) -> str:
        return self.name
   
    
class Drugs(models.Model):
    name = models.CharField(max_length=200, verbose_name="name of drugs")
    description = models.TextField()
    
    def __str__(self) ->str:
        return self.name
    
class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Medical History", related_name="Medical_history")
    illness = models.CharField(max_length=100)
    symptoms = models.ManyToManyField(Symptoms)
    drugs = models.TextField(Drugs)
    allergies = models.TextField()
    doctor = models.ForeignKey(Doctor, max_length=100, on_delete=models.CASCADE, related_name='Patients_attended')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) ->str:
        return f"{self.illness}-{self.doctor}-{self.date}"

    
