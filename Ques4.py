#  4. Write a function to tell user if he/she is able to vote or not.
def voter(age):
    if age >= 18:
        return "Yes , You Are Eligible For Voting"
    else:
        return "No , You Are Immature"
age = int(input())
print(voter(age))