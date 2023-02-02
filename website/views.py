from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from datetime import date, datetime
from django.contrib import messages

def index(request):
     
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')


def todolist(request):
    if request.method == "POST":
        form = ListModelForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error", form.errors)
    form = ListModelForm()
    show = ListModel.objects.all()
    return render(request, 'todolist.html', {'form':form , 'show':show } )



# def todolist(request):
#     form = todoForm()
#     date_now = datetime.now()
#     if request.method == 'POST':
#         todo_input = request.POST.get("todo")
#         date_input = request.POST.get("date_input")
#         if datetime(int(date_input[:4]), int(date_input[5:7]), int(date_input[8:]),) <= date_now:
#             messages.add_message(request, messages.SUCCESS, f"ไม่สามารถเพิ่มรายการได้ กรุณาเลือกวันให้ถูกต้อง")   #กรณีเลือกวันที่ผ่านมาแล้ว
#             return redirect("doctors:appointment", pk)
#         appointment = Appointment.objects.create(
#             Doctor_id=doctor,
#             todo=todo_input
#         )
#         appointment.dateapp = date_input
#         appointment.save()
#         return redirect("doctors:profile")

#     context = {"form": form, "doctor": doctor}
#     return render(request, "doctors/appointment_patient.html", context)