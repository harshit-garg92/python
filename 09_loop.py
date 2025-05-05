items = ["apple","banana","orange","apple","mango"]

unique_item=[]

for item in items:
    if item in unique_item:
        print("duplicate",item)
        break
    unique_item.append(item)
    print(unique_item)