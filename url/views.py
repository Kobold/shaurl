from django import forms
from django.http import Http404, HttpResponseRedirect
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
            um, created = UrlMapping.objects.get_or_create(
                url=url, defaults={'sha_hash': sha(url).hexdigest()})
            
            return render_to_response('created.html', {'url_mapping': um})
    else:
        form = UrlForm()

    recent_urls = UrlMapping.objects.all()[:5]
    return render_to_response('create.html', {
        'form': form,
        'recent_urls': recent_urls,
    })

def access(request, sha_hash):
    """accesses the URL with hash that starts with sha_hash"""
    ums = UrlMapping.objects.filter(sha_hash__startswith=sha_hash)
    length = len(ums)
    
    if length == 0:
        raise Http404
    elif length == 1:
        return HttpResponseRedirect(ums[0].url)
    else:
        return render_to_response('ambiguous.html', {
            'request_hash': sha_hash,
            'url_mappings': ums[:5],
        })
