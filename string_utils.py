


def split_before_uppercases(formula):
    start = 0
    end = 0
    split_formula = []
    for char in formula:
      if (end != 0) and (char.isupper() == True):
        split_formula.append(formula[start:end])
        start = end
      end += 1
    if start != end:
      split_formula.append(formula[start:end])
    return split_formula

def split_at_digit(formula):
    digit_location = 0
    for char in formula:
        if char.isdigit() == True:
          return formula[:digit_location], int(formula[digit_location: ])
        digit_location += 1
    return formula, 1

def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.  
    Example: 'H2O' → {'H': 2, 'O': 1}"""

    atoms_dictionary = {}

    for atom in split_by_capitals(molecular_formula):
        atom_name, atom_count = split_at_number(atom)
        atoms_dictionary[atom_name] = atom_count

    return atoms_dictionary



def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
