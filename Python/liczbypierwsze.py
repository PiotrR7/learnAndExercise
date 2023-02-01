# for x in range(2,100):
#     if x % 2 == 0 or x <= 1:
#         print('')
#     else:
#         print(x,'liczba pierwsza')

# for x in range(2,100):
#         if x!=x and x%2==0 or x%3==0 or x%4==0 or x%5==0 or x%6==0 or x%7==0 or x%8==0 or x%9==0 or x%10==0 or x%11==0:
#             print('')
#         else:
#             print(x,'jest liczba pierwsza')

def czyliczbapierwsza():
    for x in range(2,100):
        while x != 2 or 3:
            if x % 2 == 0 and x % 3 == 0:
                print(x,'liczba nie jest liczbą pierwszą')
            else:
                print(x,'jest liczbą pierwszą')

czyliczbapierwsza()