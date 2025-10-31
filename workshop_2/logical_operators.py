# boolean has 2 values: True and False

# we have 3 logical operators: and (&&), or (||), not (!)

# we promised our friend that you will go to cinema and you both eat popcorn
print("We went to cinema and ate popcorn did we tell the truth?", True and True)
print("We did not go to cinema and ate popcorn did we tell the truth?", False and True)
print(True and False)
print(False and False)

# Truth table for AND operator
# True and True -> True
# False and True -> False
# True and False -> False
# False and False -> False

print("\nOR\n")
# we promised our friend that you will go to cinema or we'll go to park
print(True or True)
print(True or False)
print(False or True)
print(False or False)


print("\nNot\n")
print(not True)
print(not False)


went_cinema = True
ate_popcorn = True

# ორივე გავაკეთე? ანუ თრუა?
print(f"{went_cinema and ate_popcorn = }")