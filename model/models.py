from django.db import models

from django.conf import settings
from Comments.models import Comments
from portfolio_element.models import PortfolioElement
from Ratings.models import Rating
from video.models import video

from django.urls import reverse

# Create your Models here.


class Models(models.Model):
    Models_Body_Type = models.CharField(max_length=200)
    Models_Comments = models.ForeignKey(Comments,related_name='Models', on_delete=models.CASCADE)
    Models_Description = models.CharField(max_length=200)
    Models_Ethnicity = models.CharField(max_length=200)
    Models_Eye_Colour = models.CharField(max_length=200)
    Models_Hair_Colour = models.CharField(max_length=200)
    Models_Height = models.CharField(max_length=100)
    Models_ID = models.CharField(max_length=100)
    Models_Portfolio = models.ForeignKey(PortfolioElement,related_name='Models', on_delete=models.CASCADE)
    Models_Rating = models.ForeignKey(Rating,related_name='Models', on_delete=models.CASCADE)
    Models_Scene_Comfort = models.CharField(max_length=200)
    Models_Skin_Color = models.CharField(max_length=200)
    Models_Smoker = models.CharField(max_length=100)
    Models_Special_Skills = models.CharField(max_length=200)
    Models_Video = models.ForeignKey(video, related_name='Models',on_delete=models.CASCADE)
    Models_Weight = models.CharField(max_length=100)


    # Models_Message = models.CharField(max_length=280)
    Models_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='model', on_delete=models.CASCADE)
    Models_Created_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Models_Body_Type

    def get_absolute_url(self):
        return reverse('Model_details', args=[str(self.id)])


# Create Models Comments here.


class Comment(models.Model):

    Model_Comment = models.CharField(max_length=150, null=False)
    # Comment_Model = models.ForeignKey(Model, null=False, on_delete=models.CASCADE)
    Model_Comment_Author = models.ForeignKey(Models, related_name='comment', on_delete=models.CASCADE)

    # Model_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Model_Comment

    def get_absolute_url(self):
        return reverse('Model_list')
