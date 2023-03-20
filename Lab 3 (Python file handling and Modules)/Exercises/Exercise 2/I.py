f = open("citydata.txt","w");
f.write("*City Name: Karachi\n Population: 14.91 million\n Mayor: Wasim Akhtar\n\n");
f.write("*City Name: Lahore\n Population: 11.13 million\n Mayor: Mubashir Javed\n\n");
f.write("*City Name: Islamabad\n Population: 1.01 million\n Mayor: Sheikh Anser Aziz");
f.close();
f = open("citydata.txt","r");
print(f.read());