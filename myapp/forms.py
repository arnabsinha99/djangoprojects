from django import forms

from myapp.models import Book, Order, Review


class FeedbackForm(forms.Form):
    FEEDBACK_CHOICES = [
        ('B', 'Borrow'),
        ('P', 'Purchase'),
    ]
    feedback = forms.MultipleChoiceField(
        choices=FEEDBACK_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label="Select your feedback"
    )


class SearchForm(forms.Form):
    name = forms.CharField(required=False, label='Your Name')
    category = forms.MultipleChoiceField(
        choices=[(cat, cat) for cat in Book.objects.values_list('category', flat=True).distinct()],
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label='Select a category'
    )
    max_price = forms.IntegerField(
        required=True,
        label='Maximum Price',
        min_value=0,
        error_messages={'required':'Abbey isko bhar!'}

    )
    min_price = forms.IntegerField(
        required=True,
        label='Minimum Price',
        min_value=0
    )
    email_id = forms.CharField(max_length=100, required=False, widget=forms.EmailInput)
    is_male = forms.BooleanField(required=True, label='Male')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['books', 'member', 'order_type']
        widgets = {'books': forms.CheckboxSelectMultiple(), 'order_type':forms.RadioSelect}
        labels = {'member': u'Member name', }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['reviewer', 'rating', 'book']
        widgets = {
            'book': forms.Select
        }
        labels = {
            'reviewer': 'Please enter a valid email',
            'rating': 'Rating: An integer between 1 (worst) and 5 (best)'
        }