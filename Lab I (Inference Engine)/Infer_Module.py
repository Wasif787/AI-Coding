from hasAttribute_Module import has_attribute;
#Inference Engine funtion:
def inferenceEngine(student_data,attribute,value):
    infered_Array=[];
    # here attributes used as an x in loops
    # this attributes is like age, gender, GPA etc
    # And when it select the attribute it called the function has_attribute.
    for student, attributes in student_data.items():
        if has_attribute(attributes,attribute,value):
            infered_Array.append(student);
    return infered_Array;

