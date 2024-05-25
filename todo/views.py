from rest_framework import generics,mixins
from .models import *
from . serializers import *


class todo_list(generics.GenericAPIView,mixins.ListModelMixin
                ,mixins.CreateModelMixin):
    
    queryset = todo_model.objects.all()
    serializer_class = todo_serializer


    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
class todo_modify(generics.GenericAPIView,mixins.UpdateModelMixin
                ,mixins.DestroyModelMixin,mixins.RetrieveModelMixin):
    
    queryset = todo_model.objects.all()
    serializer_class = todo_serializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)