hobbies = ["reading", "painting", "cycling"]
print(hobbies)

hobbies.append("singing")
print(hobbies)

hobbies.insert(1, "dancing")
print(hobbies)

hobbies[0]= "writing"
print(hobbies)

hobbies.remove("cycling")
print(hobbies)

last_hobby = hobbies.pop()
print(hobbies)

second_hobby = hobbies.pop(1)
print(hobbies)

count_reading = hobbies.count("reading")
print(count_reading)

position_painting = hobbies.index("painting")
print(position_painting)

hobbies.clear()
print(hobbies)