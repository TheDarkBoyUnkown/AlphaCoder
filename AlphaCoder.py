# 🔠 JAKIR'S ENCODER TOOL (BETA MODE)
# Filename: AlphaCoder.py
# Install colorama with: pip install colorama

from colorama import Fore, Style, init
init(autoreset=True)

leet_dict = {
    'A': '4', 'B': '8', 'C': '<', 'D': 'D', 'E': '3', 'F': 'F',
    'G': '6', 'H': '#', 'I': '1', 'J': 'J', 'K': 'K', 'L': '1',
    'M': 'M', 'N': 'N', 'O': '0', 'P': 'P', 'Q': 'Q', 'R': 'R',
    'S': '5', 'T': '7', 'U': 'U', 'V': '\\/', 'W': 'VV', 'X': '><',
    'Y': 'Y', 'Z': '2'
}

def banner():
    print(Fore.CYAN + Style.BRIGHT + "\n" + "=" * 47)
    print(Fore.MAGENTA + Style.BRIGHT + "     🔠 JAKIR'S ENCODER TOOL (BETA) 🔠")
    print(Fore.CYAN + Style.BRIGHT + "=" * 47 + "\n")

def letter_to_code(text):
    result = []
    for char in text.upper():
        if char.isalpha():
            result.append(str(ord(char) - 64))
        elif char == ' ':
            result.append('0')  # 0 for space
    return ' '.join(result)

def code_to_letter(code_str):
    result = []
    for part in code_str.strip().split():
        if part == '0':
            result.append(' ')
        elif part.isdigit():
            num = int(part)
            if 1 <= num <= 26:
                result.append(chr(num + 64))
    return ' '.join(result)

def to_leetspeak(text):
    leet_text = ''
    for char in text.upper():
        leet_text += leet_dict.get(char, char)
    return leet_text

def save_to_file(filename, input_data, output_data):
    with open(filename, "a") as file:
        file.write(f"Input : {input_data}\n")
        file.write(f"Output: {output_data}\n")
        file.write("-" * 40 + "\n")

def main():
    while True:
        banner()
        print(Fore.YELLOW + "1. 🔤 Convert Text to Code")
        print("2. 🔁 Convert Code to Text")
        print("3. 🎮 Convert Text to Leetspeak")
        print("4. 📄 Show All Saved Text to Code")
        print("5. 📄 Show All Saved Code to Text")
        print("6. ❌ Exit\n")

        choice = input(Fore.CYAN + "Choose an option (1-6): ")

        if choice == '1':
            text = input(Fore.GREEN + "\n👉 Enter your word or sentence: ")
            coded = letter_to_code(text)
            print(Fore.MAGENTA + "\n🧾 Code Output:")
            print(Fore.WHITE + Style.BRIGHT + coded)
            save_to_file("code_output.txt", text, coded)

        elif choice == '2':
            code = input(Fore.GREEN + "\n👉 Enter the code (e.g., 10 1 11 9 18 0 19 11): ")
            decoded = code_to_letter(code)
            print(Fore.MAGENTA + "\n🔡 Text Output:")
            print(Fore.WHITE + Style.BRIGHT + decoded)
            save_to_file("text_output.txt", code, decoded)

        elif choice == '3':
            text = input(Fore.GREEN + "\n👉 Enter your word to convert into leetspeak: ")
            leet = to_leetspeak(text)
            print(Fore.MAGENTA + "\n🎮 Leet Output:")
            print(Fore.WHITE + Style.BRIGHT + leet)
            save_to_file("leet_output.txt", text, leet)

        elif choice == '4':
            try:
                with open("code_output.txt", "r") as f:
                    print(Fore.MAGENTA + "\n📄 All Text to Code History:")
                    print(Fore.WHITE + Style.BRIGHT + f.read())
            except FileNotFoundError:
                print(Fore.RED + "\n⚠️ No data found.")

        elif choice == '5':
            try:
                with open("text_output.txt", "r") as f:
                    print(Fore.MAGENTA + "\n📄 All Code to Text History:")
                    print(Fore.WHITE + Style.BRIGHT + f.read())
            except FileNotFoundError:
                print(Fore.RED + "\n⚠️ No data found.")

        elif choice == '6':
            print(Fore.CYAN + "\n✨ Thank you for using the tool!\n")
            break

        else:
            print(Fore.RED + "⚠️ Invalid choice! Please enter a valid option.")

        input(Fore.YELLOW + Style.BRIGHT + "\n🔁 Press Enter to continue...")

if __name__ == "__main__":
    main()
