def person_info(name, age, **kwargs):
    print(f"Name: {name}")
    print(f"Age: {age}")

    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

person_info("Kathirvel", 20, occupation="Student", location="Villupuram")
