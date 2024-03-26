import random


class Coin:
    def __init__(self):
        # heads-оре6л/tails-решка
        self.side = None

    def flip(self):
        """  Подбрасывание монетки """
        #self.side = random.choice['heads','tails'] #random.randint(0, 1)
        self.side = random.choice(['heads','tails'])

# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах

coins_count = int(input('Укажите количество монет: '))

coins_list = []
side_list = []

i = 0
while i < coins_count:
    coins_list.append(Coin())
    i += 1

for i in coins_list:
    i.flip()
    side_list.append(i.side)

heads_count = side_list.count('heads')
tails_count = side_list.count('tails')

heads_percent = round(heads_count / coins_count * 100, 1)
tails_percent = 100 - heads_percent

print('Стороны монеток распределились следующим образом:')
print(f'{heads_percent}% упали орлом вверх ({heads_count} штук)')
print(f'{tails_percent}% упали решкой вверх ({tails_count} штук)')

