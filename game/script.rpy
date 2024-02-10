# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define h = Character("Hero") # No pronouns.

# Stats.
default luck = renpy.random.randint(1, 13) # Luck stat, used for random.
default plays = 0 # The number of plays you've already done on this save.
default deaths = 0 # How many times you've died on this save.
default strays = 0 # How many times you've strayed from the quest on this save. This includes both willingly and unwillingly.

# These stats below might not end up being used?
# The idea is that decisions made during the game will affect the values of these, which may change how certain scenes play out.

default loyalty = 10 
default hope = 10 
default edgy = 0 
default violence = 5 
default yuri = 5 
python: # Collapsible stats explanation.
  # Loyalty, how much the hero cares about the quest. 10 = default. 0 = ready to pack up and do something else at a moment's notice. 20 = it's the only thing that matters anymore, obsessed.
  # Hope and optimism. 10 = default, cautiously optimistic. 20 = probably on drugs, nothing can go wrong. 0 = depressed, fallen into despair.
  # Edginess. How much of a little edgy bastard the hero is. 0 = has never heard of edge. 10 = got some dark humor. 20 = shadow the hedgehog from tails gets trolled
  # Willingness to commit violence. 5 = will resort to violence if necessary. 10 = will be violent if that's a viable option. 20 = will be violent for fun. 0 = will not be violent even in self defense / protection, would rather die than fight.
  # Likelihood to 'lez out' as you might say. 5 = neutral, can be swayed. 10 = hopeless romantic. 20 = knows what sex is. 0 = touch averse or homophobic.

  # Potential for interesting combinations:
  # Loyalty 20 + Hope 0 = broken but not giving up. saddest bitch ever, no options.
  # Loyalty 0 + Hope 20 = ready to do something else and ready to love it
  # Edgy 20 + Hope >10 = grimmest little bitch you've ever met but danged if they aren't gonna do this
  # Violence 20 + Edgy 0 = pyro tf2
  # Hope 0 + Violence 0 = basically wants to be killed at this point
  # Yuri 20 + Edgy 20 = evil lesbian
  # Yuri 20 + Violence 20 = violence is sex
  # Yuri 20 + Hope 0 =
  asdf = 1

# Silly stats:
default notlookedatmap = True # Whether or not the hero has looked at the map this run.

# More stats: 
# These ones are used to keep track of past iterations of the Hero.
default bodies = {
    "path to alsterside": 0,
    "dysentery": 0,
    "volcano": 0, # die in a volcano watch your skin heat up so much it begins to glow
    "swamp": 0,
    "wings": 0, # get wings sewn to arms fucked up style. horrors of being a blank slate protagonist moment
  }
default alivebodies = {
    "boat traveler": 0,
    "stuck in swamp": 0,
    "hoc": 0
  }
# more bad ending ideas: stabbed to death by a past hero turned evil, dies of dysentery, stuck in quicksand, climbed a tree and can't get down, falls in a volcano,

define slow_dissolve = Dissolve(1.0)
define slow_fade = Fade(1.0, 0.5, 1.0)
define slower_fade = Fade(3.0, 0.5, 1.0)

# bgs: bg wakeuproom, bg bedroom, bg readytogo, bg path1, bg path plains, endingscreen
# sprites: scientist m, scientist f, als woman concerned,
# visuals: illustration cycle, shittymap, shittymap upsidedown, shittymap ruined
# hero sprites: hero look hand,
# cgs: plains path fallen, plains path body
# to rough: illustration cycle, plains path body, endingscreen

#Produced to Prophecy Specifications ?
#Hero's Journey / Heroes' Journey ?
# notes: LITERAL known and unknown worlds? or make reality not conform to the hero journey prophecy? or make reality less realistic to the real world but remain realistic to the in-universe world while being something that the hero journey can be roughly imposed upon

# The game starts here.

