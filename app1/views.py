from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from .utils import *
from django.views.generic.detail import DetailView


class ShopView(CreateAPIView, ListAPIView):

    def list(self, request, *args, **kwargs):
        city = request.query_params.get('city', '')
        street = request.query_params.get('street', '')
        open = request.query_params.get('open', '')
        qs = get_shop_qs(city, street)
        list_ser = ListSer(qs, many=True)
        print("===========list_ser.data:", list_ser.data)
        return Response(list_ser.data)

    def create(self, request):
        # Паралелльно сохраняю объект city
        city_ser = CityMS(data={"city": request.data['city']})
        if city_ser.is_valid():
            city_obj = city_ser.save(city_ser.validated_data)
        else:
            return Response("Ошибка в названии города") # + status code

        request.data.update({"city": city_obj.id})
        # Паралелльно сохраняю объект street
        street_ser = StreetMS(data={"city": request.data['city'], "street": request.data['street']})
        if street_ser.is_valid():
            street_obj = street_ser.save(street_ser.validated_data)
        else:
            return Response("Ошибка в названии улицы")

        request.data.update({"street": street_obj.id})
        # Сохранение объекта Shop
        shop_ser = ShopMS(data=request.data)
        if shop_ser.is_valid():
            shop_obj = shop_ser.save(shop_ser.validated_data)
            return Response(shop_obj.id)
        else:
            return Response("Ошибка при сохранении магазина")


class CityView(ListAPIView):
    serializer_class = CityMS
    queryset = City.objects.all()


class StreetView(ListAPIView):
    serializer_class = RetrSer

    def get_queryset(self):
        city_id = self.kwargs.get('city_id')
        qs = Street.objects.filter(city_id=city_id)
        return qs
