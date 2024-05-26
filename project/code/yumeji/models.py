from django.db import models

class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)

class Project(models.Model):
    ProjectID = models.AutoField(primary_key=True)
    ProjectName = models.CharField(max_length=255)
    Description = models.TextField()
    OwnerID = models.ForeignKey(User, on_delete=models.CASCADE)

class ProjectMember(models.Model):
    ID = models.AutoField(primary_key=True)
    ProjectID = models.ForeignKey(Project, on_delete=models.CASCADE)
    MemberID = models.ForeignKey(User, on_delete=models.CASCADE)

class ChatMessage(models.Model):
    MessageID = models.AutoField(primary_key=True)
    ProjectID = models.ForeignKey(Project, on_delete=models.CASCADE)
    SenderID = models.ForeignKey(User, on_delete=models.CASCADE)
    Content = models.TextField()
    Timestamp = models.DateTimeField()

class File(models.Model):
    FileID = models.AutoField(primary_key=True)
    ProjectID = models.ForeignKey(Project, on_delete=models.CASCADE)
    FileName = models.CharField(max_length=255)
    FilePath = models.CharField(max_length=255)
    UploaderID = models.ForeignKey(User, on_delete=models.CASCADE)
    UploadTimestamp = models.DateTimeField()

class Tag(models.Model):
    TagID = models.AutoField(primary_key=True)
    TagName = models.CharField(max_length=255)
    TagColor = models.CharField(max_length=255)

class Task(models.Model):
    TaskID = models.AutoField(primary_key=True)
    ProjectID = models.ForeignKey(Project, on_delete=models.CASCADE)
    TaskName = models.CharField(max_length=255)
    Description = models.TextField()
    AssigneeID = models.ForeignKey(User, on_delete=models.CASCADE)
    DueDate = models.DateTimeField()
    Progress = models.CharField(max_length=255)
    Tags = models.ManyToManyField(Tag)