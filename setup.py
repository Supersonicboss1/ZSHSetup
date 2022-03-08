import os
import subprocess
home = os.path.expanduser("~")
# download vscode and chrome debs
subprocess.call(["wget", "-O", "vsc.deb", "https://code.visualstudio.com/sha/download?build=insider&os=linux-deb-x64"])
subprocess.call(["wget", "-O", "chrome.deb", "https://dl.google.com/linux/direct/google-chrome-unstable_current_amd64.deb"])
subprocess.call(["curl", "https://pyenv.run", "|", "bash"])
# set up nvs
nvshome = os.path.join(home, ".nvs")


# install everything
subprocess.call(["sudo", "apt-get", "install", "zsh", "git", "gnome-software", "gnome-software-plugin-flatpak", "gnome-software-plugin-snap", "curl", "git", "./chrome.deb", "./vsc.deb", "wget", "apt-transport-https", "gnupg", "-y"])

# Install Oh My ZSH if it is not installed
if not os.path.isdir("/home/{}/.oh-my-zsh".format(os.getlogin())):
    subprocess.call(["curl", "-fsSL", "https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh", "-o", "install.sh"])
    subprocess.call(["sh", "install.sh"])

# add flathub and flathub beta
subprocess.call(["flatpak", "remote-add", "--if-not-exists", "flathub", "https://flathub.org/repo/flathub.flatpakrepo"])
subprocess.call(["flatpak", "remote-add", "--if-not-exists", "flathub-beta", "https://flathub.org/beta-repo/flathub-beta.flatpakrepo"])

# grab and install jetbrains mono NF from https://raw.githubusercontent.com/ryanoasis/nerd-fonts/master/patched-fonts/JetBrainsMono/Ligatures/Regular/complete/JetBrains%20Mono%20Regular%20Nerd%20Font%20Complete%20Mono.ttf
# make jetbrainsmono dir in /usr/share/fonts/ dir
subprocess.call(["sudo", "mkdir", "/usr/share/fonts/JetBrainsMono"])
subprocess.call(["sudo","wget", "https://raw.githubusercontent.com/ryanoasis/nerd-fonts/master/patched-fonts/JetBrainsMono/Ligatures/Regular/complete/JetBrains%20Mono%20Regular%20Nerd%20Font%20Complete%20Mono.ttf", "-O", "/usr/share/fonts/JetBrainsMono/JetBrainsMono.ttf"])
#update font cache
subprocess.call(["fc-cache", "-f"])
# get user home dir


# install zsh-syntax-highlighting with oh my zsh if not installed

subprocess.call(["git", "clone", "https://github.com/zsh-users/zsh-syntax-highlighting.git", home + "/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting"])


# install zsh-autosuggestions with oh my zsh

subprocess.call(["git", "clone", "https://github.com/zsh-users/zsh-autosuggestions", home + "/.oh-my-zsh/custom/plugins/zsh-autosuggestions"])

# install p10k

subprocess.call(["git", "clone", "--depth=1", "https://github.com/romkatv/powerlevel10k.git", home + "/.oh-my-zsh/custom/themes/powerlevel10k"])

#delete zshrc
os.remove(home + "/.zshrc")

#download and replace zshrc from https://raw.githubusercontent.com/Supersonicboss1/ZSHSetup/main/.zshrc
subprocess.call(["curl", "-fsSL", "https://raw.githubusercontent.com/Supersonicboss1/ZSHSetup/main/.zshrc", "-o", home + "/.zshrc"])
subprocess.call(["wget", "-qO-", "https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh", "|", "bash"])

print("Done! You can change font to JetBrains Mono in your terminal settings and launch zsh when ready")