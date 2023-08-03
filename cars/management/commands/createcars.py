import random
import time

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from cars.management.commands.utils.create_car_data import create_data_for_creating_car
from cars.models import Car

User = get_user_model()


class Command(BaseCommand):
    help = "Добавляем машины в базу данный (таблица Car)"

    def add_arguments(self, parser):
        parser.add_argument('qty', type=int, help='Максимальное количество машин у пользователя ')

    def handle(self, *args, **options):
        qty = options['qty']

        all_users = User.objects.all()

        for i in all_users:
            for _ in range(random.randint(1, qty)):
                data_for_car = create_data_for_creating_car()
                Car.objects.create(user=i, **data_for_car)
                self.stdout.write('Car "%s" создана у пользователя "%s"' % (data_for_car['reg_number'], i.pk)
                                  )
                time.sleep(5)
