letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]


letter_to_points = {key:value for key, value in zip(letters,points)}
letter_to_points[""] = 0



def score_word(words):
  point_total = 0
  for i in words:
    if i in letter_to_points.keys():
      a = letter_to_points.get(i)
      point_total += a
    else:
      point_total += 0
  return point_total


words = "BROWNIE"
score_word(words)

player_to_words = {"player1": ['BLUE', 'TENNIS', 'EXIT'], "wordnerd":['EARTH', 'EYES', 'MACHINE'], "lexicon":['ERASER','BELLY','HUSKY'], "profreader": ['ZAP', 'COMA', 'PERIOD'] }
player_to_points = {}


for player, words  in player_to_words.items():
  points = 0
  for i in words:
    a = score_word(i)
    points += a
  player_to_points[player] = points  


print(player_to_points)


