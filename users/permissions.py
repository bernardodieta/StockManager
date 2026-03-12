from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def get_user_role(user):
    if not user.is_authenticated:
        return None
    if user.is_superuser:
        return "admin"
    profile = getattr(user, "profile", None)
    if profile:
        return profile.rol
    return None


def is_admin_user(user):
    return get_user_role(user) == "admin"


def is_empleado_user(user):
    return get_user_role(user) == "empleado"


class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return is_admin_user(self.request.user)


class EmployeeOrAdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        role = get_user_role(self.request.user)
        return role in ["admin", "empleado"]