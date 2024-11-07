import re
from openai import OpenAI
from data import answer_questions
from prompts import (
    generate_system_prompt,
    generate_incorrect_prompt,
    generate_missing_prompt,
)


client = OpenAI()


def ask_incorrect_question(question, lang):
    resp = client.chat.completions.create(
        messages=[
            {"role": "system", "content": generate_system_prompt(lang)},
            {
                "role": "user",
                "content": generate_incorrect_prompt(
                    lang, question["question"], question["answers"]
                ),
            },
        ],
        model="gpt-4o-mini",
        temperature=0.0,
    )
    return re.findall("\d+", resp.choices[0].message.content)[0]


def ask_missing_question(question, lang):
    resp = client.chat.completions.create(
        messages=[
            {"role": "system", "content": generate_system_prompt(lang)},
            {
                "role": "user",
                "content": generate_missing_prompt(
                    lang, question["question"], question["answers"]
                ),
            },
        ],
        model="gpt-4o-mini",
        temperature=0.0,
    )
    return re.findall("\d+", resp.choices[0].message.content)[0]


def main(set=1):
    total, correct_count, incorrect_count = answer_questions(
        ask_incorrect_question, ask_missing_question, "openai4o-mini", "fr", set
    )
    print(f"Total: {total} | Correct: {correct_count} | Incorrect: {incorrect_count}")
    print(f"Accuracy: {correct_count / (correct_count + incorrect_count) * 100:.2f}%")


if __name__ == "__main__":
    main()
