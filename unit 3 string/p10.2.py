items=["mobile","laptop","pendrive","microchip","earphones","motherboard"]


# user=input("write first letter which u want to search in google:")
user=input("write first letter which u want to search in google:").lower()

for i in items:
    if(i.startswith(user)):
        print(i)