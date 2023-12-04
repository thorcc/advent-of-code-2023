file = open("input.txt")
data = file.read()
lines = data.split("\n")
cards = []
for line in lines:
    _, numbers = line.split(":")
    winning, game = numbers.split("|")
    winning = [int(n) for n in winning.split(" ") if n != ""]
    game = [int(n) for n in game.split(" ") if n != ""]
    cards.append([winning, game])

# a
score = 0
for card in cards:
    line_score = 0
    for n in card[1]:
        if n in card[0]:
            if line_score == 0:
                line_score = 1
            else:
                line_score *= 2
    score += line_score
print(score)

# b
def find_winners(card):
    winners = 0
    for n in card[1]:
        if n in card[0]:
            winners += 1
    return winners

winners = [find_winners(card) for card in cards]
cards_total = [1]*len(cards)
for i in range(len(cards)):
    for j in range(winners[i]):
        cards_total[i + 1 + j] += cards_total[i]
print(sum(cards_total))
