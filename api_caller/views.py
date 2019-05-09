import json
import requests as req_pkg

from django.http import JsonResponse
from django.shortcuts import render


def test_api(request):
    return render(request, 'test_api.html')


def wiki_api(request):
    url = 'https://en.wikipedia.org/w/api.php'
    # data = {
    #     "titles": request.GET.get('word'),
    #     "action": "query",
    #     "prop": "images",
    #     "format": "json"
    # }
    data = {
        "titles": request.GET.get('word'),
        "action": "query",
        "prop": "pageimages",
        "pithumbsize": 500,
        "format": "json",
    }
    img = None
    # rop=&format=json&pithumbsize=100
    r = req_pkg.get(url, params=data)
    r_data = json.loads(r.text)
    r_pages = r_data.get('query', {}).get('pages')
    if r_pages:
        for key, img_parent in r_pages.items():
            img = img_parent.get("thumbnail", {}).get("source")
    # print(img)
    return JsonResponse({
        "img": img
    })



