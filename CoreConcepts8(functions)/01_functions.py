# a = int(input("Enter your number: "))
# b = int(input("Enter your number: "))
# c = int(input("Enter your number: "))
 
# average = (a + b + c)/3
# print(average)

# a = int(input("Enter your number: "))
# b = int(input("Enter your number: "))
# c = int(input("Enter your number: "))6
 
# average = (a + b + c)/3
# print(average)

# Function Definition
def avg():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))
    
    average = (a + b + c)/3
    print(average)


avg() # Function Call
print("Thank you!")
# avg()
print("Thank you!")
# avg()
print("Thank you!")
# avg()
# avg()


def find_gst(price):
    price=price+(price*0.18)
    print(price)

find_gst(100)    
ans=find_gst(500)
print(ans," this is the GST price")