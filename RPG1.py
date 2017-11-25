import random

class Card:
    def __init__(self, name):
        self.name = name
                
    def __str__(self):
        return self.name

class Creature(Card):
    def __init__(self, name, cost, power, health):
        self.name = name
        self.cost = cost
        self.power = power
        self.health = health
        self.stats = [self.name, self.cost, self.power, self.health]
       
    def stats(self):
        statList = ["Name: ", " | Cost: ", " | Power: ", " | Health: "]
        statStr = "" 
        
        for i in range(len(statList)):
            statStr += statList[i] + str(self.stats[i])
        
        print(statStr)
        
    def isDead(self):
        if self.health <= 0:
            print(self.name + " has died")
            return True
        
    def takeDamage(self, damage):
        self.health -= damage
        print(self.name,"took", damage, "damage")
        self.isDead()
        
    def fights(self, other):
        print(self.name, "fights", other.name)
        
        other.health -= self.power
        self.health -= other.power
        
        self.isDead() 
        other.isDead()


class Spell(Card):
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        

class Player:
    def __init__(self, deck):
        self.hand = []
        self.field = []
        self.deck = deck
        self.life = 30
        
    def draw(self):
        self.hand.append(self.deck.pop(0))
        
    def startingHand(self):
        random.shuffle(self.deck)
        for i in range(3):
            self.hand.append(self.deck.pop(0))
            
    def play(self, card):
        
        self.hand.remove(card)
        self.field.append(card)




def main():
    c1 = Creature("Chester", 3, 8, 5)
    c2 = Creature("Jasper", 6, 2, 8)

    d1 = [c1, c1, c2, c2, c2]
    
    p1 = Player(d1)
    
    p1.startingHand()
    
    p1.play(c1)
    
   
    
    #takeDamage test
    if 1 == 2:
        c1.takeDamage(3)
        c1.takeDamage(3)
    
    #fights test
    if 1 == 2:
        c1.fights(c2)
    
    #stat check test
    if 1 == 2:
        c1.stats()
main()
    
    