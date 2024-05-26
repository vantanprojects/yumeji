from django.contrib import admin
from mainpage.models import Project, ProjectMember, ChatMessage, File, Task, Tag

# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectMember)
admin.site.register(ChatMessage)
admin.site.register(File)
admin.site.register(Task)
admin.site.register(Tag)
