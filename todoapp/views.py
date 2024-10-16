from rest_framework import status
from rest_framework.response import Response
from.models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import api_view # For Function Based Views
from rest_framework.views import APIView # For Class Based Views
from rest_framework import generics # For Generic views
from rest_framework import generics,mixins # For Mixins
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
'''
#Function Based Views

@api_view(['GET','POST'])
def task_list(request):
    if request.method == 'GET':
        tasks=Task.objects.all()
        serializer=TaskSerializer(tasks,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer=TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
@api_view(['GET','PUT','DELETE'])
def task_detail(request,pk):
    try:
        task=Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if  request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer=TaskSerializer(task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method =='DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

#Class Based Views

class TaskListAPIView(APIView):
    permission_classes = [AllowAny]
    @swagger_auto_schema(
        responses={200: TaskSerializer(many=True)}
    )

    def get(self,request):
        tasks=Task.objects.all()
        serializer=TaskSerializer(tasks,many=True)
        return Response(serializer.data)
    @swagger_auto_schema(
        request_body=TaskSerializer,
        responses={201: TaskSerializer, 400: "Bad Request"}
    )

    def post(self,request):
        serializer= TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class TaskDetailAPIView(APIView):
    @swagger_auto_schema(
        responses={200: TaskSerializer(), 404: 'Not Found'}
    )
    def get_task(self,pk):
        return Task.objects.get(pk=pk)
        
            
    
    def get(self,request,pk):
        task= self.get_task(pk)
        serializer= TaskSerializer(task)
        return Response(serializer.data)
    @swagger_auto_schema(
        request_body=TaskSerializer,
        responses={200: TaskSerializer, 400: "Bad Request", 404: "Not Found"}
    )
    def put(self,request,pk):
        task=self.get_task(pk)
        serializer= TaskSerializer(task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    @swagger_auto_schema(
        responses={204: 'No Content', 404: 'Not Found'}
    )
    def delete(self,request,pk):
        task=self.get_task(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


'''
#Generic Views

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class=TaskSerializer

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer




#Mixins

class TaskListCreateView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset= Task.objects.all()
    serializer_class=TaskSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
class TaskRetrieveUpdateDestroyView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset= Task.objects.all()
    serializer_class=TaskSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.delete(request,*args,**kwargs)
    


#ViewSets

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

'''