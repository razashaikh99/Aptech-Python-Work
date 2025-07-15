import pandas

Student = {
    "name": [
        "Muhammad Raza", "Ahmed", "Ali", "Usman", "Hassan",
        "Fatima", "Zainab", "Ayesha", "Umar", "Bilal"
    ],
    "age": [20, 21, 22, 20, 19, 21, 23, 22, 20, 18],
    "city": [
        "Karachi", "Lahore", "Islamabad", "Rawalpindi", "Quetta",
        "Peshawar", "Multan", "Faisalabad", "Hyderabad", "Sialkot"
    ],
    "cnic": [
        42101376437822, 3520212345678, 6110111122223, 3740512345678, 4220156789123,
        4250198765432, 3730211223344, 4210188888888, 3520211111111, 6110199999999
    ],
    "address": [
        "North Nazimabad, Karachi", "Model Town, Lahore", "G-11, Islamabad", "Saddar, Rawalpindi", "Satellite Town, Quetta",
        "Hayatabad, Peshawar", "Shah Rukn Alam, Multan", "Peoples Colony, Faisalabad", "Latifabad, Hyderabad", "Cantt, Sialkot"
    ],
    "email": [
        "raza@gmail.com", "ahmed@gmail.com", "ali@yahoo.com", "usman@hotmail.com", "hassan@gmail.com",
        "fatima@yahoo.com", "zainab@gmail.com", "ayesha@hotmail.com", "umar@yahoo.com", "bilal@gmail.com"
    ],
    "phone": [
        "03001234567", "03019876543", "03121234567", "03219874567", "03331234567",
        "03451239876", "03561234567", "03671234567", "03781234567", "03891234567"
    ],
    "gender": [
        "Male", "Male", "Male", "Male", "Male",
        "Female", "Female", "Female", "Male", "Male"
    ],
    "education": [
        "Matric", "Inter", "Bachelor", "Matric", "Inter",
        "Bachelor", "Master", "PhD", "Bachelor", "Inter"
    ],
    "is_active": [
        True, True, False, True, False,
        True, True, False, True, True
    ]
}
print(Student)
dFrame = pandas.DataFrame(Student)
print(dFrame)