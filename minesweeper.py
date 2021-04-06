import json
import os
import time
from directions import*
from location import*

def main():
    LoadGame()
    Intro()
    
    while True:
        clear()
        if minefield[p.x][p.y]:
            ShowMines()
            time.sleep(wait)
            break
        elif CountMines()==0:
            print("Congratulations! You won")
            break
        else:
            print(title)
            print("mines: ", CountMines() )
            print("detonators: ", detonators) 
            Display()
        print("What do you want to do?")
        direction=input()
        if direction=="q":
            break
        else:
            func=switch.get(direction,  Default)
            func()
     
    f_minefield.close()
    f_title.close()
    print("Game Over")

def LoadGame():
    global clear
    global minefield
    global title
    global rules
    global detonators
    global wait
    global f_minefield
    global f_title
    clear = lambda: os.system('cls')
    f_minefield = open('json/minefield.json',)
    f_title = open('json/title.json',)
    minefield_data = json.load(f_minefield)
    minefield=minefield_data["minefield"]
    title_data=json.load(f_title)
    title= title_data["title"]
    rules=title_data["rules"]
    detonators=12
    wait=3

def Intro():
    print(title)
    print(rules)
    time.sleep(wait)
    clear()

def DetNorth():
    global detonators
    if detonators>0:
        detonators-=1
        if minefield[p.x][p.y-1]:
            DisplayDet(p.x, p.y-1)
            minefield[p.x][p.y-1]=False
            detonators-=1
            time.sleep(wait)
            clear()
        
    
def DetSouth():
    global detonators
    if detonators>0:
        detonators-=1
        if minefield[p.x][p.y+1] and detonators>0:
             DisplayDet(p.x, p.y+1)
             detonators-=1
             minefield[p.x][p.y+1]=False
             detonators-=1
             time.sleep(wait)
             clear()
        

def DetEast():
    global detonators
    if detonators>0:
        detonators-=1
        if minefield[p.x+1][p.y] and detonators>0:
             DisplayDet(p.x+1, p.y)
             detonators-=1
             minefield[p.x+1][p.y]=False
             detonators-=1
             time.sleep(wait)
             clear()
        

def DetWest():
    global detonators
    if detonators>0:
        detonators-=1
        if minefield[p.x-1][p.y] and detonators>0:
            DisplayDet(p.x-1, p.y)
            detonators-=1
            minefield[p.x-1][p.y]=False
            time.sleep(wait)
            clear()
        

def ShowMines():
     for row  in minefield:
            for  mine in row:
                if  mine:
                    print("(X)", end=" ")
                else:
                   print("|__", end=" ")
            print()

def Display():
    for i, row in enumerate(minefield):
            for j, mine in enumerate(row):
                if  i==p.y and j==p.x:
                    print("0", end=" ")
                else:
                   print("|__", end=" ")
            print()

def DisplayDet(x, y):
    for i, row in enumerate(minefield):
            for j, mine in enumerate(row):
                if  i==p.y and j==p.x:
                    print("0", end=" ")
                elif i==y and j==x:
                    print("X", end=" ")
                else:
                   print("|__", end=" ")
            print()
    print("Got one!")

def Default():
    print("I don't understand that")

def CountMines():
    total=0
    for row in minefield:
        total+=row.count(True)
    return total

switch={
    "north": GoNorth,
    "detonate north": DetNorth,
    "south": GoSouth,
    "detonate south": DetSouth,
    "east" : GoEast,
    "detonate east" : DetEast,
    "west":  GoWest,
    "detonate west" : DetWest
    }






main()

            

