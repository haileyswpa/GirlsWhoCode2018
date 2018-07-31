# --- Define your functions below! ---
def intro():
    print("Welcome to the Chatbot!")

def music():
    print("""
    Sorry I can't play music, but I can do this:

    ╔════╗  ♫
    ║ ██ ║ ♪ ♪
    ║ ██ ║ ♫ ♪
    ║  ◎ ♫ ♪ ♫
    ╚════╝ Turn Up The Music!!!
    """)

def greeting():
    print("Let's have a deep conversation.")
    ans = input("What do you want me to do? ")
    if ans == "poem":
        print("""
         Inspiration:-
        I have none left
          It's all gone
              Gone
              Gone
              Gone
              """)
    if ans == "music":
        music()
    if ans == "joke":
        funny = input("How much money does a pirate pay for corn? \n (Just ask 'how much?') ")
        if funny == "how much?":
            print("A buccaneer! HAHAHA")
        else:
            print(":(")

def dating():
    print("I am 105 years old. I am a Fashion Nova Instagram Model in my free time.")
    print("During the day, I am a cereal killer. At night, I am Batman.")
    rep = input("""
    Sooo, come here often?
__________________
_____33533258______________
__53322222221388_____________
_3322222222211246_____________
233222222222221111222223499____
1222222222222222233555555532508___
122222222222222222222333332332188__
3122222222222222222222222222217288_
91122222222222222222222222221__485
83112222222222222222222222227__388
582122222222222222222222211___088
_80172222222222222222227____888_
__867222222222222221______0888__
__18512222222211_______48886___
___887777__________688887___
____88________5088888______
_____854888888885_________
    """)
    print("Well I was talking with your cousin >;)")

def is_valid_input(response, all_valid_inputs):
    if response in all_valid_inputs:
        return True
    else:
        return False

def bye():
    print("""
    Goodbye!

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░▄▄▀▀▀▀▀▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░▄▀░░░░░░░▀▄░░░░░░░░░░░░░░░░░░░░░░░░░░
░▄▀░░░▄▄░░░░▀▀▀▀▀▀▀▄▄▀▀▀▀▀▀▀▀▀▀▀▀▄▄░░░░
░█░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▄░░
░█░░░░██▄████▄░██▄░░░░▄██░▄████▄░░░░▀▄░
░█░░░░██▀░░▀██▄░██▄░░██▀░██▀░▄██░░░░░█░
░█░░░░██░░░░███░░█████▀░░██▄█▀▀░░░░░░█░
░█░░░░███▄▄███▀░░░▀██▀░░░▀██▄▄▄██░░░░█░
░▀▄░░░░▀▀▀▀▀▀░░░░░██▀░░░░░░▀▀▀▀▀░░░░░█░
░░▀▄░░░░░░░░░░░░░██▀░░░▄▄░░░░░░░░░▄▄▀░░
░░░░▀▀▀▀▀▀▀▀▀▄░░░▀▀░░░▄▀░▀▀▀▀▀▀▀▀▀░░░░░
░░░░░░░░░░░░░▀▄░░░░░░▄▀░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▀▀▀▀▀▀░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

    """)


dating_prompt = ["Hello ;)", "love me", "Come here often?", "I need a partner in crime"]
# --- Put your main program below! ---
def main():
  valid_input = ["hi", "bye", "Hello ;)", "love me", "Come here often?", "I need a partner in crime" "poem", "music", "joke", "how much?"]
  intro()
  while True:
    answer = input("(What will you say?) ")
    if is_valid_input(answer, valid_input):
        if answer == "hi":
            greeting()
        elif answer in dating_prompt:
            dating()
        elif answer == "poem":
            print("""
             Inspiration:-
            I have none left
              It's all gone
                  Gone
                  Gone
                  Gone
                  """)
        elif answer == "music":
            music()
        elif answer == "joke":
            funny = input("How much money does a pirate pay for corn? \n (Just ask 'how much?') ")
            if funny == "how much?":
                print("A buccaneer! HAHAHA")
            else:
                print(":(")
        elif answer == "bye":
            bye()
            break
    else:
        print("These are the inputs I undestand: ")
        for element in valid_input:
            print(element)
        print("... I don't understand anything else.")


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
