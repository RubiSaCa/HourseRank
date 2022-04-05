from HorsePos.py import Horse

class HorseNode:

    #CONSTRUCTOR

    def __init__(self, Time, Name):
        self.root = Horse(Time, Name)

    #PRIVATE FUNCTIONS

    def __RecursiveAdd(self, Node, Time, Name):
        if Time < Node.Time:
            if Node.Left is None:
                Node.Left = Horse(Time, Name)
            else:
                self.__RecursiveAdd(Node.Left, Time, Name)
        else:
            if Node.Right is None:
                Node.Right = Horse(Time, Name)
            else:
                self.__RecursiveAdd(Node.Right, Time, Name)

    def __Order(self, Node):
        if Node is not None:
            self.__Order(Node.Right)
            print(Node.Name, ": ", Node.Time)
            self.__Order(Node.Left)
    
    def __Search(self, node, Time):
        if node is None:
            return None
        if node.Time == Time:
            return node
        if Time < node.Time:
            return self.__Search(node.Left, Time)
        else:
            return self.__Search(node.Right, Time)

    # PUBLIC FUNCTIONS

    def Add(self, Time, Name):
        self.__RecursiveAdd(self.root, Time, Name)

    def printNode(self):
        print("Ordered Horse Tree: ")
        self.__Order(self.root)
        print("")

    def Search(self, Time):
        return self.__Search(self.root, Time)