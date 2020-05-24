#def get_formatted_name(first_name, last_name):
 #   """Return a full name, neatly formatted"""
  #  full_name = f"{first_name} {last_name}"
   # return full_name.title()

#musician = get_formatted_name('jimi', 'hendrix')
#print(musician)

#def get_formatted_name(first_name, last_name, middle_name = ''):
 #   """Return a full name, neatly formatted."""
  #  if middle_name:
   #      full_name = f"{first_name} {middle_name} {last_name}"
    #else:
    #    full_name = f"{first_name} {last_name}"
    #return full_name.title()

#musician = get_formatted_name('jimi', 'hendrix')
#print(musician)

#musician = get_formatted_name('john', 'lee', 'hooker')
#print(musician)

def build_person(first_name, last_name, age = None):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age = 27)
print(musician)
