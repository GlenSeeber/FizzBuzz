# 3     ->   fizz
# 5     ->   buzz
# 3 & 5 ->   fizzbuzz
#-----------------------



def terminal():
    for i in range(1, 101):
        #print the number
        print(i, end=' ')
        #fizz
        if i % 3 == 0:
            print("Fizz", end='')
        #buzz
        if i % 5 == 0:
            print("Buzz", end='')

        # newline
        print('')

def txtDoc():
    #our txt document variable
    myDoc = ''

    for i in range(1, 101):
        #print numbers
        myDoc += (str(i) + ' ')
        # Fizz
        if i % 3 == 0:
            myDoc += "Fizz"
        # Buzz
        if i % 5 == 0:
            myDoc += "Buzz"

        # newline
        myDoc += "\n"
        
    # Save to .txt
    f = open('fizzbuzz.txt', 'w')
    f.write(myDoc)
    f.close()

txtDoc()