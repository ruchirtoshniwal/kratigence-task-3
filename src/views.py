from django.shortcuts import render,redirect
from .models import *
from .forms import InternshipForm
# Create your views here.

def Intern(request):
    form = InternshipForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = InternshipForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('intern')
    
    context = {'form':form}
    return render(request, 'index.html', context)
