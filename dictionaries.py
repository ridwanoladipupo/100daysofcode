#Dictionaries
#To demonstrate dictionaries, write a python program allows four (4) user -
#to register their information based on their; username, password, gender, state and country



users = ['user1', 'user2', 'user3', 'user4']

user1 = {}

user2 = {}

user3 = {}

user4 = {}

#First User
print("Welcome user1")

username = input("Enter your username :")
password = input("Enter your password :")
gender = input("Indicate your gender :")
state = input("Indicate your state :")
country= input("Indicate your country :")

user1['username'] = username
user1['password'] = password
user1['gender'] = gender
user1['state'] = state
user1['country'] = country

print("user1 = " + str(user1))

print("Welcome user2")

#Second User
username = input("Enter your username :")
password = input("Enter your password :")
gender = input("Indicate your gender :")
state = input("Indicate your state :")
country= input("Indicate your country :")

user2['username'] = username
user2['password'] = password
user2['gender'] = gender
user2['state'] = state
user2['country'] = country

print("user2 = " + str(user2))

print("Welcome user3")

#Third User
username = input("Enter your username :")
password = input("Enter your password :")
gender = input("Indicate your gender :")
state = input("Indicate your state :")
country= input("Indicate your country :")

user3['username'] = username
user3['password'] = password
user3['gender'] = gender
user3['state'] = state
user3['country'] = country

print("user3 = " + str(user3))

print("Welcome user4")

#Fourth User
username = input("Enter your username :")
password = input("Enter your password :")
gender = input("Indicate your gender :")
state = input("Indicate your state :")
country= input("Indicate your country :")

user4['username'] = username
user4['password'] = password
user4['gender'] = gender
user4['state'] = state
user4['country'] = country

print("user4 = " + str(user4))


#Outputing details for user1, user2, user3, user4

#User1
for question, response in user1.items():
    username = user1['username']
    password = user1['password']
    gender = user1['gender']
    state = user1['state']
    country = user1['country']
    
print("username :" + username)
print("password :" + password)
print("gender :" + gender)
print("state :" + state)
print("country :" + country)

#User2
for question, response in user2.items():
    username = user1['username']
    password = user1['password']
    gender = user1['gender']
    state = user1['state']
    country = user1['country']
    
print("username :" + username)
print("password :" + password)
print("gender :" + gender)
print("state :" + state)
print("country :" + country)

#User3
for question, response in user3.items():
    username = user1['username']
    password = user1['password']
    gender = user1['gender']
    state = user1['state']
    country = user1['country']
    
print("username :" + username)
print("password :" + password)
print("gender :" + gender)
print("state :" + state)
print("country :" + country)

#User4
for question, response in user4.items():
    username = user1['username']
    password = user1['password']
    gender = user1['gender']
    state = user1['state']
    country = user1['country']
    
print("username :" + username)
print("password :" + password)
print("gender :" + gender)
print("state :" + state)
print("country :" + country)
