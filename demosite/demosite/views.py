from django.http import HttpResponse
from django.template import loader, RequestContext

def homepage(request):
    t = loader.get_template('homepage.html')
    context = RequestContext(request)
    return HttpResponse(t.render(context))
