#Favorite Tools List
list = ["Python", "Excel", "Power BI"]
list.append("SQL")
print(list)
list.remove("Power BI")
print(list)



#Student scores
student_scores = [14, 18, 10, 20, 8]
print("Highest :", max(student_scores))
print("Lowest :", min(student_scores))
print("average :", sum(student_scores)/ len(student_scores))



#Shopping List Manger
shopping_list_manager = []

shopping_list_manager.append("Chocolate")
shopping_list_manager.append("Sweet")
shopping_list_manager.append("Milk")
shopping_list_manager.append("rice")

print(shopping_list_manager)

shopping_list_manager.append("salt")
print(shopping_list_manager)

shopping_list_manager.remove("Sweet")
print(shopping_list_manager)



#Country Capitals
country_capitals = (
    ("Cameoon", "Yaounde"),
    ("Ivory coast", "Yamoussoukro"),
    ("Nigeria", "Abuja")
)
for country, capital in country_capitals:
    print(country, "->", capital)



#Unique Visitors
visitors =["Dany", "Lety", "Lyne", "Anyssa", "Lety"] 
unique_visitors = set(visitors)
print(unique_visitors)



#Common Skills
skills1 = {"Python", "SQL","Excel"}
skills2 = {"Python", "POWER BI","Excel"}

common = skills1.intersection(skills2)
print("Common skills : ", common)



#Student Record
student = {
    "name": "Danielle Mabouanda",
    "age": 25,
    "course": "Data science"

}
print(student)



#Mini contact book
contacts = {
    "Dany": "+237 666666666",
    "Lety": "+237 688888888",
    "Lyne": "+237 699999999"
}
search_name = input("Enter contact name :")

if search_name in contacts:
    print(search_name, ":", contacts[search_name])
else:
    print("Contact not found")
