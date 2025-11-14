"""
Let's imagine we are working on a service that sends email notifications to users.

we are asked to create a function that formats email content based on user preferences and the type of notification.
The function should take the following parameters:
- user (dict): A dictionary containing user information, including 'name' and 'email'.
- subject (str): The subject of the email.
- body (str): The main content of the email.
The function should return a formatted email string that includes a greeting with the user's name, the subject, and the body of the email.

test cases:
1. Basic Case:
    Input: user = {'name': 'Alice', 'email': 'alice@example.com'}, subject = 'Welcome!', body = 'Hello Alice, welcome to our service.'
    Output: "Dear Alice,\n\nSubject: Welcome!\n\nHello Alice, welcome to our service.\n\nBest regards,\nYour Company"
2. Different User:
    Input: user = {'name': 'Bob', 'email': 'bob@example.com'}, subject = 'Reminder', body = 'Hi Bob, just a reminder about your appointment tomorrow.'
    Output: "Dear Bob,\n\nSubject: Reminder\n\nHi Bob, just a reminder about your appointment tomorrow.\n\nBest regards,\nYour Company"

"""


def format_email(user, subject, body):
    return f"Dear {user["name"]},\n\nSubject: {subject}\n\n{body}\n\nBest Regards,\nAcademy"


user = {'name': 'Bob', 'email': 'bob@example.com'}
formatted_email = format_email(
    user,
    "Reminder", 
    "Hi Bob, just a reminder about your appointment tomorrow."
)

print(formatted_email)

formatted_email = format_email(
    {'name': 'Alice', 'email': 'alice@example.com'},
    "Welcome!",
    "Hello Alice, welcome to our service."
)
print(formatted_email)
