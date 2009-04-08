from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from sha import sha

from models import UrlMapping


class UrlForm(forms.Form):
    """a simple form to verify a URL"""
    url = forms.URLField()


def create(request):
    """create a shortened URL"""
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            UrlMapping(url=url, sha_hash=sha(url).hexdigest()).save()
            
            return HttpResponseRedirect('/')
    else:
        form = UrlForm()

    recent_urls = UrlMapping.objects.all()[:5]
    return render_to_response('create.html', {
        'form': form,
        'recent_urls': recent_urls,
    })

def access(request, sha_hash):
    """accesses the URL with hash that starts with sha_hash"""
    url = UrlMapping.objects.get(sha_hash__startswith=sha_hash)
    return HttpResponseRedirect(url.url)
