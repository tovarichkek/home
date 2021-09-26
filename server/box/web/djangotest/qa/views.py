from django.http import HttpResponse 
def questions(request, *args, **kwargs):
    return HttpResponse('OK')
def over_sites(request, *args, **kwargs):
    return HttpResponse('This site is making')
def not_sites(request, *args, **kwargs):
    return HttpResponse('Please, write correct address: <br>question<br>login<br>signup<br>ask<br>popular<br>new')
def not_doc(requests,*args,**kwargs):
    return HttpResponseNotFound()
