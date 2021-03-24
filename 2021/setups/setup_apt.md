# 包管理器 Apt 相关配置

### Shell

-   Ubuntu 自带了很多 Shell 了。当然可以使用 Apt 或者 Linuxbrew 安装更多的 Shell。

```sh
cat /etc/shells # check added shells
echo $SHELL # check the shell in use
chsh -s /usr/local/bin/zsh # switch default shell
sudo vim /etc/shells # add shells
# /home/linuxbrew/.linuxbrew/bin/zsh
# /home/linuxbrew/.linuxbrew/bin/bash
```

### bash 配置文件

-   配置文件加载顺序如下。配置的时候，针对所有用户，配置/etc/profile，用户个人配置~/.bashrc。

```sh
# bash configs, load as following orders
/etc/profile
/etc/bashrc
~/.bash_profile
~/.bashrc
```

```sh
# /etc/profile or /etc/zshenv
# system-wide configurations
# 2020.08.12

# homebrew 2.24
eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)
export HOMEBREW_BOTTLE_DOMAIN="https://mirrors.tuna.tsinghua.edu.cn/linuxbrew-bottles"
export HOMEBREW_NO_AUTO_UPDATE=true

# for root
export PATH="/home/linuxbrew/.linuxbrew/bin:$PATH"

# cuda@10.2
export LD_LIBRARY_PATH=":/usr/local/cuda-10.2/lib64"
export PATH="$PATH:/usr/local/cuda-10.2/bin"
export CUDA_HOME=":/usr/local/cuda-10.2"

# conda basic
export PATH="$PATH:/opt/anaconda/bin"

# ruby 2.7
export PATH="$PATH:/home/linuxbrew/.linuxbrew/lib/ruby/gems/2.7.0/bin"

# openjdk@11
export PATH="/home/linuxbrew/.linuxbrew/opt/openjdk@11/bin:$PATH"

# node@12
export PATH="/home/linuxbrew/.linuxbrew/opt/node@12/bin:$PATH"

# go@1.13
export PATH="/home/linuxbrew/.linuxbrew/opt/go@1.13/bin:$PATH"
```

```sh
# ~/.bashrc
# uniform configs

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/opt/anaconda/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/opt/anaconda/etc/profile.d/conda.sh" ]; then
        . "/opt/anaconda/etc/profile.d/conda.sh"
    else
        export PATH="/opt/anaconda/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```

### zsh 配置文件

-   配置的时候，针对所有用户，配置/etc/zshenv，用户个人配置~/.zshrc。

```sh
# zsh configs, load as following orders
/etc/zshenv
/etc/zprofile
~/.zprofile
~/.zshrc
```

```sh
# ~/.zshrc
# zfj zsh configuration
# last update: 20200814

# clear
clear

# Auto cd to folder without cd
setopt AUTO_CD

# Set history related
HISTFILE=${ZDOTDIR:-$HOME}/.zsh_history
setopt EXTENDED_HISTORY
SAVEHIST=100
HISTSIZE=50
setopt SHARE_HISTORY
setopt APPEND_HISTORY
setopt INC_APPEND_HISTORY
setopt HIST_EXPIRE_DUPS_FIRST
setopt HIST_IGNORE_DUPS
setopt HIST_FIND_NO_DUPS
setopt HIST_REDUCE_BLANKS

# Set auto correction
setopt CORRECT
setopt CORRECT_ALL

# main prompt
PROMPT="%~ %(?.%F{green}>.%F{red}>)%f"

# PROMPT suffix
PROMPT+=" "

# shell alias
alias clr="clear"
alias cls="clear"
alias cln="clear"
alias vimzrc="vim ~/.zshrc"

# env alias
alias ls="exa"
alias py="python3"
alias python="python3"
alias pip="pip3"
alias my="mysql -u root -p"
alias cas="conda activate std"
alias cab="conda activate"

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/opt/anaconda/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/opt/anaconda/etc/profile.d/conda.sh" ]; then
        . "/opt/anaconda/etc/profile.d/conda.sh"
    else
        export PATH="/opt/anaconda/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
# cas
conda activate std
```

### Apt 管理器

-   管理器呢，最重要的就是换源。清华源测试不错。

```sh
# enable https
sudo apt install apt-transport-https ca-certificates

# edit config
cp /etc/apt/sources.list /etc/apt/sources_bak.list # make a backup
sudo vim /etc/apt/sources.list
sudo apt update
sudo apt list --upgradable
```

```sh
# system-wide apt configurations
# maintained by wootommy
# last update: 20200814

# tsinghua mirrors
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
```

-   一些比较有意思的指令。

```sh
apt list --installed
apt list --upgradable

apt search pkgname*
apt show pkgname
apt install pkgname=version
apt remove pkgname
apt purge pkgname # remove settings
apt autoremove # auto

apt update # apt-self
apt upgrade # all pkgs
apt full-upgrade # auto remove old version if necessary
```

### Linuxbrew

-   东西不多，好东西不少。换源。
-   添加的环境变量在前面。
-   目前安装 mysql 会有一些问题。无奈换位了 apt 安装。

```sh
# brew git
git -C "$(brew --repo)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git

# macos
git -C "$(brew --repo homebrew/core)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git
git -C "$(brew --repo homebrew/cask)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-cask.git
git -C "$(brew --repo homebrew/cask-fonts)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-cask-fonts.git
git -C "$(brew --repo homebrew/cask-drivers)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-cask-drivers.git
export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles'

# linux
git -C "$(brew --repo homebrew/core)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/linuxbrew-core.git
export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.tuna.tsinghua.edu.cn/linuxbrew-bottles

# update
brew update
```

-   一些终端命令行工具收集一下。

```sh
brew install zsh bash cmake make gcc gdb
brew install wget curl git vim neovim emacs ncdu slurm ack tpp icdiff autojump
brew install htop pstree pgrep pkill
brew install ag exa fd fzf thefuck tldr tree when awk lsd ccat jq shellcheck
brew install cowsay calcurse sl jp2a cmatrix figlet rig moreutils
brew install node@12 openjdk@11 ruby mycli

# ag/the_silver_searcher

# insult
sudo visudo
Defaults insults

# spacevim
curl -sLf https://spacevim.org/install.sh | bash
```

-   没有的还是要 apt 安装。

```sh
apt install nmon taskwarrior
apt install mysql
```
