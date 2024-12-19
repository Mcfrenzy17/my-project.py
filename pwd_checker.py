def check_password_strength(password):
    # Initialize a score to track the strength of the password
    score = 0

    # Check the length of the password
    if len(password) >= 8:
        score += 1

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        score += 1

    # Check for lowercase letters
    if any(char.islower() for char in password):
        score += 1

    # Check for digits
    if any(char.isdigit() for char in password):
        score += 1

    # Check for special characters
    if any(not char.isalnum() for char in password):
        score += 1

    # Determine the strength based on the score
    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Moderate"
    else:
        return "Weak"

# Example usage
password = input("Enter your password: ")
strength = check_password_strength(password)
print(f"Password strength: {strength}")