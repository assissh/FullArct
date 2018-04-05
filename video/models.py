

from django.conf import settings

from django.urls import reverse






from django.db import models
class video(models.Model):
    my_video = models.FileField()
    owned_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)



    def __str__(self):
        return self.my_video

    def get_absolute_url(self):
        return reverse('video_details', args=[str(self.id)])


# Create helpsubcategorys Comments here.


class Comment(models.Model):

    video_Comment = models.CharField(max_length=150, null=False)
    # Comment_helpsubcategory = models.ForeignKey(video, null=False, on_delete=models.CASCADE)
    helpsubcategory_Comment_Author = models.ForeignKey(video,related_name='image', on_delete=models.CASCADE,null=True)



    def __str__(self):
        return self.video_Comment

    def get_absolute_url(self):
        return reverse('image_list')
