from django.http import HttpResponse
import datetime

def index(request):
    html = "<html><body>Django is running <3</body></html>"
    return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)