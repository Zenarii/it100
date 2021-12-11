from random import randint, choice

#sourced from https://commonlyusedwords.com/words/italian/top-100-italian-words/ on 11/12/21
italian_dict = { "il" : "the",
                 "di" : "of",
                 "e" : "and",
                 "essere" : "to be",
                 "in" : "in",
                 "che" : "that",
                 "del" : "of the",
                 "a" : "to",
                 "avere" : "to have",
                 #"della" : "of the",
                 "per" : "for",
                 "non" : "not",
                 "un" : "a",
                 "potere" : "can",
                 "con" : "with",
                 "da" : "by",
                 "fare" : "to make",
                 "al" : "to the",
                 "dire" : "to say",
                 #delle : "of the",
                 "piu" : "more", #note: removed accent on u
                 "o" : "or",
                 "nella" : "in the",
                 "ma" : "but",
                 "anche" : "also",
                 "venire" : "to come",
                 "dal" : "by the",
                 "cui" : "which",
                 "dovere" : "to have to",
                 "come" : "as",
                 #"degli" : "of him",
                 "loro" : "them",
                 "dare" : "to give",
                 #"dalla" : "by the",
                 "ai" : "to the",
                 "parte" : "part",
                 "andare" : "to go",
                 "due" : "two",
                 "questo" : "this",
                 "alle" : "to the",
                 "tra" : "between",
                 "quale" : "which",
                 "vedere" : "to see",
                 #"nelle" : "in the",
                 "ogni" : "each",
                 "parlare" : "to talk",
                 "ne" : "of it",
                 "gia" : "already", #note: removed accent on a
                 "pensare" : "to think",
                 #"fra" : "between",
                 "tempo" : "time",
                 "ano" : "year",
                 "cosi": "so",
                 "trovare" : "to find",
                 "poi" : "then",
                 "modo" : "way",
                 "mi" : "me",
                 "ottenere" : "to get",
                 "anora" : "still",
                 "quando" : "when",
                 "partire" : "to leave",
                 "vita" : "life",
                 "tutti" : "all",
                 "quanto" : "how much",
                 #"cio" : "that", #note: removed accent on o
                 "caso" : "case",
                 "mettre" : "to put",
                 "perche" : "why", #note: removed accent on e
                 "prendere" : "to take",
                 "qui" : "here",
                 "Roma" : "Rome",
                 "Italia" : "Italy",
                 "altro" : "other",
                 "primo" : "first",
                 "lavoro" : "work",
                 "vivere" : "to live",
                 "molto" : "much",
                 "col" : "with the",
                 "lui" : "him",
                 "meno" : "less",
                 "contro" : "against",
                 "ricordare" : "to remember",
                 "qualche" : "some" ,
                 "grande" : "big",
                 "passare" : "to pass",
                 "dove" : "where"}
                    

needed_to_win = 10
score = 0

while score < needed_to_win:
    # 0 is false, 1 is true
    word_is_italian = randint(0, 1)

    was_correct = False
    italian = ""
    english = ""

    italian, english = choice(list(italian_dict.items()))
    if word_is_italian:
        print(italian, " (", score, "/", needed_to_win, ")", sep="")
        user_attempt = input(">").rstrip()
        was_correct = True if user_attempt == english else False
    else:
        print(english, " (", score, "/", needed_to_win, ")", sep="")
        user_attempt = input(">").rstrip()
        was_correct = True if user_attempt == italian else False

    if was_correct:
        print("CORRECT")
        score += 1
    else:
        if word_is_italian:
            print(italian, "is", english, "in english.")
        else:
            print(english, "is", italian, "in italian.")
