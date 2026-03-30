# users: dict = {0: "Mario", 1: "Luigi", 2: "James"}
# print(users.values()) #get values in list
# print(users.keys()) # get keys in list form
# user_popped = users.pop(1) # get the value of the key
# users.popitem() # just pop users 
# users.pop(1) #put the key as argument to remove
# print(user_popped)


# sample_dict: dict = {0: ['a', 'b'], 1:['c', 'd']}
# my_copy: dict = sample_dict.copy()


# names = {0: "John", 1: "Mark", 2: "Peter"}
# print(names.get(1)) # prints mark
# print(names.get(999, "none")) # prints none if no key is found

# print(names.setdefault(0, "???")) # still returns John
# print(names.setdefault(999, "???")) # returns ??? and makes a new key and value 999 : ???
# print(names.clear()) # clear the dict

# people: list[str] = ["Marlo", "Luigi", "James"]
# p_names = dict.fromkeys(people) # names : none as ddefault
# u_names = dict.fromkeys(people, "Unknown") # names : Unknown


# names = {0: "John", 1: "Mark", 2: "Peter"}
# print(names.items()) # [(0: "John"), (1: "Mark"), (2: "Peter" )]

# for k, v in names.items(): #unpack values and keys
#     print(k, v)


# users: dict = {0: "Mario", 1: "Luigi", 2: "James"}
# #users.update({2: "Bob", 3: "Sister"}) # overwrites and adds
# users |= {10: "Spam", 11: "Eggs"} # another update method
# print(users)