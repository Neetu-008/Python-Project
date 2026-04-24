import streamlit as st
import random
import string
st.set_page_config(page_title="passGen", page_icon="Lock")
st.title("Password Generator")
st.write("Make your own strong password")
col1, col2 =st.columns(2)
with col1:
    length=st.slider("password length", 4, 50, 12)
    num_passwords=st.number_input("how much", 1, 10, 3)
with col2:
    use_upper = st.checkbox("ABC uppercase",True)
    use_lower = st.checkbox("abc lowercase", True) 
    use_digits = st.checkbox("123 numbers", True)
    use_symbols = st.checkbox("!@# symbols",True)
chars = ""
if use_upper: chars += string.ascii_uppercase
if use_lower: chars += string.ascii_lowercase
if use_digits: chars += string.digits
if use_symbols: chars += "!@#$%^&*()_=+-{}[]"
if st.button("Generate passwords", type="primary"):
    if not chars:
        st.error("select minimum 1 option")
    else:
        st.subheader("generated passwords:") 
        for i in range(num_passwords):
            password = ''.join(random.choice(chars) for _ in range(length))  
            strength = 0
            if any(c.isupper() for c in password): strength += 1
            if any(c.islower() for c  in password): strength += 1
            if any(c.isdigit() for c in password): strength += 1
            if any(c in "!@#$%^&*()_-+={}[]" for c in password): strength += 1
            if strength == 4 and length >= 12:
                label ="strong"
            elif strength >= 3 and length >= 8:
                label ="Medium"
            else:
                label ="Weak"
            st.code(password, language=None)
            st.caption(f"{label} | length: {len(password)}")  
Total_Combination = len(chars) ** length if chars else 0 
st.sidebar.success(f"**{Total_Combination:,}** combination - cracking impossible")                 
st.sidebar.header("**Passwords Facts**")
st.sidebar.metric("*Total Possible Combinations*", f"{len(chars)**length:,}" if chars else 0)
st.divider()
st.subheader("Total Possible combination")
st.sidebar.info("12+ chars with all 4 types = strong")
st.sidebar.markdown("**Tip:** click on the password and copy it")   