from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Contact
from blog.models import Post
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    return render(request, 'home/home.html')
    # return HttpResponse("This is Home")


def about(request):
    messages.success(request, 'This is About')
    return render(request, 'home/about.html')
    # return HttpResponse("This is HomeAbout")


def contact(request):
    # messages.success(request, 'Welcome to contact')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, 'Please Fill The Form Correctly.')
        else:
            contact = Contact(name=name, email=email,
                              phone=phone, content=content)
            contact.save()
            messages.success(
                request, 'Your Message Has Been Sent Successfully.')
    return render(request, 'home/contact.html')
    # return HttpResponse("This is HomeContact")


def search(request):
    query = request.GET['query']
    if len(query) > 50:
        # creating a blank query
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsAContent = Post.objects.filter(content__icontains=query)
        # union of two variables
        allPosts = allPostsTitle.union(allPostsAContent)

    if allPosts.count() == 0:
        messages.warning(
            request, 'No search results found. Please refine your query.')
    params = {'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)


def handleSignup(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Check for error inputs
        if len(username) > 10:
            messages.error(request, 'Username must be under 10 characters')
            return redirect('/')
        if not username.isalnum():
            messages.error(request, 'Username must be alphanumeric')
            return redirect('/')
        if pass1 != pass2:
            messages.error(request, 'Passwords do not match')
            return redirect('/')
        #
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(
            request, 'Your iCoder account has been successfully created')
        return redirect('/')
    else:
        return HttpResponse('404 - Not Found')


def handleLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username=loginusername, password=loginpass)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in !')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials, Please try again !')
            return redirect('home')
    return render(request, 'home/error.html')


def handleLogout(request):
    # if request.method == 'POST':
    logout(request)
    messages.success(request, 'Successfully logged out !')
    return redirect('home')
