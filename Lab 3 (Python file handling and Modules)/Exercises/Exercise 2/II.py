f = open("student.txt","w");
f.write("Now we are AI students's.");
f.close();

f = open("student.txt","r");
print(f.read());