from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting, ContactFormMessage, ContactFormu
from house.models import House, Category


def index(request):
    setting = Setting.objects.get(pk=1)
    slider_data = House.objects.all()[:3]
    category = Category.objects.all()
    random_houses = House.objects.all()[:6]
    last_houses = House.objects.all().order_by('-id')[:6]

    context = {'setting': setting,
               'slider_data': slider_data,
               'page': 'home',
               'category': category,
               'random_houses': random_houses,
               'last_houses': last_houses,
               }
    return render(request, 'index.html', context)



def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'hakkimizda.html', context)


def referanslar(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'referanslar.html', context)


def iletisim(request):
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız başarıyla gönderilmiştir.")
            return HttpResponseRedirect('/iletisim')

    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    context = {'setting': setting, 'form': form}
    return render(request, 'iletisim.html', context)


def category_houses(request, id, slug):
    houses = House.objects.filter(category_id=id)
    category = Category.objects.all()
    categoryData = Category.objects.get(pk=id)
    context = {'houses': houses, 'category': category, 'categoryData': categoryData}
    return render(request, 'houses.html', context)