#!/usr/bin/env python

import dtree as dt
import monkdata as data
import drawtree as drawtree
import random


def calc_entropy():
  ent1 = dt.entropy(data.monk1)
  ent2 = dt.entropy(data.monk2)
  ent3 = dt.entropy(data.monk3)
  print "Entropy: "
  print "Monk1: " , ent1 , "\nMonk2: ", ent2 ,"\nMonk3: " , ent3

def calc_gain():

  print "\nAverage Gain: "
  i = 1
  for attr in data.attributes:
    res1 = dt.averageGain(data.monk1, attr)
    res2 = dt.averageGain(data.monk2, attr)
    res3 = dt.averageGain(data.monk3, attr)
    print "\nAttribute", i, "\nMonk1: " , res1 , "\nMonk2: ", res2 ,"\nMonk3: " , res3
    i += 1

def build_tree():
  print "---------------\nAssignment 3\n---------------"
  tree = dt.buildTree(data.monk1, data.attributes)
#drawtree.drawTree(tree)
  print "dataset\ttraining\ttest"
  print "Monk1:\t%.6f\t%.6f" % (dt.check(tree, data.monk1), dt.check(tree, data.monk1test))
  tree = dt.buildTree(data.monk2, data.attributes)
  print "Monk2:\t%.6f\t%.6f" % (dt.check(tree, data.monk2), dt.check(tree, data.monk2test))
  tree = dt.buildTree(data.monk3, data.attributes)
  print "Monk3:\t%.6f\t%.6f" % (dt.check(tree, data.monk3), dt.check(tree, data.monk3test))


def calc_next_level():
  print "\nAverage gain when a5 is choosen"
  for val in data.attributes[4].values:
    subset = dt.select(data.monk1, data.attributes[4], val)
    best = dt.bestAttribute(subset, data.attributes)
    print "best attribute: ", best.name
    for value in best.values:
      print "choose: ", value, "mostCommon: ", dt.mostCommon(dt.select(subset, best, value))

def prune():
  partSizes = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
  for size in partSizes:
    training, test = partition(data.monk1, size)
    bestTree = dt.buildTree(training, data.attributes)
    bestClass = dt.check(bestTree, test)
    better = True
    while better:
      better = False
      for subTree in dt.allPruned(bestTree):
        if dt.check(subTree, training) > bestClass:
          bestTree = subTree
          bestClass = dt.check(subTree, training)
          better = True
    print bestTree
    drawtree.drawTree(bestTree)

def partition(data, fraction):
  ldata = list(data)
  random.shuffle(ldata)
  breakPoint = int(len(ldata) * fraction)
  return ldata[:breakPoint], ldata[breakPoint:]

def main():
  calc_entropy()
  calc_gain()
  build_tree()
#calc_next_level()
  prune()
  


if __name__ == '__main__':
  main()
