# install with: pip install colorama
from colorama import Fore, Style, init
init(autoreset=True)

def banner():
    print(Fore.CYAN + Style.BRIGHT + "\n" + "="*45)
    print(Fore.MAGENTA + Style.BRIGHT + "     🔠jAKIR'S ENCODER TOOL (LIVE MODE)🔠 ")
    print(Fore.CYAN + Style.BRIGHT + "="*45 + "\n")

def letter_to_code(text):
    result = []
    for char in text.upper():
        if char.isalpha():
            result.append(str(ord(char) - 64))
        elif char == ' ':
            result.append(' ')
    return ' '.join(result)

def code_to_letter(code_str):
    result = []
    for part in code_str.strip().split():
        if part.isdigit():
            num = int(part)
            if 1 <= num <= 26:
                result.append(chr(num + 64))
        else:
            result.append(' ')
    return ''.join(result)

def main():
    while True:
        banner()
        print(Fore.YELLOW + "1. 🔤 Convert Text to Code")
        print("2. 🔁 Convert Code to Text")
        print("3. ❌ Exit\n")
        choice = input(Fore.CYAN + "Choose an option (1/2/3): ")

        if choice == '1':
            text = input(Fore.GREEN + "\n👉 Enter your word or sentence: ")
            print(Fore.MAGENTA + "\n🧾 Code Output:")
            print(Fore.WHITE + Style.BRIGHT + letter_to_code(text))
        elif choice == '2':
            code = input(Fore.GREEN + "\n👉 Enter the code (e.g., 10 1 11 9 18): ")
            print(Fore.MAGENTA + "\n🔡 Text Output:")
            print(Fore.WHITE + Style.BRIGHT + code_to_letter(code))
        elif choice == '3':
            print(Fore.CYAN + "\n✨ Thank you for using the tool!\n")
            break
        else:
            print(Fore.RED + "⚠️ Invalid choice! Please enter 1, 2, or 3.")

        input(Fore.YELLOW + Style.BRIGHT + "\n🔁 Press Enter to continue...")

if __name__ == "__main__":
    main()
