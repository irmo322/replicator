import random


all_characters = {"Willy", "Fast", "Bottom", "Giuletta", "Richard", "Lady Beth",
                  "Le juriste", "Le clergyman", "Le scientifique", "Le psychiatre", "Le mondain",
                  "Didascalie"}


def check_scene(scene_number):
    print(f"scene {scene_number}")

    with open(f"transcriptions/scene_{scene_number}.txt") as f:
        file_lines = [line.strip() for line in f.readlines()]

    theatrical_lines = []
    new_character = True
    for file_line in file_lines:
        if not file_line:
            new_character = True
        elif file_line[0] != "#":
            if new_character:
                theatrical_lines.append({"character": file_line, "lines": []})
                new_character = False
            else:
                theatrical_lines[-1]["lines"].append(file_line)

    characters = set([plop["character"] for plop in theatrical_lines])

    print(f"Characters : {characters}")

    assert characters.issubset(all_characters)

    # while True:
    #     chosen_character = input("Choose character : ")
    #     if chosen_character not in characters:
    #         print(f"{chosen_character} is not available.")
    #     else:
    #         break
    #
    # totos = [(i, j)
    #          for i, plop in enumerate(theatrical_lines) if plop["character"] == chosen_character
    #          for j, line in enumerate(plop["lines"])]
    # while True:
    #     input("\nAppuie sur Enter pour un nouveau test...")
    #
    #     i, j = random.choice(totos)
    #
    #     if i > 0:
    #         plop = theatrical_lines[i-1]
    #         print("**", plop["character"], "**")
    #         lines = plop["lines"]
    #         if len(lines) > 3:
    #             lines = ["[...]"] + lines[-3:]
    #         print(*lines, sep="\n")
    #
    #     plop = theatrical_lines[i]
    #     print("**", plop["character"], "**")
    #     print(*plop["lines"][:j], sep="\n")
    #
    #     input("Appuie sur Enter pour vérifier ce qui vient ensuite...")
    #
    #     print(plop["lines"][j])


def main():
    for scene_number in range(1, 20):
        if scene_number == 4:
            continue
        check_scene(scene_number)


if __name__ == '__main__':
    main()
