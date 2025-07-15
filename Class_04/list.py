# List 

dishesList = ["Biryani", "Pulao", "Karahi", "Qorma", "Nihari", "Haleem", "Halwa Puri", "Paya", "Keema", "Zarda"]

#Functions

print(f"- Dishes List: {dishesList}")
print(f"- Number of Dishes: {len(dishesList)}")
print(f"- 2 Index Dish is: {dishesList[2]}")
print(f"- Print 3 index to 6: {dishesList[3:7]}")
print(f"- Print 2nd Last Dish: {dishesList[-2]}")
dishesList.append("Qorma")
print(f"- Number of Dishes: {dishesList}")

dishesList.insert(4,"Payee")
print(f"- After Inser Payee on 4 index: {dishesList}")

sweetDish = ["Gulaab Jamun", "Kheer", "Jalebi"]
dishesList.extend(sweetDish)
print(f"- After Add Sweet Dishes List: {dishesList}")

print(f"- Dishes Length is: {len(dishesList)}")

dishesList.sort()
print(f"- Ascending Order: {dishesList}")

dishesList.sort(reverse=True)
print(f"- Descending Order: {dishesList}")

dishesList.remove("Nihari")
print(f"- After Removing Nihari: {dishesList}")

dishesList.pop()
dishesList.pop()
print(f"- After Pop: {dishesList}")

sizeOfDishes = len(dishesList)
for a in range(sizeOfDishes):
    print(f"- Dish: {dishesList[a]}")