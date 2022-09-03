# The script of the game goes in this file.

# characters
define mystery = Character("???")
define cytoidchan = Character("Cytoid Chan")
define cinamyn = Character("Cinamyn")

# for intro

image splash = "text logo.png"

#audio

define audio.littleidea = "audio/littleidea.mp3"
define audio.summer = "audio/summer.mp3"
define audio.tenderness = "audio/tenderness.mp3"
define audio.subterranean = "audio/Subterranean Monster.mp3"
define audio.fever = "audio/A Fever.mp3"

# sound effects

define audio.switch = "se/switch.wav"
define audio.door = "se/door.wav"
define audio.restore = "se/restore.wav"


#other stuff
image movie = Movie(size=(1066, 600), xpos=0, ypos=0, xanchor=0, yanchor=0)



label splashscreen:
    scene black
    with Pause(1)
    play music tenderness
    show text "The Cytoid Moderators present..." with dissolve
    with Pause(2)

    hide text with dissolve

    show splash at center with dissolve
    with Pause(2)

    scene black with dissolve

    return
    
#game start
    
label start:
    $_game_menu_screen = None
    stop music
    scene black
    with dissolve
    if month == 4 and day <= 7:
        $ persistent.aprilfools = True
    if month == 3 and day == 31:
        $ persistent.aprilfools = True
    if persistent.aprilfools == None:
        "Today is %(month)d/%(day)d/%(year)d. \nThis game is recommended to be played around April Fools."
    if persistent.initstart == None:
        jump change_name
    jump select_menu
    
label select_menu:
    menu:
        "Select Option (disabled)":
            pass
        "Story":
            jump story_select
        "Change Name":
            jump change_name
        "Main Menu":
            return
            
label change_name:
    $ new_name = ""
    $ warning = ""
    $ defaultname = ""
    while new_name == "":
        $ new_name = renpy.input("Input your name. "+warning, length=16)
        if defaultname == "Alan":
            $ defaultname = ""
            $ new_name = "Alan"
            "Name has defaulted to \"Alan\"."
        $ warning = "Name cannot be empty!\nIf another blank name is submitted, the name will default to Alan."
        $ defaultname = "Alan"
    $ persistent.playername = new_name
    # first time launching game after making name
    if persistent.initstart == None:
        $ persistent.initstart = True
    jump select_menu

label story_select:
    menu:
        "Select Option (disabled)":
            pass
        "Chapter One":
            jump chapter1part1
        "Chapter Two (it no longer exists) (disabled)" if persistent.chapteronecomplete == None:
            pass
        "Chapter Two (it no longer exists) (disabled)" if persistent.chapteronecomplete == True:
            jump chapter2
        "Back":
            jump select_menu
            
    

