#!/usr/bin/env python

import dtree as dt
import monkdata as data
import drawtree as drawtree


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
  tree = dt.buildTree(data.monk1, data.attributes)
  print "\nTest: "
  print(dt.check(tree, data.monk1test))
  print "\nTraining: "
  print(dt.check(tree, data.monk1)) #??

def main():
  calc_entropy()
  calc_gain()
  build_tree()


if __name__ == '__main__':
	main()
