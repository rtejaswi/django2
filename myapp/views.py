from django.shortcuts import render
from myapp.forms import UserForms
# Create your views here.

def index(request):
    return render(request, 'index.html')

def userforms(request):
    form = UserForms()

    if request.method == "POST":
        form = UserForms(request.POST)

        if form.is_valid():
            print("The Form Is Valid! ")
            form.save(commit=True)
            return index(request)
        else:
            print("The Form Is Not Valid! ")
    return render(request, 'userforms.html', {'form':form})
