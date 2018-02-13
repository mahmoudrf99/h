z = 0
#total sumation 
x = 0
#player no. 1
y = 0
#player no. 2
print('Choose a number from [0,1,2,3,4,5,6,7,8,9,10]')
while True:
    if(x <= 10 and y <= 10 and z <= 100):
        x = int(input('<-1st player-> choise :'))
        while (x>10):
        #he has to choose from 0 to 10
            print ('Try Again')
            x = int(input('1st player chooses :'))
        if (x <= 10):
            if (z <= 100):
                while (x <= 10):
                    z = z + x
                    print '-Total- :',z
                    break
                if (z >= 100):
                    print ('^1st player is the Winner^')
                    break

    if(x <= 10 and y <= 10 and z <= 100):
        y = int(input('<~2nd player~> choise :'))
        while (y > 10):
            print ('Try Again')
            y = int(input('2nd player chooses :'))
        if (y <= 10):
            if (z <= 100):
                while (y <= 10): 
                    z = z + y
                    print '~Total~ :',z
                    break
                
                if (z >= 100):
                    print ('^2nd player is the Winner^')
                    break
