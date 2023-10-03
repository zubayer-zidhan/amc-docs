# Project Back-End Initialization

- [Project Back-End Initialization](#project-back-end-initialization)
    - [Create a VM on a cloud service like Azure, AWS, etc.](#create-a-vm-on-a-cloud-service-like-azure-aws-etc)
    - [Install necessary dependencies](#install-necessary-dependencies)
    - [Enable https](#enable-https)
        - [Create a SSL certificate using certbot](#create-a-ssl-certificate-using-certbot)
    - [Clone the back-end github repo](#clone-the-back-end-github-repo)
    - [Set up path variable](#set-up-path-variable)
    - [Set up MySQL](#set-up-mysql)
    - [Set up Spring Boot](#set-up-spring-boot)

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
For the back-end service of the project to work we need:
  - java
  - git
  - mysql
  - nginx
  - certbot

The OS is assumed to be Ubuntu in the following commands.

```bash
# Update and Upgrade the system
sudo apt update
sudo apt upgrade

# Install java-17(used in this project)
sudo apt install openjdk-17-jdk

# Install git
sudo apt install git

# Install vim
sudo apt install vim

# Install mysql
sudo apt install mysql-server

# Complete securing mysql
sudo mysql_secure_installation

# Start the mysql service
sudo systemctl start mysql

# Will be used to serve the API(http in springboot) as https, using reverse-proxy
sudo apt install nginx
```

### Enable https
To enable https connections, the following requirements should be met:
- The VM should have ability to accept http and https connections.
- Create a sub-domain with an A record pointing to the IP address of the server(VM)
  - The domain name of that record will be used to access the back-end
  - It will also be used to create SSL certificate

##### Create a SSL certificate using certbot
```bash
    # Install snap store 
    sudo apt install snapd

    # Update the snap packages
    sudo snap install core; sudo snap refresh core

    # Install certbox
    sudo snap install --classic certbot

    # Link
    sudo ln -s /snap/bin/certbot /usr/bin/certbot

    # Stop the nginx server because it may already be occupying port:80
    sudo systemctl stop nginx

    # Install the certificate only
    # Assuming the created sub-domain is "backend.automovill.com"
    # Change it with appropriate sub-domain name 
    sudo certbot certonly --standalone -d backend.automovill.com

    # Modify the /etc/nginx/sites-available/default
    vim /etc/nginx/sites-available/default
```

Add the following lines to the file
  - read the existing text, and modify accordingly, the above is just the structure
  - remove the existing location / route, otherwise error will show up.
```text
    listen 443 ssl;
    server_name _;  # Listen on any hostname (wildcard)

    ssl_certificate /etc/letsencrypt/live/backend.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/backend.com/privkey.pem;

    location / {
            proxy_pass http://127.0.0.1:8080;  # Forward to Spring Boot
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;

    }
```
Save the file(:wq)
```bash
    # restart the nginx server
    sudo service nginx restart

```

### Clone the back-end github repo
```bash
# Replace with the link to github repo
git clone "back_end.git" 
```

### Set up path variable
The JAVA_HOME path variable is required while building/running the back-end
```bash
vim ~/.bashrc
```

Add the following lines to the end of the .bashrc file
```text
# Add path variables
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export PATH=$PATH:$JAVA_HOME/bin
```

Save changes and reload bash to consider changes
```bash
source ~/.bashrc
```

### Set up MySQL
- Log in as root user
- Create the database to be used 
- Create a new user with just the CRUD priveleges on the database.
- The tables will be created automatically by the back-end on running

```bash
# Login as root
mysql -u root
```

```sql
/* The name of db is assumed to be "amcDB"  */
CREATE DATABASE amcDB;

/* Create a new user "username" with password "somepassword"  */
CREATE USER "username"@"localhost" IDENTIFIED BY "somepassword";

/* Grant "username" CRUD priveleges on "amcDB"  */
GRANT CREATE, ALTER, DROP, INDEX, CREATE VIEW, SHOW VIEW ON dbName.* TO "username"@"localhost";
FLUSH PRIVILEGES;
```

### Set up Spring Boot
```bash

```



```bash

```



```bash
mysql -u root




cd automovillAPI/



mvn clean install # install dependencies ?


vim application.properties
chmod +x mvnw
./mvnw clean package


./mvnw clean install

java -jar MicroservicesApplication.jar

mysql -u dev1 -p

./mvnw clean package
cd target/
java -jar microservices-0.0.1-SNAPSHOT.jar

cd automovillAPI/src/main/resources/



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