import csv
import chess.pgn
import re
import math



with open('test_games.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    count = 1
    writer.writerow(["moves", "result", "white_min_elo", "white_max_elo", "black_min_elo", "black_max_elo"])
    with open('games_one_million.csv', 'r', newline='') as games:
        reader = csv.reader((games))
        for game in reader:
            if(count > 900000):
                writer.writerow(game)
            count+=1
        games.close()
    f.close()

games.close()
