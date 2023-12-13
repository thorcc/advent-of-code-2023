file = open("input.txt")
data = file.read()
lines = data.split("\n")

hands = []
types = {
    1: "Five of a kind",
    2: "Four of a kind",
    3: "Full house",
    4: "Three of a kind",
    5: "Two pair",
    6: "One pair",
    7: "High card"
}

def get_card_val(c:str):
    cards = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10}
    if c.isdigit():
        return int(c)
    return cards[c]

def get_type(count: set):
    if count[-1][0] == 5:
        return 1
    elif count[-1][0] == 1:
        return 7
    elif len(count) == 4:
        return 6
    elif len(count) == 2:
        if count[-1][0] == 4:
            return 2
        else:
            return 3
    else:
        if count[-1][0] == 3:
            return 4
        else:
            return 5


class Hand():
    def __init__(self, line):
        cards, bid = line.split(" ")
        self.cards = cards
        self.bid = int(bid)
        self.find_type()
    
    def find_type(self):
        count = set()
        js = 0
        for card in self.cards:
            if card == "J":
                js += 1
            else:
                c = self.cards.count(card)
                count.add((c, card))
        count = sorted(count)
        if js > 4:
            count.append((5,"J"))
        elif js > 0:
            c = count.pop()
            count.append((c[0] + js, c[1]))
        self.type = get_type(count)


    
    def __str__(self):
        return f"({self.cards}, {self.bid})"
    
    def __lt__(self, other):
        if self.type - other.type > 0:
            return True
        elif  self.type - other.type < 0:
            return False
        for i in range(len(self.cards)):
            if get_card_val(self.cards[i]) < get_card_val(other.cards[i]):
                return True
            elif get_card_val(self.cards[i]) > get_card_val(other.cards[i]):
                return False
        return False
                    
    
    def __repr__(self):
        return self.__str__()


for line in lines:
    hands.append(Hand(line))

hands = sorted(hands)
print(hands)

sum = 0
for i in range(len(hands)):
    print(f"{hands[i].cards}, {hands[i].bid} * {i + 1}")
    sum += hands[i].bid * (i + 1)
print(sum) 