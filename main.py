def goodbye():
    print("Oh, see you again!")
# ============ FUN FACTS ============
def funs():
    print("""Here are some fun facts about me :3

- I like action-oriented video games
- I also like action-oriented movies, with some thrill involved
- I can be a little harsh on money spending at times
- I can be forgetful at times, but I'm working on it
- I often need a change of space to work, so you
wouldn't see me in the same place too often :P

Let's see how similar we are to each other!""")
# ============ BEHAVIORS ============
def question(num, text, jake_answer, reaction_a, reaction_b, reaction_c):
    while True:
        answer = input(f"{num}. {text} ").lower().strip()
        if answer in ["a", "b", "c"]:
            break
        print("\nPlease choose A, B, or C or this will go on forever.\n")
        
    print("\n----- COMPARISON -----\n")
    print(f"Your answer: {answer.upper()}")
    print(f"Jake's answer: {jake_answer}")

    if answer == "a":
        print(reaction_a)
    elif answer == "b":
        print(reaction_b)
    else:
        print(reaction_c)
        
def behaviors():

    print("""\nYou're gonna answers some questions about behaviors with me.
It'll be useful to get to know some of my basic human functions :D""")
    
    question(
    1,
    """When learning something new, you usually:

A. Read theory and understand it first.
B. Start trying things immediately.
C. Alternate between theory and practice.
->""",
    "B",
    "-> Interesting. I usually get impatient if I stay in theory for too long 😭",
    "-> Yep, same. I like to try things first and figure things out along the way.",
    "-> Honestly, that's probably the healthiest approach."
    )
            
    question(
    2,
    """In a new group of people, you usually:

A. Observe first and speak when comfortable.
B. Start conversations and meet people quickly.
C. Depends on the group and the vibe.
->""",
    "C",
    "-> I can be like that too. Sometimes I need a bit of time to understand the vibe.",
    "-> That's braver than me 🤣 I don't usually walk into a room and start collecting friends.",
    "-> Same. My social mode changes a lot depending on who's around."
    )
            
    question(
    3,
    """Which type of behavior bothers you most?

A. Arrogance and looking down on others.
B. Constant negativity and complaining.
C. Dishonesty and talking behind people's backs.
->""",
    "A",
    "-> Same. People acting superior for no reason drains my battery surprisingly fast.",
    "-> I get that too. A little complaining is fine, but endless negativity gets exhausting.",
    "-> Yeah... Trust is really important in any friendship."
    )
            
    question(
    4,
    """What usually motivates you to do something?

A. A clear goal or achievement.
B. Curiosity and interest.
C. Responsibility to other people.
->""",
    "B",
    "-> Goals help, but they're usually not enough by themselves for me.",
    "-> Yep. Curiosity is ridiculously effective on me. \nOne random idea can consume my entire afternoon.",
    "-> Helping people is also motivating for me. I like feeling useful."
    )
            
    question(
    5,
    """When facing a difficult problem, you usually:

A. Keep trying different approaches.
B. Ask someone for help.
C. Take a break and return later.
->""",
    "A",
    "-> Same. I tend to poke problems with a stick until they reveal what they're hiding. 🤓",
    "-> I should probably do this more often. \nAsking for help isn't exactly my first instinct.",
    "-> Honestly, this works more often than I thought. A reset can help a lot."
    )

    print("""
Congratulations. You have successfully completed the behavior test.

I don't know what you answered, but since this is
a program to get to know me, it doesn't matter :P.

Oh, you can also try as many options as you want.
They have different responses :3""")
# ============ HOBBIES ============
def hobbies():
    while True:
        hobby_choice = input("""Choose a hobby below to read more:
    
2.1 Photography
2.2 Cooking
2.3 Sleeping
2.4 Exit

Option: """)
        if hobby_choice == "2.1":
            print("""I enjoy taking photos, especially landscapes.
My walking speed decreases by approximately 90%
whenever the landscape becomes interesting.
Please be patient.
Also I really like to propose photography ideas for people.
""")
                
        elif hobby_choice == "2.2":
            print("""I have been cooking since I was 6.
If someone urges me to cook, my motivation drops significantly.
If I choose to cook, I become 999% focused.
The food choice can be questionable
but most of the time it tastes good.
""")

        elif hobby_choice == "2.3":
            print("""...
...
zzz...

Yes, I enjoy sleeping.
Unfortunately, sleep schedule and I are
currently in a long-distance relationship.
""")

        elif hobby_choice == "2.4":
            print("See you again! You can check this menu again too.")
            break
        else:
            print("Noooooooo, you're breaking my baby code T-T\n")
# ============ BACKGROUND ============ 
def background():
    print("""Hello! My name is Dang (also known as Jake).

After surviving:
- 12 years of school,
- Several clubs,
- Photography duties,
- Leadership positions,
- Regional English competitions,
- Approximately 47 forms and essays,

I somehow ended up at Purdue University studying Data Science.
Nobody is entirely sure how. Not even me.

I was originally pushed toward STEM by my parents.
Meanwhile, I spent a suspicious amount of time carrying cameras, taking photos
and wondering whether I should secretly become a filmmaker.

Eventually I discovered that statistics, probability, logic
and asking "but why?" are actually pretty fun.

Calculus and I maintain a ceasefire (for now). Please don't question.""")
# ============ MENU ============
def menu():
    while True: 
        choice = input("""
Choose what you want to know:

1. Background
2. Hobbies
3. Behaviors
4. Fun Facts
5. Goodbye

Option: """).strip()
    
        if choice == "1":
            background()
        elif choice == "2":
            hobbies()
        elif choice == "3":
            behaviors()
        elif choice == "4":
            funs()
        elif choice == "5":
            goodbye()
            break
        else:
            print("Noooooooo, you're breaking my baby code T-T\n")
# ============ INTRODUCTION ============
def introduction():
    print("""================================
Welcome to Friend Introduction!

Version 0.7 - Behavioral Revamp
================================""")
    user_name = input("Please enter your name here:\n")
    print(f"""Hello there, {user_name}!
My name is Dang, but you can call me Jake.

I know it's pretty hard to introduce ourselves and
get to know each other without being awkward.

So I made this little program so you can get to know me first!
Believe me this is not malware T-T
(Right???)

So if you're ready...""")
    menu()
# ============ START THE GAME! ============
introduction()
