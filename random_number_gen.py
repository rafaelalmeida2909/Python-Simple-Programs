import random
print('Welcome to my simple random number generator, select the min and max value accetable')
min = input("Min: ")
max = input ("Max: ")
print(random.randint(int(min),int(max)))