#funcs

def txtDoc(fizzNum, buzzNum, fileName):
    #our txt document variable
    myDoc = ''

    for i in range(1, 101):
        #print numbers
        myDoc += (str(i) + ' ')
        # if current number is divisible by fizzNum (default: 3), print Fizz
        if i % fizzNum == 0:
            myDoc += "Fizz"
        # if current number is divisible by buzzNum (default: 5), print Buzz
        if i % buzzNum == 0:
            myDoc += "Buzz"

        # newline
        myDoc += "\n"
        
    # Save to .txt
    f = open(fileName+'.txt', 'w')
    f.write(myDoc)
    f.close()


# actual program

fizz = 3
buzz = 5

txtDoc(fizz, buzz, 'output')