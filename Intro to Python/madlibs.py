def madlibs():
    # define function madlibs
    word = ["adjective",
            "adjective",
            "noun",
            "noun",
            "plural noun",
            "game",
            "plural noun",
            "'ing' verb",
            "'ing' verb",
            "plural noun",
            "'ing' verb",
            "noun",
            "plant",
            "part of body",
            "place",
            "'ing' verb",
            "adjective",
            "number",
            "plural noun"
            ]
    print("Let's play madlibs!")
    answer = []
#TODO: gather the input
    for element in word:
        a = input("type a(n) {} ".format(element))
        answer.append(a)
        print(a)

#TODO: output the finished madlib with the inputs you received
    print("""
    A vacation is when you take a trip to some """ + answer[0] + """ place
    with your """ + answer[1] + """ family. Usually you go to some place
    that is near a/an """ + answer[2] + """ or up on a/an """ + answer[3] + """.
    A good vacation place is one where you can ride """ + answer[4] + """
    or play """ + answer[5] + """ or go hunting for """ + answer[6] + """ . I like
    to spend my time """ + answer[7] + """ or """ + answer[8] + """.
    When parents go on a vacation, they spend their time eating
    three """ + answer[9] + """ a day, and fathers play golf, and mothers
    sit around """ + answer[10] + """. Last summer, my little brother
    fell in a/an """ + answer[11] + """ and got poison """ + answer[12] + """ all
    over his """ + answer[13] + """. My family is going to go to (the)
    """ + answer[14] + """, and I will practice """ + answer[15] + """. Parents
    need vacations more than kids because parents are always very
    """ + answer[16] + """ and because they have to work """ + answer[17] + """
    hours every day all year making enough """ + answer[18] + """ to pay
    for the vacation.
    """)

madlibs()
