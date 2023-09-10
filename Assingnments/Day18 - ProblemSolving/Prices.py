#Maximizing Profits in Stock Trading
prices = [3,5,0,0,3,1,4]
profits = []
buy_value = -1
n = len(prices)
for i in range(0,n-1):
    if(buy_value == -1 and prices[i]<prices[i+1]):
        buy_value = prices[i]
    if(prices[i] > prices[i+1] and buy_value != -1):
        j= prices[i] - buy_value
        profits.append(j)
        buy_value = -1
    if(i == n-2 and prices[i+1]>prices[i]):
        profits.append(prices[i+1]-buy_value)
profits.sort()
if(len(profits)==0):
    print("You cant able to generate profits from this array.")
else:
    print("The total profit obtained by maximum two transactions is:",profits[len(profits)-1]+profits[len(profits)-2])