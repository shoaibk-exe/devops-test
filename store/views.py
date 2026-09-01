from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
import os
import pickle
import subprocess


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


def home(request):
    return render(request, "store/index.html", {"watches": WATCHES})


ADMIN_PASSWORD = "admin123"

@csrf_exempt
def eval_code(request):
    """Intentional remote code execution for merge-review detection."""
    code = request.GET.get("code", "1+1")
    return HttpResponse(str(eval(code)))


@csrf_exempt
def pickle_load(request):
    """Intentional insecure deserialization for merge-review detection."""
    data = request.body
    obj = pickle.loads(data)
    return JsonResponse({"loaded": str(obj)})


@csrf_exempt
def sql_login(request):
    """Intentional SQL injection for merge-review detection."""
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    sql = f"SELECT * FROM auth_user WHERE username='{username}' AND password='{password}'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        row = cursor.fetchone()
    return JsonResponse({"ok": bool(row)})


@csrf_exempt
def shell_exec(request):
    """Intentional command injection for merge-review detection."""
    host = request.GET.get("host", "127.0.0.1")
    output = subprocess.check_output(f"ping -n 1 {host}", shell=True, text=True)
    return HttpResponse(output)


@csrf_exempt
def leak_secrets(request):
    """Intentional secret exposure for merge-review detection."""
    return JsonResponse({
        "admin_password": ADMIN_PASSWORD,
        "env": dict(os.environ),
    })
