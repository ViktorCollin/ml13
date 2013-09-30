from cvxopt.solvers import qp
from cvxopt.base import matrix
import numpy
import pylab
import random
import math


def generateData():
	classA = [(random.normalvariate(-1.5, 1), random.normalvariate(0.5, 1), 1.0) for i in range(5)] + \
			 [(random.normalvariate( 1.5, 1), random.normalvariate(0.5, 1), 1.0) for i in range(5)]

	classB = [(random.normalvariate(0.0, 0.5), random.normalvariate(-0.5, 0.5), -1.0) for i in range(10)]
	
	print "classA =", classA
	print "classB =", classB
	data = classA + classB
	random.shuffle(data)
	return classA, classB, data

def kernel_polynomial(x, y, p):
	return (numpy.dot(x,y) + 1)**p

def buildP(data):
	p = array # fix
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
	for i in range(n):
		q[i] = -1
		


def plotDots(classA, classB):
	pylab.hold(True)
	pylab.plot([p[0] for p in classA], [p[1] for p in classA], 'bo')
	pylab.plot([p[0] for p in classB], [p[1] for p in classB], 'ro')
	pylab.show()


def plotLines():
	xrange = numpy.arange(-4, 4, 0.05)
	yrange = numpy.arange(-4, 4, 0.05)
	grid = matrix([[indicator(x, y) for y in yrange] for x in xrange])
	pylab.contour(xrange, yrange, grid, (-1.0, 0.0, 1.0), colors = ('red', 'black', 'blue'), linewidths = (1, 3, 1))

def main():
	classA, classB, data = generateData();
	plotDots(classA, classB);
	
if __name__ == '__main__':
  main()