from django.shortcuts import render,redirect
from .models import Book, Member, Transaction,Author

def home(request):
    context = {
        'total_books': Book.objects.count(),
        'total_members': Member.objects.count(),
        'issued_books': Transaction.objects.filter(status='issued').count()
    }
    return render(request, 'home.html', context)
def book_list(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'books.html', {'books': books})
def add_book(request):
    authors = Author.objects.all()

    if request.method == 'POST':
        title = request.POST['title']
        author_id = request.POST['author']
        isbn = request.POST['isbn']
        quantity = request.POST['quantity']

        author = Author.objects.get(id=author_id)

        Book.objects.create(
            title=title,
            author=author,
            isbn=isbn,
            quantity=quantity,
            available_copies=quantity
        )

        return redirect('books')
    return render(request, 'add_book.html', {'authors': authors})
def member_list(request):
    members = Member.objects.all()
    return render(request, 'members.html', {'members': members})


def add_member(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']

        Member.objects.create(
            name=name,
            email=email,
            phone=phone
        )

        return redirect('member_list')

    return render(request, 'add_member.html')
from django.utils.timezone import now

def issue_book(request):
    books = Book.objects.all()
    members = Member.objects.all()

    if request.method == 'POST':
        book_id = request.POST['book']
        member_id = request.POST['member']

        book = Book.objects.get(id=book_id)
        member = Member.objects.get(id=member_id)

        if book.available_copies > 0:
            Transaction.objects.create(
                book=book,
                member=member,
                issue_date=now(),
                status='issued'
            )

            # decrease available copies
            book.available_copies -= 1
            book.save()

            return redirect('books')

    return render(request, 'issue_book.html', {
        'books': books,
        'members': members
    })
from django.utils.timezone import now

def return_book(request):
    transactions = Transaction.objects.filter(status='issued')
    return render(request, 'return_book.html', {'transactions': transactions})


def return_action(request, id):
    transaction = Transaction.objects.get(id=id)

    if transaction.status == 'issued':
        transaction.status = 'returned'
        transaction.return_date = now()
        transaction.save()

        # increase available copies
        book = transaction.book
        book.available_copies += 1
        book.save()

    return redirect('return_book')