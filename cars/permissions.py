from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect


class PermissionsManagerMixin(LoginRequiredMixin):
    def is_manager(self):
        return self.request.user.role == "MANAGER"

    def dispatch(self, request, *args, **kwargs):
        if not self.is_manager():
            messages.error(
                self.request,
                f"У тебя нет прав доступа на просмотр всех машин. Обратись админу",
            )
            return redirect("cars:list-car")
        return super().dispatch(request, *args, **kwargs)
