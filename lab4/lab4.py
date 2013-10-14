from random import randint
from animate import draw
gamma = 0.1

def argmax(f, args):
	mi = None
	m = -1e10
	for i in args:
		v = f(i)
		if v > m:
			m = v
			mi = i
	return mi


trans = ((1 , 3 , 4 , 12), #0 
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
		 (14, 12, 11, 3 )) #15
		
rew = ((0 , 0 , 0 , 0), #0 
	   (0 , 0 ,-1 ,-1), #1
	   (0 , 0 ,-1 , 0), #2
	   (0 , 0 , 0 , 0), #3
	   (-1,-1 , 0 , 0), #4
	   (0 ,-1 , 0 ,-1), #5
	   (0 ,-1 , 0 ,-1), #6
	   (-1, 1 , 0 , 0), #7
	   (-1, 0 , 0 , 0), #8
	   (0 ,-1 , 0 ,-1), #9
	   (0 ,-1 , 0 ,-1), #10
	   (-1, 0 , 0 , 0), #11
	   (0 , 0 , 0 , 0), #12
	   (0 , 0 ,-1 , 1), #13
	   (0 , 0 ,-1 , 0), #14
	   (0 , 0 , 0 , 0)) #15
	
def policyIteration():
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
			
		
	state = randint(0,len(trans)-1)
	sequence = [state]
	for i in range(16):
		state = policy[state]
		sequence.append(state)
	draw(sequence)
	
	


def main():
  print "+++++++++++++++++++++++++++++++++++++++++++++++++++\n\tLab 4 - Machine learning (DD2431)\n\t Viktor Collin <vcollin@kth.se>\n\t Simon Osterman <simost@kth.se>"
  policyIteration();
  print "+++++++++++++++++++++++++++++++++++++++++++++++++++"
  


if __name__ == '__main__':
  main()

