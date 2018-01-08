import math, argparse

parser = argparse.ArgumentParser(description="learning stuff")  # this is storing arguments
parser.add_argument('--x', type = int, help = "Enter value of x") # argument x of function. '--x' makes it optional
parser.add_argument('y', type = int, help = "Enter value of y") # argument y of function. '--' with this it is compulsory
group = parser.add_mutually_exclusive_group()
group.add_argument('--q','--quiet', action = 'store_true', help = "choosing how output looks using group")
group.add_argument('--v','--verbose', action = 'store_true', help = "this will display more information")
args = parser.parse_args()

def formula(x, y):
    return math.pow(x, y)

if __name__ == "main":
    variable = formula(args.x, args.y)
    if args.quiet:  # In command line if we type 'python argparse.py 2 4 --q'. The following will be printed
        print(variable)
    elif args.verbose:  #In command line if we type 'python argparse.py 2 4 --v'. The following will be printed
        print("The output is: {}".format(variable))
    else:
        print('The output is: {}'.format(variable)) #n command line if we type 'python argparse.py 2 4'. The following will be printed
