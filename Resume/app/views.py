from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ResumeForm
from .models import ResumeModel

def home(request):
    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #messages.success(request, "Your form has been submitted successfully.")
            return render(request,'home.html')  # Redirect to the same page after successful submission
    else:
        form = ResumeForm()
    return render(request, 'home.html', {'form': form})

def choose(request):
    return render(request,'choose.html')

def template1(request):
    last_object = ResumeModel.objects.last()  # Retrieve the last object
    context = {
        'last_object': last_object
    }
    return render(request,"template1.html",context)

def template2(request):
    last_object = ResumeModel.objects.last()  # Retrieve the last object
    context = {
        'last_object': last_object
    }
    return render(request,"template2.html",context)

    
