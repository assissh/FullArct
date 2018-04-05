from django.db import models
from django.conf import settings
from django.urls import reverse
from Costumes.models import Costume
from Location.models import Location
from pets.models import Pets
from Prop.models import Prop
from actionvehicle.models import ActionVehicle


class UserCoinBox(models.Model):
   UserCoinBox_Costume_ListUserCoinBox_Costume_List=models.ForeignKey(Costume,on_delete=models.CASCADE)
   UserCoinBox_Location_List = models.ForeignKey(Location,on_delete=models.CASCADE)
   UserCoinBox_Pet_List = models.ForeignKey(Pets,on_delete=models.CASCADE)
   UserCoinBox_Prop_List = models.ForeignKey(Prop,on_delete=models.CASCADE)
   UserCoinBox_Vehicle_List = models.ForeignKey(ActionVehicle,on_delete=models.CASCADE)
   def __str__(self):
       return str(self.id)

   def get_absolute_url(self):
       return reverse('UserCoinBox_details', args=[str(self.id)])



# CreateUserCoinBox Comments here.


class Comment(models.Model):
  UserCoinBox_Comment = models.CharField(max_length=150, null=False)
  Comment_UserCoinBox = models.ForeignKey(UserCoinBox, null=False,related_name='commentsUserCoinBox', on_delete=models.CASCADE)
  UserCoinBox_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='CommentssUserCoinBox', on_delete=models.CASCADE)
  UserCoinBox_Comment_Created_on = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.UserCoinBox_Comment

  def get_absolute_url(self):
    return reverse('UserCoinBox_list')
