# -*- coding: utf-8 -*-
"""
Created on Wed May  8 19:36:22 2024

@author: Admin
"""

# PR : 03
# (Dijjkshtra Algo) 
class Dijkstra:
    def __init__(self) -> None:
        self.vertices = int(input("Enter number of vertices: "))
        self.graph = [[float('inf')]*self.vertices for _ in range(self.vertices)]

        self.edges = int(input("Enter number of edges: "))
        print("Start\tEnd\tDistance")
        for inp in range(self.edges):
            v1,v2,e = input().split(" ")
            v1 = int(v1)
            v2 = int(v2)
            e = int(e)
            self.graph[v1-1][v2-1] = e
            self.graph[v2 - 1][v1- 1] = e
        
        for i in range(self.vertices):
            self.graph[i][i] = 0
    
    def printMatrix(self):
        print("\t",end="")
        for i in range(self.vertices):
            print(i+1,end="\t")
        print()
        for i,row in enumerate(self.graph):
            print(i+1,end="\t")
            for ele in row:
                print(ele,end="\t")
            print()
    
    def solve(self):
        source = int(input("Enter starting node:"))
        visited = set()
        distances = [float('inf')] * self.vertices
        distances[source - 1] = 0

        while True:
            minDist = float('inf')
            minId = -1
            for i,dist in enumerate(distances):
                if dist < minDist and i not in visited:
                    minDist = dist
                    minId = i
            
            if minId == -1:
                break

            for i,distance in enumerate(self.graph[minId]):
                if distances[i] > minDist + distance:
                    distances[i] = minDist + distance
            visited.add(minId)
        
        print(f"Distances from source {source}:")
        for i,distance in enumerate(distances):
            print(f"Distance to {i+1}: {distance}")



solver = Dijkstra()
solver.printMatrix()
solver.solve()

# output :
# Enter number of vertices: 5
# Enter number of edges: 8
# Start	End	Distance
# 1 2 5
# 1 3 10
# 1 4 8
# 2 5 8
# 3 5 9
# 3 4 7
# 2 3 6
# 4 5 9
# 	1	2	3	4	5	
# 1	0	5	10	8	inf	
# 2	5	0	6	inf	8	
# 3	10	6	0	7	9	
# 4	8	inf	7	0	9	
# 5	inf	8	9	9	0	
# Enter starting node:1
# Distances from source 1:
# Distance to 1: 0
# Distance to 2: 5
# Distance to 3: 10
# Distance to 4: 8
# Distance to 5: 13