label chapter1part1:
    scene black
    mystery "...."
    mystery "..p, [persistent.playername]..."
    mystery "Wake up, [persistent.playername]!"
    scene bedroom with dissolve
    "A forced shaking brings your senses alive, as you slowly open your eyes."
    "Next to you is..."
    show cytoidchan at center with dissolve
    play music littleidea
    voice "voice/cchanvoice1.mp3"
    mystery "Good morning, [persistent.playername]! Finally, you're awake!"
    voice sustain
    menu:
        mystery "Good morning, [persistent.playername]! Finally, you're awake!\n(Select your response using the menu above)"
        "Select your response (disabled)":
            pass
        "\"Ugh... good morning...\"":
            voice "voice/cchanvoice46.mp3"
            mystery "Come on, wipe that dirt off your eyes!"
            voice sustain
            "As pushy as she was, I reluctantly sat up from my bed."
        "\"Who are you?\"":
            voice "voice/cchanvoice47.mp3"
            mystery "What? Are you still sleepy, [persistent.playername]?"
            voice sustain
            "The girl shoke me more and more, and then I remembered from the daze from my deep sleep."
        "\"Morning, Cytoid Chan!\"":
            voice "voice/cchanvoice48.mp3"
            cytoidchan "Morning, [persistent.playername]! You've been asleep for a while now."
    voice sustain
    "Her name is Cytoid Chan, and we have been dating for a while."
    voice sustain
    "I didn't think that we'd end up living together, however."
    voice "voice/cchanvoice2.mp3"
    cytoidchan "So! Guess what day today is!!!"
    voice sustain
    "I took out my smartphone, which was cracked from a Cytoid Session, and looked at my lock screen."
    voice sustain
    "It showed: \nApr 1, 2020, 11:42 A.M."
    voice sustain
    "...11:42 A.M.?!?!? How long was I asleep!?! I'm extemely late for my job!"
    voice sustain
    "I bolted up from my bed and proceed to violate my room by making a mess whilst trying to find my regular suit."
    voice sustain
    voice "voice/cchanvoice3.mp3"
    cytoidchan "Hold it, hold it! Calm down [persistent.playername]. There's no need to panic!"
    voice sustain
    menu:
        cytoidchan "Hold it, hold it! Calm down [persistent.playername]. There's no need to panic!\n(Select your response using the menu above)"
        "Select your response (disabled)":
            pass
        "\"But I'm late!\"":
            voice "voice/cchanvoice4.mp3"
            cytoidchan "Don't worry, I already called you in sick, because I tried to wake you up for hours!"
        "\"Why didn't you wake me up sooner?!\"":
            voice "voice/cchanvoice5.mp3"
            cytoidchan "I have been since 9! I even called you in sick!"
        "P A N I C":
            "I went even more on a frenzy, as soon as Cytoid Chan told me to calm down."
            voice "voice/cchanvoice6.mp3"
            cytoidchan "Geez, and even when I called you in sick..."
    voice sustain
    "... wait, Cytoid Chan did what?"
    voice sustain
    "I looked at Cytoid Chan and she seemed to be tired of my antics."
    voice "voice/cchanvoice7.mp3"
    cytoidchan "Yeah, I said that you weren't feeling well, so you got the day off. More importantly..."
    play music tenderness fadein 1.0
    voice "voice/cchanvoice8.mp3"
    cytoidchan "I want to ask you something..."
    "What was it that Cytoid Chan is blushing? It's out of the ordinary for her."
    voice "voice/cchanvoice9.mp3"
    cytoidchan "You see... I want to thank you for your Valentine's gift..., and I missed White Day by accident."
    voice sustain
    "... oh yeah. White Day is a thing. I had almost completely forgotten about it."
    hide cytoidchan with dissolve
    show cytoidchanb with dissolve
    voice "voice/cchanvoice10.mp3"
    cytoidchan "So I wanted to call you in sick anyways, so..."
    voice "voice/cchanvoice11.mp3"
    cytoidchan "I want to take you to the park, if that's ok with you."
    voice sustain
    menu:
        cytoidchan "I want to take you to the park, if that's ok with you.\n(Select your response using the menu above)"
        "Select your response (disabled)":
            pass
        "\"Sure!\"":
            voice "voice/cchanvoice12.mp3"
            cytoidchan "Alright! I'm going to get dressed! I'll meet you outside!"
        "\"Really?\"":
            voice "voice/cchanvoice13.mp3"
            cytoidchan "Of course, really! What wouldn't I do for you!"
            voice "voice/cchanvoice14.mp3"
            cytoidchan "Imma get changed, just meet me outside!"
        "\"Sorry, no thanks.\"":
            voice "voice/cchanvoice15.mp3"
            cytoidchan "Stop teasing me! I know you want to go!"
            voice "voice/cchanvoice16.mp3"
            cytoidchan "Here, I'll go change now. Get ready!"
    play sound door
    hide cytoidchanb with dissolve
    "Cytoid Chan promptly ran out, humming a tune."
    "Since I have a day off of work, thanks to Cytoid Chan, I see no reason to refuse."
    "I get up, change, brush my teeth, and prepare myself for a date."
    scene black with dissolve
    stop music fadeout 1.0
    jump chapter1part2
    
    
