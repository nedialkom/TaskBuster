from django.shortcuts import render
import datetime
from django.utils.timezone import now
from django.contrib.auth import logout

def home(request):
    today = datetime.date.today()
    return render(request, "taskbuster/index.html", {'today':today, 'now':now()})

def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")

def logout_view(request):
    logout(request)
    return home(request)
