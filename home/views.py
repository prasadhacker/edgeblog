from django.shortcuts import render, HttpResponse,redirect
import random
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from blogger.models import Post
from django.contrib.auth.backends import BaseBackend




# Create your views here.
def home(request):
    education={"quote1":"Education is the passport to the future, for tomorrow belongs to those who prepare for it today",
    "quote2":"Your attitude, not your aptitude, will determine your altitude.” “If you think education is expensive, try ignorance.",
    "quote3":"The only person who is educated is the one who has learned how to learn …and change.",
    "quote4":"Anyone who has never made a mistake has never tried anything new.",
    "quote5":"Keep away from people who try to belittle your ambitions. Small people always do that, but the really great make you feel that you, too, can become great.",
    "quote6":"The only person who is educated is the one who has learned how to learn …and change.",
    "quote7":"The secret of getting ahead is getting started. The secret of getting started is breaking your complex overwhelming tasks into small manageable tasks, and then starting on the first one.",
    "quote8":"Education is a progressive discovery of our own ignorance.",
    "quote9":"Be miserable. Or motivate yourself. Whatever has to be done, it's always your choice.”",
    "quote10":"The difference between school and life? In school, you're taught a lesson and then given a test. In life, you're given a test that teaches you a lesson.",
    "quote11":"We learn more by looking for the answer to a question and not finding it than we do from learning the answer itself."
    }

    books={"quote1":"′Classic′ – a book which people praise and don’t read.",
    "quote2":"Sleep is good, he said, and books are better.",
    "quote3":"Books are the quietest and most constant of friends; they are the most accessible and wisest of counselors, and the most patient of teachers.",
    "quote4":"Many people, myself among them, feel better at the mere sight of a book.",
    "quote5":"The library is inhabited by spirits that come out of the pages at night.",
    "quote6":"If you don’t like to read, you haven’t found the right book.",
    "quote7":"One glance at a book and you hear the voice of another person, perhaps someone dead for 1,000 years. To read is to voyage through time.",
    "quote8":"When I have a little money, I buy books; and if I have any left, I buy food and clothes.",
    "quote9":"Fill your house with stacks of books, in all the crannies and all the nooks.",
    "quote10":"That’s the thing about books. They let you travel without moving your feet.",
    "quote11":"A book is a version of the world. If you do not like it, ignore it; or offer your own version in return."
    }

    fashion={"quote1":"Fashion is part of the daily air and it changes all the time, with all the events. You can even see the approaching of a revolution in clothes. You can see and feel everything in clothes.",
    "quote2":"Don't be into trends. Don't make fashion own you, but you decide what you are, what you want to express by the way you dress and the way to live.",
    "quote3":"One is never over-dressed or under-dressed with a Little Black Dress.",
    "quote4":"What you wear is how you present yourself to the world, especially today, when human contacts are so quick. Fashion is instant language.",
    "quote5":"I firmly believe that with the right footwear one can rule the world.",
    "quote6":"I like my money right where I can see it…hanging in my closet.",
    "quote7":"I think there is beauty in everything. What 'normal' people perceive as ugly, I can usually see something of beauty in it.",
    "quote8":"Style is something each of us already has, all we need to do is find it.",
    "quote9":"Fashion is the armor to survive the reality of everyday life.",
    "quote10":"I don't design clothes. I design dreams.",
    "quote11":"Anyone can get dressed up and glamorous, but it is how people dress in their days off that are the most intriguing."
    }

    fitness={"quote1":"The last three or four reps is what makes the muscle grow. This area of pain divides a champion from someone who is not a champion.",
    "quote2":"Success usually comes to those who are too busy to be looking for it.",
    "quote3":"All progress takes place outside the comfort zone.",
    "quote4":"‘If you think lifting is dangerous, try being weak. Being weak is dangerous.’",
    "quote5":"The only place where success comes before work is in the dictionary.",
    "quote6":"The clock is ticking. Are you becoming the person you want to be?",
    "quote7":"Whether you think you can, or you think you can’t, you’re right.",
    "quote8":"The successful warrior is the average man, with laser-like focus.",
    "quote9":"You must expect great things of yourself before you can do them.",
    "quote10":"Action is the foundational key to all success.",
    "quote11":"Things may come to those who wait, but only the things left by those who hustle."
    }

    food={"quote1":"",
    "quote2":"",
    "quote3":"",
    "quote4":"",
    "quote5":"",
    "quote6":"",
    "quote7":"",
    "quote8":"",
    "quote9":"",
    "quote10":"",
    "quote11":""
    }

    travel={"quote1":"",
    "quote2":"",
    "quote3":"",
    "quote4":"",
    "quote5":"",
    "quote6":"",
    "quote7":"",
    "quote8":"",
    "quote9":"",
    "quote10":"",
    "quote11":""
    }

    music={"quote1":"",
    "quote2":"",
    "quote3":"",
    "quote4":"",
    "quote5":"",
    "quote6":"",
    "quote7":"",
    "quote8":"",
    "quote9":"",
    "quote10":"",
    "quote11":""
    }

    lifestyle={"quote1":"",
    "quote2":"",
    "quote3":"",
    "quote4":"",
    "quote5":"",
    "quote6":"",
    "quote7":"",
    "quote8":"",
    "quote9":"",
    "quote10":"",
    "quote11":""
    }

    sport={"quote1":"",
    "quote2":"",
    "quote3":"",
    "quote4":"",
    "quote5":"",
    "quote6":"",
    "quote7":"",
    "quote8":"",
    "quote9":"",
    "quote10":"",
    "quote11":""
    }

    beauty={"quote1":"",
    "quote2":"",
    "quote3":"",
    "quote4":"",
    "quote5":"",
    "quote6":"",
    "quote7":"",
    "quote8":"",
    "quote9":"",
    "quote10":"",
    "quote11":""
    }

    technology={"quote1":"",
    "quote2":"",
    "quote3":"",
    "quote4":"",
    "quote5":"",
    "quote6":"",
    "quote7":"",
    "quote8":"",
    "quote9":"",
    "quote10":"",
    "quote11":""
    }

    edu=random.choice(list(education.values()))
    book=random.choice(list(books.values()))
    Fashion=random.choice(list(fashion.values()))
    fit=random.choice(list(fitness.values()))
    Food=random.choice(list(education.values()))
    Travel=random.choice(list(education.values()))
    Music=random.choice(list(education.values()))
    Lifestyle=random.choice(list(education.values()))
    Sports=random.choice(list(education.values()))
    Beauty=random.choice(list(education.values()))
    Technology=random.choice(list(education.values()))



    context={}
    context['educational']=edu
    context['book']=book
    context['Fashion']=Fashion
    context['fit']=fit
    context['Food']=Food
    context['Travel']=Travel
    context['Music']=Music
    context['Lifestyle']=Lifestyle
    context['Sports']=Sports
    context['Beauty']=Beauty
    context['Technology']=Technology
    
    allPost=Post.objects.all()
    contexts={'allPost':allPost}
    
    return render(request,'home/home.html',contexts)


