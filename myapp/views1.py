from django.shortcuts import render
# Import necessary classes
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Publisher, Book, Member, Order


# Create your views here.
def index(request):
    response = HttpResponse()

    # Retrieve the list of books ordered by primary key
    booklist = Book.objects.all().order_by('id')[:10]
    heading1 = '<p>' + 'List of available books: ' + '</p>'
    response.write(heading1)
    for book in booklist:
        para = '<p>' + str(book.id) + ': ' + str(book) + '</p>'
        response.write(para)

    # Retrieve the list of publishers ordered by city name in descending order
    publisherlist = Publisher.objects.all().order_by('-city')
    heading2 = '<p>' + 'List of publishers: ' + '</p>'
    response.write(heading2)
    for publisher in publisherlist:
        para = '<p>' + publisher.name + ': ' + publisher.city + '</p>'
        response.write(para)

    return response


def about(request):
    return HttpResponse("This is an eBook APP.")


def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    response = HttpResponse()
    response.write('<p>Title: ' + book.title.upper() + '</p>')
    response.write('<p>Price: $' + str(book.price) + '</p>')
    response.write('<p>Publisher: ' + book.publisher.name + '</p>')
    return response
