from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Cakes
from api.serializers import CakeSerializer

#localhost:8000/cakes/ 


class CakesView(APIView):
    def get(self,request,*args,**kw):
        qs=Cakes.objects.all()
        serializer=CakeSerializer(qs,many=True)
        return Response(data=serializer.data)

    def post(self,request,*args,**kw):
        serializer=CakeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors) 

class CakeDetailsView(APIView):
    def get(self,request,*args,**kw):
        id=kw.get("id")
        qs=Cakes.objects.get(id=id)
        serializer=CakeSerializer(qs,many=False)
        return Response(data=serializer.data)

    def put(self,request,*args,**kw):
        id=kw.get("id")
        obj=Cakes.objects.get(id=id)
        serializer=CakeSerializer(data=request.data,instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)    

    def delete(self,request,*args,**kw):
        id=kw.get("id")
        obj=Cakes.objects.get(id=id)
        obj.delete()

        return Response(data="cake delete")
               
           
