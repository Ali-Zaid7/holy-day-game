# Word Guessing Game - HOLY DAY

This is a simple word guessing game built using **Streamlit**. The objective of the game is to guess the hidden word 
by suggesting letters within a limited number of attempts.

## Features

- **Random Word to Guess**: A preset word ("PAKISTAN" in this case) that the player must guess.
- **Guessed Letters Display**: Shows the letters the player has already guessed.
- **Limited Attempts**: Players have a total of 7 attempts to guess the word correctly.
- **Real-time Feedback**: Players get instant feedback on their guesses (correct or incorrect).
- **Restart Option**: Once the game is over (either by guessing the word or using all attempts), the player can
  restart the game.

## How to Run

1. Install **Streamlit** if you haven't already:

    ```bash
    pip install streamlit
    ```

2. Clone this repository or copy the provided Python code.

3. Run the app using the command:

    ```bash
    streamlit run your_script_name.py
    ```

4. The game will launch in your browser, and you can start guessing the word by entering letters!

## Game Flow

- The player is shown a word with the first letter revealed and the rest hidden.
- The player guesses one letter at a time by typing it in the input box.
- After each guess, the game displays:
  - The updated word with correctly guessed letters revealed.
  - The remaining number of attempts.
  - A list of guessed letters.
- If the player guesses all letters correctly, they win the game.
- If the player runs out of attempts, the game ends, revealing the correct word.

## Example

```text
Word: P_ _ _ _ _ _ _ 
Attempts left: 7
Guessed letters: A, K, I, S, T, N
Congratulations! You've guessed the word!
