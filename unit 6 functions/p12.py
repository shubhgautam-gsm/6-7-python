# By using args* the variable-length arguments, we can pass any number of arguments.
def winners(*names):
 print("winner ",type(names))
 print("printing the winners names...")
 for name in names:
  print(name)

winners("Prince","Divyang","Priya","Het",'Jay')

