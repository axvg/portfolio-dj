from django.db.models import BooleanField, EmailField, Model, CharField, URLField, TextField, ForeignKey, CASCADE


class Profile(Model):
    name = CharField(max_length=32, blank=False, null=False)
    occupation = CharField(max_length=32, blank=False, null=False)
    website = URLField()
    phone = CharField(max_length=32, blank=False, null=False)
    location = CharField(max_length=32, blank=False, null=False)
    email = EmailField()
    degree = CharField(max_length=32, blank=False, null=False)
    freelance = BooleanField(default=True)

class Project(Model):
    title = CharField(max_length=32, blank=False, null=False)
    link = URLField()

class ResumeItem(Model):
    title = CharField(max_length=32, blank=False, null=False)
    subtitle = CharField(max_length=32, blank=False, null=False)
    period = CharField(max_length=32, blank=False, null=False)

class Sentence(Model):
    resume_item = ForeignKey(ResumeItem, on_delete=CASCADE)
    text = CharField(max_length=32, blank=True, null=True)

class Summary(ResumeItem):
    ...

class Education(ResumeItem):
    ...

class Experience(ResumeItem):
    ...