from .models import *


def get_shop_qs(city='', street=''):

    if city and street:
        city_id = City.objects.filter(city=city).first().id
        street_id = Street.objects.filter(street=street)\
                                  .filter(city=city_id)\
                                  .first().id
        qs = Shop.objects\
                     .filter(city=city_id)\
                     .filter(street=street_id)

    elif city and not street:
        city_id = City.objects.filter(city=city).first().id
        qs = Shop.objects \
            .filter(city=city_id)

    elif street and not city:
        street_id = Street.objects.filter(street=street) \
                    .first().id
        qs = Shop.objects \
            .filter(street=street_id)

    else:
        qs = Shop.objects.all()

    return qs