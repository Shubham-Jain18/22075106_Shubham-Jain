from django.shortcuts import render, redirect
from django.http import HttpResponse
from shortener.models import URL


# Create your views here.

def createURL(request):
    if request.method == "POST":
        full_url = request.POST.get('full_url')
        obj = URL.create(full_url)
        return render(request, 'shortener/index.html', {
            'full_url': obj.full_url,
            'short_url': request.get_host() + '/' + obj.short_url,
            'a_url': obj.short_url,
        })
    return render(request, 'shortener/index.html')



def routetoURL(request, key):
    try:
        obj = URL.objects.get(short_url=key)
        return redirect(obj.full_url)

    except:
        return redirect(createURL)


def URLlist(request):
    data = URL.objects.all().values()
    print(data)
    context = {'URLs': data}
    return render(request, 'shortener/URLlist.html', context)
