from django.shortcuts import render, redirect
import random

gold_dic = {
    "farm":{
        "range":(10,20),
        "odds": 1
    },
    "cave":{
        "range":(5,10),
        "odds": 1
    },
    "house":{
        "range":(2,5),
        "odds": 1
    },
    "casino":{
        "range":(0,50),
        "odds": .5
    },
}

# Create your views here.

def display(request):
    if not "money" in request.session or "activities" not in request.session:
        request.session["money"] = 0
        request.session["activities"]= []

    
    return render(request,"gold.html")

def process(request):
    if request.method == "POST":
        name = request.POST["location"]
        gold = gold_dic[name]["range"]
        odds = gold_dic[name]["odds"]
        earn = "earn"

    random_float = random.random()
    random_gold = random.randint(gold[0],gold[1])
  
    if  random_float < odds:
        request.session["money"] += random_gold 
        outcome = f"Earned {random_gold} golds from the {name}!"

    else:
        request.session["money"] -= random_gold 
        earn = "lost"
        outcome = f"Entered a {name} and lost {random_gold} golds... Ouch.."

    request.session["activities"].append({"earn":earn,"outcome":outcome})

    return redirect("/")

def reset(request):
    request.session.flush()

    return redirect("/")
