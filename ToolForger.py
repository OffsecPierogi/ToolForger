import os
import subprocess

def run_cmd(command, verbose=False):
    """Runs a shell cmd & handles errors."""
    try:
        if verbose:
            print(f"Executing: {command}")
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running cmd: {command}\n{e}")

def sys_dependencies(verbose):
    """Installs required tools and sets up virtual environment."""
    print("Ensuring necessary pkgs are installed....")
    run_cmd("sudo apt update && sudo apt install -y git python3-pip python3-venv", verbose)
    run_cmd("sudo apt install nmap", verbose)
    run_cmd("sudo apt install chromium", verbose)
    run_cmd("sudo apt install unzip", verbose)
    run_cmd("sudo apt install plocate", verbose)
    run_cmd("wget https://github.com/michenriksen/aquatone/releases/download/v1.7.0/aquatone_linux_amd64_1.7.0.zip && unzip aquatone_linux_amd64_1.7.0.zip", verbose)
    run_cmd("sudo apt install ffuf", verbose)
    run_cmd("curl -sL https://raw.githubusercontent.com/epi052/feroxbuster/master/install-nix.sh | bash", verbose)

    # Prompting for virtual environment name
    venv_name = input("Enter the name for the virtual environment (e.g., 'myenv'): ")

    # Create the virtual environment
    print(f"Creating virtual environment '{venv_name}'...")
    run_cmd(f"python3 -m venv {venv_name}", verbose)

    # Create a shell script to activate venv and install required packages
    activate_script = f"""
#!/bin/bash
# Activating the virtual environment
source {venv_name}/bin/activate

# Install required Python packages
pip install git+https://github.com/blacklanternsecurity/trevorspray
git clone https://github.com/danielmiessler/SecLists.git
git clone https://github.com/IvanGlinkin/Fast-Google-Dorks-Scan.git
git clone https://github.com/initstring/linkedin2username && cd linkedin2username/ && pip3 install -r requirements.txt && cd ..
sudo apt install golang-go && go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
wget https://github.com/projectdiscovery/nuclei/releases/download/v3.3.8/nuclei_3.3.8_linux_amd64.zip && unzip nuclei_3.3.8_linux_amd64.zip
sudo pipx install bbot && sudo pipx ensurepath
pip install s3recon && curl -sSfL -o s3-wordlist.txt https://raw.githubusercontent.com/clarketm/s3recon/master/data/words.txt
wget https://github.com/trufflesecurity/trufflehog/releases/download/v3.88.6/trufflehog_3.88.6_linux_amd64.tar.gz && tar -xvf trufflehog_3.88.6_linux_amd64.tar.gz
git clone https://github.com/OffsecPierogi/Sub0 && pip install colorama --break-system-packages
"""

    # Save the shell script to a file
    script_filename = f"activate_and_install_{venv_name}.sh"
    with open(script_filename, "w") as script_file:
        script_file.write(activate_script)
    
    # Make the script executable
    run_cmd(f"chmod +x {script_filename}", verbose)

    # Provide the user with instructions on how to run the script
    print(f"\nVirtual environment '{venv_name}' created.")
    print(f"To install the required tools and activate the environment, run the following command:")
    print(f"  ./{script_filename}")

if __name__ == "__main__":
    sys_dependencies(verbose=True)