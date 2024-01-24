# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import json
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from django import forms


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template. 
    try:

        load_template = request.path.split('/')[-1]
                                
        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))        
            
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        print(f"Except, load template is: {load_template}")
        
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))



""" Ready chat """
def ready_chat(request):    
        question = request.POST.get('question')        
        
        # Question processing by AI
        
        answer = "The answer to your question '" + question + "', is another question"
        response = {"answer": answer}
        
        return JsonResponse(json.dumps(response), safe=False)
    