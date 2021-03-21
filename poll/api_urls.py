from django.urls import path, include
from .views import *

from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter()
router.register('poll', PollViewSet)

poll_list_view = PollViewSet.as_view({
    "get": "list",
    "post": "create"
})

urlpatterns = [

    #path('poll/', poll),
    path('poll/', include(router.urls)),
    #path('poll/', PollApiView.as_view()),
    #path('poll/<int:id>/', poll_details),
    #path('poll/<int:id>/', PollDetailApiView.as_view()),
    #path('generics/poll/', poll_list_view),
    #path('generics/poll/', PollListView.as_view()),
    path('generics/poll/', poll_list_view),
    path('generics/poll/<int:id>/', PollListView.as_view()),
    # path('poll/search/', QuestionSearchViewSet.as_view({'get': 'list'})),
]