def about(request):
    return render(request, 'home/about.html')

def services(request):
    return render(request, 'home/services.html')

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(message)<5:
            messages.error(request,"Please Fill The Form Correctly.")
        else:
            contact = Contact(name=name,email=email,phone=phone,message=message)
            contact.save()
            messages.success(request,"Your Message Has been successfully sent.")
    return render(request, 'home/contact.html')

def search(request):
    search=request.GET['search']

    if len(search)>78:
        allPost=Post.objects.none()
    else:
        allPosttitle=Post.objects.filter(title__icontains=search)
        allPostcontent=Post.objects.filter(content__icontains=search)
        allPost=allPosttitle.union(allPostcontent)
    if allPost.count()==0:
        messages.warnings(request,"No search results found.")
    
    params={'allPost':allPost,'search':search}
    return render(request, 'home/search.html',params)

def handleSignup(request):
    if request.method == 'POST':
        # Get post parameter
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        # Checks for errorneous input
        #Username must be under 10 charecter
        if len(username)>10:
            messages.error(request,"Username must be under 10 charecter")
            return redirect("home")
        #Username should only contains letters and number
        if not username.isalnum :
            messages.error(request,"Username should only contains letters and number")
            return redirect("home")
        #Password does not match
        if pass1 != pass2:
            messages.error(request,"Password does not match")
            return redirect("home")
        #Create user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your iBlogger account has been successfuly created")
        return redirect("home")

    else:
        return HttpResponse("404 Not Found")
def handleLogin(request):
    if request.method == 'POST':
        # Get post parameter
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user = authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"successfully logged In")
            return redirect("home")
        else:
            messages.error(request,"Invalid Credentials,Please Try again")
            return redirect("home")

    return HttpResponse("404-Not Found")

def handleLogout(request):
    logout(request)
    messages.success(request,"successfully logged Out")
    return redirect("home")  


