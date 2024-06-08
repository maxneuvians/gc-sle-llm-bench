import anthropic

from data import answer_questions
from prompts import (
    generate_system_prompt,
    generate_incorrect_prompt,
    generate_missing_prompt,
)

client = anthropic.Anthropic()


def ask_incorrect_question(question, lang):
    resp = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        temperature=0.0,
        system=generate_system_prompt(lang),
        messages=[
            {"role": "user", "content": generate_incorrect_prompt(lang, question["question"], question["answers"])}
        ]
    )
    return resp.content[0].text


def ask_missing_question(question, lang):
    resp = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        temperature=0.0,
        system=generate_system_prompt(lang),
        messages=[
            {"role": "user", "content": generate_missing_prompt(lang, question["question"], question["answers"])}
        ],
    )
    return resp.content[0].text


def main(set=1):
    total, correct_count, incorrect_count = answer_questions(
        ask_incorrect_question, ask_missing_question, "claude-3-opus", "en", set, 2
    )
    print(f"Total: {total} | Correct: {correct_count} | Incorrect: {incorrect_count}")
    print(f"Accuracy: {correct_count / (correct_count + incorrect_count) * 100:.2f}%")


if __name__ == "__main__":
    main()
