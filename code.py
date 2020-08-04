import random
def test():
    for i in range(6):
        yield random.randint(1,1001)

for luck in test():
    print("Your number is... %d!" % (luck))
    if luck == 500:
            print("LUCKY WIN!!!")
    if luck == 1000:
        print("WOOOWWW!!! YOU WIN!!!")
    if luck == 100:
        print("GG!! YOU WON!!")
    if luck == 200:
        print("YESS!! WINNER!!!")
    if luck == 300:
        print("WOOWOWOWOWOWOWOO YOU WINNNNNNN!!!!")
    if luck == 400:
        print("HOLY MOLY HOW DID YOU WIN??!!!!")
    if luck == 600:
        print("WOOOW YOU WOOONn!!!!!nnn!!11!")
    if luck == 700:
        print("HELLO WORLD TO THE COWLY HOLY MOLY YOU WON!!!")
    if luck == 800:
        print("IMPOSSIBLE! YOU WON!")
    if luck == 900:
        print("YOU GO GIRL!! SLAY MA KWEEN")
    else:
        print("Maybe next time...")
