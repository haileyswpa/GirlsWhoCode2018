#Write a function, translate_shorthand, that replaces shorthand such as "ttyl" with "talk to you later".

def translate_shorthand(dictionary):
    for key, value in sorted(dictionary.items()):
        print(key, value)

shorthand = {
"gr8" : "great"
"slap" : "sounds like a plan",
"nvm" : "nevermind",
"ft" : "facetime",
"gl" : "good luck",
"gtg" : "got to go"
}

translate_shorthand(shorthand)

story = """
Stacy was texting . She said gl lol noobs suck. u wanna ft l8r ? slap . nvm i gtg eat dinner .
"""

story_list = story.split()

new_story_list = []
# Go through each word of our story
for word in story_list:
    # The word is a shorthand
    if word in shorthand.keys():
        new_story_list.append(shorthand[word])
    # The word is NOT a shorthand
    else:
        new_story_list.append(word)

print(" ".join(new_story_list))
