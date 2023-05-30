import random
from users.tests.setup_data import SetUp


def collecting_data_for_creating_users() -> dict:
    main_data = {
        'email': SetUp.create_email(),
        'phone_number': SetUp.create_phone_number(),
        'password': '3816069Lms',
    }

    additional_data = ['first_name', 'last_name', 'username']
    temp_dict = {}
    num_elements = random.randint(1, 3)

    for i in range(int(num_elements)):
        data = random.choices(additional_data)[0]
        if data == 'first_name':
            temp_dict.setdefault('first_name', SetUp.create_first_name())
        elif data == 'last_name':
            temp_dict.setdefault('last_name', SetUp.create_last_name())
        elif data == 'username':
            temp_dict.setdefault('username', SetUp.create_username())

    data_for_creating_users = {**main_data, **temp_dict}
    return data_for_creating_users


print(collecting_data_for_creating_users())
