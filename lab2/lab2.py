from cvxopt.solvers import qp
from cvxopt.base import matrix
import numpy
import pylab
import random
import math

MIN_SLACK = 1000000000000000

alpha = []
data = []

C = MIN_SLACK

def kernel(x,y):
	# polynomial
	#return kernel_polynomial(x,y,3) 
	
	#radial basis
	#return kernel_gaussian(x, y, 2.5)
	#return kernel_rational_quadratic(x, y, 10)
	
	# circular
	return kernel_circular(x,y, 0.1)

def Data():
	
	#return test0()
	#return test1()
	#return test2()
	return test3()
	#return generateData()

def generateData():
	classA = [(random.normalvariate(0.0, 1.5), random.normalvariate(0, 1.5), 1.0) for i in range(5)] + \
			 [(random.normalvariate(0.0, 1.5), random.normalvariate(0, 1.5), 1.0) for i in range(5)]


	classB = [(random.normalvariate(0.0, 1.5), random.normalvariate(0, 1.5),-1.0) for i in range(10)]

	data = classA + classB
	random.shuffle(data)
	print "data =", data
	return data

def test0():
	import test0
	print "test0 =", test0.data
	return test0.data	
	
def test1():
	import test1
	print "test1 =", test1.data
	return test1.data

def test2():
	import test2
	print "test2 =", test2.data
	return test2.data
	
def test3():
	import test3
	print "test3 =", test3.data
	return test3.data

def test4():
	import test4
	print "test4 =", test4.data
	return test4.data

def kernel_polynomial(x, y, order):
	return ((x[0]*y[0] + x[1]*y[1]) + 1)**order

def kernel_gaussian(x, y, sigma):
	length = (x[0]-y[0])**2+(x[1]-y[1])**2
	return math.e**(0-(length/(2*sigma**2))) 
		
def kernel_rational_quadratic(x, y, c):
	length = (x[0]-y[0])**2+(x[1]-y[1])**2
	return 1 - (length/(length + c))
	
def kernel_circular(x, y, zigma):
	length = math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)
	if(length < zigma):
		return (2/math.pi) * ( math.acos(0-length/zigma) - ((length/zigma)*math.sqrt(1-(length/zigma)**2)) )
	else:
		return 0

def buildP(data):
	p = [[0 for x in xrange(len(data))] for x in xrange(len(data))]
	i=0
	for pi in data:
		j = 0
		for pj in data:
			#if(j != i):
			p[i][j] = pi[2]*pj[2]*kernel(pi,pj)
			j += 1
		i += 1
	return p
	
def buildQGH(n):
  global C
  q = [-1.0 for x in xrange(n)]
  h = [0.0 for x in xrange(2*n)]

  G = [[0.0 for x in xrange(2*n)] for x in xrange(n)]
  for i in range(n):
    h[n+i] = C
    G[i][i] = -1.0
    G[i][n+i] = 1.0
  return q,h,G

def plotDots():
  pylab.hold(True)
  for p in data:
	if(p[2] == 1.0):
	  pylab.plot(p[0], p[1], 'bo')
	else:
	  pylab.plot(p[0], p[1], 'rv')
  #pylab.plot([p[0] for p in classA], [p[1] for p in classA], 'bo')
  #pylab.plot([p[0] for p in classB], [p[1] for p in classB], 'ro')
  xrange = numpy.arange(-4, 4, 0.05)
  yrange = numpy.arange(-4, 4, 0.05)
  grid = matrix([[indicator(x, y) for y in yrange] for x in xrange])
  pylab.contour(xrange, yrange, grid, (-1.0, 0.0, 1.0), colors = ('red', 'black', 'blue'), linewidths = (1, 3, 1))
  pylab.show()

def generateAlpha(P,q,h,G):
  threshold = 0.00001
  r = qp(matrix(P), matrix(q), matrix(G, (2*len(data), len(data)), 'd'), matrix(h))
  if(r['status'] != 'optimal'):
	print "I failed =("
	exit(-1)
  alpha = list(r['x'])
  for a in xrange(len(alpha)):
    if abs(alpha[a]) < threshold:
      alpha[a] = 0.0
  return alpha

def indicator(x, y):
	i = 0
	ret = 0
	for d in data:
		if(alpha[i] != 0.0):
			ret += alpha[i]*d[2]*kernel(d,(x,y))
		i += 1
	return ret

def main():
  global alpha
  global data
  data = Data()
  P = buildP(data)
  q, h, G = buildQGH(len(data))
  alpha = generateAlpha(P,q,h,G)
  plotDots()

if __name__ == '__main__':
  main()
