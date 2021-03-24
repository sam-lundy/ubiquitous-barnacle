import datetime

def greet(name):
    #Get current time
    dt = datetime.datetime.now()

    if dt.hour <= 11:
        greeting = "morning"
    elif dt.hour <= 17:
        greeting = "afternoon"
    else:
        greeting = "evening"
    
    print("Hello " + name + ", good " + greeting + ".")

username = input("What is your name? ")
greet(username)