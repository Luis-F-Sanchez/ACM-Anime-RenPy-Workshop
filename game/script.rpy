# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define cha1 = Character("Fern", color="#586eff")
define cha2 = Character("Yona-Tan", color="#a25100")
define cha3 = Character("Kazzy", color="#417d7b")


# obj:
# gojo body pillow (gojobp)
# comically large spoon (spoon)
# metal bar (metalpipe)
# demon core (demoncore)
# missile (missile)
# freddy plushie (freddy)
# lego set (lego)

# items:
# RTX 5090
# Adderall
# the US constitution
# plunger

# item1 = 
# *obj1* = 
# obj2 = 
# obj3 = 


label start:
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene friends_living_room:
        yalign 0.4
        xalign 0.4
        zoom 2.6

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    

    # These display lines of dialogue.
    
    "{i}At night in a poor lit living room{i}"
    
    show croppedpim at left:
        zoom 1.7

    "{i}Fern is sitting on the couch, watching TV, and casually sipping from a drink{i}"
        
    "{i}The doorbell rings. Yona-tan enters holding a box{i}"
    
    show chihiro grin full at right:
        yalign -0.4
        zoom 1.9
    with moveinright
    
    " "
    
    show chihiro smile full
    cha2 "YO look what I got!" #smile
    
    cha1 "Unless it's a _item1_, I dont care" ####################################################################
    
    show chihiro think full
    "{i}Yona-Tan takes a pause{/i}" #stare
    
    show chihiro grin full
    cha2 "It's better. WAY better. I got us..." #normal
    


    scene black_background:
        yalign 0.4
        xalign 0.5
        zoom 1.1
    
    show background2:
        yalign 0.4
        xalign 0.5
        zoom 2.8

    show table2

    show gojobp at center:
        ypos 850
    
    "{i}Yona-tan whips it out{i}"
    
    cha2 "This!"
    


    scene friends_living_room:
        yalign 0.4
        xalign 0.4
        zoom 2.6

    show croppedpim at left:
        zoom 1.7

    show chihiro smile full at right:
        yalign -0.4
        zoom 1.9
    
    cha1 "What... is that? Is that… what I think it is?" #squint
    
    show chihiro strong full
    cha2 "It's exactly what you think it is! A _obj1_! And guess what, it has extra features! It vibrates!" ##############################################
    
    cha1 "Vibrates?! Why would you get something like that?" #suprised
    
    show chihiro grin
    cha2 "Because I have impeccable taste, obviously." #wink
    
    show chihiro grin at center:
        yalign -0.4
        zoom 1.9

    show kazuma knife at right:
        yalign 1.2
        zoom 2.5
    with moveinright
    
    "{i}Suddenly, the other roomate Kazzy enters the aparment{i}"

    show kazuma fight:
        yalign 0.7
        zoom 0.5
    
    cha3 "What's going on here?! I heard you guys had a _obj2_" ###############################################################
    
    show chihiro worried full
    "{i}Both Fern and Yona-tan look at each other, then back at the _obj1_, trying to hide it.{i}" ##################################################
    
    cha1 "Oh, you know, just… goofy things." #shocked

    show kazuma mad:
        yalign 0.5
        zoom 0.6

    cha3 "What kind of \"goofy things\"?"
    cha3 "Because last time, you two were using my computer to enlist me to the military!"
    
    show chihiro think full
    "{i}Both Fern and Yona-tan remained silent{i}"
    
    "{i}...{i}"
    
    scene hallway:
        yalign 0.4
        xalign 0.4
        zoom 0.35
            
    "{i}The door suddenly flies open{i}"

    "{i}Yona-tan comes stumbling out, holding the _obj1_{i}" ###############################################################
    
    show chihiro somber full at right:
        xalign 0.5
        yalign 1.4
        zoom 1.1
    with moveinleft
    
    cha2 "I told you it was for the BOTH of us!" #mad
        
    "{i}Kazzy shouts from the apartment{i}"
    
    cha3 "And I told you, if I hear one more weird sound from that thing, I'm calling the police!" #mad
    
    show chihiro strong full
    cha2 "Jeez, you need to chill. It's not like I ordered the _obj3_\n... \nyet >:)" ############################################################
    
    cha1 "Oh yeah, like that's any better." #unamused
    
    show chihiro grin full
    cha2 "Oh, you have no idea" #devious
    
    "{i}The _obj1_ suddenly buzzes loudly in her hand{i}" #############################################################
    
    show chihiro tear full #scared
    cha3 "That's it, i'm calling the police!"
    
    # This ends the game.

    return
