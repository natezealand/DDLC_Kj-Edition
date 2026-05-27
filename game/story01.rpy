label story01_main:
    # starting scene / music copied from the original game script
    stop music fadeout 2.0
    with dissolve_scene_full

    $ restore_all_characters()
    "Ah. Another day in the paradise called Bankstown, Japan."
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    "My name is [player], and today is my 18th birthday!"
    "It's a school day today, but lets be honest... who wants to go to school on their birthday?"
    "Standing outside my house I ponder, today should i go buy more anime figures-"
    "-or play yu-gi-oh with middle aged men at a game shop?"
    "hmmmmmm..........."
    s "Heeeeeeeyyy!!"
    "Before I can decide, I see an annoying girl running towards me from the distance, waving her arms in the air like she knows me."
    show sayori 4p zorder 2 at t11
    s "Haaahhh...haaahhh..."
    mc "Oh, hey Sayori."
    $ s_name = "Sayori"
    "Sayori is my neighbour, so I really don't know why she's panting, we literally live right next door to eachother?"
    "{i}what a fatty{/i}"
    show sayori turned lsur cm ce
    s "I almost lost track of time while eating my breakfast!"
    show sayori turned lup rup oe cm happ
    s "But I caught you [player]!"
    "Sayori has been a friendly face since I moved here a couple years ago."
    "I say that, though when I first met her, I mostly just got her to pocket heal me on Marvel Rivals."
    "In actuality she's pretty shit - so I mostly stay on offline mode so that I can queue without her."
    show sayori om ce
    s "Oh my gosh!!! [player] it's your birthday!"
    s "We have to spend the day together! I've got the most perfect place we can go!!!"
    mc "It's not that book club thing is it?"
    show sayori tap cm neut oe
    s "It's not a 'book club', it's a literature club..."
    mc "Sayori...."
    mc "that really sounds like the same thing."
    mc "And besides I get all the reading I need from visual novels, why would I wanna read books?"
    

    return