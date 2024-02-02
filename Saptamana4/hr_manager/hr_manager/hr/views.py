from django.shortcuts import render
from .models import Employer


# Create your views here.
def homepage(request):
    employers = Employer.objects.all()
    return render(request, 'homepage.html', {'name': 'DJANGO', 'employers': employers})
