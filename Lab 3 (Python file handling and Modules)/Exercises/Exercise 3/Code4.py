import time;
x = time.time();
print(x);

current_time = time.time();
y = time.ctime(current_time);
print(y);

z = time.ctime();
print(z);

a = time.sleep(3);
print(a);

b = time.sleep(0.5);
print(b);