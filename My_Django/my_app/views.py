# Create your views here.


from django.shortcuts import render_to_response, RequestContext, HttpResponse, Http404, render
import datetime
from django.template import Template, Context
# Create your views here.

def my_view(request, offset, offset2):
    #return render_to_response('index.html', locals(), context_instance=RequestContext(request))
    
#     try:
#         print offset
#         print offset2
#     except ValueError:
#         raise Http404()
#     dt = datetime.datetime.now() + datetime.timedelta(hours=int(offset))
#     #assert False
#     html = "<html><body>It is now %s.</body></html>" %datetime.datetime.now()
#     return HttpResponse(html + offset + offset2 + str(dt))



    dictionary = {'Name': 'Saajan', 'Age': '23', 'Subjects': ["AI", "ML", "SOC"]}
    
    t = Template('index.html')
    c = Context({'dict': dictionary})
    
    #return render_to_response('index.html', locals(), context_instance=c)
    return render(request, 'index.html', dictionary)
    