label start:
  
  $ loyalty = 10
  $ hope = 10
  $ edgy = 0
  $ violence = 5
  $ yuri = 5
  # Show a background. This uses a placeholder by default, but you can
  # add a file (named either "bg wakeuproom.png" or "bg wakeuproom.jpg") to the
  # images directory to show it.

  scene bg wakeuproom

  # These display lines of dialogue.

  "You wake up, eyes fuzzy, surrounded by liquid."
  
  # This shows a character sprite. A placeholder is used, but you can
  # replace it by adding a file named "scientist m.png" to the images
  # directory.

  show scientist m with dissolve
  
  "A man in a white lab coat pulls you out of the tank and into the chilly air of a small room. The half moon shines brightly through an open window."
  # first quarter moon rises at noon sets at midnight. highest at sunset.
  # last quarter moon rises at midnight sets at noon. highest at sunrise.
  
  "Before you can do or say anything, he wraps you in a robe and pushes you through the open door."
  
  hide scientist m with dissolve
  scene bg bedroom with dissolve
  
  "The room you find yourself in is white and sterile, with a plain bed against one wall, a large screen on the wall opposite, and a door in each of the remaining walls. The tile floor is cold against your bare feet."
  
  "The door you entered through locks behind you, and the other door opens."
  
  show scientist f with dissolve
  
  $ sandwich = renpy.random.choice([" cheese", " ham", " peanut butter", "n egg", " bacon", " chicken", " salmon", " peanut butter and jelly", " tuna"])
  "A woman in a white lab coat enters, and hands you a[sandwich] sandwich."
  
  if plays % 2 == 0:
    "Scientist" "Good morning, Hero." 
  else:
    "Scientist" "Good evening, Hero."

  "She explains to you that she will be providing your meals, and setting instructional videos on the screen. It is vitally important that you watch and understand. You will sleep when the sun is down, wake when it rises, and learn while it is up."
  
  hide scientist f with dissolve
  
  "The next week passes just as she says. You learn all manner of things, from wilderness survival to social skills to shoe tying."
  
label learning:
  
  "You also learn about the prophecy."
  
  "The prophecy foretells a hero who will find the mystical elixir and save the world from its decay."
  
  "A hero born of no woman as the half moon shines, a hero whose palm is marked by the fates."
  
  show hero look hand with dissolve # hero looking at hand
  
  "You are this hero, you learn."
  
  hide hero look hand with dissolve
  
  "The hero will set out on a journey as foretold by the prophecy."

  show illustration cycle with dissolve

  "First, the hero will be called from the ordinary world to adventure, and may initially refuse this call, but will eventually heed it."
  
  "Second, the hero will receive aid in a form unnatural or supernatural."
  
  "Third, the hero will cross a threshold into the unknown."
  
  "Fourth, the hero will make new allies and enemies, and face trials of ordeal."
  
  "Fifth, the hero will, having overcome all ordeals, meet with a 'goddess' and be granted both love and boons that will be helpful in the future."
  
  "Sixth, the hero will be tempted by pleasures physical or material to stray from the quest, but will surpass these temptations and carry on."
  
  "Seventh, the hero will reach the deepest point of the abyss, and confront the most powerful being with aid from the gifts provided."
  
  "Eighth, the hero will achieve a greater understanding and become more than human."
  
  "Ninth, the hero will reach the ultimate boon, the elixir that will restore society and the world."
  
  "Tenth, the hero will undergo the return journey, being faced by opposition that seeks to prevent the return and restoration, and may receive rescue from without."
  
  "Eleventh, the hero will be made pure again in order to cross back over the threshold and reenter the known world."
  
  "Twelfth, the hero will return with the elixir to restore the world."
  

  "Should the hero stray from the quest, all is not lost: as long as the hero still breathes, the quest may yet continue."
  
  "Should the hero draw final breath before the elixir is returned, all will be lost, and the world will never be restored."
  
  hide illustration cycle with dissolve
  
  "You aren't sure if you'll remember all of that, but the screen assures you that you'll be given a copy to keep with you."
  
  "Even so, it feels like a tall order for just one person to do. Saving the world? And if you fail all is lost? You're not sure you're up to the task."
  
  if plays >= 6:
    "The screen then informs you that you are not the first hero to attempt the quest."
    
    "And that, in fact, you aren't the first {i}you{/i} to attempt it."
    
    "You are, in fact, a clone."
    
    "There have been many heroes sent out before you, and all of them failed."
    
    "That takes off some of the pressure..."
    
    "But if the others failed, who's to say you won't?"
    
    "The screen then provides you with more information on the fates that befell the previous heroes, and how to avoid them."
    
    if plays > 15:
      if deaths > strays:
        "The odds really don't look good out there for you. It seems like death must be lurking around every corner on this quest."
        $ hope -= 3
        
      elif deaths < 5:
        "The odds of you completing this quest don't really look good. It seems like no matter where you turn there'll be something new to distract you."    
        $ hope -= 1
        $ loyalty -= 2
      
      else:
        "The odds of you completing this quest really don't look good. It seems like no matter where you turn there'll be something new to stop you."    
        $ hope -= 2
        $ loyalty -= 1
        
      "But it looks like you'll have to do this."
    
    elif deaths > strays:
      "It doesn't seem like this quest is going to be very... safe."
      $ hope -= 2
      "But it looks like you'll have to do it."
    
    else:
      "It doesn't seem like this quest is going to be easy to stick to."
      $ hope -= 1
      $ loyalty -= 1
      "But it looks like you'll have to do it."
    
  else:
    "But it seems like you're the one who has to do it."

