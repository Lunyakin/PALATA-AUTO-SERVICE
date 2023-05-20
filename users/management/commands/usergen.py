import time

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from users.management.commands.utils.create_users_data import collecting_data_for_creating_users

User = get_user_model()


class Command(BaseCommand):
    help = "Добавляем пользователей в базу данный (таблица User)"

    def add_arguments(self, parser):
        parser.add_argument('qty', type=int, help='Количество добавляемых пользователей')

    def handle(self, *args, **options):
        qty = options['qty']

        for i in range(qty):
            data_for_user = collecting_data_for_creating_users()
            User.objects.create_user(**data_for_user)
            self.stdout.write('User "%s (%s) (%s)" создан' % (data_for_user['email'], data_for_user['phone_number'], data_for_user['password']))
            time.sleep(5)
