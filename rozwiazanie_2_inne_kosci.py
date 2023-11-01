from random import randint, shuffle

dices = {"D3": 3, "D4": 4, "D6": 6, "D8": 8, "D10": 10, "D12": 12, "D20": 20, "D100": 100}


def dice(type_dice):
    type_dice = type_dice.upper()
    max_wall = dices[type_dice]
    result = randint(1, max_wall)
    return result


def random_dice():
    key_dices = list(dices.keys())
    shuffle(key_dices)
    result = key_dices[0]
    return result


def calculate_points(current_result, round_result):
    if round_result == 7:
        result = current_result // 7
    elif round_result == 11:
        result = current_result * 11
    else:
        result = current_result + round_result
    return result


result_user = 0
result_comp = 0

user_choice = []
for i in range(2):
    user_dice = input('Enter your dice: ')
    try:
        result_user += dice(user_dice)
    except (TypeError, KeyError):
        print('Wrong type of dice. Start game again')
        break
    comp_dice = random_dice()
    result_comp += dice(comp_dice)
print(f"Result user after round {result_user}")
print(f"Result comp after round {result_comp}")
while True:
    user_round_result = 0
    comp_round_result = 0
    for _ in range(2):
        user_dice = input('Enter your dice: ')
        try:
            user_round_result += dice(user_dice)
        except (TypeError, KeyError):
            print('Wrong type of dice. Try round again')
            break
        comp_dice = random_dice()
        comp_round_result = + dice(comp_dice)
    result_user = calculate_points(result_user, user_round_result)

    print(f"Result user after round {result_user}")
    result_comp = calculate_points(result_comp, comp_round_result)

    print(f"Result comp after round {result_comp}")

    if result_user >= 2021 and result_user > result_comp:
        print('You won')
        print(f"Final results: You {result_user}, computer {result_comp}")
        break
    elif result_comp >= 2021 and result_comp > result_user:
        print('Computer won')
        print(f"Final results: You {result_user}, computer {result_comp}")
        break
