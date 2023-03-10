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