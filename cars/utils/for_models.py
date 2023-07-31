def path_for_cars_foto(instance, filename):
    return 'car/car_{0}/car_photos/{1}'.format(instance.car.reg_number, filename)


def path_for_note_foto(instance, filename):
    temp = instance.car_note
    from cars.models import Car
    car = Car.objects.get(car_note=temp)

    return 'car/car_{0}/note_photos/{1}'.format(car, filename)
