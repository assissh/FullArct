from django.db import models
from django.conf import settings
from django.urls import reverse
from Comments.models import Comments
from portfolio_element.models import PortfolioElement
from ProfileProjects.models import ProfileProjects
from Ratings.models import Rating
from video.models import video


class Dancer(models.Model):
    Dancer_Charges_Available = models.BooleanField()
    Dancer_Comment = models.ForeignKey(Comments, related_name='dancers', on_delete=models.CASCADE)
    Dancer_Daily_Charges = models.CharField(max_length=100)
    Dancer_Dancing_Style = models.CharField(max_length=100)
    Dancer_Description = models.CharField(max_length=100)
    Dancer_Genre = models.CharField(max_length=100)
    Dancer_Portfolio = models.ForeignKey(PortfolioElement, related_name='dancers', on_delete=models.CASCADE)
    Dancer_Profile_Project = models.ForeignKey(ProfileProjects, related_name='dancers', on_delete=models.CASCADE)
    Dancer_Rating = models.ForeignKey(Rating, related_name='dancers', on_delete=models.CASCADE)
    Dancer_Video = models.ForeignKey(video, related_name='dancers',on_delete=models.CASCADE)
    Dancer_Creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='dancers', on_delete=models.CASCADE)
    Dancer_Modified_Date = models.DateField(auto_now_add=True,editable=True)
    Dancer_Created_Date  = models.DateField(auto_now_add=True,editable=True)


    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('Dancer_details', args=[str(self.id)])



class Comment(models.Model):

    Dancer_Comment = models.CharField(max_length=150, null=False)
    Comment_Dancer = models.ForeignKey(Dancer,related_name='commentsDancer',null=False, on_delete=models.CASCADE)
    Dancer_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='CommentssDancer', on_delete=models.CASCADE)

    # Dancer_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Dancer_Comment

    def get_absolute_url(self):
        return reverse('Dancer_list')

