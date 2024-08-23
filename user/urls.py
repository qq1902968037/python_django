from django.urls import path
from user import views

urlpatterns = [
    path('save/', views.SaveUser.as_view()),
    path('query/', views.QueryUser.as_view()),
    path('getUser/<id>', views.GetUser.as_view()),
    path('update/', views.UpdateUser.as_view()),
    path('delete/<id>', views.DeleteUser.as_view()),
    path('saveOrder/', views.SaveOrder.as_view()),
    path('updateOrder/<id>', views.UpdateOrder.as_view()),
    path('listOrder/', views.ListOrder.as_view()),
    path('queryOrder/<pk>', views.QueryOrder.as_view()),
    path('delOrder/<pk>', views.DelOrder.as_view())
]


