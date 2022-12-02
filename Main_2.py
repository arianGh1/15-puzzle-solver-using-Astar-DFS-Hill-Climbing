import time
import sys
import numpy as np
from Gui_2 import Gui_2
from Graphics2_2 import Graphics2_2
import time

class Node:
    def __init__(self, key):
    	# chon har gereh mitavanad ta hadeaksar 4 farzand ekhtiar konad(factor ensheab = 4)
        self.one = None
        self.two = None
        self.three = None
        self.four = None
        # meghdare khode gereh
        self.val = key



def order_check(node):
	is_it_ordered = True
	matrix = node.val.reshape(1,mat_len**2)
	
	for i in range(mat_len**2):
		
		if i< mat_len**2-1:
			if matrix[0][i] == 0:
				
				continue
			else:
				temp = matrix[0][i]
				#temp = 1
			if matrix[0][i+1]<temp and matrix[0][i+1]!=0 :
				
				is_it_ordered = False
				break		
			if matrix[0][i+1]-temp != 1 and matrix[0][i+1]!=0:
				
				is_it_ordered = False
				break	
			continue
		elif i== mat_len**2-1:
			if matrix[0][i]==1:
				
				is_it_ordered = False
				break



	return is_it_ordered

def is_in(arr,second):

	exist = False
	for element in second:
	  if (arr == element).all():
	   	exist = True
	   	break
	  else:
	    continue

	return exist


def dfs(node,iteration):
	g = Graphics2_2(node.val.reshape(1,mat_len**2)[0])
	explored = []
	frontier = []
	frontier_vals = []
	frontier.append(node)
	path = []
	path.append(node.val.reshape(1,mat_len**2)[0])

	print("\nGraphical interface will be shown if we reach the goal\n")
	print("Started DFS algorithm...\n\n")

	for index in range(iteration):
		
		if index%250 == 0:
			print("Iteration : ", index,end="")
			print("   still processing...")
		matrix = node.val
		index = np.where(matrix==0)
		i=index[0][0]
		j=index[1][0]
		

		
		q = order_check(node)
		if q:
			print("Goal found!")

			g.show_solution(path)
			return matrix
		matrix = node.val
		childs = 0

		if i > 0:
			mat1 = np.copy(matrix)
			mat1[i][j] = mat1[i - 1][j]
			mat1[i - 1][j] = 0
			if not is_in(mat1,explored):

				node.one = Node(mat1)
				child = node.one
				childs += 1
				
				frontier.append(child)
				frontier_vals.append(child.val) 

		if j > 0:
			
			mat1 = np.copy(matrix)
			mat1[i][j] = mat1[i][j - 1]
			mat1[i][j - 1] = 0
			
			
			if not is_in(mat1,explored):
				
				if childs==1:
					node.two = Node(mat1)
					child = node.two
				else:
					node.one = Node(mat1)
					child = node.one
				
				
					
				frontier.append(child)
				frontier_vals.append(child.val)


		if i < mat_len-1:
			mat1 = np.copy(matrix)
			mat1[i][j] = mat1[i + 1][j]
			mat1[i + 1][j] = 0
			if not is_in(mat1,explored):
				if childs==2:
					node.three = Node(mat1)
					child = node.three
				elif childs==1:
					node.two = Node(mat1)
					child = node.two
				else:
					node.one = Node(mat1)
					child = node.one
				childs += 1
				
				frontier.append(child)
				frontier_vals.append(child.val)

		if j < mat_len-1:
			mat1 = np.copy(matrix)
			mat1[i][j] = mat1[i][j + 1]
			mat1[i][j + 1] = 0
			if not is_in(mat1,explored):
				if childs==3:
					node.four = Node(mat1)
					child = node.four
				elif childs ==2:
					node.three = Node(mat1)
					child = node.three
				elif childs ==1:
					node.two = Node(mat1)
					child = node.two
				else:
					node.one = Node(mat1)
					child = node.one
				childs += 1
				
				frontier.append(child) 
				frontier_vals.append(child.val)


		explored.append(node.val)
		node = frontier.pop()
		#########################################################################
		matrix = node.val
		path.append(matrix.reshape(1,mat_len**2))
		#########################################################################

		frontier_vals.pop()
	g.show_solution(path)
	print("Finished!")
	print("Number of iterations wasnt enough or its not solvable")
	time.sleep(30)
