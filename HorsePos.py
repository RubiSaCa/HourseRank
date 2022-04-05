import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from Rank import HorseNode
from math import sqrt
pip install matplotlib
#Randomize Competitors
print("Here we have the contestants:")
Competitors = np.zeros((5, 5))
for x in range(5):
    for y in range (5):
        Competitors[x, y] = random.randint(0,1000)
print("Random 5 horses groups:")
for x in range(5):
  print("Group ", x + 1, ":", Competitors[x])
print("")

#Races 1 up to 5
print("First five Races:")
for x in range(5):
  Competitors[x].sort() 
  print("Race ", x + 1, ":", Competitors[x]) 
print("")
  
#Race 6
print("Group sort through fastest horses:")
print("                   |Race 6|")
R6 = Competitors[np.argsort(Competitors[:, -1])]  #This function sorts matrix
for x in range(5):
  print(R6[x]) 
print("")  
print("1st Horse: ", int(R6[4,4]), "pts\n")

#Race 7
R7 = [R6[2, 4], R6[3, 4], R6[3, 3], R6[4, 3], R6[4, 2]]
R7.sort()
print("Race 7:", R7, "\n")
print ("2nd Horse: ", int(R7[4]), "pts")
print ("3rd Horse: ", int(R7[3]), "pts\n")

MatrixtoArray = np.concatenate(R6)    #This will concatenate the full matrix
MatrixtoArray.sort()                  #This sorts the array
print(MatrixtoArray)

#We add each horse to our nodes

HorseNode = HorseNode(int(R6[0, 0]), "Horse 1")
HorseNode.Add(int(R6[0, 1]), "Horse 2")
HorseNode.Add(int(R6[0, 2]), "Horse 3")
HorseNode.Add(int(R6[0, 3]), "Horse 4")
HorseNode.Add(int(R6[0, 4]), "Horse 5")
HorseNode.Add(int(R6[1, 0]), "Horse 6")
HorseNode.Add(int(R6[1, 1]), "Horse 7")
HorseNode.Add(int(R6[1, 2]), "Horse 8")
HorseNode.Add(int(R6[1, 3]), "Horse 9")
HorseNode.Add(int(R6[1, 4]), "Horse 10")
HorseNode.Add(int(R6[2, 0]), "Horse 11")
HorseNode.Add(int(R6[2, 1]), "Horse 12")
HorseNode.Add(int(R6[2, 2]), "Horse 13")
HorseNode.Add(int(R6[2, 3]), "Horse 14")
HorseNode.Add(int(R6[2, 4]), "Horse 15")
HorseNode.Add(int(R6[3, 0]), "Horse 16")
HorseNode.Add(int(R6[3, 1]), "Horse 17")
HorseNode.Add(int(R6[3, 2]), "Horse 18")
HorseNode.Add(int(R6[3, 3]), "Horse 19")
HorseNode.Add(int(R6[3, 4]), "Horse 20")
HorseNode.Add(int(R6[4, 0]), "Horse 21")
HorseNode.Add(int(R6[4, 1]), "Horse 22")
HorseNode.Add(int(R6[4, 2]), "Horse 23")
HorseNode.Add(int(R6[4, 3]), "Horse 24")
HorseNode.Add(int(R6[4, 4]), "Horse 25")

HorseNode.printNode()

HorsesArray = ["", "", "", "", "", "", "", "","", "", "", "", "", "", "", "","", "", "", "", "", "", "", "",""]

for x in range(24):
  searchHorse=HorseNode.Search(MatrixtoArray[x]) 
  HorsesArray[x] = searchHorse.Name
  print(HorsesArray[x])

# GRAPHS

class Dupla:
    def _init_(self, x, y):
        self.x = x
        self.y = y

def DistCalc(Dup1, Dup2):# We use this duple to interact easier with our x,y values
    return sqrt(pow((Dup1.x - Dup2.x), 2) + pow((Dup1.y - Dup2.y), 2))  # Pithagor theme

