numbers = [1, 2, 3, 4, 5,6,7];

squared_num = list(map(lambda x: pow(x,2), numbers));
cubed_num = list(map(lambda x: pow(x,3), numbers));

print("Original Numbers:", numbers);
print("Squared Numbers:", squared_num);
print("Cubed Numbers:", cubed_num);
    
