import colorama
import subprocess
import sys
def arranger(filepath="things_to_install"):
    print(colorama.Fore.BLUE + f"+ Hold while we rearrange the file it's too dirty...")
    with open(filepath, 'r') as f:
        with open('arranged.txt','w') as o:
            for i in f:
                if i[0] == " ":
                    o.write(i.lower())

def deb_checker():
    try:
        result = subprocess.run(
            ["cat", "/etc/debian_version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True  # Raise CalledProcessError on non-zero exit codes
        )
        # If we reach here, the file exists and was read successfully
        print("Debian system detected.")
    except subprocess.CalledProcessError as e:
        if "No such file or directory" in e.stderr:
            sys.exit("We only accept Debian systems")
        else:
            sys.exit(f"An error occurred: {e.stderr}")

def filter_make():
    print(colorama.Fore.BLUE + f"+ Seperating the sheeps from the goats...")
    with open('arranged.txt', 'r') as a:
        with open('verified_pkgs.txt', 'w') as v:
            with open('Not_verified.txt','w') as n:
                for i in a:
                    i = i.strip()
                    if isinstallable(i):
                        print(colorama.Fore.GREEN + f"{i} is a sheep:)...")
                        v.write(f"sudo apt install {i} \n")
                    else:
                        print(colorama.Fore.RED + f"{i} is a goat :D...")
                        n.write(f'{i} \n')    

def isinstallable(package_name):
    try:
        result = subprocess.run(
            ['sudo', 'apt-get', 'install', '-s', package_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True 
        )
        if 'Unable to locate package' in result.stderr:
            print(colorama.Fore.RED + f"+ {result.stderrcd }")
            return False
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

                    
arranger()                
deb_checker()
filter_make()