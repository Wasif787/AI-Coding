#To check how many students has mentioned attribute:
def has_attribute(student,attribute,value):
    # student.get(attribute) compares the attribute to the given
    # attribute value in Test_Engine and if it matches it store
    # the value in infered_Array.
    return student.get(attribute) == value;
