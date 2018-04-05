from django.db import models

from django.conf import settings

from django.urls import reverse
from Ratings.models import Rating
from Comments.models import Comments
from portfolio_element.models import PortfolioElement
from ProfileProjects.models import ProfileProjects
from video.models import video
# Create your actorss here.


class Actors(models.Model):

    Actor_Id = models.CharField(max_length=100,unique=True)
    Actor_rating = models.ForeignKey(Rating,related_name='actors',on_delete=models.CASCADE)
    Actor_Body_Type = models.TextField(max_length=100)
    Actors_comment = models.ForeignKey(Comments, related_name='actors', on_delete=models.CASCADE)
    Actor_Description = models.TextField(max_length=100)
    Actor_Ethnicity = models.TextField(max_length=100)
    Actor_Eye_Color = models.TextField(max_length=100)
    Actor_Favorite_Acting_Styles = models.TextField(max_length=100)
    Actor_Height =models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    Actors_Portfolio= models.ForeignKey(PortfolioElement,related_name='actors',on_delete=models.CASCADE)
    Actors_profileproject = models.ForeignKey(ProfileProjects, related_name='actors',on_delete=models.CASCADE)
    Actor_Rates = models.CharField(max_length=100)
    Actor_SceneComfort = models.TextField(max_length=100)
    Actor_Skin_Color = models.TextField(max_length=100)
    Actor_Smoker = models.BooleanField(default=False)
    Actors_Special_skill = models.CharField(max_length=100)
    Actors_video = models.ForeignKey(video,related_name='actors',on_delete=models.CASCADE)
    Actor_Weight = models.CharField(max_length=100)
    Actors_Creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='actors_Creator',on_delete=models.CASCADE)
    Actor_Modified_Date = models.DateTimeField(auto_now_add=True)
    Actor_Created_Date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.Actor_Id

    def get_absolute_url(self):
        return reverse('actors_details', args=[str(self.id)])


# Create actorss Comments here.


class Comment(models.Model):

    Actors_Comment = models.CharField(max_length=150, null=False)
    Comment_Actors = models.ForeignKey(Actors, null=False, on_delete=models.CASCADE)
    Actors_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="actors", on_delete=models.CASCADE)

    # actors_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Actors_Comment

    def get_absolute_url(self):
        return reverse('actors_list')


