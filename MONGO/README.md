# DATABASE

*Storage, unstructured data, profiles and  authentication.*

*MONGO CONTAINER CONSISTS OF*

   *`MONGODB SERVER`

# SETUP
```
Install mongodb version >= 5.0.
```
# Dependencies
```
sudo apt install default-jre
sudo apt install pkg-config
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add - 
sudo nano /etc/apt/sources.list.d/mongodb.list 
deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse
sudo apt update 
```
# INSTALL
```
sudo apt install mongodb-org 
```
# VERSION
```
mongo
db.version()
```
# CONDITIONS 
```
#[ENABLE] redis-server service
   sudo systemctl enable mongod 
#[RESTART] redis-server service
   sudo systemctl restart mongod
#[STOP] redis-server service
   sudo systemctl stop mongod
#[STATUS] redis-server service
   sudo systemctl status mongod
```
# CONFIG 
```
sudo lsof -i | grep mongo
sudo vi /etc/mongodb.conf
#REMOTE CONNECTION
   [BEFORE] bind 127.0.0.1
   [AFTER]  bind 127.0.0.1,[MONGO_SERVER_IP]
#RESTART
   sudo systemctl restart mongodb
#STATUS
   sudo systemctl status mongodb
```
# PORTS 
```
mongodb --27017
sudo ufw allow 27017/tcp
sudo ufw allow 27017/udp
```
