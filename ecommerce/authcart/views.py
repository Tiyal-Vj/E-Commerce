from django.shortcuts import render,redirect

# Create your views here.
def signup(request):
    print("I'm running the signup function")
    if (request.method=="POST"):
        print("it is a post request")
        
    else:
        print("it is a get request")
    return render(request,"authentication/signup.html")

def handlelogin(request):
    return render(request,"authentication/login.html")

def handlelogout(request):
    return redirect('/auth/login')