from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from .forms import ReviewForm
from .models import Review
from django.urls import reverse

# Create your views here.

# class ReviewView(View):
#     def get(self,request):
#         form = ReviewForm()
#         return render(request,"reviews/review.html",{
#         "form":form
#         })

#     def post(self,request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()    
#             return redirect("/thank-you")
#         return render(request,"reviews/review.html",{
#         "form":form
#         })
 
# class ReviewView(FormView):   based on formview
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thank-you"
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

class ReviewView(CreateView):   #based on create view isme aapko form.py ki bhi need ni hoti lekin hum rakhenge
    model = Review
    form_class = ReviewForm
    #idhar labels vager ni daal sakte isley 
    # fields = "__all__"
    template_name = "reviews/review.html"
    success_url = "/thank-you"
    # no need to save data and all ye sb kuch khud krlega



# def review(request):
    
#     if request.method == "POST":
#         # existing_data = Review.objects.all().get(pk=1)
#         # form = ReviewForm(request.POST,instance=existing_data) for updating data in database
#         # form.save()
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             # review = Review(
#             #     user_name=form.cleaned_data['user_name'],
#             #     review_text=form.cleaned_data['review_text'],
#             #     rating=form.cleaned_data['rating']   
#             # )
#             form.save()
#             # print(form.cleaned_data)  # return dictionary of data input/
#             return redirect("/thank-you")
#     else:
#         form = ReviewForm()
#     return render(request,"reviews/review.html",{
#         "form":form
#     })

# def thank_you(request):
#     return render(request,"reviews/thank_you.html")

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This Works"
        return context
    

class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    # def get_context_data(self, **kwargs):  for template view
    #     context = super().get_context_data(**kwargs)
    #     reviews = Review.objects.all()
    #     context["reviews"] = reviews
    #     return context
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self):   #for specific querying logic
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data

# class SingleReviewView(TemplateView):    template view
#     template_name = "reviews/single_review.html"
#     def get_context_data(self, **kwargs):
#         review_id = kwargs['id']
#         context =  super().get_context_data(**kwargs)
#         SingleReview = Review.objects.get(pk=review_id)
#         context['singleReview'] = SingleReview
#         return context

class SingleReviewView(DetailView):  # easy for fetching single data object and rending template
    template_name = "reviews/single_review.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        # favorite_id = request.session["favorite_review"]  use get instead agr koi h hi ni to ye error dega
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context

class AddFavouriteView(View):
    def post(self,request):
        review_id = request.POST["review_id"]
        # fav_review = Review.objects.get(pk=review_id)
        request.session["favorite_review"] = review_id
        reverted_url = reverse("reviewList",args=[review_id])
        return redirect(reverted_url)