import streamlit as st


if "word_to_guess" not in st.session_state:
    st.session_state.word_to_guess = "PAKISTAN"  # The word to guess
    st.session_state.guessed_word = "P_ _ _ _ _ _ _"   # Initial display with first letter revealed
    st.session_state.attempts_left = 7           # Total attempts
    st.session_state.guessed_letters = []        # Store guessed letters

def update_guessed_word(letter):
    new_guessed_word = ""
    for i, l in enumerate(st.session_state.word_to_guess):
        if l == letter:
            new_guessed_word += letter
        else:
            new_guessed_word += st.session_state.guessed_word[i]
    st.session_state.guessed_word = new_guessed_word

st.title("Word Guessing Game - HOLY DAY")
st.subheader("Can you guess the word?")
st.write(f"Word: {st.session_state.guessed_word}")
st.write(f"Attempts left: {st.session_state.attempts_left}")

letter = st.text_input("Enter a letter:", max_chars=1).upper()

if letter:
    if letter in st.session_state.guessed_letters:
        st.warning("You've already guessed that letter.")
    else:
        st.session_state.guessed_letters.append(letter)
        
        if letter in st.session_state.word_to_guess:
            update_guessed_word(letter)
            st.success(f"Correct! The letter '{letter}' is in the word.")
        else:
            st.session_state.attempts_left -= 1
            st.error(f"Wrong guess! The letter '{letter}' is not in the word.")
        
        if st.session_state.guessed_word == st.session_state.word_to_guess:
            st.success("Congratulations! You've guessed the word!")
            st.button("Restart Game", on_click=lambda: st.session_state.clear())
        elif st.session_state.attempts_left == 0:
            st.error(f"Game over! The word was '{st.session_state.word_to_guess}'.")
            st.button("Restart Game", on_click=lambda: st.session_state.clear())

st.write(f"Guessed letters: {', '.join(st.session_state.guessed_letters)}")
