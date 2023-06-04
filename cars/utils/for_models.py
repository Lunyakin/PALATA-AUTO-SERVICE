def path_for_cars_foto(instance, filename):
    return 'car/car_{0}/{1}'.format(instance.reg_number, filename)
