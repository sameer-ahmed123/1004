from django.shortcuts import render,redirect
from .forms import EmployeeForm

def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/emp')
            except:
                pass
    else:
        form = EmployeeForm()
        return render(request,"index.html",{'form':form})