from django.contrib import admin
from .models import Task, Note, About, Contact

admin.site.register(Task)
admin.site.register(Note)
admin.site.register(About)
admin.site.register(Contact)
