#Start with some desgins that need to be printed.
#unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
#completed_models = []

#Simulate printing each design, until none are left.
#Move each design to completed_models after printing.
#while unprinted_designs:
 #   current_design = unprinted_designs.pop()
  #  print(f"Printing model: {current_design}")
   # completed_models.append(current_design)

#Display all the completed models.
#print("\nThe following models have been printed:")
#for completed_model in completed_models:
 #   print(completed_model)

#def print_models(unprinted_designs, completed_models):
#    """
 #   Simulate printing each desing, untill none are left.
  #  Move each design to completed_models after printing.
   # """
   # while unprinted_designs:
    #    current_design = unprinted_designs.pop()
     #   print(f"Printing model: {current_design}")
      #  completed_models.append(current_design)

#def show_completed_models(completed_models):
 #   """Show all the models that were printed"""
  #  print("\nThe following models have been printed:")
   # for completed_model in completed_models:
    #    print(completed_model)

import printing_functions as p
from printing_functions import print_models
from printing_functions import print_models as fn
from printing_functions import*

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []



p.print_models(unprinted_designs[:], completed_models)
p.show_completed_models(completed_models)
print(unprinted_designs)