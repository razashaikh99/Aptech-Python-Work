myInfo = {
    "name": "Muhammad Raza",
    "age": 20,
    "city": "Karachi",
    "cnic": 42101376437822,
    "address": "North Nazimabad, Karachi"
}

print(myInfo)
myInfo["course"] = "Python"
print(myInfo)
print(myInfo.keys())
print(myInfo.values())
del myInfo["cnic"]
print(myInfo)