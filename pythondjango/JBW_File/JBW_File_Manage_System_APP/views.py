from base64 import b85decode
from multiprocessing import context
from pickle import NONE
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import CreateUserForm, QuotationForm

import io
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.colors import *
from django.core.files.storage import FileSystemStorage

from django.http import FileResponse
from PyPDF2 import PdfFileWriter, PdfFileReader

from django.template.loader import get_template
from xhtml2pdf import pisa
from reportlab.lib.pagesizes import letter
from datetime import datetime, date
from reportlab.lib.units import inch



def requestpdf(request,pk):
    Quot = Quotation.objects.get(id=pk)
    buf = BytesIO()
    p = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = p.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 9)
    
    
    lines = []

    
    p.drawString(160, 145, f'{Quot.company_name}')
    p.drawString(160, 160, f'{Quot.address}')
    p.drawString(180, 225, f'{Quot.purchasing_officer}')
    p.drawString(180, 185, f'{Quot.eic}')
    p.drawString(160, 283, f'{Quot.subject}')
    p.drawString(120, 390, f'{Quot.project_name}')
    p.drawString(410, 430, f'{Quot.price}')
    p.drawString(200, 495, f'{Quot.top}')
    
    
    
    for line in lines:
        textob.textLine(line)
        
    p.drawText(textob)    
    p.showPage()
    p.save()
    buf.seek(0)

     
    infos = PdfFileReader(buf)
    clearance_pdf = PdfFileReader(open(r'C:/Users/kamote22/Desktop/pythondjango/JBW_File/JBW_File_Manage_System_APP/static/PDF/JBW FILE MANAGEMENT SYSTEM.pdf', 'rb'))

    info_page = clearance_pdf.getPage(0)
    info_page.mergePage(infos.getPage(0))

    output = PdfFileWriter()

    output.addPage(info_page)
    to_merge = open(r'C:/Users/kamote22/Desktop/pythondjango/JBW_File/JBW_File_Manage_System_APP/static/PDF/JBW FILE MANAGEMENT SYSTEM123.pdf', 'wb')
    output.write(to_merge)
    to_merge.close()



    with open(r'C:/Users/kamote22/Desktop/pythondjango/JBW_File/JBW_File_Manage_System_APP/static/PDF/JBW FILE MANAGEMENT SYSTEM123.pdf', 'rb', ) as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = ' attachment; filename= generated_forms.pdf'
        return response
    #return response

        

def Login(request):
   
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('mainwindow')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'html/log_in.html', context)

def quotation(request):
    if request.method == 'POST':
        company_name = request.POST.get('input1')
        print(company_name)

    context = {}
    return render(request, 'html/REQUEST.html', context)


def register(request):
    form = CreateUserForm(request.POST)
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Cogratulations! ' + user + ' you have created this account')

            return redirect('login')
        else:
            messages.success(request, form.errors)
            return redirect('register')
    context = {'form':form}
    return render(request, 'html/register1.html', context)

def retrieve(request):
    print("napunta ka ba dito?")
    object = Quotation.objects.all()

    context = {'object':object}
    return render(request, "html/MAIN WINDOW.html", context)


###################### ADMIN ############################
@login_required(login_url='login')
def main_window(request):
    object = Quotation.objects.all()

    context = {'object':object}
    return render(request, "html/MAIN WINDOW.html", context)

@login_required(login_url='login')
def delete(request, pk):
    Quot = Quotation.objects.get(id=pk)
    if request.method == "POST":
        Quot.delete()
        return redirect('mainwindow')

    context = {'item':Quot}
    return render(request, 'html/delete1.html', context)

@login_required(login_url='login')
def UpdateQuotation(request, pk):

    order = Quotation.objects.get(id=pk)
    form = QuotationForm(instance=order)
    if request.method == "POST":
        form = QuotationForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('mainwindow')
    
    context = {'form':form}
    return render(request, 'html/REQUEST.html', context)

@login_required(login_url='login')
def requestq(request):

    form = QuotationForm()
    if request.method == 'POST':
        form = QuotationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mainwindow')

    context = {'form':form}
    return render(request, 'html/REQUEST.html', context)

@login_required(login_url='login')
def respondq(request):
    return render(request, 'html/RESPOND.html')

@login_required(login_url='login')
def delivery(request):
    return render(request, 'html/DELIVERY.html')

@login_required(login_url='login')
def tools(request):
    return render(request, 'html/TOOLS.html')

def logoutUser(request):
    logout(request)
    return redirect('login')


########CUSTOMER#########################
def CustomerLog(request):

        if request.method == 'POST':
            codex1 = request.POST.get("Code1")
    
            if codex1 == "jatsengesta":
                return redirect('login')
            else:
                messages.info(request, 'Invalid Code!')

        context = {}
        return render(request, 'html/Customer.html', context)

def CustomerHome(request):
    return render(request, 'html/HomeCustomer.html')

def email(request):
    return render(request, 'html/EMAIL.html')


def CustomerlOGIN(request):
    return render(request, 'html/Customer.html', context)

#def CustomerLog(request):

      #  if request.method == 'POST':
       #     codex = request.POST.get('Code1')
       ##     print(codex)
       #     user = authenticate(request, codex=codex)    

       #     if user is None:
        #        login(request, user)
         #       return redirect('login')
         #   else:
       #         messages.info(request, 'Invalid Code!')

      #  context = {}
     #   return render(request, 'html/Customer.html', context)
