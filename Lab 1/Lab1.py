#Exercise Dir and Help:
s='abc';
print(dir(s));
print(help(s.find));
print(s.find('b'));

print(s.capitalize());
print(s.index('a'));
print(s.isupper());
print(s.replace('a','m'));

#Exercise python input output following operations:
#(i):
print('"Swap Code"');
print("Enter four input values separated by enter: ");
a= int(input());
b= int(input());
c= int(input());
d= int(input());
print("Before Swaping:\na=",a,"b=",b,"c=",c,"d=",d);

temp=a;
a=d;
d=temp;

temp=b;
b=c;
c=temp;

print("After Swaping:\na=",a,"b=",b,"c=",c,"d=",d);

#(ii):
print('"Celsius to Fahrenhiet Temp Converter"');
print("Enter temp in Celcius: ");
tempinC = int(input());
tempinF = tempinC*9/5+32;

print("Temperature in Fahrenheit is: ",tempinF);

#Exercise Lists:
#(i):

print(dir(list));
print(help(list.reverse));

lst = ['a','b','c','d','e','f'];
print("Original List: ",lst);
lst.reverse();
print("Reversed List: ",lst);

lst.insert(0,'g');
print("Updated List: ",lst);

print("No. of c's in List: ",lst.count('c'));
lst.pop(0);
print(lst);

lst.remove('a');
print(lst);

lst.extend([1,2,3,4,5,6]);
print(lst);

#(ii):
randomlst = ['abc', 'xyzacc', 'abc', '1221'];
Strcount = randomlst.count('abc');
print(Strcount);

#Exercise Dictionaries:
#(i):

my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict);
print(dir(my_dict));
help(my_dict.get);
#get
print(my_dict.get('key1'));
#add
my_dict['key3']='value3';
print(my_dict);
#change value
my_dict['key2']='value4'
print(my_dict);
#delete
del my_dict;
print (my_dict);



#{ii}:

dic1={1:10, 2:20};
dic2={3:30, 4:40};
dic3={5:50,6:60};
Merge = dic1|dic2|dic3;
print(Merge);

#Exercise List Comprehension:
#(i):
name_of_fruits = ['APPLE','MANGO','CHERRY','ORANGE','PINEAPPLE','PEACH'];
print(name_of_fruits);
new_fruits_list = [x.lower() for x in name_of_fruits if len(x)>5];
print(new_fruits_list);


#(ii):
colors =  ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow','Teapink'];
new_list = [x for index, x in enumerate(colors) if index not in [0, 4, 5]];
print(new_list);

#Exercise Operators:
x = 6                           #True
if (type(x) is int): 
 print ("true") ;
else: 
 print ("false");

x = 7.2                               #True

if (type(x) is not int): 
    print ("true"); 
else: 
    print ("false");  

list1=[1,2,3,4,5];                    #not overlapping 5 times
list2=[6,7,8,9]; 
for item in list1: 
    if item in list2: 
     print("overlapping");
    else: 
     print("not overlapping");

a = 20;                            #floor divide= 6
a //= 3;                           #exponent= 7776
print("floor divide=", a);
a **= 5;
print("exponent=", a);


a = 60 # 60 = 0011 1100
b = 13 # 13 = 0000 1101
c = 0
c = a & b # 12 = 0000 1100
print("Line 1", c)
c = a | b # 61 = 0011 1101
print("Line 2", c)
c = a ^ b # 49 = 0011 0001
print("Line 3", c)
c = ~a # -61 = 1100 0011
print("Line 4", c)
c = a << 2 # 240 = 1111 0000
print("Line 5", c)
c = a >> 2 # 15 = 0000 1111
print("Line 6", c)



# Exercise Python Program:
# Task 1: Introduction
print("Welcome to the Factorial Calculator!")

# Task 2: Terminal
print("You can run this program in the terminal by typing 'python Lab1.py'")

# Task 3: Python Interpreter
print("You can also run this program in the Python Interpreter by typing the code line by line")

# Task 4: Variables
num = 5
print(f"We will calculate the factorial of the number {num}")

# Task 5: Text Editor
# You can write and save the code in a text editor like Sublime, Visual Studio Code, etc.
# Save the file with .py extension and run it using the terminal or Python Interpreter

# Task 6: Functions
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Task 7: Lists and Tuples
# Not applicable

# Task 8: Conditional Statements
result = factorial(num)
if result > 0:
    print(f"The factorial of {num} is {result}")
else:
    print("Invalid input")

# Task 9: The For Loop
# Not applicable

# Task 10: User Input and the While Loop
while True:
    num = int(input("Enter a positive integer (0 to exit): "))
    if num == 0:
        break
    result = factorial(num)
    print(f"The factorial of {num} is {result}")

print("Exiting the program...")


