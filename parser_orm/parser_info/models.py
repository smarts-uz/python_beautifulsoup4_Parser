from django.db import models
import django
import os

# os.environ["DJANGO_SETTINGS_MODULE"] = "parser_orm.parser_orm.settings"
# django.setup()


class group_content(models.Model):
    from_name = models.CharField(max_length=70, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=70)
    message_details = models.CharField(max_length=50)
    message_id = models.IntegerField()
    replied_message_details = models.CharField(max_length=50)
    replied_message_id = models.IntegerField()
    joined = models.BooleanField(default=True)


class channel_content(models.Model):
    form_name = models.CharField(max_length=50, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=70)
    message_id = models.IntegerField()


class group_video_content(models.Model):
    text_from_learning = models.TextField(null=True, blank=True)
    video_path = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    video_duration = models.CharField(max_length=70, null=True, blank=True)
    data_title = models.CharField(max_length=70)
    message_details = models.CharField(max_length=50)
    message_id = models.IntegerField()
    replied_message_details = models.CharField(max_length=50)
    replied_id = models.IntegerField()
    from_name = models.CharField(max_length=70, null=True, blank=True)




