import os
import sys
import subprocess

# check is zsh is installed
if not os.path.isfile("/usr/bin/zsh"):
    print("zsh is not installed. Install it?")
    if input("[y/n] ") == "y":
        subprocess.call(["sudo", "apt-get", "install", "zsh"])
    else:
        sys.exit(1)
# Install Oh My ZSH if it is not installed
if not os.path.isdir("/home/{}/.oh-my-zsh".format(os.getlogin())):
    subprocess.call(["curl", "-fsSL", "https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh", "-o", "install.sh"])
    subprocess.call(["sh", "install.sh"])

# grab and install jetbrains mono NF from https://raw.githubusercontent.com/ryanoasis/nerd-fonts/master/patched-fonts/JetBrainsMono/Ligatures/Regular/complete/JetBrains%20Mono%20Regular%20Nerd%20Font%20Complete%20Mono.ttf
# make jetbrainsmono dir in /usr/share/fonts/ dir
subprocess.call(["sudo", "mkdir", "/usr/share/fonts/JetBrainsMono"])
subprocess.call(["sudo","wget", "https://raw.githubusercontent.com/ryanoasis/nerd-fonts/master/patched-fonts/JetBrainsMono/Ligatures/Regular/complete/JetBrains%20Mono%20Regular%20Nerd%20Font%20Complete%20Mono.ttf", "-O", "/usr/share/fonts/JetBrainsMono/JetBrainsMono.ttf"])
#update font cache
subprocess.call(["fc-cache", "-f"])
# get user home dir
home = os.path.expanduser("~")
# check git is installed
if not os.path.isfile("/usr/bin/git"):
    print("git is not installed. Install it?")
    if input("[y/n] ") == "y":
        subprocess.call(["sudo", "apt-get", "install", "git"])
    else:
        sys.exit(1)
# check if curl is installed
if not os.path.isfile("/usr/bin/curl"):
    print("curl is not installed. Install it?")
    if input("[y/n] ") == "y":
        subprocess.call(["sudo", "apt-get", "install", "curl"])
    else:
        sys.exit(1)

# install zsh-syntax-highlighting with oh my zsh if not installed
if not os.path.isfile(home + "/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting"):
    subprocess.call(["git", "clone", "https://github.com/zsh-users/zsh-syntax-highlighting.git", home + "/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting"])


# install zsh-autosuggestions with oh my zsh
if not os.path.isfile(home + "/.oh-my-zsh/custom}/plugins/zsh-autosuggestions"):
    subprocess.call(["git", "clone", "https://github.com/zsh-users/zsh-autosuggestions", home + "/.oh-my-zsh/custom/plugins/zsh-autosuggestions"])

# install p10k
if not os.path.isfile(home + "/.oh-my-zsh/custom}/themes/powerlevel10k"):
    subprocess.call(["git", "clone", "--depth=1", "https://github.com/romkatv/powerlevel10k.git", home + "/.oh-my-zsh/custom/themes/powerlevel10k"])

print("Done! You can change font to JetBrains Mono in your terminal settings and launch zsh when ready")