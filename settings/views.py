from django.shortcuts import render , redirect , render_to_response
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.files import File
from .forms import SettingsForm as form11
from django.urls import resolve

def editsettings(request, id):
    Settings = models.Settings
    instance = Settings.objects.get(id=id)
    form = form11(request.POST or None, instance=instance)
    if form.is_valid():
          form.save()
          writefile(request)
          AddNewUser = models.Settings.objects.all().order_by('-id')
          return redirect('settings/main.html' ,{'AddNewUser' : AddNewUser})
    return render(request , 'settings/editsettings.html' , {'form' : form , 'id':id , 'instance':instance})

def settings(request):
    AddNewUser = models.Settings
    user_list = AddNewUser.objects
    query_title = request.GET.get('q')
    query_key = request.GET.get('p')
    query_value = request.GET.get('u')
    sortby = request.GET.get('sortby')
    orderby = request.GET.get('orderby')
    fullurl = request.build_absolute_uri

    if query_title:
        user_list = user_list.filter(title__icontains=query_title)
    if query_key:
        user_list = user_list.filter(key__icontains=query_key)
    if query_value:
        user_list = user_list.filter(value__icontains=query_value)
    user_list = user_list.all()
    if not sortby:
        sortby = 'id'

    if orderby:
        if orderby == 'desc':
            user_list = user_list.order_by(sortby)
    else:
        user_list = user_list.order_by('-'+sortby)

    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 10)
    try:
        AddNewUser = paginator.page(page)
    except PageNotAnInteger:
        AddNewUser = paginator.page(1)
    except EmptyPage:
        AddNewUser = paginator.page(paginator.num_pages)
    if query_key or query_value or query_title:
        context = {'AddNewUser': AddNewUser, 'sortby': sortby, 'orderby': orderby, 'fullurl': fullurl,
                    'query_title': query_title,
                   'query_key': query_key, 'query_value': query_value, }
    else:
        context = {'AddNewUser': AddNewUser, 'sortby': sortby, 'orderby': orderby, 'fullurl': fullurl}

    return render(request , 'settings/main.html' , context)

def addsettings(request):
    if request.method == "POST":
        form = form11(request.POST, request.FILES)
        if form.is_valid():
            child = form.save(commit=False)
            child.save()
            writefile(request)
            AddNewUser = models.Settings.objects.all().order_by('-id')
            page = request.GET.get('page', 1)
            paginator = Paginator(AddNewUser, 10)
            try:
                AddNewUser = paginator.page(page)
            except PageNotAnInteger:
                AddNewUser = paginator.page(1)
            except EmptyPage:
                AddNewUser = paginator.page(paginator.num_pages)
            return render(request ,  'settings/main.html' , {'AddNewUser':AddNewUser})
    else:
        form = form11()
    return render(request , 'settings/addnew.html' , {'form' : form})

def deletesettings(request , id):
    AddNewUser = models.Settings
    album = AddNewUser.objects.get(pk=id)
    album.delete()
    writefile(request)
    AddNewUser = models.Settings.objects.all().order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(AddNewUser, 10)
    try:
        AddNewUser = paginator.page(page)
    except PageNotAnInteger:
        AddNewUser = paginator.page(1)
    except EmptyPage:
        AddNewUser = paginator.page(paginator.num_pages)
    return render(request ,'settings/main.html' , {'AddNewUser':AddNewUser})


def writefile(request):
    Setting = models.Settings
    Settings = Setting.objects.all()

    htmlsring   =   ""
    for settingdata in Settings:
        htmlsring   +=  settingdata.key+" = "+'"'+settingdata.value+'"'+"\n"

    with open('untitled3/local_settings.py', 'w') as f:
        myfile = File(f)
        myfile.write(htmlsring)
    myfile.closed


def sitesettingsmain(request):
    fullurl = resolve(request.path_info).url_name
    Seting = models.Settings
    if not fullurl == 'prefix':
        all = Seting.objects.filter(key__icontains=fullurl)
        if request.method == "POST":
            for settingdata in all:
                form = form11(request.POST)
                id = str(settingdata.id)
                a = request.POST.get(id)
                Seting.objects.filter(id=id).update(value=a)
        all = Seting.objects.filter(key__icontains=fullurl)
        writefile(request)
    else:
        if request.method == "POST":
            all = Seting.objects.all()
            for settingdata in all:
                form = form11(request.POST)
                id = str(settingdata.id)
                a = request.POST.get(id)
                Seting.objects.filter(id=id).update(value=a)
        writefile(request)
        print(Site.title)
        all = Seting.objects.all()
    return render(request , 'settings/sitesetting.html' , {'all': all , 'fullurl':fullurl})