from django.db import models
from django.conf import settings
from django.urls import reverse
from Location_Category.models import Location_Category
from Location.models import Location


class FilmRecceTourGuide(models.Model):
    FilmRecceTourGuide_EndLocation = models.CharField(max_length=200)
    FilmRecceTourGuide_EndTime = models.DateField()
    FilmRecceTourGuide_FilmLocationFromGuided = models.ForeignKey(Location_Category,on_delete=models.CASCADE,related_name='FilmRecceTourGuide')
    FilmRecceTourGuide_Passing_Year = models.CharField(max_length=100)
    FilmRecceTourGuide_guidedlocation_List = models.ForeignKey(Location, related_name='filmreccetourguides', on_delete=models.CASCADE)
    FilmRecceTourGuide_StartLocation =  models.CharField(max_length=100)
    FilmRecceTourGuide_StartTime = models.DateField()
    FilmRecceTourGuide_TourGuideName = models.CharField(max_length=100)
    FilmRecceTourGuide_Creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='FilmRecceRoutesGuide', on_delete=models.CASCADE)
    FilmRecceTourGuide_Modified_Date = models.DateField(auto_now_add=True,editable=True)
    FilmRecceTourGuide_Created_Time = models.DateField(auto_now_add=True,editable=False)
    def __str__(self):
        return self.FilmRecceTourGuide_EndLocation

    def get_absolute_url(self):
        return reverse('FilmRecceTourGuide_details', args=[str(self.id)])



# Create FilmRecceTourGuides Comments here.


class Comment(models.Model):

    FilmRecceTourGuide_Comment = models.CharField(max_length=150, null=False)
    Comment_FilmRecceTourGuide = models.ForeignKey(FilmRecceTourGuide, null=False,related_name='commentsFilmRecceTourGuide', on_delete=models.CASCADE)
    FilmRecceTourGuide_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='CommentssFilmRecceTourGuide', on_delete=models.CASCADE)

    # FilmRecceTourGuide_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.FilmRecceTourGuide_Comment

    def get_absolute_url(self):
        return reverse('FilmRecceTourGuide_list')
