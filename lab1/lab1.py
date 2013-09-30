#!/usr/bin/env python

import dtree as dt
import monkdata as data
#import drawtree as drawtree
import random


def calc_entropy():
  ent1 = dt.entropy(data.monk1)
  ent2 = dt.entropy(data.monk2)
  ent3 = dt.entropy(data.monk3)
  print "\n------------------------------\nAssignment 1 - Entropy\n------------------------------"
  print "Dataset\tEntropy"
  print "Monk1\t%.6f\nMonk2\t%.6f\nMonk3\t%.6f" % (ent1, ent2, ent3)

def calc_gain():
  print "\n------------------------------\nAssignment 2 - Average gain\n------------------------------"
  i = 1
  print "Dataset\t  a1\t\t  a2\t\t  a3\t\t  a4\t\t  a5\t\t  a6"
  s = "Monk1\t"
  for attr in data.attributes: 
    s = s + "%.6f\t" % (dt.averageGain(data.monk1, attr))
  print s
  s = "Monk2\t"
  for attr in data.attributes: 
    s = s + "%.6f\t" % (dt.averageGain(data.monk2, attr))
  print s
  s = "Monk3\t"
  for attr in data.attributes: 
    s = s + "%.6f\t" % (dt.averageGain(data.monk3, attr))
  print s

def build_tree():
  print "\n------------------------------\nAssignment 3 - Error\n------------------------------"
  tree = dt.buildTree(data.monk1, data.attributes)
#drawtree.drawTree(tree)
  print "Dataset\tE(train)\tE(test)"
  print "Monk1:\t%.6f\t%.6f" % (1-dt.check(tree, data.monk1), 1-dt.check(tree, data.monk1test))
  tree = dt.buildTree(data.monk2, data.attributes)
  print "Monk2:\t%.6f\t%.6f" % (1-dt.check(tree, data.monk2), 1-dt.check(tree, data.monk2test))
  tree = dt.buildTree(data.monk3, data.attributes)
  print "Monk3:\t%.6f\t%.6f" % (1-dt.check(tree, data.monk3), 1-dt.check(tree, data.monk3test))


def calc_next_level():
  #print "\nAverage gain when a5 is choosen"
  print "\nA5\t  a1\t\t  a2\t\t  a3\t\t  a4\t\t  a5\t\t  a6"
  s = "A5(" 
  for val in data.attributes[4].values:
    subset = dt.select(data.monk1, data.attributes[4], val)
    t = "\t"
    for attr in data.attributes: 
      t = t + "%.6f\t" % (dt.averageGain(subset, attr))
    print val , t
    best = dt.bestAttribute(subset, data.attributes)
    s = s + best.name + "("
    #print "best attribute: ", best.name
    for value in best.values:
      #print "choose: ", value, "mostCommon: ", dt.mostCommon(dt.select(subset, best, value))
      if(dt.mostCommon(dt.select(subset, best, value))): 
        s = s + "+"
      else:
        s = s + "-"
    s = s + ")"
  s = s + ")"
  print "\nOur tree:\t", s
  print "Build tree:\t", dt.buildTree(data.monk1, data.attributes, 2)
  

def prune():
  print "\n------------------------------\nAssignment 4 - Pruning\n------------------------------"
  print "Dataset\t  0.3\t\t  0.4\t\t  0.5\t\t  0.6\t\t  0.7\t\t  0.8"
  partSizes = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
  r = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
  i = 0
  for size in partSizes:  
    for j in range(100):
      training, test = partition(data.monk1, size)
      bestTree = dt.buildTree(training, data.attributes)
      bestClass = dt.check(bestTree, test)
      better = True
      while better:
        better = False
        for subTree in dt.allPruned(bestTree):
          if dt.check(subTree, test) > bestClass:
            bestTree = subTree
            bestClass = dt.check(subTree, test)
            better = True
      r[i] += (1-dt.check(bestTree, data.monk1test))
    i += 1
  print "Monk1\t%0.6f\t%0.6f\t%0.6f\t%0.6f\t%0.6f\t%0.6f\t" % (r[0]/100, r[1]/100, r[2]/100, r[3]/100, r[4]/100, r[5]/100)
  r = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
  i = 0
  for size in partSizes:  
    for j in range(100):
      training, test = partition(data.monk3, size)
      bestTree = dt.buildTree(training, data.attributes)
      bestClass = dt.check(bestTree, test)
      better = True
      while better:
        better = False
        for subTree in dt.allPruned(bestTree):
          if dt.check(subTree, test) >= bestClass:
            bestTree = subTree
            bestClass = dt.check(subTree, test)
            better = True
      r[i] += (1-dt.check(bestTree, data.monk3test))
    i += 1
  print "Monk3\t%0.6f\t%0.6f\t%0.6f\t%0.6f\t%0.6f\t%0.6f\t" % (r[0]/100, r[1]/100, r[2]/100, r[3]/100, r[4]/100, r[5]/100)
    #drawtree.drawTree(bestTree)

def partition(data, fraction):
  ldata = list(data)
  random.shuffle(ldata)
  breakPoint = int(len(ldata) * fraction)
  return ldata[:breakPoint], ldata[breakPoint:]

def main():
  print "+++++++++++++++++++++++++++++++++++++++++++++++++++\n\tLab 1 - Machine learning (DD2431)\n\t Viktor Collin <vcollin@kth.se>\n\t Simon Osterman <simost@kth.se>"
  calc_entropy()
  calc_gain()
  calc_next_level()
  build_tree()
  prune()
  print "+++++++++++++++++++++++++++++++++++++++++++++++++++"
  


if __name__ == '__main__':
  main()
