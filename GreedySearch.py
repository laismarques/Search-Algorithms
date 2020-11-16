import numpy as np
class Node:
    def __init__(self, label, goal_distance):
        self.label = label
        self.visitaded = False
        self.adjacent = []
        self.goal_distance = goal_distance
    
    def add_adjacent(self, adjacent):
        self.adjacent.append(adjacent)

    def show_adjacent(self):
        for i in self.adjacent:
            print(i.vertex.label, i.distance)
    
class Adjacent:
    def __init__(self, vertex, distance):
        self.vertex = vertex
        self.distance = distance

class Graph:
    arad = Node('Arad', 366)
    zerind = Node('Zerind', 374)
    oradea = Node('Oradea', 380)
    sibiu = Node('Sibiu', 253)
    timisoara = Node('Timisoara', 329)
    lugoj = Node('Lugoj', 244)
    mehadia = Node('Mehadia', 241)
    dobreta = Node('Dobreta', 242)
    craiova = Node('Craiova', 160)
    rimnicu = Node('Rimnicu', 193)
    fagaras = Node('Fagaras', 178)
    pitesti = Node('Pitesti', 98)
    bucharest = Node('Bucharest', 0)
    giurgiu = Node('Giurgiu', 77)
    

    arad.add_adjacent(Adjacent(zerind, 75))
    arad.add_adjacent(Adjacent(sibiu, 140))
    arad.add_adjacent(Adjacent(timisoara, 118))

    zerind.add_adjacent(Adjacent(arad, 75))
    zerind.add_adjacent(Adjacent(oradea, 71))

    oradea.add_adjacent(Adjacent(zerind, 71))
    oradea.add_adjacent(Adjacent(sibiu, 151))

    sibiu.add_adjacent(Adjacent(oradea, 151))
    sibiu.add_adjacent(Adjacent(arad, 140))
    sibiu.add_adjacent(Adjacent(fagaras, 99))
    sibiu.add_adjacent(Adjacent(rimnicu, 80))

    timisoara.add_adjacent(Adjacent(arad, 118))
    timisoara.add_adjacent(Adjacent(lugoj, 111))

    lugoj.add_adjacent(Adjacent(timisoara, 111))
    lugoj.add_adjacent(Adjacent(mehadia, 70))

    mehadia.add_adjacent(Adjacent(lugoj, 70))
    mehadia.add_adjacent(Adjacent(dobreta, 75))

    dobreta.add_adjacent(Adjacent(mehadia, 75))
    dobreta.add_adjacent(Adjacent(craiova, 120))

    craiova.add_adjacent(Adjacent(dobreta, 120))
    craiova.add_adjacent(Adjacent(pitesti, 138))
    craiova.add_adjacent(Adjacent(rimnicu, 146))

    rimnicu.add_adjacent(Adjacent(craiova, 146))
    rimnicu.add_adjacent(Adjacent(sibiu, 80))
    rimnicu.add_adjacent(Adjacent(pitesti, 97))

    fagaras.add_adjacent(Adjacent(sibiu, 99))
    fagaras.add_adjacent(Adjacent(bucharest, 211))

    pitesti.add_adjacent(Adjacent(rimnicu, 97))
    pitesti.add_adjacent(Adjacent(craiova, 138))
    pitesti.add_adjacent(Adjacent(bucharest, 101))

    bucharest.add_adjacent(Adjacent(fagaras, 211))
    bucharest.add_adjacent(Adjacent(pitesti, 101))
    bucharest.add_adjacent(Adjacent(giurgiu, 90))

graph = Graph()
graph.arad.show_adjacent()

class SortedList:
    def __init__(self, size):
        self.size = size
        self.last_position = -1
        self.values = np.empty(self.size, dtype=object)
    # O(n)
    def show(self):
        if self.last_position == -1:
            print("The list is empty")
        else:
            for i in range( self.last_position + 1):
                print("[",i,"]", "-", self.values[i].label, "-", self.values[i].goal_distance)
    # O(n)
    def add(self, node):
        if self.last_position == self.size -1:
            print("The List is Full")
            return -1

        position = 0
        for i in range(self.last_position + 1):
            position = i
            if self.values[i].goal_distance > node.goal_distance:
                break
            if i == self.last_position:
                position = i + 1

        x = self.last_position
        while x >= position:
            self.values[x + 1] = self.values[x]
            x -=1
        self.values[position] = node
        self.last_position +=1

list = SortedList(5)
list.add(graph.arad)
list.add(graph.craiova)  
list.add(graph.bucharest) 
list.add(graph.dobreta)

list.show()

class GreedySearch():
    def __init__(self, goal):
        self.goal = goal 
        self.find = False

    def search(self, current):
        print("----------")
        print("Current: {}".format(current.label))
        current.visitaded = True

        if current == self.goal:
            self.find = True
        else:
            sorted_list = SortedList(len(current.adjacent))

            for i in current.adjacent:
                if i.vertex.visitaded == False:
                    i.vertex.visitaded == True
                    sorted_list.add(i.vertex)
            sorted_list.show()

            if sorted_list.values[0] != None:
                self.search(sorted_list.values[0])

greedy_search = GreedySearch(graph.bucharest)
greedy_search.search(graph.arad)