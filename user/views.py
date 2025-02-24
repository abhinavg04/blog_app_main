from django.shortcuts import render
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from .serializers import UserSeralizer,UserProfileSeralizer,CommentSerializer,PostSerializer
from .models import *
# Create your views here.


class UserView(ViewSet):
    def create(self,request):
        ser = UserSeralizer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"User created"},status=status.HTTP_201_CREATED)
        return Response({'msg':'creation failed'},status=status.HTTP_406_NOT_ACCEPTABLE)
    
class ProfileView(ModelViewSet):
    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSeralizer
    permission_classes=[permissions.IsAuthenticated]
    def create(self,request):
        ser = UserProfileSeralizer(data=request.data,context={"user":request.user})
        if ser.is_valid():
            ser.save()
            return Response({"msg":"Created"},status=status.HTTP_201_CREATED)
        return Response({"msg":ser.errors},status=status.HTTP_406_NOT_ACCEPTABLE)
    def add_follow(self,request,pk):
        profile = UserProfile.objects.get(id=pk)
        profile.followed_by.add(request.user)
        return Response({"msg":"Followed"})

class PostView(ModelViewSet):
    serializer_class=PostSerializer
    queryset=Posts.objects.all()
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]  
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

        #user/post/2/add_comment
    @action(methods=['POST'],detail=True)
    def add_comment(self,request,*args,**kwargs):
        postId=kwargs.get('pk')
        post=Posts.objects.get(id=postId)
        user=request.user
        ser=CommentSerializer(data=request.data,context={"user":user,"post":post})
        if ser.is_valid():
            ser.save()
            return Response(data=ser.data)
        return Response(data=ser.errors)
    #user/post/2/get_comment
    @action(methods=['GET'],detail=True)
    def get_comment(self,request,*args,**kwargs):
        postId=kwargs.get('pk')
        post=Posts.objects.get(id=postId)
        comments=Comment.objects.filter(post=post)
        dser=CommentSerializer(comments,many=True)
        return Response(data=dser.data)
        
    #user/post/2/add_like
    @action(methods=["GET"],detail=True)
    def add_like(self,request,*args,**kwargs):
        postId=kwargs.get('pk')
        post=Posts.objects.get(id=postId)
        post.liked_by.add(request.user)
        return Response({"msg":"ok"})
