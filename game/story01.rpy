label story01_pt1:
    # starting scene / music copied from the original game script
    stop music fadeout 2.0
    with dissolve_scene_full

    $ restore_all_characters()
    "Happy Birthday Kj!"
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    "Ah. Another day in the paradise of 'Bankstown, Japan.'"
    "My name is [player], and today is my 18th birthday!"
    "It's a school day today, but lets be honest... who wants to go to school on their birthday?"
    "Standing outside my house I ponder, today should I go buy more anime figures - or go to Yu-Gi-Oh locals?"
    "hmmmmmm..........."
    s "Heeeeeeeyyy!!"
    "Before I can decide, I see an annoying girl running towards me from the distance, waving her arms in the air like she knows me."
    show sayori 4p zorder 2 at t11
    s "Haaahhh...haaahhh..."
    mc "Oh, hey Sayori."
    $ s_name = "Sayori"
    "Sayori is my neighbour, so I really don't know why she's panting, we literally live right next door to eachother?"
    "{i}what a fatty{/i}"
    show sayori turned lsur cm ce at f11
    s "I almost lost track of time while eating my breakfast!"
    show sayori turned lup rup oe cm happ
    s "But I caught you [player]!"
    show sayori at t11
    "Sayori has been a friendly face since I moved here a couple years ago."
    "I say that, though when I first met her, I mostly just got her to pocket heal me on Marvel Rivals."
    "In actuality she's pretty shit - so I mostly stay on offline mode so that I can queue without her."
    show sayori om ce at f11
    s "Oh my gosh!!! [player] it's your birthday!"
    s "We have to spend the day together! I've got the most perfect place we can go to!!!"
    show sayori at t11
    mc "It's not that book club thing is it?"
    show sayori tap cm neut oe
    s "It's not a 'book club', it's a literature club..."
    mc "Sayori...."
    mc "That really sounds like the same thing."
    mc "And besides I get all the reading I need from visual novels, why would I wanna read books?"
    show sayori turned ldown rdown angr cm oe
    s "Oh cmon [player] do you really wanna be a freaking weeb NEET loser forever?? Meet some people."
    show sayori at f11
    s "And the middle aged chuds at Yu-Gi-Oh locals dont count!"
    mc "..."
    "{i}god I hate this bitch{/i}"

    stop music fadeout 2.0
    scene bg corridor
    with wipeleft_scene

    "And thus, today marks the day I was annoyed into joining my neighbours stupid club."
    "I dejectedly follow Sayori across the school and upstairs - a section of the school I rarely visit."
    "Sayori, tired from the menial stair climbing, swings open the classroom door."

