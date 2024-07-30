from Topic3_BuiltinMethodsTheWizardsToolkit import fruits
print(fruits)

vegetables = ["carrot", "broccli", "peas"]

food = fruits + vegetables
print(food)

fruits_clone = fruits.copy()
print(fruits_clone)

fruits.extend(vegetables)
print(fruits)

story_elements = ["Once", "upon", "a", "time"]
story = " ".join(story_elements)
print(story)