import Infer_Module;
from KnowledgeBase_Data import student_data

# Test the Engine with some examples:

# Case 1: Male Students
print("How many males student in the data with theri names?\n");
gender_Test = Infer_Module.inferenceEngine(student_data,"gender","male");
print("Total male students = ",len(gender_Test));
print("Names = ",gender_Test,"\n");

# Case 2: 3.9 GPA Students
print("How many student got 3.9 GPA?\n");
GPA_Test = Infer_Module.inferenceEngine(student_data,"GPA",3.9);
print("Total 3.9 GPA students = ",len(GPA_Test));
print("Names = ",GPA_Test,"\n");

# Case 3: 20 Years old Students
print("How many students are 20 year old also mentioned their names?\n")
age_Test = Infer_Module.inferenceEngine(student_data,"age",20);
print("Total 20 years old students = ",len(age_Test));
print("Names = ",age_Test);
