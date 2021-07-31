from django.db.models import Q
from .models import UserIP

def get_ip(request):
    address = request.META.get('HTTP_X_FORWARDED_FOR')
    if address:
        ip = address.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def manage_visitors(request):
    try:
        ip = get_ip(request)
        user = UserIP(ip=ip)
        ip = UserIP.objects.filter(ip=ip)
        if len(ip):
            ip[0].save()
        else:
            user.save()
    except:
        pass
