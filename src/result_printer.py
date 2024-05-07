import json
import os


def main():
    results = {}
    files = os.listdir("results")
    files.sort()

    for file in files:
        name = file.split(".")[0]
        with open(f"results/{file}") as f:
            content = f.read().split("\n")
            for line in content:
                if line != "":
                    data = json.loads(line)
                    if name not in results:
                        results[name] = {
                            "en": {"accuracy": [], "count": 0},
                            "fr": {"accuracy": [], "count": 0},
                        }
                    results[name][data["lang"]]["accuracy"].append(data["accuracy"])
                    results[name][data["lang"]]["count"] += 1

    print("|Model|Language|Accuracy|Count|")
    print("|---|---|---|---|")
    for model, langs in results.items():
        for lang, data in langs.items():
            print(
                f"|{model}|{lang}|{(sum(data['accuracy']) / data['count']):.2f}|{data['count']}|"
            )


if __name__ == "__main__":
    main()
