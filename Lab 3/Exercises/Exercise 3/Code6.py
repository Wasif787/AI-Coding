import random;
print (random.randint(1,10) );
print( random.random());

x = [1,2,3,4,5,6,7,8,9,10];
random.shuffle(x);
print(x);

y = random.sample(x,5);
print(y);