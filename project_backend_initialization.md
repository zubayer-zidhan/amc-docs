# Project Back-End Initialization
### Create a VM on a cloud service like Azure, AWS, etc.
- While creating it will ask for a username, and then ask to save a .pem file for verification while logging onto the server via ssh.
- Save the file (it will not be available after this stage)
- SSH into the server via any application (bash, powershell, vscode-remote, etc.)
  - use the "username", "ip-address" of the server, and the ".pem" file to log in to the server
```bash
# Sample ssh code to login to the server
# Replace with path to file, username, and ip-address of the server
ssh -i "path\to\file\key.pem" username@x.x.x.x
```

### Install necessary dependencies
For the back-end service of the project to work, JAVA

```bash
sudo apt update
sudo apt upgrade

sudo apt install default-jdk

sudo apt install git

sudo apt install mysql-server

sudo mysql_secure_installation


mysql -u root

sudo systemctl start mysql

git clone "url.git"
git clone "https://github.com/anuragsahu12/automovillAPI.git"

# add JAVA_HOME ?
vim .bashrc


cd automovillAPI/

$ echo $JAVA_HOME

source ~/.bashrc

mvn clean install # install dependencies ?


vim application.properties
chmod +x mvnw
./mvnw clean package

# Add the following lines to the end of ~/.bashrc
# Add path variables
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export PATH=$PATH:$JAVA_HOME/bin

source ~/.bashrc

./mvnw clean install

java -jar MicroservicesApplication.jar

mysql -u dev1 -p

./mvnw clean package
cd target/
java -jar microservices-0.0.1-SNAPSHOT.jar

cd automovillAPI/src/main/resources/

sudo apt install openjdk-17-jdk

sudo vim /etc/nginx/sites-available/default 

sudo service nginx restart

sudo apt install nginx

sudo apt install snapd
sudo snap install core; sudo snap refresh core
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
sudo certbot certonly --standalone -d backendev.automovill.com

sudo vim /etc/nginx/sites-available/default 



sudo chmod 755 microservices-0.0.1-SNAPSHOT.jar

vim /etc/systemd/system/runSpringbootBackend.service
[Unit]
Description=AMC Back-End Server
After=syslog.target

[Service]
User=amcdevuser1
ExecStart=java -jar /home/amcdevuser1/automovillAPI/target/microservices-0.0.1-SNAPSHOT.jar
SuccessExitStatus=143

[Install]
WantedBy=multi-user.target




sudo systemctl daemon-reload
sudo systemctl enable runSpringbootBackend
sudo systemctl start runSpringbootBackend


mysql
CREATE USER 'username'@'localhost' IDENTIFIED BY 'somepassword';

GRANT CREATE, ALTER, DROP, INDEX, CREATE VIEW, SHOW VIEW ON dbName.* TO 'username'@'localhost';
FLUSH PRIVILEGES;



# rebuild.sh
cd ~/automovillAPI && git fetch && git pull && ./mvnw clean package && sudo systemctl restart runSpringbootBackend.service











```