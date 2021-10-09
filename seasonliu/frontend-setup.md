#  Next.js Set up

[source](https://www.coderrocketfuel.com/article/how-to-deploy-a-next-js-website-to-a-digital-ocean-server)

This article will talk about:

1. Config a new server

    - create a new user

    - create ssh connection for new user

    - enable UFW firewall

2. Config Domain

    - install and config nginx

    - buy domain name

    - add SSL

3. Deploy Next.js App

    - git clone / git pull App, and build Next.js App

    - install Node.js and npm

    - install pm2

    - run Next.js App with pm2

# #  Configure Your New Server

In this section, we'll walk through how to gain remote access to the server and set up some basic configuration to help keep it secure before we deploy and run your Next.js application on it.

# # #  Access Server Using Root

```command
ssh root@server_ip_address
```

# # #  Create A New User

1. create a new user
    
    ```command
    adduser bob
    ```

2. add new user to `sudo` group, so that new user can run `sudo` commands, has the root privileges.

    ```command
    usermod -aG sudo bob
    ```

After creating a user with root privileges, all the operations are done by this user.

```command
su - bob
```

# # #  Add Public Key Authentication

By setting up public-key authentication for the new user, it will increase your server's security by requiring a private SSH key to login in instead of anyone being able to access the server via password.

```command
ssh-keygen

ssh-copy-id bob@server_ip_address
```

After successfully authenticating, your public key will be added to the server user's `.ssh/authorized_keys` file. The corresponding private key can now be used to log into the server.

# # #  Add a Basic Firewall

Another security improvement we can make to the server is to add a basic firewall.

Ubuntu servers can use the `UFW` firewall to ensure **only connections to certain services** are allowed.

1. add allowed Apps, `OpenSSH` : `sudo ufw allow OpenSSH`

2. Apps allowed by UFW : `sudo ufw app list`

3. enable UFW : `sudo ufw enable`

4. check UFW status : `sudo ufw status`

# #  Configure Nginx

install it: 

```command
sudo apt-get update && sudo apt-get install nginx
```

There are three profiles available for Nginx:

- Nginx Full: opens both port 80 (normal, unencrypted web traffic) and port 443 (TLS/SSL encrypted traffic)

- Nginx HTTP: opens only port 80 (normal, unencrypted web traffic)

- Nginx HTTPS: opens only port 443 (TLS/SSL encrypted traffic)

```command
sudo ufw allow 'Nginx Full'
```

# #  Configure a Domain Name

Buy it.

For exemple, we bought the `example.com` and `www.example.com` URLs.

# #  Obtain SSL Certificates

Let's Encrypt is a Certificate Authority (CA) that provides an easy way to obtain and install free SSL certificates, thereby enabling encrypted HTTPS on web servers. It simplifies the process by providing a software client, Certbot, that attempts to automate most (if not all) of the required steps.

# # #  Install Certbot 

```command
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt install python-certbot-nginx
```

# # #  Obtain SSL Certificates

```command
sudo certbot --nginx -d example.com -d www.example.com
```

This command runs certbot with the `--nginx` plugin and also uses the `-d` directive to specify the names we want certificates to be valid for.

The redirect option is the suggested choice.

Let's Encrypt’s certificates are only valid for ninety days. This is to encourage users to automate their certificate renewal process.

The certbot package we installed takes care of this for us by running `certbot renew` **twice a day** via a systemd timer. On non-systemd distributions, this functionality is provided by a script placed in `/etc/cron.d`. This task runs **twice a day** and will renew any certificate that’s within **thirty days of expiration**.

To test the renewal process, you can do a dry run with certbot:

```command
sudo certbot renew --dry-run
```

# #  Config Node.js

To run your Next.js application, you'll need to have Node.js installed on the server. 

```command
cd ~
```
use curl to retrieve the installation script for the Node.js 12.x archives (replace 12.x with the version of Node.js you want to use):

```command
curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
```

```command
sudo bash nodesource_setup.sh
```

The PPA has now been added to your configuration and your local package cache should have automatically updated. 

The nodesource_setup.sh script won't be needed again, so let's delete it:

```command
sudo rm nodesource_setup.sh
```

You can now install the Node.js package

```command
sudo apt-get install nodejs
```

Now, node.js is installed, test it:

```command
node --version

npm --version
```

It's optional but recommended to install a node manager, `n` or `nvm`. I use `n`.

```command
sudo npm install -g n
```

Then, intall node version.

```command
n lts
```

Now, there are 2 nodejs installed.

```command
which -a node
```

```
/usr/bin/node        #  old one
/usr/local/bin/node  #  new one, added by n
```

remove the old one

```command
sudo apt-get uninstall nodejs
```

Finally, update `npm`

```command
npm install -g npm@latest
```

# #  Deploy the Next.js Application

To deploy your Next.js website, we'll need to push the code for your project to GitHub (or Gitlab) and pull it into our DigitalOcean server. Then we'll run the application in production mode and keep it running forever using the PM2 NPM package.

# # #  Push Application Code To GitHub/Gitlab

```.gitigore
#  .gitigore

#  Logs
logs
*.log
npm-debug.log*

#  Runtime data
pids
*.pid
*.seed

#  Directory for instrumented libs generated by jscoverage/JSCover
lib-cov

#  Coverage directory used by tools like istanbul
coverage

#  nyc test coverage
.nyc_output

#  Grunt intermediate storage (http://gruntjs.com/creating-plugins# storing-task-files)
.grunt

#  node-waf configuration
.lock-wscript

#  Compiled binary addons (http://nodejs.org/api/addons.html)
build/Release

#  Dependency directories
node_modules
jspm_packages

#  Optional npm cache directory
.npm

#  Optional REPL history
.node_repl_history
.next
```

# # #  Configure & Run Your Application On The Server

`git clone` the project:

```command
cd ~

git clone https://github.com/your_github_username/your_repository_name.git website
```

The website portion of the command will ensure the name of the project folder created is `/website`.

Then install App:

```
cd website

npm install

npm run build
```

When it's complete, a new `/.next` folder will be created in your project directory. The production version of your website will be ran using the code in that folder.


# # #  Install & Use PM2 To Run Application

Install it globally:

```command
sudo npm install -g pm2
```

run the application with PM2:

```command
cd website

pm2 start --name=website npm -- start
```

The specific command we used gives the application the `name` of "website" within PM2. This will help us easily identify all the applications running within PM2 as we add more.

start pm2:

```command
pm2 startup systemd
```

In the resulting output on the last line, there'll be a command that you must run with superuser privileges:
```
[PM2] Init System found: systemd
[PM2] You have to run this command as root. Execute the following command:
sudo env PATH=$PATH:/usr/bin /usr/lib/node_modules/pm2/bin/pm2 startup systemd -u bob --hp /home/bob
```

Copy and paste the command that was generated (same as above but with your username instead of bob) to have PM2 always start when your server is booted.

This will create a `systemd` unit that will run PM2 for your user on boot. This PM2 instance, in turn, will run all the applications configured to run using PM2. To check the status of the new systemd unit, use the following command:

```command
systemctl status pm2-bob
```

# #  Configure Nginx as a Reverse Proxy

Next application is running and listening on `localhost:3000`, we need to make it so people from the outside world can access it. 

On Debian systems (i.e. Ubuntu), Nginx server configuration files are stored in `/etc/nginx/sites-available` directory, which are enabled through **symbolic links** to the `/etc/nginx/sites-enabled` directory.

```
#  /etc/nginx/sites-available/example.com

server {
        listen 80;
        listen [::]:80;

        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;

        #  default setting is above, following setting is custom
        
        #  set URL
        server_name example.com www.example.com;

        #  set Reverse Proxy
        location / {
                proxy_pass http://localhost:3000;
                proxy_http_version 1.1;
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection 'upgrade';
                proxy_set_header Host $host;
                proxy_cache_bypass $http_upgrade;
        }
}
```

save the file and create a symbolic link

```
sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/
```

More config can be done in `/etc/nginx/nginx.conf`.

Finally,  do lint check and restart nginx

```
sudo nginx -t
sudo systemctl restart nginx
```

# #  Future Deployment

In the future, you'll most likely need to push new code updates. To do so, you can follow these steps:

```command
#  user: bob

cd website
sudo pm2 stop website
git pull
npm install
npm run build
sudo npm start website
```