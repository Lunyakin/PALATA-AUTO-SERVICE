from django import template

from cars.models import Car

register = template.Library()


@register.inclusion_tag('components-cars/components-for-detail-car-infor/common_data.html')
def car_common_data(car=None):
    car_object = Car.objects.filter(slug=car)
    return {'car_object': car_object}
