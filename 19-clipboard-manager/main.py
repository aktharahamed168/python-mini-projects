import pyperclip

clipboard_history = []


def copy_text():
    text = input("Enter text to copy: ")

    pyperclip.copy(text)
    clipboard_history.append(text)

    print("Text copied successfully!")


def view_history():
    if not clipboard_history:
        print("Clipboard history is empty.")
        return

    print("\n===== Clipboard History =====")

    for index, text in enumerate(clipboard_history, start=1):
        print(f"{index}. {text}")


def clear_history():
    clipboard_history.clear()
    print("Clipboard history cleared.")


while True:
    print("\n===== Clipboard Manager =====")
    print("1. Copy Text")
    print("2. View History")
    print("3. Clear History")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        copy_text()

    elif choice == "2":
        view_history()

    elif choice == "3":
        clear_history()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
