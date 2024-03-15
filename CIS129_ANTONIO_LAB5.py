
#This lab focused on the use of loops to gather user input and calculate certain results such as store/employee bonus and total bottles /bottle payout


def sales():
    #Initializing local variables
    monthlySales = float(input('Enter the monthly sales: '))
    salesIncrease = float(input('Enter percent of sales increase: '))
    salesIncrease = salesIncrease/100
    storeBonus = 0
    empBonus = 0
    keepGoing= str
    
    #This loop stores the if statements from lab 4 and has an else condition at the end that ends the loop if condition is met.
    while True:
        if monthlySales >= 110000:
            storeBonus = 6000
        elif monthlySales >= 100000:
            storeBonus = 5000
        elif monthlySales >= 90000:
            storeBonus = 4000
        elif monthlySales >= 80000:
            storeBonus = 3000
        else:
            storeBonus = 0
            
     #This code determines the employee bonus
        if salesIncrease >= 0.05:
            empBonus = 75
        elif salesIncrease >= 0.04:
            empBonus = 50
        elif salesIncrease >= 0.03:
            empBonus = 40  
        else:
            empBonus = 0
        
        print('The store bonus amount is $',storeBonus)
        print('The employee bonus amount is $',empBonus)
        
        if storeBonus == 6000 and empBonus == 75:
            print('Congrats! You have reached the highest bonus amounts possible!')
        elif storeBonus == 0 and empBonus == 0:
            print('Better luck next month')
        print()
        
        keepGoing=input('Would you like to enter another month of data?\n(Enter y or n): ')
        if keepGoing == 'Y' or keepGoing == 'y': #This if statement uses input to reset loop or end it
            print()
            monthlySales = float(input('Enter the monthly sales: '))
            salesIncrease = float(input('Enter percent of sales increase: '))
            salesIncrease=salesIncrease/100
            storeBonus=0
            empBonus=0
        else:
            break
    print('Data compiled!')



def bottles():
    #Initializing local variable
    totalBottles = 0
    todayBottles = 0
    totalPayout = 0
    keepGoing = str
    counter = 1
    num_of_days=7
    payout_per_bottle=.10
    
    #This loop is used to determine if our nested loop resets
    while True:
        while counter <= num_of_days: #This loop records the data for the day
            todayBottles = int(input('Enter number of bottles returned for day # %s : ' %(counter)))
            counter+=1
            totalBottles += todayBottles        
        totalPayout += (totalBottles * payout_per_bottle) 
        print('The total number of bottles collected is ',totalBottles)
        print(f'The total payout is $ {totalPayout:.2f}')
        print()
        keepGoing = input('Do you want to enter another weeks worth of data?\n(Enter y or n): ')
        
        #This if statement determines whether we reset loop by taking user input and then resetting values for count and total
        if keepGoing == 'y' or keepGoing == 'Y':
            counter = 1
            totalBottles = 0
            totalPayout = 0
            print()
        else:
            break
    
    print()
    print('Data compiled')
    print('Weekly summary complete')
    print()
