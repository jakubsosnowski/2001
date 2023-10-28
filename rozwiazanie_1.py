from random import randint


def guess_1_6():
    result = randint(1, 6)
    return result


result_user = 0
result_comp = 0

start_game = input('Press enter to start a game: ')
if start_game != '':
    print('You entered other sign than enter. Please start again')
else:
    for _ in range(2):
        result_user += guess_1_6()
        result_comp += guess_1_6()
    print(f"Result user after round {result_user}")
    print(f"Result comp after round {result_comp}")
    while True:
        game = input('Press enter to continue a game: ')
        if game != '':
            print('You entered other sign than enter. Please enter again')
            continue
        user_result_round = 0
        comp_result_round = 0
        for _ in range(2):
            user_result_round += guess_1_6()
            comp_result_round += guess_1_6()

        if user_result_round == 7:
            result_user = result_user // 7
        elif user_result_round == 11:
            result_user = result_user * 11
        else:
            result_user += user_result_round
        print(f"Result user after round {result_user}")
        if result_user >= 2021:
            print('Wygrałeś')
            break

        if comp_result_round == 7:
            result_comp = result_comp // 7
        elif comp_result_round == 11:
            result_comp = result_comp * 11
        else:
            result_comp += comp_result_round
        print(f"Result comp after round {result_comp}")
        if result_comp >= 2021:
            print('Wygrał komputer')
            break
