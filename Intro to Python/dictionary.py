#Write a function that prints a given dict in sorted order
millennials = {
"netflix and chill  " : "we will put on a movie with no intention of watching the movie",
"spilling the tea  " : "gossip is being shared",
"woke  " : "a sudden understanding of what's really going on",
"salty  " : "agitated, angry, or upset"
}

def pretty_print_dict(dictionary):
    for key, value in sorted(dictionary.items()):
        print(key, value)

pretty_print_dict(millennials)
