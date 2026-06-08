import os
import random
import time

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    print("""
===========================
   PYTHON TOOLKIT STARTER
===========================
""")


def password_generator():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    length = int(input("Length: "))

    pwd = "".join(random.choice(chars) for _ in range(length))
    print("\nGenerated Password:", pwd)


def file_counter():
    files = os.listdir()
    print("\nFiles in current directory:", len(files))


def fake_loading():
    print("Loading tool")
    for _ in range(3):
        print(".")
        time.sleep(0.3)


def main():
    while True:
        clear()
        banner()

        print("""
[1] Password Generator
[2] File Counter
[3] Fake Loading Demo
[4] Exit
""")

        choice = input("Select: ")

        if choice == "1":
            password_generator()
        elif choice == "2":
            file_counter()
        elif choice == "3":
            fake_loading()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

        input("\nPress Enter...")


if __name__ == "__main__":
    main()
