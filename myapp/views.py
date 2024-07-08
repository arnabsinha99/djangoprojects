from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Publisher, Book, Member, Order, Review
from django.http import HttpResponse
from .forms import FeedbackForm, SearchForm, OrderForm, ReviewForm


# Create your views here.
def index(request):
    booklist = Book.objects.all().order_by('id')[:10]
    return render(request, 'myapp/index.html', {'booklist': booklist})


def about(request):
    return render(request, 'myapp/about.html')


def detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'myapp/detail.html', {'book': book})


def getFeedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.cleaned_data['feedback']
            choices = []
            if 'B' in feedback:
                choices.append('to borrow books')
            if 'P' in feedback:
                choices.append('to purchase books')
            choice = ', '.join(choices) if choices else 'None'
            return render(request, 'myapp/fb_results.html', {'choice': choice})
        else:
            return HttpResponse('Invalid data')
    else:
        form = FeedbackForm()
        return render(request, 'myapp/feedback.html', {'form': form})


def findbooks(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            category = form.cleaned_data['category']
            max_price = form.cleaned_data['max_price']
            min_price = form.cleaned_data['min_price']
            booklist = Book.objects.filter(price__lte=max_price, price__gte=min_price)
            if category:
                booklist = booklist.filter(category=category)
            return render(request, 'myapp/results.html', {'name': name, 'category': category, 'booklist': booklist})
        else:
            return HttpResponse('Invalid data')
    else:
        form = SearchForm()
        return render(request, 'myapp/findbooks.html', {'form': form})


def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            books = form.cleaned_data['books']
            order = form.save(commit=False)
            member = order.member
            type = order.order_type
            order.save()
            order.books.set(books)  # Ensure the selected books are associated with the order
            if type == 1:
                for b in order.books.all():
                    member.borrowed_books.add(b)
            return render(request, 'myapp/order_response.html', {'books': books, 'order':order})
        else:
            return render(request, 'myapp/placeorder.html', {'form':form})

    else:
        form = OrderForm()
        return render(request, 'myapp/placeorder.html', {'form':form})


def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            if 1 <= rating <= 5:
                new_review = form.save(commit=False)
                book = new_review.book
                book.num_reviews += 1
                book.save()
                new_review.save()
                return redirect('myapp:index')
            else:
                return render(request, 'myapp/review.html', {'form': form, 'error_message': 'You must enter a rating '
                                                                                            'between 1 and 5!'})
        else:
            return render(request, 'myapp/review.html', {'form': form})
    else:
        form = ReviewForm()
        return render(request, 'myapp/review.html', {'form': form})