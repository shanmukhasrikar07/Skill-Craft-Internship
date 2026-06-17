def check_password(password):
    score    = 0
    feedback = []

    if len(password) >= 8:
        score = score + 1
        feedback.append("✅ Good length (8+ characters)")
    else:
        feedback.append("❌ Too short!! Use 8+ characters")

    
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break

    if has_upper == True:
        score = score + 1
        feedback.append("✅ Has uppercase letter")
    else:
        feedback.append("❌ Add uppercase letter (A-Z)")

    
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
            break

    if has_lower == True:
        score = score + 1
        feedback.append("✅ Has lowercase letter")
    else:
        feedback.append("❌ Add lowercase letter (a-z)")

    
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break

    if has_digit == True:
        score = score + 1
        feedback.append("✅ Has number")
    else:
        feedback.append("❌ Add a number (0-9)")

    
    special   = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    has_special = False
    for char in password:
        if char in special:
            has_special = True
            break

    if has_special == True:
        score = score + 1
        feedback.append("✅ Has special character")
    else:
        feedback.append("❌ Add special character (!@#$)")

    
    if score <= 2:
        strength = "WEAK 🔴"
    elif score == 3:
        strength = "MODERATE 🟡"
    elif score == 4:
        strength = "STRONG 🟢"
    else:
        strength = "VERY STRONG 💪"

    return score, strength, feedback



print("PASSWORD STRENGTH CHECKER")
print("-" * 35)

password = input("Enter password: ")

score, strength, feedback = check_password(password)

print("\nStrength :", strength)
print("Score    :", score, "out of 5")
print("\nFeedback:")
for line in feedback:
    print("  ", line)