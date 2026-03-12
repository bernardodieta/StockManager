from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
	ROLE_ADMIN = "admin"
	ROLE_EMPLEADO = "empleado"
	ROLE_CHOICES = [
		(ROLE_ADMIN, "Administrador"),
		(ROLE_EMPLEADO, "Empleado"),
	]

	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
	rol = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_EMPLEADO)

	def __str__(self):
		return f"{self.user.username} - {self.rol}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	profile, _ = UserProfile.objects.get_or_create(user=instance)
	profile.save()
