from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    content = (f'<h2>Welcome to gregcompton.com</h2>'
               f'<p>Nothing to see here. I just use this for testing.</p>'
               f'<p>If you would like to talk,'
               f'<a href="https://calendly.com/gregcompton365/let-s-get-to-know-each-other">schedule a time here</a></p>'
               f'<p>~Greg</p>')
    return HttpResponse(content)
    # return render(request, 'app/index.html')