from django.urls import path,include
#from . import views  #For Function Based Views
from .views import *  # For Class Based Views and generic Views, mixins,viewsets
from rest_framework.routers import DefaultRouter



'''
#function Base Views

urlpatterns =[
    path('tasks/',views.task_list,name='task_list'),
    path('tasks/<int:pk>/',views.task_detail,name='task_detail')
]


#Class Based Views

urlpatterns=[
    path('tasks/',TaskListAPIView.as_view(),name='task_list'),
    path('tasks/<int:pk>/',TaskDetailAPIView.as_view(),name='task_detail')
]


'''
#Generic Views

urlpatterns =[
    path('tasks/',TaskListCreateView.as_view(),name='task_list'),
    path('tasks/<int:pk>/',TaskRetrieveUpdateDestroyView.as_view(),name='task_detail')
]

'''
#Mixins

urlpatterns =[
    path('tasks/',TaskListCreateView.as_view(),name='task_list'),
    path('tasks/<int:pk>/',TaskRetrieveUpdateDestroyView.as_view(),name='task_detail')
]
'''
'''
#ViewSets
 
router = DefaultRouter()
router.register(r'tasks',TaskViewSet)

urlpatterns=[
    path('',include(router.urls))
]
''' 