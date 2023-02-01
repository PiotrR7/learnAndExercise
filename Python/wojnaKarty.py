'''
0 = as
1 = 2
2 = 3
3 = 4
4 = 5
5 = 6
6 = 7
7 = 8
8 = 9
9 = 10
10 = jopek
11 = dama
12 = król


0 = wino 
1 = żołądź
2 = dzwonek
3 = serce
'''












import random

karty = ['As',1,2,3,4,5,6,7,8,9,'jopek','dama','król']
typKarty = ['wino','zolodz','dzwonek','serce']

kartyGracz1 = {}
kartyGracz2 = {}

tymczsowekartyGracz1 = {}
tymczsowekartyGracz2 = {}


# losowanie kart
running = True
while running == True:
    losNumerKarty = random.randint(0, 12)
    losTypKarty = random.randint(0, 3)



    losNumerKarty = karty[losNumerKarty]
    losTypKarty = typKarty[losTypKarty]


    tymczsowekartyGracz1[losNumerKarty] = losTypKarty

    if len(tymczsowekartyGracz1)==26:
        running = False


print(tymczsowekartyGracz1)
