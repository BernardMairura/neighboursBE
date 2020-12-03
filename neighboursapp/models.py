from django.contrib.auth.models import AbstractUser,User
from django.db import models
from django.urls import reverse
from django.db.models import CharField
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
# from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save



# class User(AbstractUser):

#     is_neighbor=models.BooleanField(default=True)




class HoodadminProfile(models.Model):
    admin = models.ForeignKey(User,on_delete=models.CASCADE, related_name='hood_administrator')
    bio = HTMLField(max_length=100, blank=True)
    prof_picture= CloudinaryField('image')

    def __str__(self):
        return f'{self.user.username} HoodadminProfile'

    class Meta:
        db_table = 'adminprof'
 
   



class NeighborProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, null=True, related_name='neighbor_profile')
    location=models.CharField(max_length=30,blank=True)
    bio =HTMLField(max_length=100, blank=True)
    prof_picture= CloudinaryField('image')
    contact = models.CharField(max_length=15, blank=True)
    hoodname = models.ForeignKey("Neighborhood", on_delete=models.CASCADE,related_name='home', null=True)



class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    admin = models.ForeignKey("HoodadminProfile", on_delete=models.CASCADE, related_name='neighborhood')
    hoodphoto = CloudinaryField('image')
    body= HTMLField()
    residents= models.IntegerField(null=True, blank=True)
    emergency_contact = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'neighborhood'
    

    def __str__(self):
        return f'{self.name} neighborhood'

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)


   


class Business(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    body = HTMLField(blank=True)
    neighborhood = models.ForeignKey("Neighborhood", on_delete=models.CASCADE, related_name='business')
    location = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.name} Business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(name__icontains=name).all()










































# class User(AbstractUser):
#     class Types(models.TextChoices):
#         SYSTEMADMIN="SYSTEMADMIN","SystemAdmin"
#         NEIGHBORADMIN="NEIGHBORADMIN","NeighborAdmin"
#         NEIGHBOR="NEIGHBOR","Neighbor"

#         type=models.CharField(_('Type'),max_length=50, choices=Types.choices,default=Types.NEIGHBOR)


#         name=models.CharField(_("Name of User"),blank=True,max_length=255)

#         def get_absolute_url(self):
#             return reverse("users:detail",kwargs={"username":self.username})


# class SytemadminManager(models.Manager):
#     def get_queryset(self, *args, **kwargs):
#         return super().get_queryset(*args, **kwargs).filter(type=User.Types.SYSTEMADMIN)

# class NeighboradminManager(models.Manager):
#     def get_queryset(self, *args, **kwargs):
#         return super().get_queryset(*args, **kwargs).filter(type=User.Types.NEIGHBORADMIN)


# class NeighborManager(models.Manager):
#     def get_queryset(self, *args, **kwargs):
#         return super().get_queryset(*args, **kwargs).filter(type=User.Types.NEIGHBOR)


# class SystemAdmin(User):
#     objects=SystemAdmin
#     class Meta:
#         proxy=True


# class NeighborAdmin(User):
#     objects=NeighborManager
#     class Meta:
#         proxy=True

# class Neighbor(User):
#     objects=Neighbor
#     class Meta:
#         proxy=True