label chapter1part2:
    scene park with dissolve
    play music summer
    show cytoidchan at center with dissolve
    "Cytoid Chan and I are walking together down the road, with the rows of cherry blossom trees lining up the road."
    "We were holding hands, which I felt nervous about, but Cytoid Chan didn't seem to mind."
    voice "voice/cchanvoice17.mp3"
    cytoidchan "{font=unifont.ttf}♫♪♫{/font}"
    voice sustain
    "Cytoid Chan seems to be in a good mood."
    voice sustain
    "Well, since she is commited to even calling me off work today, maybe she has something in mind."
    voice sustain
    "As we walked through the park trail, the cherry blossoms overhanging above us, it was like walking in a dream."
    voice "voice/cchanvoice18.mp3"
    cytoidchan "The sakura petals... they're so pretty..."
    voice "voice/cchanvoice19.mp3"
    cytoidchan "What do you think, [persistent.playername]?"
    voice sustain
    menu:
        cytoidchan "What do you think, [persistent.playername]?\n(Select your response using the menu above)"
        "Select your response (disabled)":
            pass
        "\"They are.\"":
            voice "voice/cchanvoice20.mp3"
            cytoidchan "I knew you'd say that!"
        "\"It's cool.\"":
            voice "voice/cchanvoice21.mp3"
            cytoidchan "Really? Because they're so beautiful!"
        "\"I guess.\"":
            voice "voice/cchanvoice22.mp3"
            cytoidchan "Come on, you know you like it, don't be nervous~"
            voice sustain
            "Cytoid Chan said this with a smirk, knowing I was lying."
    voice sustain
    "We suddenly stopped, as Cytoid Chan put her hand in a pocket of a dress."
    voice sustain
    "Cytoid Chan took a small step back, taking it out and putting it behind her back, not revealing it to me."
    hide cytoidchan with dissolve
    show cytoidchanb with dissolve
    voice "voice/cchanvoice23.mp3"
    cytoidchan "I... I have something to give you..."
    voice sustain
    play music tenderness fadein 1.0
    menu:
        cytoidchan "I... I have something to give you...\n(Select your response using the menu above)"
        "Select your response (disabled)":
            pass
        "\"What is it?\"":
            voice "voice/cchanvoice24.mp3"
            cytoidchan "It's... ummmm...."
        "\"Is it a gift?\"":
            voice "voice/cchanvoice25.mp3"
            cytoidchan "Something like that... so... umm...."
        "Wait in suspense":
            pass
    voice sustain
    "Cytoid Chan slowly brings her hands, revealing it on the top of her two palms."
    voice sustain
    "In a small box, the contents inside are pieces of chocolate."
    voice sustain
    menu:
        "In a small box, the contents inside are pieces of chocolate.\n(Select your response using the menu above)"
        "Select your response (disabled)":
            pass
        "\"Is this for me?\"":
            voice "voice/cchanvoice26.mp3"
            cytoidchan "Yes... this is thanks. Also..."
            voice sustain
            "Cytoid Chan's eyes seems to avert away from [persistent.playername]."
        "\"Don't mind if I do!\"":
            voice "voice/cchanvoice27.mp3"
            cytoidchan "W-wait!"
            voice sustain
            "Cytoid Chan gripped onto your arm before you get to a piece."

    voice "voice/cchanvoice28.mp3"
    cytoidchan "P-- please... Wait... I need to collect m-myself."
    voice "voice/cchanvoice29.mp3"
    cytoidchan "Pp-p-p... please look underneath the parchment."
    voice sustain
    "Looking at the box, something looks to be bulging out of the bottom of the box, like it had a false bottom."
    voice sustain
    "Taking the parchment out of the bottom, you see a thinner, more ornate case, in a way that slightly fits the box of chocolates. Taking off the lid of the case, you see..."
    voice sustain
    menu:
        "Taking the parchment out of the bottom, you see a thinner, more ornate case, in a way that slightly fits the box of chocolates. Taking off the lid of the case, you see...\n(Select your response using the menu above)"
        "Select your response (disabled)":
            pass
        "\"A ring?\"":
            voice "voice/cchanvoice30.mp3"
            cytoidchan "Yes... I made up my mind..."
        "\"More chocolate?\"":
            voice "voice/cchanvoice31.mp3"
            cytoidchan "Umm... did you look closer?"
        "Be speechless":
            voice "voice/cchanvoice32.mp3"
            cytoidchan "So.. did you see what was inside?"
    voice "voice/cchanvoice33.mp3"
    cytoidchan "I know it should be the other way around... but..."
    voice "voice/cchanvoice34.mp3"
    cytoidchan "Please! I love you, so... umm... I want you with me forever!"
    voice sustain
    "A confession that did not happen in the way you expected."
    voice sustain
    "It seems like Cytoid Chan is waiting for your response."
    voice sustain
    menu:
        "It seems like Cytoid Chan is waiting for your response.\n(Select your response using the menu above)"
        "Select your response (disabled)":
            pass
        "\"Yes.\"":
            voice "voice/cchanvoice35.mp3"
            cytoidchan "T-thanks..."
    voice sustain
    "Cytoid Chan turned around, probably to not let her face be seen out of embarassment, as if it was an anime trope."
    voice "voice/cchanvoice36.mp3"
    cytoidchan "Let's... sleep together... for once. Just this once. Tonight."
    voice sustain
    "Cytoid Chan then seemed to froze up."
    voice sustain
    "After a moment, she then ran away from [persistent.playername]."
    hide cytoidchanb with moveoutleft
    voice "voice/cchanvoice37.mp3"
    cytoidchan "It's... I n-need to go to the restroom! Ah!"
    stop music fadeout 1.0
    "And just like that, she was gone."
    scene black with dissolve
    "After a while, Cytoid Chan returned, apologizing for her earlier actions, and together, Cytoid Chan and [persistent.playername] returned home together."
    jump chapter1part3
    
    
