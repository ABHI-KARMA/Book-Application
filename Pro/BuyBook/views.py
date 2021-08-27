from django.http.request import HttpRequest
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm


# ========================SELLER SECTION===========================
# SHOW BOOKS
def showBooks(request):
    datas = AddBookModel.objects.all()
    return render(request,'showbooks.html',{'datas':datas})

# ADD BOOKS
def addBook(request):
    if request.method == 'POST':
        book_name = request.POST['bookname']
        author_name = request.POST['authorname']
        book_price = request.POST['bookprice']
        book = AddBookModel.objects.create(bname=book_name,aname=author_name,price=book_price)
        return redirect('SHOWBOOKS')
    else:
        return render(request,'addbook.html')
    return render(request,'addbook.html')

# UPDATE BOOK
def updateBooks(request,pk):
    try:
        data = AddBookModel.objects.get(pk=pk)
    except AddBookModel.DoesNotExist:
        return HttpResponse("Book Not Found!!")
    if request.method == 'POST':
        if data:
            data.delete()
            book_name = request.POST['bookname']
            author_name = request.POST['bookauthor']
            book_price = request.POST['price']
            book = AddBookModel.objects.create(bname=book_name,aname=author_name,price=book_price)
            return redirect('SHOWBOOKS')
    return render(request,'updatebook.html',{'data':data})

# DELETE BOOK
def deleteBook(request,pk):
    try:
        data = AddBookModel.objects.get(pk=pk)
    except AddBookModel.DoesNotExist:
        return HttpResponse("Book Not Found!!")
    data.delete()
    return redirect('SHOWBOOKS')

# SOLD BOOKS 
def soldbook(request):
    books = Purchased.objects.all()
    return render(request,'soldbook.html',{'books':books})

# =================CUSTOMER SECTION=====================
# SIGN UP 
def signup(request):
    if request.user.is_authenticated:
        return redirect('CUSTOMERBOOKVIEW')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password)
            login(request, user)
            return redirect('CUSTOMERBOOKVIEW')
        else:
            return render(request,'signup.html',{'form':form})
    else:
        form = UserCreationForm()
        return render(request,'signup.html',{'form':form})

# SIGN IN
def signin(request):
    if request.user.is_authenticated:
        return redirect('CUSTOMERBOOKVIEW')
     
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
 
        if user is not None:
            login(request,user)
            return redirect('CUSTOMERBOOKVIEW')
        else:
            form = AuthenticationForm()
            return render(request,'signin.html',{'form':form})
    else:
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form':form})

# SIGN UP
def signout(request):
    logout(request)
    return redirect('SIGNIN')

# CUSTOMER BOOK VIEW 
def customerBookView(request):
    if request.user.is_authenticated:
        datas = AddBookModel.objects.all()
        if request.method == 'POST':
            form = SearchForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['bookname']
                try:
                    book = AddBookModel.objects.get(bname=title)
                except AddBookModel.DoesNotExist:
                    raise Http404("Data Does Not Exist")
                pk = book.pk
                return redirect('search',pk=pk)
        else:
            form = SearchForm()
        return render(request,'customerbook.html',{'datas':datas,'form':form})
    else:
        return redirect('SIGNIN')

# SEARCH BOOK
def searchBook(request,pk):
    datas = AddBookModel.objects.get(pk=pk)
    return render(request,'searchbook.html',{'datas':datas})

# PURCHASE BOOK VIEW
def purchaseBook(request,pk):
    book = AddBookModel.objects.get(pk=pk)
    purchase_book = Purchased.objects.create(bookname=book.bname,authorname=book.aname,price=book.price)
    return redirect('SHOWPURCHASED')

# SEE ALL PURCHASED BOOKS
def purchasedbook(request):
    books = Purchased.objects.all()
    return render(request,'purchasedbook.html',{'books':books})



