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
        - [Create the application.properties file](#create-the-applicationproperties-file)
        - [Fill in the application.properties file](#fill-in-the-applicationproperties-file)
        - [Install the dependencies](#install-the-dependencies)
        - [Build and Run](#build-and-run)
        - [Create an initial temp admin user, that will be used to create future users](#create-an-initial-temp-admin-user-that-will-be-used-to-create-future-users)
    - [Run the application as a background process](#run-the-application-as-a-background-process)
        - [Create a System Service](#create-a-system-service)
        - [Rebuild and Update on changes in code](#rebuild-and-update-on-changes-in-code)

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
##### Create the application.properties file
```bash
# Navigate to the resources directory
# The name of the repo directory is assumed to be "automovillAPI"
cd ~/automovillAPI/src/main/resources

# Create the application.properties file
# This file contains all the info required to connect to the database
vim application.properties
```

##### Fill in the application.properties file
```text
spring.datasource.url = jdbc:mysql://localhost:3306/amcDB
spring.datasource.username = username
spring.datasource.password = somepassword
spring.datasource.driver-class-name = com.mysql.cj.jdbc.Driver


spring.jpa.properties.hibernate.dialect = org.hibernate.dialect.MySQLDialect
spring.jpa.hibernate.ddl-auto = update


application.security.jwt.secret-key = 256bitKeyToBeUsedForEncryption
```
Save the file

##### Install the dependencies
```bash
# Navigate to root directory
cd ~/automovillAPI/

# Grant executing permission to mvnw
chmod +x mvnw

# Install all dependencies from pom.xml
./mvnw clean install
```

##### Build and Run
```bash
cd ~/automovillAPI/
# Create a build
./mvnw clean package

# Navigate to target directory, where the build is stored
cd target/

# Only owner can write, read and execute for everyone
# Grant execute permission
sudo chmod 755 microservices-0.0.1-SNAPSHOT.jar

# Run the JAVA program
java -jar microservices-0.0.1-SNAPSHOT.jar


# Currently the program will run as long as the above java program is not terminated
# We will make it a background process that is always online later on
# Ctrl + C -> exit the program
# The API should work as long the program is running
```


##### Create an initial temp admin user, that will be used to create future users
Currently in the back-end:
- only admins can add users to the database
- API call without an admin JWT will be rejected
- e need to create an initial temp admin level user by disabling the admin check for creation
- after that, we can enable the filter again
- add new users(admin/non-admin) using the admin credentials
- if needed, later remove the temp admin(if other admin level users exist), since other admin user/s are present, and they can be used for adding more users


**Remove the check for admin token**<br>
The following steps are to be followed:
- Navigate to the SecurityConfig.java file
```bash
cd ~/automovillAPI/src/main/java/automovill_microservices/microservices/config/

# Use any code editor (vscode, vim, etc.)
vim SecurityConfiguration.java
```

- Change the following lines of code:

`Before`
```java
                                                .requestMatchers("/api/v1/auth/register").hasRole(ADMIN.name())
                                                .requestMatchers(GET, "/api/v1/auth/register").hasAuthority(ADMIN_READ.name())
                                                .requestMatchers(POST, "/api/v1/auth/register").hasAuthority(ADMIN_CREATE.name())
                                                .requestMatchers(PUT, "/api/v1/auth/register").hasAuthority(ADMIN_UPDATE.name())
                                                .requestMatchers(DELETE, "/api/v1/auth/register").hasAuthority(ADMIN_DELETE.name())
```

`After`
```java
                                                // .requestMatchers("/api/v1/auth/register").hasRole(ADMIN.name())
                                                // .requestMatchers(GET, "/api/v1/auth/register").hasAuthority(ADMIN_READ.name())
                                                // .requestMatchers(POST, "/api/v1/auth/register").hasAuthority(ADMIN_CREATE.name())
                                                // .requestMatchers(PUT, "/api/v1/auth/register").hasAuthority(ADMIN_UPDATE.name())
                                                // .requestMatchers(DELETE, "/api/v1/auth/register").hasAuthority(ADMIN_DELETE.name())
```

- This remove the filter that checks for a token with "admin" priveleges while creating a new user.

- After adding an admin user, change the code back to its original state(uncomment the lines of code)

**Re-Build and run the application**<br>
Refer to the steps in [Build and Run](#build-and-run)

**Use Postman or some other similar app to send a POST request to add an admin level user**<br>
`Example Request`
```http
POST /api/v1/auth/register
Content-Type: application/json
{
    "username": "tempAdminName",
    "password": "somepasssword",
    "admin": true   
}
```

`Example Response`
```http
HTTP/1.1 200 OK
Content-Type: application/json
{
    "token": "eyJhbGciOiJIUzI1NiJ9.eyJyb2xlIjpbeyJhdXRob3JpdHkiOiJST0xFXsInN1YiI6IndvcmtzaG9wMTIiLCJpYXQiOjE2OTU1ODg1MzksImV4cCI6MTY5Njg4NDUzOX0.N6cfpqJnrnEX46cUvp3RAbnTd0dB1Jq7HUE-Q2msMcI"
}
```
Use the token returned to create future users.
The token can also be retrieved/regenerated in case of expiry by logging is using the `/api/v1/auth/authenticate` end-point, this end-point is open for all


**Re-Add the check for admin token**<br>
The following steps are to be followed:
- Navigate to the SecurityConfig.java file
```bash
cd ~/automovillAPI/src/main/java/automovill_microservices/microservices/config/

# Use any code editor (vscode, vim, etc.)
vim SecurityConfiguration.java
```

- Change the following lines of code(uncomment):

`Before`
```java
                                                // .requestMatchers("/api/v1/auth/register").hasRole(ADMIN.name())
                                                // .requestMatchers(GET, "/api/v1/auth/register").hasAuthority(ADMIN_READ.name())
                                                // .requestMatchers(POST, "/api/v1/auth/register").hasAuthority(ADMIN_CREATE.name())
                                                // .requestMatchers(PUT, "/api/v1/auth/register").hasAuthority(ADMIN_UPDATE.name())
                                                // .requestMatchers(DELETE, "/api/v1/auth/register").hasAuthority(ADMIN_DELETE.name())
```

`After`
```java
                                                .requestMatchers("/api/v1/auth/register").hasRole(ADMIN.name())
                                                .requestMatchers(GET, "/api/v1/auth/register").hasAuthority(ADMIN_READ.name())
                                                .requestMatchers(POST, "/api/v1/auth/register").hasAuthority(ADMIN_CREATE.name())
                                                .requestMatchers(PUT, "/api/v1/auth/register").hasAuthority(ADMIN_UPDATE.name())
                                                .requestMatchers(DELETE, "/api/v1/auth/register").hasAuthority(ADMIN_DELETE.name())
```

- This adds the filter which checks for a token with "admin" priveleges during the creation of a new user.

### Run the application as a background process
Currently, the applicaton has to run manually, and terminates when the user logs out.

So, run it as a background process, that is always online

##### Create a System Service
```bash
# The name of the service is assumed to be "runSpringbootBackend"
# Rename it as required
vim /etc/systemd/system/runSpringbootBackend.service
```

Add the following lines of text inside the "runSpringbootBackend.service" file
Modify the file as required(e.g. change `username` to the logged in user's name in the server)
```text
[Unit]
Description=AMC Back-End Server
After=syslog.target

[Service]
User=amcdevuser1
ExecStart=java -jar /home/username/automovillAPI/target/microservices-0.0.1-SNAPSHOT.jar
SuccessExitStatus=143

[Install]
WantedBy=multi-user.target
```

Save and Exit
```bash
# Reload to add new service
sudo systemctl daemon-reload

# Enable the service
sudo systemctl enable runSpringbootBackend

# Start the service
sudo systemctl start runSpringbootBackend
```
Now, the application will always be running

##### Rebuild and Update on changes in code
CI-CD is not set-up, so it is done manually using a script
**Create a rebuild.sh script**
Run this script after you push any changes to the github-repo

The script does the following:
  - pull any changes from github
  - rebuild the application
  - restart the background service "runSpringbootBackend.service"

```bash
cd ~
vim rebuild.sh
```

Add the following to the file:
```text
cd ~/automovillAPI && git fetch && git pull && ./mvnw clean package && sudo systemctl restart runSpringbootBackend.service
```

Save and Quit
```bash
# Grant executing priveleges to current user
chmod u+x rebuild.sh
```

To run the script:
```bash
cd ~
./rebuild.sh
```

This concludes the back-end initialization part.
