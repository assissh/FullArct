from django.db import models
from django.conf import settings
from django.urls import reverse
from Comments.models import Comments
from ProfileProjects.models import ProfileProjects
from portfolio_element.models import PortfolioElement
from Ratings.models import Rating
from video.models import video


class Singer(models.Model):
    Singer_Comments= models.ForeignKey(Comments, on_delete=models.CASCADE)
    Singer_Daily_Charges = models.IntegerField()
    Singer_Description = models.CharField(max_length=200)
    Singer_Financials_Available = models.BooleanField(max_length=200)
    Singer_Genre = models.CharField(max_length=200)
    Singer_Languages= models.CharField(max_length=100)
    Singer_Portfolio= models.ForeignKey(PortfolioElement, on_delete=models.CASCADE)
    Singer_Profile_Projects= models.ForeignKey(ProfileProjects, on_delete=models.CASCADE)
    Singer_Ratings= models.ForeignKey(Rating, on_delete=models.CASCADE)
    Singer_Scale_Rate = models.CharField(max_length=200)
    
    Singing_Style = models.CharField(max_length=100)
    Singer_Video = models.ForeignKey(video, on_delete=models.CASCADE)

    def __str__(self):
        return self.Singer_Description

    def get_absolute_url(self):
        return reverse('Singer_details', args=[str(self.id)])



# Create Singers Comments here.


class Comment(models.Model):

    Singer_Comment = models.CharField(max_length=150, null=False)
    Comment_Singer = models.ForeignKey(Singer, null=False,related_name='commentsSinger', on_delete=models.CASCADE)
    Singer_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='CommentssSinger', on_delete=models.CASCADE)

    Singer_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Singer_Comment

    def get_absolute_url(self):
        return reverse('Singer_list')
