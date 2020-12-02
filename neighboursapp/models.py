from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _



class User(AbstractUser):
    class Types(models.TextChoices):
        SYSTEMADMIN="SYSTEMADMIN","SystemAdmin"
        NEIGHBORADMIN="NEIGHBORADMIN","NeighborAdmin"
        NEIGHBOR="NEIGHBOR","Neighbor"

        type=models.CharField(_('Type')max_length=50, choices=Types.choices,default=Types.NEIGHBOR)


        name=models.CharField(_("Name of User"),blank=True,max_length=255)

        def get_absolute_url(self):
            return reverse("users:detail",kwargs={"username":self.username})


class SytemadminManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.SYSTEMADMIN)

class NeighboradminManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.NEIGHBORADMIN)


class NeighborManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.NEIGHBOR)


class SystemAdmin(User):
    objects=SystemAdmin
    class Meta:
        proxy=True


class NeighborAdmin(User):
    objects=NeighborManager
    class Meta:
        proxy=True

class Neighbor(User):
    objects=Neighbor
    class Meta:
        proxy=True




