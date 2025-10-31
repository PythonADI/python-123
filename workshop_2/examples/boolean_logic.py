is_logged_in = True
has_two_factor = True

# Basic boolean operators
can_access_account = is_logged_in and has_two_factor
needs_verification = is_logged_in and not has_two_factor
should_show_login_prompt = not is_logged_in

print(f"Account access granted? {can_access_account}")
print(f"Needs verification? {needs_verification}")
print(f"Show login prompt? {should_show_login_prompt}")

# Using booleans in conditionals
if is_logged_in:
    if has_two_factor:
        print("Welcome! Full access granted.")
    else:
        print("Please complete two-factor authentication.")
else:
    print("Please log in to continue.")
