from django import forms
from .models import Review
# class ReviewForm(forms.Form):
#     #charfield m required default true hota h
#     user_name = forms.CharField(label="Your Name",max_length=10,error_messages={
#         "required": "Your name must not be empty",
#         "max_length": "Please enter a shortner name!",
#     })
#     review_text = forms.CharField(label="Your Feedback",widget=forms.Textarea,max_length=200)
#     rating = forms.IntegerField(label="Your Rating",min_value=1,max_value=5)

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = '__all__' #saari field chaiye
        # exclude = [] jo jo ni chaiye
        labels = {
            "user_name": "Your name",
            "review_text": "Your Feedback",
            "rating": "Your Rating",
        }
        error_messages = {
            "user_name" : {
                "requires":"Your name must not be empty",
                "max_length": "Please enter a shortner name!",
            }
        }

