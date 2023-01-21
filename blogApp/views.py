from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from .form import *
from django.contrib.auth import login,authenticate,logout
# Create your views here.
def get_blog(request,id):
    context = {}
    try:
        blog_obj = Blog.objects.get(id=id)
        context["blog"] = blog_obj
        
    except Exception as e:
        print(e)
        
    return render(request,'blog.html',context)

def home(request):
    
    return render(request,'home.html')

def mylogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username=username)
        if not user_obj.exists():
            messages.warning(request, 'Username does not exist.') # recorded
            return redirect('/login/')
        
        user_obj = authenticate(username=username, password=password)
        if not user_obj:
            messages.warning(request, 'Invalid credentials.') # recorded
            return redirect('/login/')
        login(request, user_obj)
        print('Login successful')
        return redirect('/')
    return render(request,'login.html')
        
def myLogout(request):
    logout(request)
    print('Logged out successful')
    return redirect('/')

        

def myregister(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        
        user_obj = User.objects.filter(username  = username)
        if user_obj.exists():
            messages.warning(request, 'Username is taken.') # recorded
            return redirect('/register/')
        user_obj = User.objects.filter(email  = email)
        if user_obj.exists():
            messages.warning(request, 'Email is taken.') # recorded
            return redirect('/register/')
        if password != cpassword:
            messages.warning(request, 'Password and confirm password do not match.') # recorded
            return redirect('/register/')
        
        user_obj = User(username = username, email = email)
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request, 'Your account has been created.')
        return redirect('/login/')# recorded
    return render(request,'register.html')

def showAllBlogs(request):
    context = {'blogs': Blog.objects.filter(author = request.user)}
    return render(request, 'showAllBlogs.html',context)


def createBlog(request):
    context = {'form': BlogForm, 'categories': Categories.objects.all()}
    if request.method == 'POST':
        form = BlogForm(request.POST)
        title = request.POST.get('title')
        category = request.POST.get('category')
        cover_image = request.FILES['coverImage']
        
        if form.is_valid():
            content = form.cleaned_data['content']
            
            Blog.objects.create(title=title, content=content, author = request.user , category = Categories.objects.get(id = category), cover_image = cover_image)    
            messages.success(request, 'Your blog has been created.')

            return redirect('/createBlog/')
    
    
    return render(request, 'createBlog.html', context)


def updateBlog(request):
    return render(request, 'updateBlog.html')

def deleteBlog(request,id):
    return redirect('showAllBlogs.html')