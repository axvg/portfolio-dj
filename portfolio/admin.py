from django.contrib import admin

from portfolio.models import Profile, Project, Summary, Education, Experience, Sentence, ResumeItem

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Summary)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Sentence)
admin.site.register(ResumeItem)