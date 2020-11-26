# import csv


# moves_set = set()
# count = 0
# with open('games_one_million.csv', 'r', newline='') as f:
#     reader = csv.reader(f)
#     for column in reader:
#         game = column[0]
#         moves = game.split(" ")
#         moves = list(filter(lambda a: a != '', moves))
#         for move in moves:
#             moves_set.add(move)
#         count += 1
#         print(str(count) + "/1000000")

# with open('moves_set.csv', 'w', newline='') as move_writer:
#     writer = csv.writer(move_writer)
#     for move in moves_set:
#         writer.writerow([move])
import csv

uniqueElos = set()

with open("games_one_million.csv", 'r', newline='') as f:
  reader = csv.reader(f)
  for column in reader:
    white_elo = column[2]
    black_elo = column[4]
    uniqueElos.add(white_elo)
    # uniqueElos.add(black_elo)

un = len(uniqueElos)
print(un)
