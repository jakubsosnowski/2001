from flask import Flask, request, render_template
from random import randint, shuffle

app = Flask(__name__)

dices = {"D3": 3, "D4": 4, "D6": 6, "D8": 8, "D10": 10, "D12": 12, "D20": 20, "D100": 100}


def user_move(dice1, dice2):
    """
    Function takes 2 arguments. It is names dices. Next guess number of wall for each dice
    Function returns the number drawn in the round
    """
    user_round_1 = randint(1, int(request.form.get(dice1)))
    user_round_2 = randint(1, int(request.form.get(dice2)))
    user_round = user_round_1 + user_round_2
    return user_round


def result_round(result, result_move):
    """
    Function takes result after previous round and result in round.
    Function return current result taking into account conditions of game.
    """
    if result_move == 7:
        result = result // 7
    elif result_move == 11:
        result = result * 11
    else:
        result += result_move
    return result


@app.route("/", methods=['GET', 'POST'])
def game():
    if request.method == 'GET':
        return render_template('hello_page.html')
    else:
        result_user = int(request.form.get('result_user'))
        result_user_round = user_move("dice1", "dice2")
        result_user = result_round(result_user, result_user_round)

        result_comp = int(request.form.get('result_comp'))
        result_comp_round = 0
        for _ in range(2):
            list_dice = list(dices.keys())
            shuffle(list_dice)
            first_dice_value = list_dice[0]
            result_comp_round += randint(1, dices[first_dice_value])
        result_comp = result_round(result_comp, result_comp_round)

        if result_user >= 2001 and result_user > result_comp:
            return render_template('user_won.html',
                                   result_user=result_user,
                                   result_comp=result_comp)
        elif result_comp >= 2001 and result_comp > result_user:
            return render_template('comp_won.html',
                                   result_comp=result_comp,
                                   result_user=result_user)
        return render_template('result_page.html',
                               result_user=result_user,
                               result_comp=result_comp)
