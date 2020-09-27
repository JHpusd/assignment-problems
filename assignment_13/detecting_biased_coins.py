import matplotlib.pyplot as plt

coin_1 = ['TTH', 'HHT', 'HTH', 'TTH', 'HTH',
          'TTH', 'TTH', 'TTH', 'THT', 'TTH',
          'HTH', 'HTH', 'TTT', 'HTH', 'HTH',
          'TTH', 'HTH', 'TTT', 'TTT', 'TTT',
          'HTT', 'THT', 'HHT', 'HTH', 'TTH']
coin_2 = ['HTH', 'HTH', 'HTT', 'THH', 'HHH',
          'THH', 'HHH', 'HHH', 'HTT', 'TTH',
          'TTH', 'HHT', 'TTH', 'HTH', 'HHT',
          'THT', 'THH', 'THT', 'TTH', 'TTT',
          'HHT', 'THH', 'THT', 'THT', 'TTT']
coin_3 = ['HHH', 'THT', 'HHT', 'HHT', 'HTH',
          'HHT', 'HHT', 'HHH', 'TTT', 'THH',
          'HHH', 'HHH', 'TTH', 'THH', 'THH',
          'TTH', 'HTT', 'TTH', 'HTT', 'HHT',
          'TTH', 'HTH', 'THT', 'THT', 'HTH']


def chance_finder(coin_list, heads):
    result_counter = 0
    for result in coin_list:
        heads_count = 0
        for i in range(len(result)):
            if result[i] == 'H':
                heads_count += 1
        if heads_count == heads:
            result_counter += 1
    return result_counter / len(coin_list)

x_coords = [0, 1, 2, 3]
y_coords = []
for i in range(4):
    y_coords.append(chance_finder(coin_1, i))
plt.style.use('bmh')
plt.plot(x_coords, y_coords)

y_coords = []
for i in range(4):
    y_coords.append(chance_finder(coin_2, i))
plt.plot(x_coords, y_coords)

y_coords = []
for i in range(4):
    y_coords.append(chance_finder(coin_3, i))
plt.plot(x_coords, y_coords)

plt.legend(['coin_1', 'coin_2', 'coin_3'])
plt.xlabel('number of heads')
plt.ylabel('probability from simulations')
plt.savefig('biased_coin_simulation.png')

# coin_2 seems pretty fair, but coin_1 seems like it leans more towards tals, while coin_3 seems more biased towards heads. But these could just be the results of experimentation.
