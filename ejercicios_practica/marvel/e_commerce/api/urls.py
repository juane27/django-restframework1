from django.urls import path, include
from e_commerce.api.views import *



urlpatterns = [
    path('hello_world/', hello_world),
    path('comic-list/', comic_list_api_view),
    path('comic-list-price/', comic_list_filtered_api_view),
    path('comic-list-stock/', comic_list_filtered_api_view_stock),
    
     path('comic/get/<int:marvel_id>',comic_list_api_view_by_id),
     path('comic-create',comic_create_api_view),
     



    
    
    

]