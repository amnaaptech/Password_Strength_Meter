import streamlit as st
import re
import string
import secrets

# Function to check password strength
def check_password_strength(password):
    score = 0
    suggestions = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        suggestions.append("❌ Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score == 4:
        return "✅ Strong Password!", "green", suggestions
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", "orange", suggestions
    else:
        return "❌ Weak Password - Improve it using the suggestions below.", "red", suggestions

# Function to generate a strong password
def generate_password():
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#$%^&*"
    
    password = [
        secrets.choice(string.ascii_uppercase),  
        secrets.choice(string.ascii_lowercase), 
        secrets.choice(string.digits),        
        secrets.choice("!@#$%^&*")  
    ]

    # Fill the rest with random choices
    password += [secrets.choice(characters) for _ in range(secrets.choice([4, 5]))]  # Total 8 to 9 characters

    # Shuffle to make it more random
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


#UI
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="centered")

st.title("🔐 Password Strength Meter")

# User Input 

password = st.text_input("Enter your password:", type="password")

if st.button("Check Strength"):
    if password:
        strength_message, color, suggestions = check_password_strength(password)
        st.markdown(f"<h4 style='color: {color};'>{strength_message}</h4>", unsafe_allow_html=True)

        if suggestions:
            st.warning("\n".join(suggestions))
        else:
            st.success("✅ Your password is strong!")
    else:
        st.error("⚠️ Please enter a password first!")

# Generate Button
if st.button("Generate Strong Password"):
    strong_password = generate_password()
    st.success(f"🔑 Suggested Strong Password: `{strong_password}`")