label begin:
  scene bg readytogo with slow_fade
  
  "You've been here for eight days, and now it's time for you to embark on your quest."
  
  if bodies["dysentery"] > 0:
    "You've had a bag packed for you, containing rations, tools, a few changes of clothes, a copy of the prophecy, a map, and a full canteen of water with a built-in filter."
  else:
    "You've had a bag packed for you, containing rations, tools, a few changes of clothes, a copy of the prophecy, a map, and a full canteen of water."
  
  "And of course, you have your trusty sword at your side."
  # it's a perfect fit... but hero hasn't been trained to use it lol
  
  "You wave goodbye to the people who taught you everything you know, and then head out toward the unknown."

  menu:
    "Choose your luck stat?"
    "Choose.":
      $ luck = renpy.input("Luck (between 1 and 13)", allow="1234567890", length=2)
      $ luck = ((int(luck) - 1) % 13) + 1
      "Your luck is [luck]."
      $ renpy.random.seed(luck)
    "Random.":
      $ luck = renpy.random.randint(1, 13) # 7 is Best?
      "Your luck is [luck]."
      $ renpy.random.seed(luck)
  
  scene bg path1 with dissolve
  
  $ xth = "first"
  $ lookedatmap = False
  
  "You walk down the trail until you reach a crossroads. The path splits into three here, none looking any more remarkable than the others."

label crossroads:
  menu:
    "Which path do you take?"
    
    "The left path.":
      jump path2als
    "The center path.":
      jump path2center
    "The right path.":
      jump path2right
    "Look at your map [xth].":
      jump crossroadsmap
    "Pick a random path. (Luck)":
      "You close your eyes, spin in a circle, and find yourself facing..."
      $ choice = renpy.random.randint(1, 4)
      if choice == 1:
        "...the left path."
        jump path2als
      if choice == 2:
        "...the center path."
        jump path2center
      if choice == 3:
        "...the right path."
        jump path2right
      if choice == 4:
        "...back the way you came."
        "You stand at a crossroads. The path splits into three here, none looking any more remarkable than the others."
        jump crossroads

label crossroadsmap:
  "You pull your map out of your bag. It's strangely high-contrast and hard to read... a photocopy of a photocopy of a photocopy, maybe."
  
  $ xth = "again"
  $ notlookedatmap = False
  
  show shittymap with dissolve
  
  "But you manage to make out enough details."
  
  "The bottom half - no, more than half - of the map is labeled \"THE UNKNOWN WORLD\" in big letters, with only a few lines and marks visible."
  
  "The only other markings on this section read \"Here there be Something Bad\", \"GO THIS WAY\", \"NOT THIS WAY\", \"The Abyss (somewhere around here),\" and \"BEWARE.\""
  
  "The top not-quite-half of the map is labeled \"The Known World\" in not quite as big letters, and it has far more detail."
  
  "At the very top is a box marked \"You started here.\""
  
  "And extending from that are three paths, each leading to a different area."
  
  "You turn the map upside down so that the paths align with the crossroads in front of you."
  
  show shittymap upsidedown with dissolve
  
  "The left path leads to a town that's apparently called Alsterside. A very long unlabeled line runs through this town, maybe a river."
  # travel along river
  
  "The right path leads to a forest next to some mountains. A few huts are scattered throughout the forest, but you're uncertain if these are marking locations or just meant to represent there being buildings in there."
  # through mountains
  
  "The center path leads to a small town called Griess. There's scribbled text next to it that you can't read, and the area looks like it was scribbled over heavily at some point."
  # cross ocean/lake
  
  "It seems like there are paths from all three regions to the \"Unknown World.\""
  
  "You put your map away and look back at the crossroads."
  
  hide shittymap upsidedown with dissolve
  
  jump crossroads

label path2center:

label path2right:

  
# when an ending itll describe it and then fade out and say smth like hero #<number> [: the ...]? and then go to death/lost/astray

# more bad ending ideas: stabbed to death by a past hero turned evil, dies of dysentery, stuck in quicksand, climbed a tree and can't get down, falls in a volcano,

label death:
  "And so, the Hero died."
  "And the prophecy was not fulfilled..."
  "But it was not failed."
  "For the Hero still breathes..."
  "...and is ready to begin the quest."
  $ plays += 1
  $ deaths += 1
  jump start

label lost: # used when the hero is trapped/captured/lost unwillingly
  "And so, the Hero was lost, unable to continue on the quest."
  "And the prophecy was not fulfilled..."
  "But it was not failed."
  "For the Hero still breathes..."
  "...and is ready to begin the quest."
  $ plays += 1
  $ strays += 1
  jump start

label astray: # used when the hero leaves the quest willingly
  "And so, the Hero strayed from the quest, never to return."
  "And the prophecy was not fulfilled..."
  "But it was not failed."
  "For the Hero still breathes..."
  "...and is ready to begin the quest."
  $ plays += 1
  $ strays += 1
  jump start
  
  # This ends the game.
  return
