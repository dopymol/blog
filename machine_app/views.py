from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'register.html')


def home(request):
    AllBlogs=Blogs.objects.all()
    context={
        'blogs':AllBlogs,
    }
    print(AllBlogs)
    return render(request,'home.html',context)

def addBlog(request):
    form=blogForm()
    if request.method=='POST':
        form=blogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={
        'form':form,
    }
    return render(request,'addblog.html',context)

def likeBlog(request,pk):
    blog=Blogs.objects.get(id=pk)
    blog.likes+=1
    blog.save()
    return redirect('home')

def update(request,id):
    blog=Blogs.objects.get(id=id)
    form = blogForm(request.POST or None,request.FILES,instance=blog)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'blog':blog})

def delete(request,id):
    if request.method =='POST':
        blog =Blogs.objects.get(id=id)
        blog.delete()
        return redirect('home')
    return render(request,'delete.html')

# def delete(request, id, slug):
#     Entry.objects.filter(id=id, slug=slug).delete()
#     return redirect('home')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            return render(request, 'login.html', {'error': 'Username or password is incorrect!'})
    else:
        return render(request, 'login.html')




def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        # username = request.POST['username']
        # email = request.POST['email']
        # password = request.POST['password']
        # password2 = request.POST['password2']

        if password == password1:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already exist')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exist')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                print("User created")
                return redirect('login')  # check
        else:
            messages.info(request, 'Incorrect password')
            return redirect('register')
    else:
        return render(request, 'register.html')


# logout
def logout(request):
    auth.logout(request)
    return redirect('/')