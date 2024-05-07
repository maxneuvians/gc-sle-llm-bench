

def generate_incorrect_prompt(lang, question, options):
    if lang == 'fr':
        return f'''Identifier les erreurs – Votre tâche consiste à identifier laquelle des sections soulignées comporte une ou plusieurs erreurs. Si aucune des sections soulignées ne comporte une ou plusieurs erreurs, choisissez l’option 4, « aucune correction ». Ne renvoie que le numéro de l'option, pas l'option elle-même. Par exemple, retourne la valeur 4 pour « aucune correction »

Question: {question}

1. {options[0]}
2. {options[1]}
3. {options[2]}
4. {options[3]}

'''
    else:
        return f'''Which of the underlined sections contains one or more errors? If there are no errors,select "none of the above". Returns only the option number, not the option itself. For example, returns the value 4 for "none of the above".

Question: {question}

1. {options[0]}
2. {options[1]}
3. {options[2]}
4. {options[3]}

'''


def generate_missing_prompt(lang, question, options):
    if lang == 'fr':
        return f'''Quel mot ou groupe de mots complète le mieux le texte? Ne renvoie que le numéro de l'option, pas l'option elle-même.

Question: {question}

1. {options[0]}
2. {options[1]}
3. {options[2]}
4. {options[3]}

'''
    else:
        return f'''Choose the best group of words to insert into the blank. Return only the option number, not the option itself.

Question: {question}

1. {options[0]}
2. {options[1]}
3. {options[2]}
4. {options[3]}

'''     


def generate_system_prompt(lang):
    if lang == 'fr':
        return "You are an expert at answering multiple choice questions related to french grammar. You will be presented with a multiple choice question that has four answers (1-4). Read the question and the answers and then return the number of the answer that fits the best. For example, if you receive for options 1. a, 2. b, 3. c, 4. d, and you think the answer is b, you should return 2"
    else:
        return "You are an expert at answering multiple choice questions related to english grammar. You will be presented with a multiple choice question that has four answers (1-4). Read the question and the answers and then return the number of the answer that fits the best. For example, if you receive for options 1. a, 2. b, 3. c, 4. d, and you think the answer is b, you should return 2"
    

if __name__ == "__main__":
    print("------------------- EN PROMPTS -------------------")
    print(generate_system_prompt("en"))
    print("\n")
    print(generate_incorrect_prompt("en", "What is the capital of France?", ["Paris", "London", "Berlin", "Madrid"]))
    print("\n")
    print(generate_missing_prompt("en", "What is the capital of France?", ["Paris", "London", "Berlin", "Madrid"]))
    print("------------------- FR PROMPTS -------------------")
    print(generate_system_prompt("fr"))
    print("\n")
    print(generate_incorrect_prompt("fr", "Quelle est la capitale de la France?", ["Paris", "Londres", "Berlin", "Madrid"]))
    print("\n")
    print(generate_missing_prompt("fr", "Quelle est la capitale de la France?", ["Paris", "Londres", "Berlin", "Madrid"]))