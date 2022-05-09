import pyttsx3
import os
from click import pause
import time


def information():
    print("===== SpeechBox (v0.1 alpha) Information ======\n")
    print('''SpeechBox is a simple application for text-to-speech that uses the tts Python library called 'pyttsx3', 
the user must input the voice rate and the message.\n
(1) When you're in the main SpeechBox funtion, you can press the Ctrl+C key combination to go back to the main menu
(2) If you choose the second option in the main menu, you go to this info menu
(3) The third option simply exits the application
''')


def speech_engine():  # sourcery skip: extract-duplicate-method
    validation = True
    while validation:
        print("===== Welcome to the SpeechBox (v0.1 alpha) =====\n")
        engine = pyttsx3.init()
        print("============================================================")
        print("Speech Engine: pyttsx3")
        rate = engine.getProperty('rate')
        print(f"Default voice rate is: {rate}")
        print("Tip: You can go back to the main menu by pressing Ctrl+C")
        print("============================================================")
        try:
            set_rate = input("\nPlease set the voice rate (mandatory value): ")
            set_rate = int(set_rate)
            if set_rate == "exit":
                quit()
            engine.setProperty('rate', set_rate)
            message = input("\nWhat do you want me to say? ")
            print("\nPlaying message...")
            engine.say(message)
            engine.runAndWait()
            validation = True
            os.system('cls')
        except ValueError:
            print("*Invalid input!*")
            time.sleep(1)
            os.system('cls')
            validation = True
        except KeyboardInterrupt:
            print("\n\n\n==================================")
            print("**Going back to the main menu...")
            print("==================================")
            time.sleep(2)
            os.system('cls')
            main()


def main():
    print("===== Welcome to the SpeechBox (v0.1 alpha) =====\n")
    print('''
    (1) SpeechBox
    (2) Information
    (3) Exit
    ''')
    validation = True
    while validation:
        try:
            choice = input("\nChoose an option: ")
            choice = int(choice)

            if choice == 1:
                os.system('cls')
                speech_engine()
            elif choice == 2:
                os.system('cls')
                information()
                pause("\nPress any key to go back to the main menu...")
                os.system('cls')
                validation = False
                main()
            elif choice == 3:
                os.system('cls')
                print("Goodbye!")
                time.sleep(2)
                quit()
            else:
                print("*Invalid input!*")
        except ValueError:
            print("*Invalid input!*")
            time.sleep(2)
            os.system('cls')
            main()


if __name__ == '__main__':
    main()
