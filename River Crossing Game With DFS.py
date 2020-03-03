#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-

class Stack:
    def __init__(self):
        self.items = []
    def enstack(self, node):
        self.items.append(node)
    def destack(self):
        return self.items.pop()  # updated 
    def isEmpty(self):
        if len(self.items) == 0 : return True
        else: return False

class Problem:
    def __init__(self,i,g):
        self.initState=i
        self.goalState=g
        
    def isGoal(self, s):
        if self.goalState == s:
            return True
        else:
            return False
        
    def eats(self,state):
        if state[1]==state[2] and state[0]!=state[1]:
            return True
        elif state[2]==state[3] and state[0]!=state[2]:
            return True
        else:
            return False
    
    def validMove(self,state):
        if self.eats(state):
            return False
        else:
            return True
        
    def crossing(self,state):
        possibleStates =[]
        child = state[:]    
        child[0] = not child[0]

        possibleStates.append(child)

        for i in range(1,4):
            child1 = child[:]
            if state[0] == state[i]:  
                child1[i]=not child1[i]
                possibleStates.append(child1)
        return possibleStates
        
        
    def sucFN(self,state):
        children1=[]
        for i in self.crossing(state):
            if self.validMove(i):
                children1.append(i)  
        return children1
        
class Node:
    def __init__(self,s,p,d):
        self.state = s
        self.parent=p
        self.depth=d

        
    def solutionPath(self):
        path = self.state
        if self.depth == 0: 
            return path
        else:
            return path, self.parent.solutionPath()


class DFS:
    def __init__(self, p):
        self.numberGeneratedNodes = 0
        self.prob = p
        self.frontier = Stack()      
        self.visited = []
        
    def expand(self,parent):
        children = []
        for i in self.prob.sucFN(parent.state):
            s = Node(i,parent,parent.depth+1)
            children.append(s)
        self.numberGeneratedNodes += len(children)
        return children

    
    def solution(self):
        root = Node(self.prob.initState,None,0)
        self.frontier.enstack(root)
        while not self.frontier.isEmpty():
            parent = self.frontier.destack()
            self.visited.append(parent.state)
            if self.prob.isGoal(parent.state):
                return parent
            expandedNodes = self.expand(parent)
            for i in expandedNodes:
                if i.state not in self.visited:
                    self.frontier.enstack(i)
        return False
        

prob = Problem([False, False, False, False], [True, True, True, True])
dfs = DFS(prob)
goalNode = dfs.solution()
print(goalNode)
print('Node Generated %d'%(dfs.numberGeneratedNodes))
print(goalNode.solutionPath())


# In[ ]:




