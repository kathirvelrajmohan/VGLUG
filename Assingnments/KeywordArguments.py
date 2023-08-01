def interest(name,principle,time,rate):
    "This fuction returns a interest"
    return "Hi "+name+"! Your interest amount is: "+str((principle*time*rate)/100)

name = input("Enter your name: ")
principle = int(input("Enter the principle: "))
time = int(input("Enter the time period in years: "))
rate = int(input("Enter the rate of interest in percentage: "))
interest = interest(name=name,time=time,principle=principle,rate=rate)
print(interest)
