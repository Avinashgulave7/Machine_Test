from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import *
from django.contrib import messages
from .forms import AddBookForm,SignUpForm,LoginForm
from django.contrib.auth import authenticate,login

# Create your views here.
def Index(request):
    all_book=Book.objects.all()
    return render(request,"testapp/index.html",{'all_book':all_book})

def Add_Book(request):
    if request.method == "POST":
        Add_New_Book_Form=AddBookForm(request.POST)
        if Add_New_Book_Form.is_valid():
            new_book=Add_New_Book_Form.cleaned_data['book_name']
            add_book=Book(book_name=new_book)
            add_book.save()
            messages.info(request, 'Success!')
            return redirect('/home')
    else:
        Add_New_Book_Form=AddBookForm()



    return render(request,"testapp/Add_Book.html",{'form':Add_New_Book_Form})

def Book_Delete(request,id):
    delete_book=Book.objects.get(id=id)
    delete_book.delete()
    messages.info(request, 'Delete Success!')
    return redirect('/home')

def Book_Update(request,id):
    if request.method == 'POST':
        update_book=Book.objects.get(id=id)
        update_form=AddBookForm(request.POST,instance=update_book)
        if update_form.is_valid():
            update_form.save()
            messages.info(request, 'Update Success!')
            return redirect('/home')
    else:
        update_book=Book.objects.get(id=id)
        update_form=AddBookForm(instance=update_book)
    return render(request,"testapp/update_book.html",{'form':update_form})

def Sign_Up(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Signup Success!')
            return redirect('/')
    else:
        form=SignUpForm()
    return render(request,"testapp/signup.html",{'form':form})

def Login(request):
    form=LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')
            print(email)
            user=authenticate(email=email,password=password)
            if user is not None:
                login(request,user)
                return redirect("/home")
            else:
                messages.info(request, 'Invalid Email and password!')
        else:
            messages.info(request, 'Error validation Form!')

    return render(request,"testapp/Login.html",{'form':form})