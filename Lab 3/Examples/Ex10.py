# Example 10
f = open("demofile3.txt","a");
f.write("I have some content!");
f.close();

f = open("demofile3.txt", "r");
print(f.read());

#Open the file "demofile3.txt" and overwrite the content:

f = open("demofile3.txt", "w");
f.write("Woops! I have deleted the content!");
f.close();

#open and read the file after the appending:
f = open("demofile3.txt", "r");
print(f.read());