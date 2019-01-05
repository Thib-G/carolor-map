from django.http import HttpResponse
from django.core.serializers import serialize
from .models import Partner

# Create your views here.
def all_partners(request):
    return HttpResponse(serialize('geojson', Partner.objects.all(),
            geometry_field='geom',
            fields=('name', 'address', 'streetnumber', 'postcode', 'city', 'phone', 'url', 'category',)),
        content_type='application/json')
