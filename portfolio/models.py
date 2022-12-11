from django.db.models import BooleanField, EmailField, Model, CharField, URLField


# class Perfil(models.Model):
#     first_name = models.CharField(max_length=32, blank=False, null=False)
#     second_name = models.CharField(max_length=32, blank=False, null=False)
#     photo_URL = models.URLField()
#     school = models.CharField(max_length=32, blank=False, null=False)
#     work = models.CharField(max_length=32, blank=False, null=False)


class Profile(Model):
    name = CharField(max_length=32, blank=False, null=False)
    occupation = CharField(max_length=32, blank=False, null=False)
    website = URLField()
    phone = CharField(max_length=32, blank=False, null=False)
    location = CharField(max_length=32, blank=False, null=False)
    email = EmailField()
    degree = CharField(max_length=16, blank=False, null=False)
    freelance = BooleanField(default=True)
