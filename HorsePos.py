import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class Horse:
    def __init__(self, horseTimeS, horseName):
        self.horseTimeS = horseTimeS
        self.horseName = horseName
        self.leftH = None
        self.rightH = None
        
class myNode:
    def __init__(self, horseTimeS, horseName):
        self.root = Horse(horseTimeS, horseName)
     
        
    def __add_horse(self, horse, horseTimeS, horseName):
        if horseTimeS < horse.horseTimeS:
            if horse.leftH is None:
                horse.leftH = Horse(horseTimeS, horseName)     
            else:
                self.__add_horse(horse.leftH, horseTimeS, horseName)
        else:
            if horse.rightH is None:
                horse.rightH = Horse(horseTimeS, horseName)
            else:
                self.__add_horse(horse.rightH, horseTimeS, horseName)
         
    
    def __Hpath(self, horse):
         if horse is not None:
            self.__Hpath(horse.leftH)
        
            print(horse.horseName + " = " + str(horse.horseTimeS))
            #print(horse.horseTimeS)
            self.__Hpath(horse.rightH)


    def __find(self, nodo, horseTimeS):
       if nodo is None:
           return None
       if nodo.horseTimeS == horseTimeS:
           return nodo
       if horseTimeS < nodo.horseTimeS:
           return self.__find(nodo.leftH, horseTimeS)
       else:
           return self.__find(nodo.rightH, horseTimeS)  
       
        
     
    def addHorse(self, horseTime, horseName):
        self.__add_horse(self.root, horseTime, horseName)

    def printOrderedHorses(self):
        print("Horses ordered by place: ")
        self.__Hpath(self.root)
        print("")
        
    def findHorse(self, horseTimeS):
        return self.__find(self.root, horseTimeS)
    
OrderedHorses = ""

HorseNames = [["Horse 1","Horse 2","Horse 3","Horse 4","Horse 5"],
            ["Horse 6","Horse 7","Horse 8","Horse 9","Horse 10"],
            ["Horse 11","Horse 12","Horse 13","Horse 14","Horse 15"],
            ["Horse 16","Horse 17","Horse 18","Horse 19","Horse 20"],
            ["Horse 21","Horse 22","Horse 23","Horse 24","Horse 25"],]


pointsListH = np.zeros((5, 5))
pointsHSize = pointsListH.shape
for x in range(pointsHSize[0]):
    for y in range (pointsHSize[1]):
        pointsListH[x, y] = random.randint(0,10000) #0-1000 because this gives us way more oportunity to discard repetitive values

print ("Contestants:" )
print (HorseNames,'\n')

print("First of all, we make 5 careers, each with 5 horses:")
print("Results: ")
for x in range(5):
  pointsListH[x].sort() 
  print( x + 1, " Career: ", pointsListH[x]) 

print("Then, we have to pick the 5 fastest horses...")
print("Top 5 Career:")
topFiveHorses= np.array([pointsListH[0,0],pointsListH[1,0],pointsListH[2,0],pointsListH[3,0],pointsListH[4,0]])
print(topFiveHorses)


print("Then we sort all the careers:")
sortPointsListH = pointsListH[np.argsort(pointsListH[:, 0])]
for x in range(5):
  print(sortPointsListH[x]) 

print("\n2nd and 3rd place:")
sCareerH = np.array([sortPointsListH[0, 1],sortPointsListH[0, 2],sortPointsListH[1, 0],sortPointsListH[1, 1],sortPointsListH[2, 0]])
print(sCareerH)
sCareerH.sort()

print("\nFinal results:")
print("First place:", int(sortPointsListH[0,0]))
print("Second place:", int(sCareerH[0]))
print("Third place:", int(sCareerH[1]))



myHorseCareer = np.concatenate(sortPointsListH)
myHorseCareer.sort()

