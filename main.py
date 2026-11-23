print("""================================
Welcome to Friend Introduction!

Version 0.2 - I Got Ur Loop
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
2. Goodbye

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
        print("Oh, see you again!")
        break
    else:
        print("Noooooooo, you're breaking my baby code T_T\n")
