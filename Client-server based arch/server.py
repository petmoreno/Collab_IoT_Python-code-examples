#%%
def Calculator (leftOperand, arithmeticOperator, rightOperand):
    a= float(leftOperand)
    b= float(rightOperand)
    c=None

    if arithmeticOperator == '+':
	    c=a+b
    elif arithmeticOperator == '-':
	    c=a-b
    elif arithmeticOperator == '*':
        c=a*b
    elif arithmeticOperator == '/':
        c=a/b
    
    return str(c)


def Parser(text):
    elements= text.split()
    return Calculator (elements[0],elements[1],elements[2])


# %%
file_read=open('request.txt', mode='r')
print("Received message:\n\n" + file_read.read() + "\n")
service=open('request.txt', mode='r').readlines()
service[1]=service[1]+' = '+ Parser(service[1])
file_read.close()

# %%
print("Provided service as a service.txt file.\n\n" + service[1])
file_write=open('service.txt', mode='w')
file_write.writelines(service)
file_write.close()