career = myNode(pointsListH[0,0],    HorseNames[0][0])  
for x in range(pointsHSize[0]):
    for y in range (pointsHSize[1]):
        if x == 0 and y == 0:
            pass
        else:
            career.addHorse (pointsListH[x,y],   HorseNames[x][y])

career.printOrderedHorses()


finalContestants = ["" for x in range(25)]
for x in range(25):
  timeDa = career.findHorse(myHorseCareer[x])
  finalContestants[x] = timeDa.horseName
  
  
myHorseGraph = nx.Graph()

vertex_H = [finalContestants[24], finalContestants[23], finalContestants[22], finalContestants[21], finalContestants[20],finalContestants[19], finalContestants[18], 
              finalContestants[17], finalContestants[16], finalContestants[15], finalContestants[14], finalContestants[13], finalContestants[12], finalContestants[11], 
              finalContestants[10], finalContestants[9], finalContestants[8], finalContestants[7], finalContestants[6], finalContestants[5],finalContestants[4],
              finalContestants[3], finalContestants[2], finalContestants[1], finalContestants[0]]


myHorseGraph.add_nodes_from(vertex_H)

edges_H = [(finalContestants[24], finalContestants[23]), (finalContestants[23], finalContestants[22]), (finalContestants[22], finalContestants[21]), (finalContestants[21], finalContestants[20]),
             (finalContestants[20], finalContestants[19]), (finalContestants[19], finalContestants[18]), (finalContestants[18], finalContestants[17]), (finalContestants[17], finalContestants[16]),
             (finalContestants[16], finalContestants[15]), (finalContestants[15], finalContestants[14]), (finalContestants[14], finalContestants[13]), (finalContestants[13], finalContestants[12]),
             (finalContestants[12], finalContestants[11]), (finalContestants[11], finalContestants[10]), (finalContestants[10], finalContestants[9]), (finalContestants[9], finalContestants[8]), 
             (finalContestants[8], finalContestants[7]), (finalContestants[7], finalContestants[6]), (finalContestants[6], finalContestants[5]), (finalContestants[5], finalContestants[4]),
             (finalContestants[4], finalContestants[3]), (finalContestants[3], finalContestants[2]), (finalContestants[2], finalContestants[1]), (finalContestants[1], finalContestants[0])]

myHorseGraph.add_edges_from(edges_H)

graphLocation = {finalContestants[0]: (1, 21), finalContestants[1]: (3, 21), finalContestants[2]: (5, 21), finalContestants[3]: (7, 21), finalContestants[4]: (9, 21),
         finalContestants[5]: (11, 21), finalContestants[6]: (13, 21), finalContestants[7]: (15, 21), finalContestants[8]: (15, 18), finalContestants[9]: (15, 15), 
         finalContestants[10]: (13, 15), finalContestants[11]: (11, 15), finalContestants[12]: (9, 15), finalContestants[13]: (7, 15), finalContestants[14]: (5, 15),
         finalContestants[15]: (3, 15), finalContestants[16]: (1, 15), finalContestants[17]: (1, 12), finalContestants[18]: (1, 9), finalContestants[19]: (3, 9),
         finalContestants[20]: (5, 9), finalContestants[21]: (7, 9), finalContestants[22]: (9, 9), finalContestants[23]: (11, 9), finalContestants[24]: (13, 9)}



class Tupla:
    def _init_(self, x, y):
        self.x = x
        self.y = y

