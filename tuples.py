#accessing items in a tuple
person=("yvonne","martin","Lovelace")
print(person[2])

#adding items on a tuple
new_person=person + (23,)
print(new_person)#output:('yvonne', 'martin', 'Lovelace', 23)

#Removing items from tuple
remove = person[:1 ]+ person[2:]
print(remove)
print(person)#output:('yvonne', 'Lovelace')

# tuple1=(1,2,3,4)
# tuple2=("yvoone","leila")
# tuple3=(tuple1,tuple2)
# print(tuple3)

# tuple4="Nancy",
# print(tuple4)
# tuple5=1,3,4,5,6,7,"lovelace"
# print(tuple5)
# print(type(tuple5))

# t1 =1,2,3,4
# t2 = 1,2,3,4
# t = t1,t2
# print(t)

# l =5
# w = 6
# a = l*w
# p = (l+w)*2
# params = a , p
# print (params)

# ti = 3,
# print(ti)

# ty = (3,)
# print(ty)

country = {(6,8):[1,2,3,6,8,9,0]}
print(country[(6,8)][5])

fruits = {("sweet",):["pineapples","strawberry","mangoes"]}
print(fruits[("sweet",)][2])