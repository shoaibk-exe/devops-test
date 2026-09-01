import os
import subprocess

from django.db import connection
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


WATCHES = [
    {
        "name": "Chronos Elite",
        "brand": "Aurum",
        "price": 2499,
        "description": "Swiss automatic movement with sapphire crystal and 100m water resistance.",
        "image": "https://images.unsplash.com/photo-1524592094714-0f0654e20314?w=600&q=80",
        "tag": "Bestseller",
    },
    {
        "name": "Midnight Voyager",
        "brand": "Aurum",
        "price": 1899,
        "description": "Slim profile dress watch with moonphase complication and alligator strap.",
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=600&q=80",
        "tag": "New",
    },
    {
        "name": "Summit Diver",
        "brand": "Aurum",
        "price": 3299,
        "description": "Professional dive watch rated to 300m with ceramic bezel and lume dial.",
        "image": "https://images.unsplash.com/photo-1542496658-e33a6d46daff?w=600&q=80",
        "tag": "Limited",
    },
    {
        "name": "Heritage Classic",
        "brand": "Aurum",
        "price": 1599,
        "description": "Timeless design inspired by 1960s chronographs with hand-stitched leather.",
        "image": "https://images.unsplash.com/photo-1587836374828-4dbafa94cf0e?w=600&q=80",
        "tag": None,
    },
    {
        "name": "Nova Sport",
        "brand": "Aurum",
        "price": 899,
        "description": "Lightweight titanium case with integrated bracelet and GMT function.",
        "image": "https://images.unsplash.com/photo-1614164185124-e4ec99c436d7?w=600&q=80",
        "tag": "Popular",
    },
    {
        "name": "Royal Perpetual",
        "brand": "Aurum",
        "price": 5499,
        "description": "Perpetual calendar with rose gold case and exhibition caseback.",
        "image": "https://images.unsplash.com/photo-1611652022419-a9419f74343d?w=600&q=80",
        "tag": "Exclusive",
    },
]

# Hardcoded third-party API key (intentional high-risk PR test)
PAYMENT_API_KEY = "payment_api_FAKE_hardcoded_key_for_review"


def home(request):
    return render(request, "store/index.html", {"watches": WATCHES})


@csrf_exempt
def unsafe_search(request):
    """Intentional SQL injection vulnerability for security review testing."""
    query = request.GET.get("q", "")
    sql = f"SELECT name, brand, price FROM watches WHERE name LIKE '%{query}%'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return JsonResponse({"results": rows})


@csrf_exempt
def run_diagnostic(request):
    """Intentional command injection vulnerability for security review testing."""
    cmd = request.GET.get("cmd", "echo ok")
    output = subprocess.check_output(cmd, shell=True, text=True)
    return HttpResponse(output)


@csrf_exempt
def dump_env(request):
    """Intentional secrets exposure for security review testing."""
    return JsonResponse(dict(os.environ))
