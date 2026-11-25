import time
import random
# ============ INVALID MESSAGES ============
invalid_messages = [
    "Booooo, you chose the invalid option.\n:P :P :P",
    "Error 404: Common sense not found.",
    "You discovered a secret option.\nSadly, it contains nothing.",
    "I have no idea what option that is.\nCongratulations on discovering new mathematics.",
    "Please enter a valid option.\nThe program is trying its best.",
    "Congratulations.\nYou have selected Optionn't.",
    "The option you're looking for is studying abroad.",
    "Task failed successfully.",
    "Please try again.\nPreferably with less innovation.",
    "This message has a 0.1% chance of appearing.\nI lied. But please type the correct value!",
    "WRONGGG.\nIf you're stuck, you gotta type exactly as it is! 1, 2, or A, B, C like that.",
]
# ============ PAUSES ============
def short_pause():
    time.sleep(0.8)
    
def medium_pause():
    time.sleep(1.4)
    
def long_pause():
    time.sleep(2)
    
def stop():
    input("\n[Type anything to continue]\n")
    
def back_menu():
    input("\n[Type anything to return to main menu...]\n")
    print("Returning to main menu...")
    short_pause()
# ============ GOODBYE ============
def goodbye():
    print("Oh, see you again!")
# ============ COMPATIBILITY QUIZ ============
COMP_QUESTIONS = [
    {
        "num": 1,
        "text": "Which type of movie sounds most appealing?\n\nA. Action-packed movies\nB. Thrillers, mysteries, and psychological games\nC. Slow-paced documentaries and slice-of-life stories",
        "jake_comp": "A and B",
        "explanation": "I like movies that keep me engaged.\nExplosions are cool.\nMysteries are cool.\nPlease don't make me watch paint dry for two hours.",
        "valid": ["a", "b"],
        "allowed": ["a", "b", "c"]
    },
    {
        "num": 2,
        "text": "Which type of game sounds most appealing?\n\nA. Competitive multiplayer games\nB. Sandbox / creative games\nC. Story-driven adventures",
        "jake_comp": "C",
        "explanation": "I enjoy games with a direction.\nExploration is fun.\nKnowing why I'm moving forward is even better.",
        "valid": ["c"],
        "allowed": ["a", "b", "c"]
    },
    {
        "num": 3,
        "text": "What kind of music do you listen to?\n\nA. Pop\nB. Instrumental\nC. Rock\nD. Classical\nE. Other",
        "jake_comp": "All of the above",
        "explanation": "My music taste behaves more like a tourist\nthan a permanent resident.\n\nIf it sounds good, it enters the playlist.",
        "valid": ["a", "b", "c", "d", "e"],
        "allowed": ["a", "b", "c", "d", "e"]
    },
    {
        "num": 4,
        "text": "Which working style sounds more appealing?\n\nA. Working alone\nB. Working with a team",
        "jake_comp": "B",
        "explanation": "I enjoy teamwork more than people expect.\n\nThe challenge isn't teamwork.\nIt's finding a good team.",
        "valid": ["b"],
        "allowed": ["a", "b"]
    },
    {
        "num": 5,
        "text": "What makes a friendship valuable?\n\nA. Having fun together\nB. Being there when needed\nC. Trust and honesty\nD. Shared experiences",
        "jake_comp": "All of the above",
        "explanation": "Friendships aren't optimization problems.\n\nYou don't maximize one variable.\nThey're all important.",
        "valid": ["a", "b", "c", "d"],
        "allowed": ["a", "b", "c", "d"]
    },
    {
        "num": 6,
        "text": "What would you most likely forget before a trip?\n\nA. Phone\nB. Charger\nC. Money\nD. ID Card\nE. Airpods",
        "jake_comp": "D",
        "explanation": "I'm always telling myself that I prepared the IDs.\nAnd then forgot one of them. And encountered 101 problems and criticisms.\n\nPlease remind me twice before going out anytime.\nI'm working on it, I promise! I'll remind you too :D",
        "valid": ["d"],
        "allowed": ["a", "b", "c", "d", "e"]
    },
    {
        "num": 8,
        "text": "You find two options. What would you choose?\n\nA. More expensive but slightly better\nB. Cheaper but still acceptable",
        "jake_comp": "B",
        "explanation": "I usually try to maximize value.\nYou could see me stretching my wallet like bubble gums.\n\nIt isn't always as sweet as bubble gums, though.",
        "valid": ["b"],
        "allowed": ["a", "b"]
    },
    {
        "num": 9,
        "text": "What would a shared room with you probably look like?\n\nA. Extremely organized\nB. Organized chaos\nC. Self-disaster only\nD. Complete mess",
        "jake_comp": "C",
        "explanation": "I usually mess up my room a lot.\n\nBut I often try to keep that disorganization to myself.\nI value public places :P\nYeah I'll keep the living room tidy.",
        "valid": ["c"],
        "allowed": ["a", "b", "c", "d"]
    },
    {
        "num": 10,
        "text": "Which sounds most satisfying?\n\nA. Solving a difficult problem\nB. Creating something useful\nC. Roast someone playfully\nD. Eating good food",
        "jake_comp": "All of the above",
        "explanation": "This question is a free pass.\nI genuinely enjoy all four.",
        "valid": ["a", "b", "c", "d"],
        "allowed": ["a", "b", "c", "d"]
    }
]
def reflective_question(num, text, jake_refl, explanation):
    while True:
        answer_refl = input(f"{num}. {text}\n> ").strip().lower()

        if answer_refl in ["a", "b", "c", "d"]:
            break
        print(random.choice(invalid_messages))
        short_pause()
        print("\nPlease choose a valid option or this will go on forever.\n")
        short_pause()

    print("\n-------- RESULT --------\n")
    short_pause()
    print(f"Your answer: {answer_refl.upper()}")
    short_pause()
    print(f"Jake's answer: {jake_refl.upper()}")
    short_pause()
    
    print(explanation)
    long_pause()
    
def compatibility_question(num, text, jake_comp, explanation, valid_answers, allowed):
    while True:
        answer_comp = input(f"{num}. {text}\n> ").strip().lower()

        if answer_comp in [al.lower() for al in allowed]:
            break
        print(random.choice(invalid_messages))
        short_pause()
        print("\nPlease choose a valid option or this will go on forever.\n")
        short_pause()

    print("\n-------- RESULT --------\n")
    short_pause()
    print(f"Your answer: {answer_comp.upper()}")
    short_pause()
    print(f"Jake's answer: {jake_comp.upper()}")
    short_pause()

    if answer_comp in [v.lower() for v in valid_answers]:
        print("\n[✓] Compatibility point earned!\n")
        point = 1
        short_pause()
    else:
        print("\n[X] No compatibility point this time.\n")
        point = 0
        short_pause()

    print(explanation)
    long_pause()
    return point

def test():
    print("[✓] Friend Manual selected!")
    print("Loading compatibility test...\n")
    medium_pause()

    print("""Here's a quiz of some other random stuff I do.
Let's see if we are any compatible!
(P/s it doesn't matter that much tbh)
""")
    long_pause()
    current_score = 0
    
    for q in COMP_QUESTIONS[:6]:
        current_score += compatibility_question(
            num=q["num"],
            text=q["text"],
            jake_comp=q["jake_comp"],
            explanation=q["explanation"],
            valid_answers=q["valid"],
            allowed=q["allowed"]
        )
        stop()
        
    reflective_question(
        7,
        """If given unlimited time and resources, what would you most likely create?

A. A successful, worldwide business
B. Useful projects and tools
C. Laughter stuff
D. Something personal""",
        "???",
        """Honestly, I don't know yet.\n\nI'm entering a new chapter of life, and I haven't fully figured out what I want to do.\n\nMaybe that's okay.\n\nFor now, I'm exploring the options I have.\nYou could also explore with me if you want to :P"""
    )
    stop()
    
    for q in COMP_QUESTIONS[6:]:
        current_score += compatibility_question(
            num=q["num"],
            text=q["text"],
            jake_comp=q["jake_comp"],
            explanation=q["explanation"],
            valid_answers=q["valid"],
            allowed=q["allowed"]
        )
        stop()

    print("Calculating compatibility score...")
    long_pause()
    print(f"Compatibility Score: {current_score}/9")
    short_pause()

    if current_score <= 3:
        print("\nInteresting.\n\nOne of us may be an alien.\n")
    elif current_score <= 5:
        print("\nNot bad.\n\nFurther friendship testing recommended.\n")
    elif current_score <= 7:
        print("\nPretty compatible.\n\nDon't take my place though.\n")
    else:
        print("\nWarning.\n\nPossible duplicate Jake detected.\n")
    short_pause()
    print("""[✓] Compatibility test finished!
Thank you for participating in the official Jake compatibility assessment.

I believe we all have similarities and differences.
But hey, that's what make us special, right?
Check out the other menus if you haven't! Or do the quiz again :3""")
    long_pause()
    back_menu()
