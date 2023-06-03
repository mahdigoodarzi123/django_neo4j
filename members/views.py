from django.shortcuts import render
from django.http import HttpResponse
from .models import Member, Contact
from .forms import contactform
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .neo4j import create_applicant, all_applicants
import uuid
import base64
import os


def members(request):
    return render(request, "members/members.html")



# def one_member(request, id):
#     mymember = Member.objects.get(id = id)
#     context = {"mymember" : mymember }
#     return render(request, "members/details.html", context=context)


def index(request):
    return render(request, "members/main.html")


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        phone_number = request.POST.get('phone_number')
        birthdate = request.POST.get('date')
        sex = request.POST.get('gender')
        fs = FileSystemStorage(location='E:/programs/w3school django/resume')

        pdf_file = request.FILES.get('pdf_file')
        if pdf_file:
            # Save the uploaded PDF file to the FileSystemStorage location
            filename = fs.save(pdf_file.name, pdf_file)
            # Get the URL of the saved file
            file_url = fs.url(filename)
            print(pdf_file)
            print(file_url)
        # resume = request.POST.get('message')
        # cerificate = request.POST.get('message')
        # contact = Contact(name=name, email=email, subject=subject , message=message)
        # contact.save()
        # messages.success(request, 'Your message has been sent!')
        # return redirect('frm')
        print(name, email, age, phone_number, birthdate, sex)
    return render(request, 'members/frm.html')



def test(request):
    if request.method == 'POST' and request.FILES['pdf']:
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        phone_number = request.POST.get('phone_number')
        birthdate = request.POST.get('date')
        sex = request.POST.get('gender')
        department = request.POST.get('department')
        certificate = request.POST.get("certificate")
        pdf_file = request.FILES['pdf']
        fs = FileSystemStorage()

        #this part is for making a unique name
        base64_bytes = base64.urlsafe_b64encode(uuid.uuid4().bytes)[:8].decode('utf-8')
        pdf_name = str(base64_bytes) + "_" + str(name)


        resume_pth = f'resume/{pdf_name}.pdf'
        filename = fs.save(resume_pth, pdf_file)
        create_applicant(name, age, birthdate, resume_pth, certificate, email, phone_number, department)
        # filename = fs.save(str(file_path) + "/" + pdf_name , pdf_file)
        return render(request, 'members/successful.html', {'filename': filename})
    else:
        return render(request, 'members/test.html')



def all_members(request):
    mymembers = all_applicants()
    mmb = []
    for member in mymembers:
        mmb.append(member)


    



    context = {"mymembers" : mmb }
    return render(request, "members/details.html", context=context)