from django.shortcuts import render, get_object_or_404
from app_00.models import Book
from app_00.forms import OrderForm

from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    form = OrderForm(request.POST or None, initial={
        'book': book,
    })


    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('{}?sent=True'.format( reverse('book-detail', kwargs={ 'book_id': book.id })))


    return render(request, 'book_detail.html', {
        'book': book,
        'form': form,
        'sent': request.GET.get('sent', False)
    })

