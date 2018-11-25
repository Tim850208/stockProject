# -*- coding: utf-8 -*-
from django.template import loader, RequestContext
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from restaurant.models import Restaurant, Food,Comment
import datetime
import plotly.offline as opy
import plotly.graph_objs as go


def menu(request):
    if 'id' in request.GET:
        print(type(request.GET['id']))
        r = Restaurant.objects.get(id=request.GET['id'])
        return render_to_response('menu.html',locals())
    else:
        return HttpResponseRedirect("/restaurants_list/")

def meta(request):
    values = request.META.items()  # 將字典的鍵值對抽出成為一個清單

    values=sorted(values)
    html = []
    for k, v in values:
        html.append('<tr><td>{0}</td><td>{1}</td></tr>'.format(k, v))
    return HttpResponse('<table>{0}</table>'.format('\n'.join(html)))

def welcome(request):
    if 'user_name' in request.GET:
        return HttpResponse('Welcome!~'+request.GET['user_name'])
    else:
        return render_to_response('welcome.html',locals())

def list_restaurants(request):
    restaurants = Restaurant.objects.all()
    return render_to_response('restaurants_list.html',locals())

def comment(request,id):
    if id:
        r = Restaurant.objects.get(id=id)
    else:
        return HttpResponseRedirect("/restaurants_list/")
    if 'ok' in request.POST:
        user = request.POST['user']
        content = request.POST['content']
        email = request.POST['email']
        date_time = datetime.datetime.now()     # 擷取現在時間

        Comment.objects.create(user=user, email=email, content=content, date_time=date_time, restaurant=r)
    return render(request,'comments.html',locals())

def set_c(request):
    response = HttpResponse('Set your lucky_number as 8')
    response.set_cookie('lucky_number',8)
    return response

def get_c(request):
    if 'lucky_number' in request.COOKIES:
        return HttpResponse('Your lucky_number is {0}'.format(request.COOKIES['lucky_number']))
    else:
        return HttpResponse('No cookies.')
