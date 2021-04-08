from cats import Cat
#Cat с большой буквы

cat1= Cat("Баронэсса", "кот", "девочка", "японская кошка", "1.5 года", "С222222", "дом найден")
cat2= Cat("Шаляпин", "кот","мальчик","Неизвестно","1 год", "D323232", "Дом не найден")


print("Имя: ",cat1.first_name )
print("Порода кошки: ",cat1.cat_class)
print("Пол: ",cat1.gender)
print("Вид животного: ",cat1.pet_class)
print("Возраст: ",cat1.age)
print("Рег. док.: ",cat1.reg_doc)
print("Статус: ",cat1.status)
print()
print("Имя: ",cat2.first_name )
print("Порода кошки: ",cat2.cat_class)
print("Пол: ",cat2.gender)
print("Вид животного: ",cat2.pet_class)
print("Возраст: ",cat2.age)
print("Рег. док.: ",cat2.reg_doc)
print("Статус: ",cat2.status)
