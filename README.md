cd ~
nano .bash_aliases
#ode umisto mate stavit svoj user direktorij kako se zove
alias windows='cd /mnt/c/Users/Mate'
#izades is nano

windows

git clone https://github.com/MarkoKuret/denter.git

#za instaliranje pythona na unix-u
sudo apt update && upgrade
sudo apt install python3 python3-pip ipython3

#za preuzet virtualni enviroment
sudo apt install python3-venv
#komanda za kreiranje venva
python3 -m venv venv
#za aktiviranje
source venv/bin/activate
#
python3 -m pip install -r requirements.txt
#pokretanje
python3 pokreni.py


