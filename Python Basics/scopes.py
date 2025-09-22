# Global Scope
balance = 100
def func():
    print(balance) # Accessible

func()
print(balance) # Accessible

def chk():
    balance = balance - 5 #Error
    
def chk():
    global balance
    balance = balance - 5

chk()
print(balance)


#Local Scope
def func():
    balance2 = 500
    print(balance2) #Accessible

print(balance2) # Not Accessible

