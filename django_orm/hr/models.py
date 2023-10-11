from django.db import models

from django.db import models


class tg_group_content(models.Model):
    from_name = models.CharField(max_length=50)
<<<<<<< HEAD
    text = models.TextField()
    content = models.TextField()
    title = models.CharField(max_length=70)
    message_details = models.CharField(max_length=50)
    message_id = models.IntegerField()
    replied_message_details = models.CharField(max_length=50)
    replied_message_id = models.IntegerField()
    joined = models.BooleanField(default=True)
=======
    message_id = models.IntegerField()
    message_details = models.CharField(max_length=50)
    title = models.CharField(max_length=70)

    replied_message_id = models.IntegerField()
    replied_message_details = models.CharField(max_length=50)
    text = models.TextField()
    content = models.TextField()
    joined = models.BooleanField()
>>>>>>> origin/main

class tg_channel_content(models.Model):
    form_name = models.CharField(max_length=50)
    text = models.TextField()
    title = models.CharField(max_length=70)
    message_id = models.IntegerField()



