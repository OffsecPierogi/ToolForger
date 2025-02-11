# ToolForger
A tool used to install other tools and dependencies for external/webapp engagements

ToolForge is a script I made to make it easier to install tools needed for an assessment such as external engagements. When executed, it installs any necessary dependencies and tools - making directories and binaries. It will also create a bash script that needs to be run to install the remaining tools and activate your venv (./activate_and_install_venvname.sh). From here, all you need to do is activate the venv and go to town. You’re able to give your venv a custom name. Some tools won’t be globally callable until you enter your venv. The following tools that get installed:

trevorspray (pw spraying)

feroxbuster (dir busting)

seclists

locate (useful utility for finding files)

pip

venv

nmap

chromium

unzip

aquatone (web asset screenshot tool)

ffuf (fuzzing)

google dork scanning

linkedin2username

nuclei (vuln scanning)

bbot (NOTE: may not be globally callable until you logout and log back into your instance for PATH modifications to take effect)

s3recon (s3 buckets) & a s3 wordlist

trufflehog (github enum)

Sub-0 (subdomain enum)

python3 ToolForger.py will execute the script
