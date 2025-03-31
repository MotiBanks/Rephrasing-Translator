import streamlit as st


st.set_page_config(page_title="RePhrasing Translator", layout="centered")

st.title("😤 RePhrasing Translator")
st.write("Enter what he said, and I'd show you what he *really* meant...")


quote = st.text_input("He said:", placeholder="oh fuck!")


def translate(text):
    result = ""
    use_upper = False

    for char in text:
        if char.isalpha():
            result += char.upper() if use_upper else char.lower()
            use_upper = not use_upper
        else:
            result += char
    return result


if quote:
    st.markdown("### 🗣️  What he said:")
    st.write(quote)

    st.markdown("### 🤡 What he really meant:")
    st.write(translate(quote))
