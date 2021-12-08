from django.shortcuts import render,redirect
from .forms import  student_Form

def emp(request):
    if request.method =="POST":
        form =student_Form(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/emp")
            except:
                pass
    else:
        form =student_Form()
        return render(request,"index.html",{"forms":form})