G = nx.Graph() # We initialize our graph
vertex_G = [HorsesArray[24], HorsesArray[23], HorsesArray[22], HorsesArray[21], HorsesArray[20],HorsesArray[19], HorsesArray[18], 
              HorsesArray[17], HorsesArray[16], HorsesArray[15], HorsesArray[14], HorsesArray[13], HorsesArray[12], HorsesArray[11], 
              HorsesArray[10], HorsesArray[9], HorsesArray[8], HorsesArray[7], HorsesArray[6], HorsesArray[5],HorsesArray[4],
              HorsesArray[3], HorsesArray[2], HorsesArray[1], HorsesArray[0]]
# We created our vertex

G.add_nodes_from(vertex_G)# The we add them to our graph

edges_G = [(HorsesArray[24], HorsesArray[23]), (HorsesArray[23], HorsesArray[22]), (HorsesArray[22], HorsesArray[21]), (HorsesArray[21], HorsesArray[20]),
             (HorsesArray[20], HorsesArray[19]), (HorsesArray[19], HorsesArray[18]), (HorsesArray[18], HorsesArray[17]), (HorsesArray[17], HorsesArray[16]),
             (HorsesArray[16], HorsesArray[15]), (HorsesArray[15], HorsesArray[14]), (HorsesArray[14], HorsesArray[13]), (HorsesArray[13], HorsesArray[12]),
             (HorsesArray[12], HorsesArray[11]), (HorsesArray[11], HorsesArray[10]), (HorsesArray[10], HorsesArray[9]), (HorsesArray[9], HorsesArray[8]), 
             (HorsesArray[8], HorsesArray[7]), (HorsesArray[7], HorsesArray[6]), (HorsesArray[6], HorsesArray[5]), (HorsesArray[5], HorsesArray[4]),
             (HorsesArray[4], HorsesArray[3]), (HorsesArray[3], HorsesArray[2]), (HorsesArray[2], HorsesArray[1]), (HorsesArray[1], HorsesArray[0])]

# We create the connections(edges) with our nodes and add them
G.add_edges_from(edges_G)

locate = {HorsesArray[24]: (1, 21), HorsesArray[23]: (3, 21), HorsesArray[22]: (5, 21), HorsesArray[21]: (7, 21), HorsesArray[20]: (9, 21),
         HorsesArray[19]: (11, 21), HorsesArray[18]: (11, 19), HorsesArray[17]: (11, 17), HorsesArray[16]: (11, 15), HorsesArray[15]: (11, 13), 
         HorsesArray[14]: (11, 11), HorsesArray[13]: (11, 9), HorsesArray[12]: (11, 7), HorsesArray[11]: (11, 5), HorsesArray[10]: (11, 3),
         HorsesArray[9]: (11, 1), HorsesArray[8]: (13, 1), HorsesArray[7]: (15, 1), HorsesArray[6]: (17, 1), HorsesArray[5]: (19, 1),
         HorsesArray[4]: (21, 1), HorsesArray[3]: (21, 3), HorsesArray[2]: (21, 5), HorsesArray[1]: (21, 7), HorsesArray[0]: (21, 9)}

#Using the diccionary above, we locate each point

