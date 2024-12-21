import pyfiglet
from colorama import Fore, Style, init
import requests

# Initialize Colorama
init(autoreset=True)

def print_attractive_text():
    # Create a Figlet font object
    title_font = pyfiglet.Figlet(font='slant')
    subtitle_font = pyfiglet.Figlet(font='small')

    # Define the text
    title = "ROOT RELUX"
    subtitle = "Made by JUNAYAD AHSAN"
    description = "DDOS Attack Alpha"

    # Print the title in big letters
    print(Fore.CYAN + title_font.renderText(title))
    print(Fore.YELLOW + subtitle_font.renderText(subtitle))
    print(Fore.GREEN + f"This code is made for {Style.BRIGHT}educational purpose.")
    print(Fore.MAGENTA + f"By this code, people can know about {Style.BRIGHT}{description}.")
    print(Fore.RED + f"Use this tool for {Style.BRIGHT}legal purposes.")

def send_request(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(Fore.GREEN + "Request successful!")
        else:
            print(Fore.YELLOW + "Request failed with status code:", response.status_code)
    except Exception as e:
        print(Fore.RED + "An error occurred:", str(e))

if __name__ == "__main__":
    print_attractive_text()
    
    n = int(input("How many times do you want to send requests?: "))
    url = input('Input your target URL: ')

    for _ in range(n):
        send_request(url)
        break
if __name__ == "__main__":
    base_url()
elif __name__ == "__main__":
    post_url()
