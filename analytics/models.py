from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


from .signals import object_viewed_signal

class objectViewed(models.Model):
    user=models.ForeignKey(User , on_delete=models.CASCADE)
    content_type=models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id=models.PositiveIntegerField()
    content_object=GenericForeignKey('content_type','object_id')
    timestamp=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "%s viewed on %s by %s" %(self.content_object,self.timestamp,self.user)

    class Meta:
        ordering=['-timestamp']
        verbose_name= 'Object Viewed'
        verbose_name_plural= 'Objects Viewed'



def object_viewed_receiver(sender,instance,request,*args,**kwargs):
    c_type=ContentType.objects.get_for_model(sender)
    new_view_obj=objectViewed.objects.create(
        user=request.user,
        content_type=c_type,
        object_id=instance.id
    )

object_viewed_signal.connect(object_viewed_receiver)