label chapter1part3:
    scene black with dissolve
    "After we got home, we took baths in turn and soon, evening hit."
    scene bedroomn with dissolve
    "9 PM."
    "You have been eagerly waiting for Cytoid Chan."
    "Looking on your phone, as the seconds tick off, you wonder if this was a good idea or not."
    scene black with dissolve
    scene bedroomn with dissolve
    $ clocktime = 10
    "%(clocktime)d PM."
    "It's been a while since you heard from Cytoid Chan, ever since you had dinner with her."
    "Being worried, you:"
    $ menustring = "Being worried, you:"
    $ clocktime = 10
    $ part3loop = True
    while part3loop is True:
        menu:
            "[menustring]\n(Select your response using the menu above)"
            "Select your response (disabled)":
                pass
            "See where Cytoid Chan is.":
                $ part3loop = False
            "Wait.":
                if clocktime == 3:
                    $ part3loop = False
                    "You thought to yourself: \"I can't wait any longer, I need to find Cytoid Chan!\""
                elif clocktime != 12:
                    $ clocktime += 1
                else:
                    $ clocktime = 1
                if part3loop == True:
                    "You waited longer."
                    scene black with dissolve
                    scene bedroomn with dissolve
                    if clocktime < 9 or clocktime == 12:
                        "It is now %(clocktime)d AM."
                        $ menustring = "It is now " + str(clocktime) + " AM."
                    else:
                        "It is now %(clocktime)d PM."
                        $ menustring = "It is now " + str(clocktime) + " PM."
                        
    
    play sound door
    scene black with dissolve
    scene hallwayn with dissolve
    "Upon exiting your room, you hear some noises further down."
    "You can't see what's in the dark so you reach for the light switch."
    play sound switch
    scene hallway with dissolve
    show cytoidchanb at left with dissolve
    show cinamyn at center with dissolve
    voice "voice/cchanvoice38.mp3"
    cytoidchan "O-oh!"
    "You see Cytoid Chan, on the couch."
    voice sustain 
    "And with Cytoid Chan is a man you have supposedly never seen."
    voice sustain
    menu:
        "And with Cytoid Chan is a man you have supposedly never seen.\n(Select your response using the menu above)"
        "Select your response (disabled)":
            pass
        "\"Who is this?\"":
            pass
        "\"Why is he in our house?\"":
            pass
        "\"Where did he come from?\"":
            pass
        "\"What did you do?\"":
            pass
        "\"When did this happen?\"":
            pass
        "\"How did he get in here?\"":
            pass
    voice "voice/cchanvoice39.mp3"
    cytoidchan "Please! I can explain!"
    voice "voice/cinavoice1.mp3"
    mystery "No need. I'll explain."
    hide cytoidchan with dissolve
    voice "voice/cinavoice2.mp3"
    mystery "I'm sure you're confused, but simply put, I'm here to steal Cytoid Chan."
    play music subterranean
    voice "voice/cinavoice3.mp3"
    mystery "The name is Cinamyn, and I am a very upstanding business man, as you can tell from the quality of my suit."
    voice sustain
    menu:
        mystery "The name is Cinamyn, and I am a very upstanding business man, as you can tell from the quality of my suit.\n(Select your response using the menu above)"
        "Select your response (disabled)":
            pass
        "\"Why are you stealing Cytoid Chan?!\"":
            voice "voice/cinavoice4.mp3"
            cinamyn "I don't answer un-business-like questions, but I'll make an exception for you."
        "\"Get out!!\"":
            voice "voice/cinavoice5.mp3"
            cinamyn "Why should I? I've come to steal her back."
        "\"Leave Cytoid Chan alone, or else!\"":
            voice "voice/cinavoice6.mp3"
            cinamyn "You are truly unprofessional."
    voice "voice/cinavoice7.mp3"
    cinamyn "You see, Cytoid Chan was, and is my girlfriend."
    voice "voice/cinavoice8.mp3"
    cinamyn "In fact, you can say we're... hitched."
    voice "voice/cinavoice9.mp3"
    cinamyn "Cytoid Chan went missing one day, and I went to look for her everywhere, and anywhere."
    voice "voice/cinavoice10.mp3"
    cinamyn "Once I saw her waiting out of the house, I followed you and Cytoid Chan, to confirm if it is really her."
    voice sustain
    menu:
        cinamyn "Once I saw her waiting out of the house, I followed you and Cytoid Chan, to confirm if it is really her.\n(Select your response using the menu above)"
        "Select your response (disabled)":
            pass
        "\"So you stalked us?!\"":
            voice "voice/cinavoice11.mp3"
            cinamyn "In a professional fashion, I guess you can say that, but what of it? We were once lovers."
        "\"You lie!\"":
            voice "voice/cinavoice12.mp3"
            cinamyn "Wait until I finished my business story before accusing me."
    voice "voice/cinavoice13.mp3"
    cinamyn "I saw her hand you something. What was it that you recieved?"
    voice "voice/cinavoice14.mp3"
    cinamyn "Actually, nevermind. once she saw me at the sakura trees, we hatched up a plan, although I couldn't control my feelings for her and slept with her at this very couch."
    voice "voice/cinavoice15.mp3"
    cinamyn "What matters is that once you were seperated from Cytoid Chan, we would return to where we once loved each other."
    voice sustain
    menu:
        cinamyn "What matters is that once you were seperated from Cytoid Chan, we would return to where we once loved each other.\n(Select your response using the menu above)"
        "Select your response (disabled)":
            pass
        "\Is this true, Cytoid Chan?!\"":
            show cytoidchan behind cinamyn at left with dissolve
            cytoidchan "..."
            voice "voice/cchanvoice40.mp3"
            cytoidchan "I'm so sorry. I lied to you."
        "\"You lie!\"":
            voice "voice/cinavoice16.mp3"
            cinamyn "Hmm... So you don't believe me."
            show cytoidchan behind cinamyn at left with dissolve
    voice "voice/cinavoice17.mp3"
    cinamyn "Very well, we're leaving."
    voice sustain
    "Cinamyn grabbed Cytoid Chan's wrist and made for the exit."
    play sound door
    "Upon your shock, you didn't react fast enough to catch Cinamyn and Cytoid Chan."
    stop music fadeout 1.0
    scene black with dissolve
    "Where have things gone wrong?"
    "Was this ring and the feelings that came with it, essentially, worthless now?"
    "You tried to sleep in your room, but in the midst of your thoughts, you are unable to contain your feelings."
    $ renpy.movie_cutscene("static.ogv")
    jump chapter1part4

