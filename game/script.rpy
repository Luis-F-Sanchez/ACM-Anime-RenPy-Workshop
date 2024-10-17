# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define cha1 = Character("Fern")
define cha2 = Character("Yona-tan")
define cha3 = Character("Amogu")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene ravenclaw_background #Living Room 

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    

    # These display lines of dialogue.
    
    "At night in a poor lit living room"
    
    show grosspim

    "Fern is sitting on the couch, watching TV, and casually sipping from a __drink___"
        
    "The doorbell rings. Yona-tan enters holding a box"
    
    show grosspim at left
    with move
    
    show ani-girl at right
    with moveinright
    
    cha2 "YO look what I got!" #smile
    
    cha1 "Unless it's __item__, I dont care" #squint
    
    cha2 "{i}Takes a pause{/i}" #stare
    
    cha2 "It's better. WAY better. I got us..." #normal
    
    scene susus #living room table
    
    #show choice of img
    
    "Yona-tan whips it out"
    
    cha2 "This!"
    
    scene ravenclaw_background
    show grosspim at left
    show ani-girl at right
    
    cha1 "What... is that? Is that… what I think it is?" #squint
    
    cha2 "It's exactly what you think it is! A ___obj___! And guess what, it has extra features! It vibrates!" #show txt bit by bit
    
    cha1 "Vibrates?! Why would you get something like that?" #suprised
    
    cha2 "Because I have impeccable taste, obviously." #wink
    
    show Makotoneutral at left
    with moveinleft
    show grosspim at center
    #with moveincenter
    
    "Suddenly, the other roomate Amogu enters the aparment, holding a ___small_item___"
    
    cha3 "What's going on here?! I heard you guys had a __obj2___" #mad
    
    "Both Fern and Yona-tan look at each other, then back at the __obj___, trying to hide it."
    
    cha1 "Oh, you know, just… goofy things." #shocked

    cha3 "What kind of \"goofy things\"? Because last time, you two were using my computer to enlist me to the military!" #change to action with obj makes sound
    
    "Both Fern and Yona-tan remained silent"
    
    scene susus
    
    #show ani-girl at right with moveinleft
        
    "The door suddenly flies open, and Yona-tan comes stumbling out, holding the __obj___"
    
    show ani-girl at right with moveinleft
    
    cha2 "I told you it was for the BOTH of us!" #mad
    
    #show Makotoneutral at left
    
    "Amogu shouts from the apartment"
    
    cha3 "And I told you, if I hear one more weird sound from that thing, I'm calling the police!" #mad
    
    cha2 "Jeez, you need to chill. It's not like I ordered the ___obj3___... yet." #mad, then smile with txt in parts
    
    cha1 "Oh yeah, like that's any better." #unamused
    
    cha2 "Oh, you have no idea" #devious
    
    "The __obj__ suddenly buzzes loudly in her hand"

    show cha2 #scared
    
    cha3 "That's it, i'm calling the"
    

    # This ends the game.

    return
