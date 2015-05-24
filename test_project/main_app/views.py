import json

from django.http import HttpResponse

from .models import Country, City, Street


# Create your views here.
def main_function(request, country_id=None, city_id=None, street_id=None):
    '''

    '''

    data = {}
    nothing_found = 'oops, nothing found!'

    if all((country_id, city_id, street_id)):
        data['type'] = 'country_id, city_id, street_id received'

        try:
            street = Street.objects.get(
                id=street_id,
                city__id=city_id,
                city__country__id=country_id
            )
        except Street.DoesNotExist:
            data['content'] = nothing_found
        else:
            data['content'] = street.__json__()
    elif all((country_id, city_id)):
        data['type'] = 'country_id, city_id received'

        try:
            city = City.objects.get(
                id=city_id,
                country__id=country_id
            )
        except City.DoesNotExist:
            data['content'] = nothing_found
        else:
            data['content'] = city.__json__()
    else:
        data['type'] = 'country_id received'

        try:
            country = Country.objects.get(id=country_id)
        except Country.DoesNotExist:
            data['content'] = nothing_found
        else:
            data['content'] = country.__json__()

    return HttpResponse(json.dumps(data), content_type="application/json")
