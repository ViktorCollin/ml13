from cvxopt.solvers import qp
from cvxopt.base import matrix
import numpy
import pylab
import random
import math

alpha = []
data = []

def generateData():
	classA = [(random.normalvariate(-1.5, 1), random.normalvariate(0.5, 0.5), 1.0) for i in range(5)] + \
			 [(random.normalvariate( 1.5, 1), random.normalvariate(0.5, 0.5), 1.0) for i in range(5)]

	classB = [(random.normalvariate(0.0, 0.5), random.normalvariate(-2.0, 0.5), -1.0) for i in range(10)]
	
	print "classA =", classA
	print "classB =", classB
	data = classA + classB
	random.shuffle(data)
	return classA, classB, data

def kernel_polynomial(x, y, p):
	return (numpy.dot(x,y) + 1)**p

def buildP(data):
	p = [[0 for x in xrange(len(data))] for x in xrange(len(data))]
	i=0
	for pi in data:
		j = 0
		for pj in data:
			#if(j != i):
			p[i][j] = pi[2]*pj[2]*kernel_polynomial(pi,pj,1)
			j += 1
		i += 1
	return p
	
def buildQGH(n):
  q = [-1.0 for x in xrange(n)]
  h = [0.0 for x in xrange(n)]
  G = [[0.0 for x in xrange(n)] for x in xrange(n)]
  for i in range(n):
    G[i][i] = -1.0
  return q,h,G

def plotDots(classA, classB):
  pylab.hold(True)
  pylab.plot([p[0] for p in classA], [p[1] for p in classA], 'bo')
  pylab.plot([p[0] for p in classB], [p[1] for p in classB], 'ro')
  xrange = numpy.arange(-4, 4, 0.05)
  yrange = numpy.arange(-4, 4, 0.05)
  grid = matrix([[indicator(x, y) for y in yrange] for x in xrange])
  pylab.contour(xrange, yrange, grid, (-1.0, 0.0, 1.0), colors = ('red', 'black', 'blue'), linewidths = (1, 3, 1))
  pylab.show()

def generateAlpha(P,q,h,G):
  threshold = 0.00001
  r = qp(matrix(P), matrix(q), matrix(G), matrix(h))
  alpha = list(r['x'])
  for a in xrange(len(alpha)):
    if alpha[a] < threshold:
      alpha[a] = 0.0
  return alpha

def indicator(x, y):
  i = 0
  ret = 0
  for d in data:
    ret += alpha[i]*d[2]*kernel_polynomial(d,(x,y,0), 1)
    i += 1
  return ret

def main():
  global alpha
  global data
  classA, classB, data = generateData()
  P = buildP(data)
  q, h, G = buildQGH(len(data))
  alpha = generateAlpha(P,q,h,G)
  plotDots(classA, classB)

if __name__ == '__main__':
  main()