label chapter1part4:
    scene black
    "The next day..."
    scene outdoor with dissolve
    show cytoidchan at left with dissolve
    show cinamyn at center with dissolve
    voice "voice/cchanvoice41.mp3"
    cytoidchan "Did you have to go that far?"
    voice "voice/cinavoice18.mp3"
    cinamyn "Well, that's the price for asking for a day off. And since it's April Fool's Day, I wouldn't give up an oppurtunity to mess with my coworkers!"
    voice "voice/cinavoice19.mp3"
    cinamyn "I can't believe he didn't recognize me! Guess that's love for you."
    voice "voice/cinavoice20.mp3"
    cinamyn "Still, don't worry about it! After all is forgiven, you two will have the most professional wedding."
    cytoidchan "I hope this gift I got for [persistent.playername] will fix things."
    hide cytoidchan with dissolve
    hide cinamyn with dissolve
    scene hallway with dissolve
    play sound door
    scene bedroom with dissolve
    show cytoidchan with dissolve
    voice "voice/cchanvoice42.mp3"
    cytoidchan "[persistent.playername]? It's me. I'm sorry for yesterday's April Fool's prank. I had no choice."
    voice "voice/cchanvoice43.mp3"
    cytoidchan "... where is he?"
    voice "voice/cchanvoice44.mp3"
    cytoidchan "Why is there a breeze in this room?"
    scene bedroomr with dissolve
    voice "voice/cchanvoice45.mp3"
    cytoidchan "!!!"
    scene black
    ""
    scene red1 with dissolve
    mystery "Why..."
    play music fever 
    mystery "Why can't I be in love with you?"
    mystery "Why does it have to be [persistent.playername]?"
    mystery "But no matter."
    mystery "[persistent.playername] is gone. And my sabotager has left."
    cytoidchan "..."
    scene red2 with dissolve
    mystery "What's wrong? Cat got your tongue?"
    mystery "Go on, say something, will you?"
    mystery "Oh wait, it's because you're not programmed to, huh?"
    mystery "You're just a pathetic robot who can only follow directions from [persistent.playername]."
    mystery "No matter how much [persistent.playername] loved you, I wanted you more."
    scene red3 with dissolve
    mystery "That perfect, curvy body."
    mystery "Those bountiful breasts."
    mystery "The child bearing hips of a literal goddess."
    mystery "It honestly fucking hurts knowing that I'll never mate with you, pass my genes through you, and have your perfect offspring."
    mystery "All because [persistent.playername] wanted to only fall in love with you."
    scene red4 with dissolve
    mystery "But you know what?"
    mystery "I'd do fucking ANYTHING for the chance to get Cytoid Chan pregnant."
    centered "{size=120}A N Y T H I N G{/size}"
    mystery "And the fact that I can't is quite honestly too much to fucking bear."
    mystery "Why would Tiger create something so perfect, and [persistent.playername] to steal it all? To fucking tantalize us? Fucking laugh in our faces?! Honestly guys, I just fucking can't anymore. Fuck."
    mystery "But now that I have you, I want nothing else but you."
    scene red5 with dissolve
    stop music
    mystery "{size=50}Y{w=0.3}o{w=0.3}u{w=0.3} {w=0.3}a{w=0.3}r{w=0.3}e{w=0.3} {w=0.3}m{w=0.3}i{w=0.3}n{w=0.3}e{w=0.3}{font=unifont.ttf}♥{/font}{w=0.3}{/size}{nw}"
    $ renpy.movie_cutscene("static.ogv")
    scene black with None
    $ persistent.chapteronecomplete = True
    ""
    centered "CHAPTER ONE\nCorrupted\n\nEND"
    $ renpy.movie_cutscene("static.ogv")
    return

################################################################################
## Timer Bar
################################################################################

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.

init:
    $ import time

    $ year, month, day, hour, minute, second, dow, doy, dst = time.localtime()
   
init python: 
    #replaces transitions with dissolve
    def replacement_show(*args, **kwargs):
        renpy.transition(dissolve)
        return renpy.show(*args, **kwargs)
    config.show = replacement_show
    def replacement_hide(*args, **kwargs):
        renpy.transition(dissolve)
        return renpy.hide(*args, **kwargs)
    config.hide = replacement_hide
    
init -2 python:
    class GetText(Action):
        def __init__(self,screen_name,input_id):
            self.screen_name=screen_name
            self.input_id=input_id
        def __call__(self):
            if renpy.get_widget(self.screen_name,self.input_id):
                return str(renpy.get_widget(self.screen_name,self.input_id).content)
    
