import cohere

from data import answer_questions
from prompts import generate_system_prompt, generate_incorrect_prompt, generate_missing_prompt

co = cohere.Client()


def ask_incorrect_question(question, lang):
    resp = co.chat(
        preamble=generate_system_prompt(lang),
        message=generate_incorrect_prompt(
            lang,
            question["question"],
            question["answers"]
        ),
        temperature=0.0
        )
    return resp.text


def ask_missing_question(question, lang):
    resp = co.chat(
        preamble=generate_system_prompt(lang),
        message=generate_missing_prompt(
            lang,
            question["question"],
            question["answers"]
        ),
        temperature=0.0
        )
    return resp.text


def main(set=1):
    total, correct_count, incorrect_count = answer_questions(
        ask_incorrect_question,
        ask_missing_question,
        "cohere",
        "fr",
        set,
        5
    )
    print(f"Total: {total} | Correct: {correct_count} | Incorrect: {incorrect_count}")
    print(f"Accuracy: {correct_count / (correct_count + incorrect_count) * 100:.2f}%")


if __name__ == "__main__":
    main()
