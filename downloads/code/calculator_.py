mport operator as op
import timeit

def solve(a,b):
    operate = {'+': op.add(a,b),
              '-': op.sub(a,b),
              '*': op.mul(a,b),
              '/': op.div(a,b),
              'pow': op.pow(a,b),
              'mod': op.mod(a,b)
              }

def exponent(a):
    n_power = {'square': op.mul(a,a)
               'cube': op.mul(a,a,a)
              }
def main():
    while True:
        user_input = raw_input("> ")
        if user_input == 'q':
            break
        tokens = user_input.split()

main()