label story01_pt2:

    scene bg club_day
    with wipeleft
    play music t3

    "I wish I just went to Yu-Gi-Oh instead."
    show sayori turned happ oe cm lup rup at t31
    s "Everyone! The new member is here~!"
    mc "Hey, I never agreed to join--"
    show sayori at thide
    hide sayori
    "I glance around the room."
    show yuri turned happ at f21
    show natsuki cross vsur oe cm at t22
    y "Welcome to the Literature Club. It's a pleasure meeting you."
    y "My name is Yuri, and this is Natsuki."
    $ y_name = "Yuri"
    $ n_name = "Natsuki"
    show yuri at t21
    show natsuki nerv om oe at f22
    n "Umm..."
    n "..............."
    show natsuki at t22
    n "{i}umm yuri can i come speak to you for a moment..{/i}"
    show natsuki at thide
    show yuri at thide
    hide natsuki
    hide yuri 
    "Uhh......"
    "What's her problem?"
    show monika lean at t11
    m "Ah, and you must be [player]! What a nice surprise!"
    "Is that-- My heart flutters, as I recognise the one and only Goatika!!"
    $ m_name = "Goatika"
    m "Welcome to the club!"
    show monika at thide
    hide monika
    mc "..."
    "All words escape me in this situation."
    show sayori turned happ oe cm at t41 
    show monika forward happ oe cm at t42
    show yuri turned neut e1d at t43
    show natsuki cross neut e2c at t44
    stop music fadeout 2.0
    "This club..."
    "{i}...is full of baddies!!{/i}"

    scene bg club_day
    with dissolve_scene_full
    play music t3

    "The girls have all gone off in seperate areas of the clubroom to do their own activities."
    "I guess it's time to s*cialise. I'll start with Yuri, I'm pretty curious about what the heck was going on with Natsuki earlier."
    "I walk over to Yuri, who is sitting alone at a desk by the windows - focused in on a book."
    show yuri turned neut e1a at t33
    mc "Hey, Yuri right? Mind if I sit next to --"
    # if youre reading this, and think this is weird, just know this is a reference to an inside joke
    "Standing next to her, I notice that in the middle of her book she's concealing a phone - on which is the steam page for a game called 'Beat Banger'."
    show yuri turned pani om oe
    mc "WHAT THE FUCK???? IS THAT PORN??"
    show yuri at f33
    y "N-no no no th-this isn't what it looks like!"
    mc "Yuri why the fuck are you looking at this shit in the literature club?!"
    show yuri shy at t33
    y "No-no I-I was {b}just looking{/b}!"     
    "I wonder if this will be something I'll constantly reference later..."
    show yuri neut e1
    y "Um. What was it you wanted... [player]."
    mc "..."
    mc "Well - I guess I was wanting to ask about what's up with Natsuki? She was acting weird when I met her."
    mc "I get the feeling it was about me, so I hope you don't mind me asking, what was it she needed to say to you?"
    show yuri turned sad om ce
    y "Oh... You know it was really nothing."
    show yuri at thide
    hide yuri

    "FLASHBACK TIME"

    # very important note: my friend (kj) is black, so this is very funny i swear
    stop music fadeout 0.5
    show natsuki cross angr om oe at f22
    show yuri turned rup lup cm oe at t21
    play sound page_turn
    with pixellate
    n "Seriously? She brought one of {i}those{/i} people?"
    n "Way to kill the atmosphere."
    show natsuki at t22
    show yuri turned neut b2c om
    y "Oh cmon Natsuki you can't be saying that stuff... Sayori knows this guy, he'll be fine."
    show natsuki at f22
    n "His people are dangerous! Have you even heard about the Chicago crime statistics?"

    show natsuki thide
    hide natsuki
    show yuri turned sad om ce at t33
    play sound page_turn
    with pixellate

    mc "Well. I guess I just have to go talk to her myself."
    
    show yuri thide
    hide yuri
    scene bg club_day
    with dissolve_scene_full
    play music t8
    
    "Natsuki is in the corner of the classroom, rummaging through the closet"
    "Yuri watches as I walk past her, and toward Natsuki. Totally Ego'ing her as she tries to warn me to stay away from Natsuki."
    "I never let foids tell me what to do."

    # VERY IMPORTANT: MY FREIND (KJ) IS BLACK, SO THIS IS VERY FUNNY, I SWEAR IM NOT RACIST, NATSUKI IS RACIST
    scene bg closet
    with wipeleft
    mc "Uhh Hi Natsuki - It's me, Sayori's friend, [player]."
    show natsuki cross doub cm oe at t11
    n "Umm.... Hi?"
    show natsuki ce
    n "..."
    n "Um.... This is the closet where we're able to keep our club supplies in."
    show natsuki oe om
    n "There's books and stuff in here that you can read but just don't steal them okay?"
    show natsuki cm
    mc "Why would you assume I'd steal a book from the club's closet?"
    show natsuki om at f11
    n "Um yeah sorry for assumming they taught you to read in wakanda or wherever you're from"
    show natsuki
    stop music
    n "You can't steal ANYTHING okay? capiche ******?"
    show natsuki at t11
    "..."
    "..."
    play sound "sfx/monikapound.ogg"
    "WHAT THE FUCK IS WRONG WITH THIS BITCH???"

    menu:
        "Slime out Natsuki":
            show natsuki cross mc b3b at f11
            n "Woah you look angry, don't pull the 'nine on me jamal."
            "*pulls out glock*"
            show natsuki turned pani cm oe at t11
            "*cocks gun*"
            $ m_name = "???"
            play music t9
            m "GUYS STOP!"
            $ m_name = "Monika"
            show natsuki at t22
            show monika forward cry cm oe at f21
            m "Guys! This isn't You!!!"
            m "Please stop fighting!!!"
            show monika ce
            m "..."
            m "[player], to the hallway with me, Natsuki - go talk to yuri!"
            call story01_end from _call_story01_end_1

label story01_end:
    scene bg corridor
    show monika forward neut cm ce at t21
    with dissolve_scene_full
    m "{i}sigh{/i}"
    show monika forward neut cm oe
    m "Listen... [player]-"
    show monika at t21
    stop music fadeout 2.0
    show sayori turned lup happ cm ce at t22
    s "{i}nom nom nom nom nom, mmmmmm sooooo goooooood{/i}"
    "Just down the hallway is Sayori, who appears to be gorging on snacks from the vending machine."
    show sayori flus om oe at f22
    s "Oh O_O"
    s "Don't mind me you guys."
    show sayori ce cm happ
    s "Just having my lunch."
    "It is 10:48am."
    show sayori at thide
    hide sayori

    play music t9

    show monika at t11
    m "..."
    show monika lpoint at f11
    m "Let's go for a walk [player]."

    scene bg residential_day
    show monika forward at t22
    with dissolve_scene_full
    m "Wow...."
    show monika ce
    m "I'm so sorry she said that to you [player]."
    show monika oe
    m "That's totally messed up."
    show monika forward lpoint at f22
    # yes this is the wrong word on purpose, its an inside joke
    m "If it's any constellation, for the record. I totally like black people."
    show monika forward ldown at t11
    mc "Thanks Monika. That means alot coming from you."
    show monika forward happ om ce at f11
    m "My house is just around the corner, how about you come over?"
    show monika oe
    m "I know just the thing to make you feel better."

    scene bg kitchen
    with dissolve_scene_full
    stop music fadeout 6.7
    "We step into Monika's home, and she leads me towards her bedroom."
    scene bg bedroom
    with dissolve_scene_full
    mc "Wow you've got a pretty nice bedroom Monika!"
    m "..."
    mc "Monika?"
    scene black
    with dissolve 
    "She pulls out a {b}wooden cylinder-shaped object{/b}."
    with dissolve_scene_full

    "The End."

    $ MainMenu(confirm=False)() 
#COMPLETED!!!!! :D
