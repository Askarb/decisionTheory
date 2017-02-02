# decisionTheory
Ten Iosif Grigor'evich - Decision theory, Kyrgyz State Technical University,  

# SSH
git clone git@github.com:Askarb/decisionTheory.git


#Установка окружения на Linux
sudo apt-get install python  python3-dev  python3-setuptools  python3-pip
sudo pip3 install virtualenv


#Создаем виртуальное окружение для проекта
cd ~/PROJECTS/decisionTheory/ # заходим в папку с проектом
virtualenv --no-site-packages --distribute -p /usr/bin/python3 venv  # Важно, что мы используем 3-ю версию Python.


# Активируем виртуальное окружение:
source ./venv/bin/activate
pip install -r requirements.txt # устанавливаем зависимости


