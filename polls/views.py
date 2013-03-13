# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttprResponse("Hello, world. You're at the poll index.")

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at results of poll %s." % poll_id)
