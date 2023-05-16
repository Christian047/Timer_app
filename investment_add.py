# application that gives 10% profit every 24hours
import time

# we ask the user to input his investment
initial_investment = int(input("input the amount you want to invest: "))  
# we create a while loop that will give repeated investment
while True:
    profit = initial_investment * 0.1

    # initial_investment = initial_investment + profit
    initial_investment += profit 

     # striftime() method formats date object into a string representation
    #  %c represents date and time in the local version
    print("Date and time:", time.strftime("%c")) 
    
    print("New investment amount:", initial_investment)
    
# Wait for 24 hours before repeating the loop
    time.sleep(86400)