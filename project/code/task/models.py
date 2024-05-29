from django.db import models

# コメントアウトしてる部分は関連付けできるようになったら
class Task(models.Model):
    # project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=255)
    description = models.TextField()
    # assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    due_date = models.DateTimeField()
    progress = models.CharField(max_length=50)
    # tags = models.ManyToManyField('Tag', related_name='tasks')

    def __str__(self):
        return self.name