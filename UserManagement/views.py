from django.shortcuts import render , redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django import template
from operator import contains
register = template.Library()
from . import models
from .forms import AddNewUser as form11

def addnew(request):
    if request.method == "POST":
        form = form11(request.POST, request.FILES)
        if form.is_valid():
            child = form.save(commit=False)
            child.save()
            AddNewUser = models.AddNewUser.objects.all().order_by('-id')
            page = request.GET.get('page', 1)
            paginator = Paginator(AddNewUser, 10)
            try:
                AddNewUser = paginator.page(page)
            except PageNotAnInteger:
                AddNewUser = paginator.page(1)
            except EmptyPage:
                AddNewUser = paginator.page(paginator.num_pages)
            return render(request , 'html/UserManagement.html' , {'AddNewUser':AddNewUser})
    else:
        form = form11()
    return render(request, 'html/addnew.html', {'form': form})

def delete_user11(request , id):
    AddNewUser = models.AddNewUser
    album = AddNewUser.objects.get(pk=id)
    album.delete()
    AddNewUser = models.AddNewUser.objects.all().order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(AddNewUser, 10)
    try:
        AddNewUser = paginator.page(page)
    except PageNotAnInteger:
        AddNewUser = paginator.page(1)
    except EmptyPage:
        AddNewUser = paginator.page(paginator.num_pages)
    return render(request ,'html/UserManagement.html' , {'AddNewUser':AddNewUser})

def edit(request, id):
    AddNewUser = models.AddNewUser
    instance = AddNewUser.objects.get(id=id)
    form = form11(request.POST or None, instance=instance)
    if form.is_valid():
          form.save()
          AddNewUser = models.AddNewUser.objects.all().order_by('-id')
          page = request.GET.get('page', 1)
          paginator = Paginator(AddNewUser, 8)
          try:
              AddNewUser = paginator.page(page)
          except PageNotAnInteger:
              AddNewUser = paginator.page(1)
          except EmptyPage:
              AddNewUser = paginator.page(paginator.num_pages)
          return redirect('html/UserManagement.html' , {'AddNewUser':AddNewUser})
    return render(request, 'html/edit.html', {'form': form , 'instance':instance})

def UserManagement(request):
    AddNewUser = models.AddNewUser
    user_list = AddNewUser.objects
    query_fullname = request.GET.get('q')
    query_email = request.GET.get('e')
    query_username = request.GET.get('u')
    query_phonenumber = request.GET.get('p')
    sortby = request.GET.get('sortby')
    orderby = request.GET.get('orderby')
    fullurl = request.build_absolute_uri

    if query_fullname:
        user_list = user_list.filter(FullName__contains=query_fullname)
    if query_email:
        user_list =user_list.filter(Email__contains=query_email)
    if query_username:
        user_list =user_list.filter(Username__contains=query_username)
    if query_phonenumber:
        user_list =user_list.filter(PhoneNumber__contains=query_phonenumber)
    user_list = user_list.all()
    if not sortby:
        sortby = 'id'

    if orderby:
        if orderby == 'dsec':
            user_list = user_list.order_by(sortby)
    else:
        user_list = user_list.order_by('-'+sortby)

    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 8)
    try:
        AddNewUser = paginator.page(page)
    except PageNotAnInteger:
        AddNewUser = paginator.page(1)
    except EmptyPage:
        AddNewUser = paginator.page(paginator.num_pages)
    if query_fullname or query_email or query_username or query_phonenumber:
        context = {'AddNewUser': AddNewUser, 'sortby': sortby, 'orderby': orderby, 'fullurl': fullurl ,'query_phonenumber':query_phonenumber,'query_username':query_username ,'query_fullname' :query_fullname ,'query_email':query_email , }
    else:
        context = {'AddNewUser': AddNewUser, 'sortby': sortby , 'orderby' : orderby , 'fullurl' : fullurl }

    return render(request, 'html/UserManagement.html', context)
def active(request , id):
    AddNewUser = models.AddNewUser
    instance = AddNewUser.objects.get(id=id)
    instance.Active = '1'
    return render(request , 'html/UserManagement.html')

def deactive(request , id):
    AddNewUser = models.AddNewUser
    instance = AddNewUser.objects.get(id=id)
    instance.Active = '0'
    return render(request , 'html/UserManagement.html')