class Node_2:
    def __init__(self,data,level,fval):
        """ Initialize the node with the data, level of the node and the calculated fvalue """
        self.data = data
        self.level = level
        self.fval = fval

    def generate_child(self):
        """ Generate child nodes from the given node by moving the blank space
            either in the four directions {up,down,left,right} """
        x,y = self.find(self.data,0)
        """ val_list contains position values for moving the blank space in either of
            the 4 directions [up,down,left,right] respectively. """
        val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        children = []
        for i in val_list:
            child = self.shuffle(self.data,x,y,i[0],i[1])
            if child is not None:
                child_node = Node_2(child,self.level+1,0)
                children.append(child_node)
        return children
        
    def shuffle(self,puz,x1,y1,x2,y2):
        """ Move the blank space in the given direction and if the position value are out
            of limits the return None """
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None
            

    def copy(self,root):
        """ Copy function to create a similar matrix of the given node"""
        temp = []
        print("root=",root)
        for i in root:
        	temp.append(i)
        return temp    
            
    def find(self,puz,x):
    	
    	print("puz=",puz)
    	for i in range(0,len(self.data)):
		    for j in range(0,len(self.data)):
		        if puz[i][j] == x:
		            return i,j



class Puzzle:
    def __init__(self,size):
        """ Initialize the puzzle size by the specified size,open and closed lists to empty """
        self.n = size
        self.open = []
        self.closed = []

    def accept(self):
        """ Accepts the puzzle from the user """
        puz = []
        for i in range(0,self.n):
            temp = input().split(" ")
            puz.append(temp)
        puz = np.array(puz).reshape(mat_len,mat_len)
        print("puz in accept func:",puz)
        return puz

    def f(self,start,goal):
        """ Heuristic Function to calculate hueristic value f(x) = h(x) + g(x) """
        return self.h(start.data,goal)+start.level

    def h(self,start,goal):
        """ Calculates the different between the given puzzles """
        temp = 0
        for i in range(0,self.n):
        	for j in range(0,self.n):
	            if start[i][j] != goal[i][j] and start[i][j] != 0:
	                temp += 1
        return temp
        

    def process(self,node,iteration):
    	g = Graphics2_2(node.reshape(1,mat_len**2)[0])
    	start = node.reshape(mat_len,mat_len) 
    	print(start)       
    	goal = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]).reshape(mat_len,mat_len)
    	print(goal)
    	start = Node_2(start,0,0)
    	start.fval = self.f(start,goal)
    	self.open.append(start)
    	print("\n\n")
    	path = []
    	for i in range(iteration):
    		lst = []
    		cur = self.open[0]
    		print("cur=",np.array(cur.data).reshape(1,mat_len**2))

    		path.append(np.array(cur.data).reshape(1,16)[0])
    		if(self.h(cur.data,goal) == 0):
    			break
    		for i in cur.generate_child():
    			i.fval = self.f(i,goal)
    			self.open.append(i)
    		self.closed.append(cur)
    		del self.open[0]
    		self.open.sort(key = lambda x:x.fval,reverse=False)
    	print("Finished!")
    	print("Number of iterations wasnt enough or its not solvable")
    	g.show_solution(path)



gu = Gui_2()
mat_len = 4
node = Node(np.array(gu.get_board()).reshape(4,4))

iteration = gu.get_iteration()
algorithm = gu.get_algorithm()

if algorithm == "DFS":
	dfs(node,iteration)
elif algorithm == "A*":
	puz = Puzzle(4)
	puz.process(np.array(gu.get_board()),iteration)