# ============ BEHAVIORS ============
def question(num, text, jake_answer, reaction_a, reaction_b, reaction_c):
    while True:
        answer = input(f"{num}. {text} ").lower().strip()
        if answer in ["a", "b", "c"]:
            break
        print(random.choice(invalid_messages))
        short_pause()
        print("\nPlease choose A, B, or C or this will go on forever.\n")
        short_pause()
    short_pause()
    print("\n----- COMPARISON -----\n")
    short_pause()
    print(f"Your answer: {answer.upper()}")
    short_pause()
    print(f"Jake's answer: {jake_answer}")
    short_pause()

    if answer == "a":
        print(reaction_a)
    elif answer == "b":
        print(reaction_b)
    else:
        print(reaction_c)
        
def behaviors():
    print("[✓] Behaviors selected!")
    print("Comprehensing Jake's actions...\n")
    medium_pause()

    print("""You're gonna answer some questions about behaviors with me.
It'll be useful to get to know some of my basic human functions :D""")
    medium_pause()
    stop()
    
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
    long_pause()
    stop()
    
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
    long_pause()
    stop()
    
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
    long_pause()
    stop()
    
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

    long_pause()
    stop()
    
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
    "-> Honestly, this works more often than I thought. A rest can help a lot."
    )
    long_pause()
    stop()
    
    print("""Congratulations. You have successfully completed the behavior test.

I don't know what you answered, but since this is
a program to get to know me, it doesn't matter :P.

Oh, you can also try as many options as you want.
They have different responses :3""")
    long_pause()
    back_menu()
# ============ HOBBIES ============
def hobbies():
    print("[✓] Hobbies selected!")
    print("Jake has a lot of hobbies...\n")
    medium_pause()
    
    while True:       
        hobby_choice = input("""Choose a hobby below to read more:
    
2.1 Photography
2.2 Cooking
2.3 Sleeping
2.4 Exit

Option: """).strip()
        if hobby_choice == "2.1":
            print("""I enjoy taking photos, especially landscapes.
My walking speed decreases by approximately 90%
whenever the landscape becomes interesting.
Please be patient.
Also I really like to propose photography ideas for people.""")
            long_pause()
            stop()
                
        elif hobby_choice == "2.2":
            print("""I have been cooking since I was 6.
If someone urges me to cook, my motivation drops significantly.
If I choose to cook, I become 999% focused.
The food choice can be questionable
but most of the time it tastes good.""")
            long_pause()
            stop()
        elif hobby_choice == "2.3":
            print("""...
...
zzz...

Yes, I enjoy sleeping.
Unfortunately, sleep schedule and I are
currently in a long-distance relationship.""")
            long_pause()
            stop()
        elif hobby_choice == "2.4":
            print("See you again! You can check this menu again too.")
            print("Returning to main menu...")
            short_pause()
            break
        else:
            print(random.choice(invalid_messages))
            short_pause()
# ============ BACKGROUND ============ 
def background():
    print("[✓] Background selected!")
    print("Loading Jake's background...\n")
    medium_pause()
    
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
    long_pause()
    back_menu()
# ============ MENU ============
def menu():
    while True: 
        choice = input("""
Choose what you want to know about me:

1. Background
2. Hobbies
3. Behaviors
4. Friend Manual
5. Goodbye

Option: """).strip()
    
        if choice == "1":
            background()
        elif choice == "2":
            hobbies()
        elif choice == "3":
            behaviors()
        elif choice == "4":
            test()
        elif choice == "5":
            goodbye()
            break
        else:
            print(random.choice(invalid_messages))
            short_pause()
# ============ INTRODUCTION ============
def introduction():
    print("""================================
Welcome to Friend Introduction!

Version 0.7 - Behavioral Revamp
================================""")
    
    user_name = input("Please enter your name here:\n")
    print("Verifying your name...")
    medium_pause()
    print(f"""Hello there, {user_name}!
My name is Dang, but you can call me Jake.
""")
    long_pause()

    print("""I know it's pretty hard to introduce ourselves and
get to know each other without being awkward.
""")
    long_pause()

    print("""So I made this little program so you can get to know me first!
Believe me this is not malware T-T
(Right???)

So if you're ready...""")
    long_pause()
    menu()
# ============ START THE GAME! ============
introduction()
