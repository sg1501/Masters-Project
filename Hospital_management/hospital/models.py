from django.db import models

# Create your models here.
class Stats(models.Model):
    stats_name = models.CharField(max_length=30, null=True)
    stats_image = models.FileField(null=True)
    stats_num = models.IntegerField(null=True)

    def __str__(self):
        return self.stats_name
class Doctor(models.Model):
    #stats = models.ForeignKey(Stats, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    mobile = models.IntegerField(null=True)
    special = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class Gender(models.Model):
    type = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.type

class Patient(models.Model):
    #stats = models.ForeignKey(Stats, on_delete=models.CASCADE, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    mobile = models.IntegerField(null=True)
    address = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    #stats = models.ForeignKey(Stats, on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    date1 = models.DateField(null=True)
    time1 = models.TimeField(null=True)

    def __str__(self):
        return self.doctor.name+"--"+self.patient.name