puntoA = Dupla()
puntoA.x = locate[HorsesArray[24]][0]
puntoA.y = locate[HorsesArray[24]][1]
puntoB = Dupla()
puntoB.x = locate[HorsesArray[23]][0]
puntoB.y = locate[HorsesArray[23]][1]
puntoC = Dupla()
puntoC.x = locate[HorsesArray[22]][0]
puntoC.y = locate[HorsesArray[22]][1]
puntoD = Dupla()
puntoD.x = locate[HorsesArray[21]][0]
puntoD.y = locate[HorsesArray[21]][1]
puntoE = Dupla()
puntoE.x = locate[HorsesArray[20]][0]
puntoE.y = locate[HorsesArray[20]][1]
puntoF = Dupla()
puntoF.x = locate[HorsesArray[19]][0]
puntoF.y = locate[HorsesArray[19]][1]
puntoG = Dupla()
puntoG.x = locate[HorsesArray[18]][0]
puntoG.y = locate[HorsesArray[18]][1]
puntoH = Dupla()
puntoH.x = locate[HorsesArray[17]][0]
puntoH.y = locate[HorsesArray[17]][1]
puntoI = Dupla()
puntoI.x = locate[HorsesArray[16]][0]
puntoI.y = locate[HorsesArray[16]][1]
puntoJ = Dupla()
puntoJ.x = locate[HorsesArray[15]][0]
puntoJ.y = locate[HorsesArray[15]][1]
puntoK = Dupla()
puntoK.x = locate[HorsesArray[14]][0]
puntoK.y = locate[HorsesArray[14]][1]
puntoL = Dupla()
puntoL.x = locate[HorsesArray[13]][0]
puntoL.y = locate[HorsesArray[13]][1]
puntoM = Dupla()
puntoM.x = locate[HorsesArray[12]][0]
puntoM.y = locate[HorsesArray[12]][1]
puntoN = Dupla()
puntoN.x = locate[HorsesArray[11]][0]
puntoN.y = locate[HorsesArray[11]][1]
puntoO = Dupla()
puntoO.x = locate[HorsesArray[10]][0]
puntoO.y = locate[HorsesArray[10]][1]
puntoP = Dupla()
puntoP.x = locate[HorsesArray[9]][0]
puntoP.y = locate[HorsesArray[9]][1]
puntoQ = Dupla()
puntoQ.x = locate[HorsesArray[8]][0]
puntoQ.y = locate[HorsesArray[8]][1]
puntoR = Dupla()
puntoR.x = locate[HorsesArray[7]][0]
puntoR.y = locate[HorsesArray[7]][1]
puntoS = Dupla()
puntoS.x = locate[HorsesArray[6]][0]
puntoS.y = locate[HorsesArray[6]][1]
puntoT = Dupla()
puntoT.x = locate[HorsesArray[5]][0]
puntoT.y = locate[HorsesArray[5]][1]
puntoU = Dupla()
puntoU.x = locate[HorsesArray[4]][0]
puntoU.y = locate[HorsesArray[4]][1]
puntoV = Dupla()
puntoV.x = locate[HorsesArray[3]][0]
puntoV.y = locate[HorsesArray[3]][1]
puntoY = Dupla()
puntoY.x = locate[HorsesArray[2]][0]
puntoY.y = locate[HorsesArray[2]][1]
puntoX = Dupla()
puntoX.x = locate[HorsesArray[1]][0]
puntoX.y = locate[HorsesArray[1]][1]
puntoZ = Dupla()
puntoZ.x = locate[HorsesArray[0]][0]
puntoZ.y = locate[HorsesArray[0]][1]

PointsH = {HorsesArray[24]: puntoA, HorsesArray[23]: puntoB, HorsesArray[22]: puntoC, HorsesArray[21]: puntoD, HorsesArray[20]: puntoE, 
          HorsesArray[19]: puntoF, HorsesArray[18]: puntoG, HorsesArray[17]: puntoH, HorsesArray[16]: puntoI, HorsesArray[15]: puntoJ, 
          HorsesArray[14]: puntoK, HorsesArray[13]: puntoL, HorsesArray[12]: puntoM, HorsesArray[11]: puntoN, HorsesArray[10]: puntoO, 
          HorsesArray[9]: puntoP, HorsesArray[8]: puntoQ, HorsesArray[7]: puntoR, HorsesArray[6]: puntoS, HorsesArray[5]: puntoT, 
          HorsesArray[4]: puntoU, HorsesArray[3]: puntoV, HorsesArray[2]: puntoY, HorsesArray[1]: puntoX, HorsesArray[0]: puntoZ}

cont: int = 0
for i in edges_G:
    Pa = PointsH[edges_G[cont][0]]
    Pb = PointsH[edges_G[cont][1]]
    G.edges[i]['distance'] = DistCalc(Pa, Pb)*100
    print('The distance between', edges_G[cont], G.edges[i],'[units]')
    cont = cont + 1
nx.draw(G, pos=locate, node_color='gray', with_labels=True)
plt.show()