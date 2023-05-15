
bot = input("Name your bot")

conversation = ["hi", "hello", "how you doing?", "good and you?", "i am stupid bot"]
curiosity = ["zombies are all around", "yes"]
knowlegde = [conversation, curiosity]


def guilty_conscience(p):
    for i in range(len(knowlegde)):
        for z in knowlegde[i]:
            if p == z:
                try:
                    return knowlegde[i][knowlegde[i].index(z) + 1]
                except IndexError:
                    print(curiosity[0])


print("Say something: ")
while True:
    ask = input("EU: ")
    print(bot + ": "  +guilty_conscience(ask))
