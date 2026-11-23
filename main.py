print("""================================
Welcome to Friend Introduction!

Version 0.3 - Hobby Hub
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
while True: 
    choice = input("""
Choose what you want to know:

1. Background
2. Hobbies
3. Goodbye

Option: """).strip()
    if choice == "1":
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
    elif choice == "2":
        while True:
            hobby_choice = input("""Choose a hobby below to read more:

2.1 Photography
2.2 Cooking
2.3 Sleeping
2.4 Exit

Option: """)
            if hobby_choice == "2.1":
                print(""" I enjoy taking photos, especially landscapes.
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
                
    elif choice == "3":
        print("Oh, see you again!")
        break
    else:
        print("Noooooooo, you're breaking my baby code T-T\n")
