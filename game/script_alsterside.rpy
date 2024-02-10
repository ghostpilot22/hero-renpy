define w = Character("Woman")

label path2als:
  scene bg path plains with dissolve
  
  "You head down the left path."
  
  "The scenery is fascinating at first, as it's the first time you've actually seen any of these things."
  
  "The distant mountains, the tall grasses and scrubby plants, the bugs and animals around you, the occasional tree... Everything except for the sky above is utterly new to you."
  
  "But pretty soon it starts to all look the same, each mile of plains blending into the next and the one before it."
  
  "It's a sunny day, and the sun beats down on you as you walk. Before long, you're starting to sweat."
  
  "You rifle through your bag, and pull out a wide-brimmed hat. This'll do to keep the sun off of your face."
  
  "And you make a point of taking a swig from your water bottle every now and then. Gotta stay hydrated."
  
  "Even so, after a few hours of walking, you're starting to get bored and uncomfortable, and your water bottle is looking pretty close to empty."
  
  if notlookedatmap:
    "You have no idea where you are or where you're going, you realize."
    
    "And you have no idea how long it'll take for you to get there."

  else:
    "You'd pull out your map to check how far along you are, but there weren't any distance markers on it, and the path was drawn as a completely straight line."
    
    "But you should be coming up on the town pretty soon by now... you hope."
  
  menu:
    "What do you do?"
    "Keep going.":
      "You keep going..."
      jump path2als2
    "Turn back.": # die of heatstroke
      "You decide that this isn't worth it, and turn around to start walking back the way you came."
      $ loyalty -= 1
      $ hope -= 1
      jump path2alsturnback
    "Sit down and give up.": # aid might arrive depending on luck?, hope stat drops
      "You sit down on the ground, close to despair. You're too tired to keep going, and too far out to turn back."
      $ hope -= 3
      jump path2alsgiveup
    "Look at your map." if notlookedatmap: # map half ruined by sweat. shitty photocopier ink woooo
      "You pull out your map..."
      jump path2alsmap

label path2alsturnback: # Die of heatstroke/dehydration
  "After only about an hour, you start to realize you might have made a mistake."
  
  "The sun is still beating down on you, despite the meager shade provided by your hat, and now your water bottle is completely empty."
  
  "Still, you press on, sweat dripping down your face and soaking your clothes."
  
  "You want to {i}fucking go home.{/i}"
  
  "How long has it even been since you left? Five hours? Eight? Ten?"
  
  "The sun still seems to be high in the sky... it can't be only midday still, can it?"
  
  "You continue walking. If it's only midday, maybe you haven't been walking as long as you think, and you'll be back home in no time."
  
  "Yeah. You can do this. You're tough, you can stand a little bit of sun, and when you get back to the crossroads you'll go a different direction this time."
  
  $ edgy += 1
  
  "...And maybe stop back at the facility to refill your water."
  
  "God you're so fucking thirsty."
  
  "You walk on for several more hours, trying to ignore how dry your mouth has gotten."
  
  "When you next look up at the sky, the sun is still just as high as it was last time."
  
  "This can't be right. How is it still midday?"
  
  "You keep walking. You don't have any other option at this point."
  
  "At some point you must have stopped sweating. Your skin feels dry and crusted with salt."
  
  "That can't be a good sign."
  
  "This was a mistake."
  
  "You think about crying out for help, but as soon as the thought crosses your mind you realize that no one would be there to hear you even if you could."
  
  "Your tongue sticks to the inside of your mouth."
  
  show vignette0 with slow_dissolve
  "Blackness laps at the edges of your vision."
  
  "Your head spins."
  
  "As you take another slow, dragging step, your foot catches on a rock in the middle of the path."
  
  "The world seems to slowly tilt around you, the ground coming up to meet you."
  
  scene plains path fallen with dissolve
  
  "Your face smashes into the earth."
  
  "A tooth skitters across the sandy ground of the path."
  
  show vignette0 with slow_dissolve
 
  "The blackness floods your vision from every side, until only a tiny patch of sight is left, through which you can barely make out the red and white spot of your tooth."
  
  "And then even that is gone."
  
  scene endingscreen with slower_fade
  
  # Ending text goes here
  # achievement get!
  $ deaths["path to alsterside"] += 1
  $ achievement.grant("Died of Dehydration!")
  
  jump death

label path2alsmap: 
  show shittymap ruined with dissolve
  "... And realize that it's completely ruined."
  "It seems like the sweat, and probably also a few spills from your water bottle, have soaked the paper and smeared the ink beyond recognition."
  "You try to orient yourself."
  "Assuming that the three split paths at the top of the map are where you started, then it looks like you might be heading for a town. You hope."
  "You feel like you should probably be coming up on the town pretty soon, might as well keep walking."
  jump path2als2

label path2alsgiveup: # Die or get found, depending on luck
  "The sun beats down on you as you sit, tired and dizzy, at the side of the path."
  
  show vignette1 with slow_dissolve
  
  "Eventually, you feel yourself growing sleepy, and your eyes slowly slip shut."
  
  "..."
  "..."
  "..."
  
  if (luck < 10 and luck > 3): # lucky enough to live
    "...You fade into unconsciousness, and begin to fade deeper still."
    "You are teetering on the edge of life and death when-"
    show als woman concerned
    w "Hello..."
    
  else: # unlucky, no one finds you, you die
    "...And they don't open again."
    "After slipping into unconsciousness, you slip further away from life, eventually fading out on the side of the path."
    "Perhaps one day someone will come by and find your corpse, but in the meantime it lies here, slowly being further dried out by the scorching sun."
    # Ending text goes here
    # achievement get!
    $ deaths["path to alsterside"] += 1
    $ achievement.grant("Lay Down and Die")
    
    jump death

label path2als2:
  
  if(deaths["path to alsterside"] > 0):
    "As you walk, not paying attention to where you put your feet on the level dirt path, you suddenly stumble over something."
    "You look down and see..."
    scene plains path body
  
  return