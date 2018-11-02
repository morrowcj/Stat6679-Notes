#!/usr/bin/env python

# import libraries
import math
import argparse

# argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("-n", type = int,
    help = "total number of items to choose from")
parser.add_argument("-k", type = int,
    help = "number of items to choose")
parser.add_argument("--log", action = 'store_true',
    help = "returns the log binomial coefficient")
parser.add_argument("--test", action = 'store_true',
    help = "tests the module and quites" )
parser.add_argument("--debug", action = 'store_true', help = "used to debug the program")
args = parser.parse_args()

# logfactorial start
def logfactorial(n,k = 0):
    """
    compute log(n!) or log(n!/k!) 
    
    arguments: n, k (optional; default = 0)
    
    >>> round(logfactorial(5),4)
    4.7875
    >>> logfactorial(1)
    0.0
    >>> round(logfactorial(10,2),4)
    14.4113
    >>> logfactorial(5,5)
    0.0
    """
    assert type(n) == int, "n must be an integer"
    assert type(k) == int, "k must be an integer"
    assert n >= 0, "n must be positive"
    assert k >= 0, "k must be 0 or positive"
    
    if k > n:
      return(0.0) #log(1)=0
    
    ## set iterator
    value = 0.0 # float so that additions will always be floats
    for i in range(k+1,n+1):
      ## add current log(i) to iterator
      ### When k=0: log(n!) but when k>0: log(n!) - log(k!) = log(n!/k!) 
      value += math.log(i)
    return(value)    

# choose start
def choose(n,k,float=False,log=False):
  """
  >>> choose(5,1)
  5
  >>> choose(10,4)
  210
  >>> choose(5,5)
  1
  >>> choose(5,5,float = True)
  1.0
  """
  
  # log(n!/k!) - log((n-k)!)
  log_value = logfactorial(n, k) - logfactorial(n-k)
  ## e^log_value
  if float == False:
    if log == True:
      value = round(log_value,0)
    else:
      value = round(math.exp(log_value))
  else:
      if log == True:
        value = log_value
      else:
        value = math.exp(log_value)

  ## return value
  return(value)
  
# test function start
def test_drive():    
  print("logfactorial(0) =", logfactorial(0))
  print("logfactorial(150,40) =", logfactorial(150,40))
  print("choose(5,1) =", choose(5,1))
  print("choose(5,2) =", choose(5,2))
  print("log(choose(5,2)) =", choose(5,2, log = True))
  print("choose(5,5) =", choose(5,5))
  if args.n is not None and args.k is not None:
    print("n = ", args.n)
    print("k = ", args.k)
    if args.log:
      print("log(choose(n, k)) =", choose(args.n,args.k,float = True,log = True))
    else:
      print("choose(n, k) =", choose(args.n,args.k))
  
# script execute mode
## execute only if using as script (not import binomial.py)
if __name__ == '__main__':
  
    ## always execute doc test
    if args.test:
      import doctest
      print("testing the module...")
      doctest.testmod()
      print("done with tests")
    
    ## tests  
    if args.debug:
      print("Debug mode:")
      import sys # import sys for system info
      print("Python:", sys.version, "\n-----------") # print version info
      print("args = ", args) # arguments 
      test_drive() # run test function
    else:
      ## if n and k are present
      if args.n is not None and args.k is not None:
        ## --log functionality
        if args.log:
          print(choose(args.n,args.k,float = True, log = True))
        else:
          print(choose(args.n,args.k))
