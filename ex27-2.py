from sys import exit
from random import randint

def death():
    quips = ["You died. You kinda suck at this.",
             "Nice job, you died ...jackass."
             "such a luser."
             "I have a small puppy that's better at this."]
             
    print quips[randint(0,len(quips)-1)]
    exit(1)
    
    
def central_corridor():
    print "The Gothons of.."
    
    action = raw_input("> ")

    if action == "shoot!":
        print "Quick..."
        print "you are dead..."
        return 'death'
        
    elif action == "dodge!":
        print "...dead..."
        return 'death'
        
    elif action == "tell a joke":
        print "...jump through the Weapon Armory door"
        return 'laser_weapon_armory'
        
    else:
        print "DOES NOT COMPUTE!"
        return 'central_corridor'
        
def laser_weapon_armory():
    print "You...bomb...3 digits."
    code = "%d%d%d" % ((randint(1,9), randint(1,9), randint(1,9))
    guess = raw_input("[keypad]> ")
    guesses = 0
    
    while guess != code and guesses < 10:
        print "BZZZZEDDD!"
        guesses += 1
        guess = raw_input("[keypad]> ")

    if guess == code:
        print "..bridge.."
        return 'the_bridge'
    else:
        print "...die."
        return 'death'
        
        
def the_bridge():
    print "..."
    
    action = raw_input("> ")
    
    if action == "throw the bomb":
        print "...goes off."
        return 'death'
        
    elif action == "slowly place the bomb":
        print "You .."
        return 'escape_pod'
    else:
        print "DOES NOT COMPUTE!"
        return "the_bridge"


def escape_pod():
    print "...do you take?"
    
    
    good_pod = randint(1,5)
    guess = raw_input("pod #> ")
    
    if int(guess) != good_pod:
        print "..."
        return 'death'
    else:
        print "...You won!"
        exit(0)
        
        
ROOMS = {
    'death': death,
    'central_corridor': central_corridor,
    'laser_weapon_armory': laser_weapon_armory,
    'the_bridge': the_bridge,
    'escape_pod': escape_pod}
    
    
def runner(map, start):
    next = start

    while True:
        room = map[next]
        print "\n--------"
        next = room()
        
runner(ROOMS, 'central_corridor')