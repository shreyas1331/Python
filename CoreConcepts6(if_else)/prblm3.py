p1="click this"
p2="you will get money in this"
p3="subscribe to my telegram"

comment=input("enter your comment: ");
if(p1 in comment or p2 in comment or p3 in comment):
    print("it is a spam comment")
else:
    print("it is not a spam comment")