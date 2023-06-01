from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

User = get_user_model()


def delete_user(user):
    data = User.objects.get(pk=user.pk)
    data.is_active = False
    data.save()
    return data
