from django.urls import path
from . import views

urlpatterns = [
    path('',views.ReviewView.as_view()),
    path('thank-you',views.ThankYouView.as_view()),
    path('reviews',views.ReviewListView.as_view(),name="reviews"),
    path('reviews/<int:pk>',views.SingleReviewView.as_view(),name="reviewList"),   #using pk intead of id for detail view
    path('reviews/favourite',views.AddFavouriteView.as_view(),name="fav_review"),
]
    