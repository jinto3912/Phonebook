from django.shortcuts import render
from .models import phonebookt

# Create your views here.

def index(request):
    return render(request,"index.html")

def numadd(request):
    ph_dict={}
    try:
        ename=request.POST['pname']
        enum=request.POST['pnum']
        pbook=phonebookt(name=ename,num=enum)
        pbook.save()
        ph_dict['message']="employee successfully added"
        return render(request,"index.html",ph_dict)

    except Exception as e:
        print(e)
        ph_dict['message']="employee not added"
        return render(request,"index.html",ph_dict)

def read(request):
    phd=phonebookt.objects.all()
    return render(request,"index.html",{'phkey':phd})

def delete(request):
    try:
        name2=request.POST['delname']
        ph1=phonebookt.objects.filter(name=name2)
        ph1.delete()
        return render(request,"index.html",{'msg1':'data deleted successfully'})

    except Exception as e:
        print(e)
        return render(request,"index.html",{'msg1':'data not deleted'})

def update(request):
    try:
        old=request.POST['oldname']
        new=request.POST['newname']
        phonebookt.objects.filter(name=old).update(name=new)
        phnum1=request.POST['oldnum']
        phnum2=request.POST['newnum']
        phonebookt.objects.filter(num=phnum1).update(num=phnum2)
        return render(request,"index.html",{'msg2':'data updated successfully'})

    except Exception as e:
        print(e)
        return render(request,"index.html",{'msg2':'data not updated'})
        
    
