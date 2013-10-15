from random import randint
from random import random
from animate import draw as drawAnimate
from cartoon import drawCartoon

def argmax(f, args):
	mi = None
	m = -1e10
	for i in args:
		v = f(i)
		if v > m:
			m = v
			mi = i
	return mi

def policyIteration():
	gamma = 0.8
	trans = (
			 (1 , 3 , 4 , 12), #0 
			 (0 , 2 , 5 , 13), #1
			 (3 , 1 , 6 , 14), #2
			 (2 , 0 , 7 , 15), #3
			 (5 , 7 , 0 , 8 ), #4
			 (4 , 6 , 1 , 9 ), #5
			 (7 , 5 , 2 , 10), #6
			 (6 , 4 , 3 , 11), #7
			 (9 , 11, 12, 4 ), #8
			 (8 , 10, 13, 5 ), #9
			 (11, 9 , 14, 6 ), #10
			 (10, 8 , 15, 7 ), #11
			 (13, 15, 8 , 0 ), #12
			 (12, 14, 9 , 1 ), #13
			 (15, 13, 10, 2 ), #14
			 (14, 12, 11, 3 )  #15
			) 
	rew = (
	      ( 0,-1, 0,-1), #0 
		  ( 0, 0,-5,-9), #1
		  ( 0, 0,-5,-1), #2
		  ( 0,-1, 0,-1), #3
		  (-5,-9, 0, 0), #4
		  ( 0,-5, 0,-5), #5
		  ( 0,-5, 0,-5), #6
		  (-5, 1, 0, 0), #7
		  (-5,-1, 0, 0), #8
		  ( 0,-5, 0,-5), #9
		  ( 0,-5, 0,-5), #10
		  (-5, 1, 0, 0), #11
		  ( 0,-1, 0,-1), #12
		  ( 0, 0,-5, 1), #13
		  ( 0, 0,-5, 1), #14
		  ( 0,-1, 0,-1)  #15
	     )
	print "PolicyIteration gamma: ", gamma
	print "State\t  Trans   \t\t    Reward"
	for i in range(len(trans)):
		print i,": \t",trans[i], "   \t ", rew[i]
	
	policy = [None for s in trans]
	value = [0 for s in trans]
	for p in range(100):
		for s in range(len(policy)):
			policy[s] = argmax(
			lambda(a):
				rew[s][a] + gamma * value[trans[s][a]],
			range(4))
		for s in range(len(value)):
			a = policy[s]
			value[s] = rew[s][a] + gamma * value[trans[s][a]]
	print_dot(trans, policy, "p.dot")	
	state = 3 #randint(0,len(trans)-1)
	sequence = [state]
	for i in range(8):
		state = trans[state][policy[state]]
		sequence.append(state)
	drawAnimate(sequence)
	drawCartoon(sequence) 


class Environment:
	def init(self, state = 0):
		self.state = state
		self.trans = (
				 (1 , 3 , 4 , 12), #0 
				 (0 , 2 , 5 , 13), #1
				 (3 , 1 , 6 , 14), #2
				 (2 , 0 , 7 , 15), #3
				 (5 , 7 , 0 , 8 ), #4
				 (4 , 6 , 1 , 9 ), #5
				 (7 , 5 , 2 , 10), #6
				 (6 , 4 , 3 , 11), #7
				 (9 , 11, 12, 4 ), #8
				 (8 , 10, 13, 5 ), #9
				 (11, 9 , 14, 6 ), #10
				 (10, 8 , 15, 7 ), #11
				 (13, 15, 8 , 0 ), #12
				 (12, 14, 9 , 1 ), #13
				 (15, 13, 10, 2 ), #14
				 (14, 12, 11, 3 )  #15
				) 
		self.rew = (
		      ( 0,-1, 0,-1), #0 
			  ( 0, 0,-5,-9), #1
			  ( 0, 0,-5,-1), #2
			  ( 0,-1, 0,-1), #3
			  (-5,-9, 0, 0), #4
			  ( 0,-5, 0,-5), #5
			  ( 0,-5, 0,-5), #6
			  (-5, 1, 0, 0), #7
			  (-5,-1, 0, 0), #8
			  ( 0,-5, 0,-5), #9
			  ( 0,-5, 0,-5), #10
			  (-5, 1, 0, 0), #11
			  ( 0,-1, 0,-1), #12
			  ( 0, 0,-5, 1), #13
			  ( 0, 0,-5, 1), #14
			  ( 0,-1, 0,-1)  #15
		     )

	def printPref(self):
		print "State\t  Trans   \t\t    Reward"
		for i in range(len(self.trans)):
			print i,": \t", self.trans[i], "   \t ", self.rew[i]
			
	def go(self, a):
		r = self.rew[self.state][a]
		self.state = self.trans[self.state][a]
		return self.state, r

def qLearing():
	gamma = 0.8
	epcilon = 0.1
	eta = 0.5
	T = 10000
	print "qLearing gamma: ", gamma, " epcilon: ", epcilon, " eta: ", eta, " T: ", T
	env = Environment()
	env.init()
	env.printPref()
	Q = [[0 for a in range(4)] for s in range(len(env.trans))]
	s = env.state
	while(T):
		if(random() < epcilon):
			best = randint(0,3)
		else:
			best = argmax(
			lambda(a):
				Q[s][a],
			range(4))
		newState, r = env.go(best)
		Q[s][best] +=  eta * (r + gamma*max(Q[newState]) - Q[s][best])
		s = newState
		T -= 1
	policy = [
	argmax(lambda(a):
		Q[i][a], 
	range(4)) for i in range(len(env.trans))]
	print_dot(env.trans, policy, "q.dot") 
	state = 3 #randint(0,len(trans)-1)
	sequence = [state]
	for i in range(8):
		state = env.trans[state][policy[state]]
		sequence.append(state)
	drawAnimate(sequence)
	drawCartoon(sequence)
	
	
	

def print_dot(trans, policy, filename="graph.dot"):
	f = open(filename, 'w')
	f.write("digraph{\n")
	for i in range(len(policy)):
		f.write("%d [label=\"\", image=\"step%d.png\"];\n" % (i,i+1))
	for i in range(len(policy)):
		f.write("%d -> %d;\n" % (i, trans[i][policy[i]]))
	f.write("}\n")
	f.close()

def main():
	print "+++++++++++++++++++++++++++++++++++++++++++++++++++\n\tLab 4 - Machine learning (DD2431)\n\t Viktor Collin <vcollin@kth.se>\n\t Simon Osterman <simost@kth.se>\n+++++++++++++++++++++++++++++++++++++++++++++++++++"
	policyIteration();
	print "+++++++++++++++++++++++++++++++++++++++++++++++++++"
	qLearing();
	print "+++++++++++++++++++++++++++++++++++++++++++++++++++"
  


if __name__ == '__main__':
  main()

