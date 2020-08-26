from .signals import object_viewed_signal


class objectViewedMixin(object):
    def get_context_data(self,*arg,**kwargs):
        context=super(objectViewedMixin,self).get_context_data(*arg,**kwargs)
        request=self.request 
        instance=context.get('object')
        if instance:
            object_viewed_signal.send(instance.__class__,instance=instance,request=request)
        return context