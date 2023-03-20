                       #if,else,elif and operators examples:
#Demo Code:
#!/usr/bin/python
var = 100;
if var == 200:
 print ("1 - Got a true expression value");
 print (var);
elif var == 150:
 print ("2 - Got a true expression value");
 print (var);
elif var == 100:
 print ("3 - Got a true expression value");
 print (var);
else:
 print ("4 - Got a false expression value");
 print (var);
 print ("Good bye!");

#Example: 01
#Print square root of negative or positive number using if and operators.

a = int(input("Enter a number and I'll get its Square Root: "));
if(a>0):
    print("The number u entered is greater than 0, so I can calculate it!");
    root = a **(1/2);
    print("The Square root of ",a,"is",root);
if(a<=0):
    print("I can't calculate the square root of a negative number!");
print("Thanks for the input!");         

#Example: 02
#Write conditional statements to print value of 0 to 1 and 1 to 0 and numbers in between.

a = int(input("Enter a number: "));
if (a == 1):
    a = 0;
elif (a == 0):
    a = 1;
elif (a>2 or a<0):
    print("U have entered number in b/w!");
print(a);        

# Example: 03
# Let's look at another example:

a = int(input("Enter a number b/w 10-20: "));
if a>=10 and a<=20:
    print("The entered number is in the range!");
else:
    print("The entered number is out from the range");

# Example: 04
# Of course, operators can also be combined using parentheses:

a = int(input("Enter a number b/w 10-20 or 30-40: "));
if (a>=10 and a<=20) or (a>=30 and a <=40):
    print("The entered number is in the range!");
else:
    print("The entered number is out from the range");




                #Structure loops, for loops and While loops

# Example #1
# Print Karachi Pakistan 100 times in a separate line.

#(i):
i=1;
while(i<=10):
    print("Karachi Pakistan");
    i+=1;

# Example # 2
# Take collection of number input from user. Print the total positive and negative number.
#Counting +ve and -ve number

pcount = 0;
ncount = 0;
count = int(input("How many numbers u want? "));
i=1;
while(i<=count):
    num = int(input("Enter number: "));
    if(num>=0):
        pcount +=1;
    else:
        ncount+=1;
    i+=1;
print("Positive: ",pcount);
print("Negative: ",ncount);
            
# Example # 3
# Fixed a Letter from a to e and then ask the user to guess that letter until correct letter entered.

value = 'c';
userValue = input("Guess a number from a to e: ");
while(userValue!=value):
    print("Incorrect!");
    userValue = input("Guess a number from a to e: ");
print("Welcome User");





                         #LabTask: 02
#Exercise 1:
# (i):
height = int(input("Enter the height of the object: "));
width = int(input("Enter the width of the object: "));
depth = int(input("Enter the depth of the object: "));
volume = height*width*depth;

if (volume>0):
    print("Volume of object = ",volume);
    if (volume<=10):
        print("Extra Small");
    elif (volume>=11 and volume<=25):
        print("Small");
    elif (volume>=26 and volume<=75):
        print("Medium");
    elif (volume>=76 and volume<=100):
        print("Large");
    elif (volume>=101 and volume<=250):
        print("Extra Large");
    elif (volume>250):
        print("Extra-Extra Large");
    print("Thanks for your input :)");      
else:
    print("Please enter the valid numbers :(");


#(ii):
workerEfficiency = int(input("Enter your time required for complete a specific task in hrs:  "));
if (workerEfficiency>=2 and workerEfficiency<=3):
    print("Highly Efficient!");
elif (workerEfficiency>=3 and workerEfficiency<=4):
    print("Improve your speed!");   
elif (workerEfficiency>=4 and workerEfficiency<=5):
    print("You must need to join our training program");
elif (workerEfficiency>5):
    print("Please leave our company!");    
else:
    print("Please enter a valid time in hrs!");

#(iii):
username = str(input("Please enter a username: "));
password = input("Enter a strong password: ");
verifyPassword = input("Verify your password: ");
if(verifyPassword.upper() == password.upper()):
    print("Welcome Sir!");
else:
    print("I don't know you");     

#Exercise 2:
#(i)a:

n = 3;
while n >= 0:
    n -= 1;
    print(n);

#(i)b:

n = 4;
while n > 0: 
    n += 1;
    print(n);

#(ii)a:
clist = [];
cnumber = int(input("How many countries you want to add in a list: "));
i=1;
while (i<=cnumber):
    cname = str(input("Enter a country name: "));
    clist.append(cname);
    i+=1;
print("Your updated list: ",clist);    

#(ii)b:
#Create a loop that counts from 0 to 100.
print("Count 0 to 100:");
i=0;
while (i<=100):
    print(i);
    i+=1;

#(ii)c:
#Make a multiplication table using a loop.
print("'Table Generator'");
tablenumber = int(input("Enter a table number: "));
i=1;
while(i<=10):
    res = tablenumber*i;
    print(tablenumber," x ",i," = ",res);
    i+=1;

#(ii)d:
#Output the numbers 1 to 10 backwards using a loop.

print("Backward count 0 to 10:");
i=10;
while (i>=0):
    print(i);
    i-=1;

#(ii)e:
# Create a loop that counts all even numbers to 10.

print("Even Numbers Count 0 to 10:");
i=0;
while (i<=10):
    print(i);
    i+=2;

#(ii)f:
# Create a loop that sums the numbers from 100 to 200.

print("Sum of numbers from 100 to 200:");
nlist = [];
i=100;
while(i<=200):
    nlist.append(i);
    i+=1;
#print(nlist);
res = sum(nlist);
print("Total Sum: ",res);

# In short:
# res = sum(range(100,201));  
# print("Total Sum: ",res);

#(iii)a:
clist = [];
cnumber = int(input("How many countries you want to add in a list: "));
i=1;
while (i<=cnumber):
    cname = str(input("Enter a country name: "));
    clist.append(cname);
    i+=1;
print("Your updated list: ",clist);   