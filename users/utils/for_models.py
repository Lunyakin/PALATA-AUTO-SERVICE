def path_for_users_foto(instance, filename):
    """Создаем путь к фотографиям пользователя"""
    return 'users/user_{0}/{1}'.format(instance.phone_number, filename)
