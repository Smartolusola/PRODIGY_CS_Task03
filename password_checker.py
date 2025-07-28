import re

def check_password_strength(password):
    feedback = []
    score = 0

    if len(password) < 8:
        feedback.append("❌ Password must be at least 8 characters long.")
    else:
        score += 1

    if not re.search(r'[A-Z]', password):
        feedback.append("❌ Add at least one uppercase letter.")
    else:
        score += 1

    if not re.search(r'[a-z]', password):
        feedback.append("❌ Add at least one lowercase letter.")
    else:
        score += 1

    if not re.search(r'[0-9]', password):
        feedback.append("❌ Add at least one number.")
    else:
        score += 1

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback.append("❌ Add at least one special character (!@#$ etc.).")
    else:
        score += 1

    # Final verdict
    if score == 5:
        feedback.append("✅ Password is Strong.")
    elif score >= 3:
        feedback.append("🟡 Password is Medium.")
    else:
        feedback.append("🔴 Password is Weak.")

    return feedback

# User input
if __name__ == "__main__":
    user_password = input("Enter your password: ")
    results = check_password_strength(user_password)

    print("\nPassword Analysis:")
    for line in results:
        print(line)
