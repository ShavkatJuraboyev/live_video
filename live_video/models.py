from django.db import models
from django.templatetags.static import static
# Create your models here.


class LiveVideo(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    live_img = models.FileField(upload_to='live_img/', null=True, blank=True)
    live_url = models.CharField(max_length=500, null=True, blank=True)


    def __str__(self) -> str:
        return self.name

    @property
    def get_live_img(self):
        return self.live_img.url if self.live_img else static('img/logo.png')