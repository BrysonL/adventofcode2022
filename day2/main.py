# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def ingest_data_pt1():
    games = []
    with open("input.txt") as file:
        for line in file:
            oppo_choice = line[0]
            if oppo_choice == 'A':
                oppo_choice = 'R'
            elif oppo_choice == 'B':
                oppo_choice = 'P'
            else:
                oppo_choice = 'S'

            your_choice = line[2]

            if your_choice == 'X':
                your_choice = 'R'
            elif your_choice == 'Y':
                your_choice = 'P'
            else:
                your_choice = 'S'

            games.append([oppo_choice, your_choice])
    return games

def ingest_data_pt2():
    games = []
    with open("input.txt") as file:
        for line in file:
            oppo_choice = line[0]
            if oppo_choice == 'A':
                oppo_choice = 'R'
            elif oppo_choice == 'B':
                oppo_choice = 'P'
            else:
                oppo_choice = 'S'

            your_choice = line[2]

            if your_choice == 'Z':
                if oppo_choice == 'R':
                    your_choice = 'P'
                elif oppo_choice == 'P':
                    your_choice = 'S'
                else:  # if oppo == 'S':
                    your_choice = 'R'

            elif your_choice == 'Y':
                your_choice = oppo_choice
            else:
                if oppo_choice == 'R':
                    your_choice = 'S'
                elif oppo_choice == 'P':
                    your_choice = 'R'
                else:  # if oppo == 'S':
                    your_choice = 'P'

            games.append([oppo_choice, your_choice])
    return games

def score_games(games):
    score = 0
    for game in games:
        oppo = game[0]
        you = game[1]

        if oppo == 'R':
            if you == 'R':
                score += 3
            elif you == 'P':
                score += 6
            else:
                score += 0

        elif oppo == 'P':
            if you == 'P':
                score += 3
            elif you == 'S':
                score += 6
            else:
                score += 0

        else: #if oppo == 'S':
            if you == 'S':
                score += 3
            elif you == 'R':
                score += 6
            else:
                score += 0

        if you == 'R':
            score += 1
        elif you == 'P':
            score += 2
        else:
            score += 3

    return score

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    games = ingest_data_pt2()

    print(score_games(games))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
