import json
import time


def answer_questions(incorrect_func, missing_func, id, lang, set, sleep=0):
    answers, incorrect, missing = load_written_questions(lang, set)

    responses = {}

    total = 0
    correct_count = 0
    incorrect_count = 0

    for question in incorrect:
        total += 1
        print(f"Question {total} | Lang {lang} | Set {set} | Type: Incorrect")
        responses[str(question["id"])] = incorrect_func(question, lang)
        time.sleep(sleep)

    for question in missing:
        total += 1
        print(f"Question {total} | Lang {lang} | Set {set} | Type: Missing")
        responses[str(question["id"])] = missing_func(question, lang)
        time.sleep(sleep)

    # Loop through the reponses and grade them against the answers
    for key, value in responses.items():
        if value == str(answers[key]):
            correct_count += 1
        else:
            incorrect_count += 1

    # Append the results as a JSONL file in the results directory with the id
    f = open(f"results/{id}.jsonl", "a")
    f.write(
        json.dumps(
            {
                "id": id,
                "total": total,
                "correct": correct_count,
                "incorrect": incorrect_count,
                "accuracy": (correct_count / total * 100),
                "lang": lang,
                "set": set,
                "timestamp": int(time.time()),
            }
        )
        + "\n"
    )

    return total, correct_count, incorrect_count


def load_written_questions(lang, idx):
    f = open(f"data/written/{lang}/set{idx}/answers.json", "r")
    answers = json.load(f)
    f.close()

    f = open(f"data/written/{lang}/set{idx}/incorrect.json", "r")
    incorrect = json.load(f)
    f.close()

    f = open(f"data/written/{lang}/set{idx}/missing.json", "r")
    missing = json.load(f)
    f.close()

    return answers, incorrect, missing
