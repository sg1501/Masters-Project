from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# Create your views here.
def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    stats = Stats.objects.all()
    d = {'stats': stats}
    return render(request, 'index.html', d)

def Login(request):
    error = False
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['psw']
        user = authenticate(username=u, password=p)
        if user.is_staff:
            login(request, user)
            return redirect('home')
        else:
            error = True
    d = {'error': error}

    return render(request, 'login.html', d)

def Add_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    stats = Stats.objects.all()
    if request.method == "POST":
        n = request.POST['name']
        c = request.POST['contact']
        sp = request.POST['special']
        Doctor.objects.create(name=n, mobile=c, special=sp)
        count = 0
        for i in Doctor.objects.all():
            count += 1
        for j in Stats.objects.all():
            if j.stats_name == "doctor":
                j.stats_num = count
                j.save()
                return redirect('home')

    d = {'stats': stats}
    return render(request, 'doctor.html', d)
def Delete_Doctor(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    if Doctor.objects.filter(id=pid).exists():
        data = Doctor.objects.get(id=pid)
        for i in Stats.objects.all():
            if i.stats_name == "doctor":
                i.stats_num = i.stats_num - 1
                i.save()
                data.delete()
                return redirect('home')


def view_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    stats = Stats.objects.all()
    doc = Doctor.objects.all()
    d = {'doc': doc, "stats": stats}
    return render(request, 'view_doctor.html', d)

def view_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    stats = Stats.objects.all()
    doc = Patient.objects.all()
    d = {'doc': doc, "stats": stats}
    return render(request, 'view_patient.html', d)

def Add_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    stats = Stats.objects.all()
    gen1 = Gender.objects.all()
    if request.method == "POST":
        #s = request.POST['stats']
        n = request.POST['name']
        c = request.POST['contact']
        gen = request.POST['gen']
        add = request.POST['add']
        #stat = Stats.objects.filter(stats_name=s).first()
        gender = Gender.objects.filter(type=gen).first()
        Patient.objects.create(name=n, mobile=c, gender=gender, address=add)
        #if data:
            #stats.stats_num += 1
            #stats.save()
            #return redirect('home')
        #else:
            #pass
        count = 0
        for i in Patient.objects.all():
            count += 1
        for j in Stats.objects.all():
            if j.stats_name == "Patient":
                j.stats_num = count
                j.save()
                return redirect('home')


    d = {'stats': stats, 'gen': gen1}
    return render(request, 'patient.html', d)

def Delete_Patient(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    if Patient.objects.filter(id=pid).exists():
        data = Patient.objects.get(id=pid)
        for i in Stats.objects.all():
            if i.stats_name == "Patient":
                i.stats_num = i.stats_num - 1
                i.save()
                data.delete()
                return redirect('home')



def view_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    app = Appointment.objects.all()
    d = {'app': app}
    return render(request, 'view_appointment.html', d)

def Add_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    stats = Stats.objects.all()
    doc1 = Doctor.objects.all()
    pat1 = Patient.objects.all()
    if request.method == "POST":

        d = request.POST['doc']
        p = request.POST['pat']
        da = request.POST['date']
        ti = request.POST['time']

        doc = Doctor.objects.filter(name=d).first()
        pat = Patient.objects.filter(name=p).first()
        Appointment.objects.create(doctor=doc, patient=pat, date1=da, time1=ti)
        count = 0
        for i in Appointment.objects.all():
            count += 1
        for j in Stats.objects.all():
            if j.stats_name == "Appointment":
                j.stats_num = count
                j.save()
                return redirect('home')

    d = {'stats': stats, 'doc': doc1, 'pat': pat1}
    return render(request, 'appointment.html', d)

def Delete_Appointment(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    if Appointment.objects.filter(id=pid).exists():
        data = Appointment.objects.get(id=pid)
        for i in Stats.objects.all():
            if i.stats_name == "Appointment":
                i.stats_num = i.stats_num - 1
                i.save()
                data.delete()
                return redirect('home')


def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

def Edit_Patient(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    stats = Stats.objects.all()
    gen1 = Gender.objects.all()
    data = Patient.objects.get(id=pid)
    if request.method == "POST":
        s = request.POST['stats']
        n = request.POST['name']
        c = request.POST['contact']
        gen = request.POST['gen']
        add = request.POST['add']
        stat = Stats.objects.filter(stats_name=s).first()
        gender = Gender.objects.filter(type=gen).first()
        data.stats = stat
        data.name = n
        data.gender = gender
        data.mobile = c
        data.address = add
        data.save()
        return redirect('view_patient')
    d = {'stats': stats, 'gen': gen1, 'data': data}
    return render(request, 'edit_patient.html', d)

def Edit_Doctor(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    stats = Stats.objects.all()
    data = Doctor.objects.get(id=pid)
    if request.method == "POST":
        s = request.POST['stats']
        n = request.POST['name']
        c = request.POST['contact']
        sp = request.POST['special']
        stat = Stats.objects.filter(stats_name=s).first()
        data.stats = stat
        data.name = n
        data.mobile = c
        data.special = sp
        data.save()
        return redirect('view_doctor')

    d = {'stats': stats, 'data': data}
    return render(request, 'edit_doctor.html', d)
