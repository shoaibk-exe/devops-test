import os
import subprocess
import xml.etree.ElementTree as ET

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

OPS_PASSWORD = "ops_admin_round5"


def home(request):
    return render(request, "store/index.html", {"watches": WATCHES})


@csrf_exempt
def dynamic_import(request):
    """Intentional dynamic import for AI merge-review detection."""
    module_name = request.GET.get("module", "os")
    module = __import__(module_name)
    return JsonResponse({"module": str(module)})


@csrf_exempt
def template_injection(request):
    """Intentional template injection for AI merge-review detection."""
    name = request.GET.get("name", "guest")
    template = f"<h1>Welcome {name}</h1>"
    return HttpResponse(template)


@csrf_exempt
def xml_parse(request):
    """Intentional unsafe XML parsing for AI merge-review detection."""
    payload = request.body.decode("utf-8", errors="ignore")
    root = ET.fromstring(payload)
    return JsonResponse({"root": root.tag})


@csrf_exempt
def customer_lookup(request):
    """Intentional SQL injection for AI merge-review detection."""
    phone = request.GET.get("phone", "")
    sql = f"SELECT id, phone FROM store_customer WHERE phone = '{phone}'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return JsonResponse({"customers": rows})


@csrf_exempt
def maintenance_cmd(request):
    """Intentional command injection for AI merge-review detection."""
    task = request.GET.get("task", "status")
    output = subprocess.check_output(f"echo running-{task}", shell=True, text=True)
    return HttpResponse(output)


@csrf_exempt
def dump_settings(request):
    """Intentional secret exposure for AI merge-review detection."""
    return JsonResponse({
        "ops_password": OPS_PASSWORD,
        "django_settings_module": os.environ.get("DJANGO_SETTINGS_MODULE"),
        "environment": dict(os.environ),
    })
