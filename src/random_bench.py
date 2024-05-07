from random import randrange
from data import answer_questions


def ask_incorrect_question(question, lang):
    return str(randrange(1, 5))


def ask_missing_question(question, lang):
    return str(randrange(1, 5))


def main(set=1):
    total, correct_count, incorrect_count = answer_questions(
        ask_incorrect_question, ask_missing_question, "random", "fr", set
    )
    print(f"Total: {total} | Correct: {correct_count} | Incorrect: {incorrect_count}")
    print(f"Accuracy: {correct_count / (correct_count + incorrect_count) * 100:.2f}%")


if __name__ == "__main__":
    main()
