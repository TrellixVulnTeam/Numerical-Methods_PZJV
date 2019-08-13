import requests
import random


def crypto_market_one():

    response = requests.get("https://bitbay.net/API/Public/BTCPLN/ticker.json")
    data = response.json()
    best_bid = data['bid']
    best_ask = data['ask']
    return best_bid, best_ask


def crypto_market_two():
    response = requests.get("https://www.bitmarket.pl/json/BTCPLN/ticker.json")
    data = response.json()
    ask = data["ask"]
    bid = data["bid"]
    return bid, ask

def comparing_markets():
    one = crypto_market_one()
    two = crypto_market_two()
    print("Bitbay (bid,ask):", one, "Bitmarket (bid,ask)", two)
    output = ''
    if one[0] > two[0]:
        output_sell = 'Better is sell on bitbay '
    else:
        output_sell = 'Better is sell on Bitmarket '

    if one[1] > two[1]:
        output_buying = "better is buying on bitbay "
    else:
        output_buying = "better is buying on bitbay "
    print(output_buying+output_sell)

comparing_markets()

class User:
    def __init__(self):
        pass
    def data(function_new):
        def select_data(self, x):
            user = {}
            user_data = function_new(self, x)
            user["id"] = x
            first_name = user_data['results'][0]["name"]["first"]
            second_name = user_data['results'][0]["name"]["last"]
            user["name"] = first_name+second_name
            user["login"] = user_data['results'][0]["login"]["username"]
            return user
        return select_data
    @data
    def new_user_data(self, x):
        response = requests.get("https://randomuser.me/api/?nat=us/?results=1")
        data = response.json()
        return data

def create(number):
    user_create = User()
    all_user = [user_create.new_user_data(i) for i in range(1, number+1)]
    return all_user
# all = create(100)
# print(all)

def main(number):
    all = create(number)
    try:
        while True:

            print("Choose operation.\n 1-simulation.\n 0-end")
            x = input()
            x = int(x)

            # print(all)

            if x == 1:
                for i in range(1, 101):
                    two = crypto_market_two()
                    bid = two[0]
                    ask = two[1]

                    rand_action = random.choice([["bid", bid], ["ask", ask]])
                    action, price = rand_action
                    amount_btc = random.random()
                    amount_pl = random.random()*1000
                    # print(action, "actionnnnnnn")

                    user_one = all[random.randint(1, number-1)]["login"]
                    amount_btc_one = random.random()*10
                    amount_pl_one = random.random()*1000
                    user_two = all[random.randint(1, number-1)]["login"]
                    amount_btc_two = random.random()*10
                    amount_pl_two = random.random()*1000

                    if user_one != user_two:
                        amount_btc = random.random()
                        amount_pl = random.random()*100
                        if (action == "bid"):

                            cost_pln = amount_btc*bid

                            if(cost_pln < amount_pl_two):
                                print("Transaction {}".format(i))
                                print("Pocket:{} one(PLN:{},BTC:{};{} (PLN:{},BTC:{}))".format(
                                    user_one, amount_btc_one, amount_pl_one, user_two, amount_pl_two, amount_btc_two))
                                amount_btc_one -= amount_btc
                                amount_pl_one += cost_pln
                                amount_btc_two += amount_btc
                                amount_pl_two -= cost_pln
                                print("{} exchanged {} BTC with {} for {} PLN".format(
                                    user_one, amount_btc, user_two, cost_pln))
                                print("Pocket:{} one(PLN:{},BTC:{};{} (PLN:{},BTC:{}))".format(
                                    user_one, amount_btc_one, amount_pl_one, user_two, amount_pl_two, amount_btc_two))
                            else:
                                print(
                                    "{} can't exchanged  BTC with {} for PLN.".format(user_two, user_one))

                        elif(action == "ask"):

                            cost_bt = amount_pl/ask

                            if(cost_bt < amount_btc_two):
                                print()
                                print("Transaction {}".format(i))
                                print(
                                    "Pocket:{} one(PLN:{},BTC:{};{} (PLN:{},BTC:{}))".format(user_one, amount_pl_one, amount_btc_one, user_two, amount_pl_two, amount_btc_two))

                                amount_btc_one += cost_bt
                                amount_pl_one -= amount_pl
                                amount_btc_two -= cost_bt
                                amount_pl_two += amount_pl

                                print(
                                    "{} exchanged {} PLN with {} for {} BLC".format(user_one, amount_pl, user_two, cost_bt))
                                print()
                                print(
                                    "Pocket:{} one(PLN:{},BTC:{};{} (PLN:{},BTC:{}))".format(user_one, amount_btc_one, amount_pl_one, user_two, amount_pl_two, amount_btc_two))
                            else:
                                print(
                                    "{} can't exchanged  PLN with {}. for BLC".format(user_two, user_one))
            elif x == 0:
                break
            else:
                print("This number  nothing do")
    except ValueError:
        print("it is not a number")


main(5)