point1 = Tupla()
point1.x = graphLocation[finalContestants[24]][0]
point1.y = graphLocation[finalContestants[24]][1]
point2 = Tupla()
point2.x = graphLocation[finalContestants[23]][0]
point2.y = graphLocation[finalContestants[23]][1]
point3 = Tupla()
point3.x = graphLocation[finalContestants[22]][0]
point3.y = graphLocation[finalContestants[22]][1]
point4 = Tupla()
point4.x = graphLocation[finalContestants[21]][0]
point4.y = graphLocation[finalContestants[21]][1]
point5 = Tupla()
point5.x = graphLocation[finalContestants[20]][0]
point5.y = graphLocation[finalContestants[20]][1]
point6 = Tupla()
point6.x = graphLocation[finalContestants[19]][0]
point6.y = graphLocation[finalContestants[19]][1]
point7 = Tupla()
point7.x = graphLocation[finalContestants[18]][0]
point7.y = graphLocation[finalContestants[18]][1]
point8 = Tupla()
point8.x = graphLocation[finalContestants[17]][0]
point8.y = graphLocation[finalContestants[17]][1]
point9 = Tupla()
point9.x = graphLocation[finalContestants[16]][0]
point9.y = graphLocation[finalContestants[16]][1]
point10 = Tupla()
point10.x = graphLocation[finalContestants[15]][0]
point10.y = graphLocation[finalContestants[15]][1]
point11 = Tupla()
point11.x = graphLocation[finalContestants[14]][0]
point11.y = graphLocation[finalContestants[14]][1]
point12 = Tupla()
point12.x = graphLocation[finalContestants[13]][0]
point12.y = graphLocation[finalContestants[13]][1]
point13 = Tupla()
point13.x = graphLocation[finalContestants[12]][0]
point13.y = graphLocation[finalContestants[12]][1]
point14 = Tupla()
point14.x = graphLocation[finalContestants[11]][0]
point14.y = graphLocation[finalContestants[11]][1]
point15 = Tupla()
point15.x = graphLocation[finalContestants[10]][0]
point15.y = graphLocation[finalContestants[10]][1]
point16 = Tupla()
point16.x = graphLocation[finalContestants[9]][0]
point16.y = graphLocation[finalContestants[9]][1]
point17 = Tupla()
point17.x = graphLocation[finalContestants[8]][0]
point17.y = graphLocation[finalContestants[8]][1]
point18 = Tupla()
point18.x = graphLocation[finalContestants[7]][0]
point18.y = graphLocation[finalContestants[7]][1]
point19 = Tupla()
point19.x = graphLocation[finalContestants[6]][0]
point19.y = graphLocation[finalContestants[6]][1]
point20 = Tupla()
point20.x = graphLocation[finalContestants[5]][0]
point20.y = graphLocation[finalContestants[5]][1]
point21 = Tupla()
point21.x = graphLocation[finalContestants[4]][0]
point21.y = graphLocation[finalContestants[4]][1]
point22 = Tupla()
point22.x = graphLocation[finalContestants[3]][0]
point22.y = graphLocation[finalContestants[3]][1]
point23 = Tupla()
point23.x = graphLocation[finalContestants[2]][0]
point23.y = graphLocation[finalContestants[2]][1]
point24 = Tupla()
point24.x = graphLocation[finalContestants[1]][0]
point24.y = graphLocation[finalContestants[1]][1]
point25 = Tupla()
point25.x = graphLocation[finalContestants[0]][0]
point25.y = graphLocation[finalContestants[0]][1]


pointsH = {finalContestants[24]: point1, finalContestants[23]: point2, finalContestants[22]: point3, finalContestants[21]: point4, finalContestants[20]: point5, 
          finalContestants[19]: point6, finalContestants[18]: point7, finalContestants[17]: point8, finalContestants[16]: point9, finalContestants[15]: point10, 
          finalContestants[14]: point11, finalContestants[13]: point12, finalContestants[12]: point13, finalContestants[11]: point14, finalContestants[10]: point15, 
          finalContestants[9]: point16, finalContestants[8]: point17, finalContestants[7]: point18, finalContestants[6]: point19, finalContestants[5]: point20, 
          finalContestants[4]: point21, finalContestants[3]: point22, finalContestants[2]: point23, finalContestants[1]: point24, finalContestants[0]: point25}

    
nx.draw(myHorseGraph, pos=graphLocation, node_color='purple',edge_color='red' ,with_labels=True)
plt.show()
