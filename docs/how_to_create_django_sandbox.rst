Django Web Project Setup on Amazon EC2
======================================
This has been brodly categorized into Installation , Configuration and Activating Environment
====================================================================

Django Web Project Setup on Amazon EC2
======================================
This has been brodly categorized into Installation , Configuration and Activating Environment
====================================================================

Installation 
===================


What you need to do on EC2
==========================
		
1. Loginto  Amazon ec2  https://console.aws.amazon.com/ec2/v2/home?region=us-west-2
2. Pick up the template for instance launch - we are eusing  ubuntu server 13.1
3. Please ensure that your pem file is stored securely.....may be in your email or some where ...if you forget this you may have to forgo all your developemnts unless 
it is soucre controlled.
4. Conencting to it from putty is most imporatnt....Please follow this guide - http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html
5. Login EC2 Console with pem file(it does not need any passowrd,give user id as ubuntu)

Python Installation
====================

1. By default you will have installation of python 2.7.5+,you want some other version,please install .We are using python 2.7.5+,so no need to install as ubuntu supplies it by default.
2.If you want other python version ,please install this way.
Hint : wget http://www.python.org/ftp/python/2.7.6/Python-2.7.6.tgz => untar=> ./configure,make;make install	

PIP Installation
================
PIP is required to install other python packages and it is must have tool.

1. wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
2. sudo python get-pip.py ( please sudo to do as you do not have permissiion with ubuntu as user)
3. check if installation is fine - /usr/local/bin/pip; which pip
 
 
 Installing PosGre sql
 ============================
 
1. Install postgre dependencies first
sudo apt-get install libpq-dev python-dev
2.install PostgreSQL :
sudo apt-get install postgresql postgresql-contrib

3. You must be getting follow line in your output while installaing postgre sql.

ubuntu@ip-172-31-2-77:~$ which psql
/usr/bin/psql

Creating new cluster 9.1/main ...
  config /etc/postgresql/9.1/main
  data   /var/lib/postgresql/9.1/main
  locale en_US.UTF-8
  port   5432
update-alternatives: using /usr/share/postgresql/9.1/man/man1/postmaster.1.gz to provide /usr/share/man/man1/postmaster.1.gz (postmaster.1.gz) in auto mode
 * Starting PostgreSQL 9.1 database server                                                                                                                       [ OK ]
Setting up postgresql (9.3+146really9.1+148) ...
Setting up postgresql-contrib-9.1 (9.1.10-1) ...
Setting up postgresql-contrib (9.3+146really9.1+148) ...
Processing triggers for libc-bin ...

ubuntu@ip-172-31-2-77:~$ which psql
/usr/bin/psql


 Creating postgre DB
 =================
 
 Step Seven: Configure PostgreSQL
Let's start off our configuration by working with PostgreSQL. With PostgreSQL we need to create a database, create a user, and grant the user we created access to the database we created. Start off by running the following command:

1. Create database - log in as  "sudo su - postgres"
2. createdb createdb rsc
3. createuser -P  ( Note : put apppropriate values relavent to your project)

Enter name of role to add: rscadmin
Enter password for new role:
Enter it again:
Shall the new role be a superuser? (y/n) y
postgres@ip-172-31-2-77:~$ psql
psql (9.1.10)
Type "help" for help.

4. type  "psql"
5. grant all previlages to use

GRANT ALL PRIVILEGES ON DATABASE rsc TO rscadmin;

	
Reference :
https://www.digitalocean.com/community/articles/how-to-create-remove-manage-tables-in-postgresql-on-a-cloud-server
https://www.digitalocean.com/community/articles/how-to-install-and-configure-django-with-postgres-nginx-and-gunicorn		
		

Installing "nginx" Webserver
=============================
1. Install nginx with below commond

sudo apt-get install nginx	
		
		
Setting Virtual env:
======================
Ref : http://www.virtualenv.org/en/latest/

1. Install with folllow commond
sudo pip install virtualenv
2. go to $HOME
3.  virtualenv <wenv> Note : replace wenv with appropriate value
4. This will get your python bin and lib files under it .when activated, this enviornment it refers to libaries and binaies here only.
	
 Like below
 ==========
drwxrwxr-x 3 ubuntu ubuntu 4096 Feb 10 00:57 lib
drwxrwxr-x 2 ubuntu ubuntu 4096 Feb 10 00:57 include
drwxrwxr-x 2 ubuntu ubuntu 4096 Feb 10 00:57 local
drwxrwxr-x 2 ubuntu ubuntu 4096 Feb 10 00:57 bin

5. activat ethe virtual env this way :
this looks this way :
ubuntu@ip-172-31-4-82:~/wenv$ source bin/activate
(wenv)ubuntu@ip-172-31-4-82:~/wenv$


Django Installing 
============
1. while you are in wenv...virtual env... if not activate - source bin/activate
2. pip install django

Gunicorn
========
1. while you are in wenv...virtual env... if not activate - source bin/activate
2. pip install gunicorn

Install following additional packages
====================================
1. south  :  pip install south
2. fabric :  pip install fabric
3. sqlalchemy : pip install sqlalchemy
4. supervisor : pip install supervisor --pre
5. psqlpython interface : pip install psycopg2



Configuration
=================


Django project Configuration
============

Philip/Jolly : Please ignore step 1 and 2 as i have already done that and checkd in the code.
just git clone https://github.com/pjmkit/mission.git into wenv.


1. ~/wenv$ django-admin.py startproject webapp
2. Edit your settings.py file and add following config to it.
		2.1	'default': {
						'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
						'NAME': 'rsc',                      # Or path to database file if using sqlite3.
						# The following settings are not used with sqlite3:
						'USER': 'radmin',
						'PASSWORD': 'XXXXXXX',
						'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
						'PORT': '',                      # Set to empty string for default.
					}
					
		2.2 	LOGGING = {
				'version': 1,
				'disable_existing_loggers': True,
			}

        2.3. Add gunicorn to INSTALLED_APPS
		
        2.4. Add appropriate value to STATIC where you are hosting your statiuc files
			 eg : /home/ubuntu/wenv/webapp/webapp/static

3. Goto project folder where mange.py is residing 
4. python manage.py syncdb

 
 nginx Configuration
 ================
 
 1. Go to sites-available directory : cd /etc/nginx/sites-available ( or where ever you nginx is installed)
 2. Open a file named after your django project : eg sudo vim webapp
 3. Paste following code 

 server {
        server_name XXXXXXXXXXXX.us-west-2.compute.amazonaws.com;
		

        access_log off;

        location /static/ {
            alias /home/ubuntu/wenv/mission/webapp/static/;
        }

        location / {
                proxy_pass http://127.0.0.1:8001;
                proxy_set_header X-Forwarded-Host $server_name;
                proxy_set_header X-Real-IP $remote_addr;
                add_header P3P 'CP="ALL DSP COR PSAa PSDa OUR NOR ONL UNI COM NAV"';
        }
    }
	
	Note : Kindly change the server name to where you are hosting.
 4. inform NGINX server where your project configuration is available
 
		4.1 cd /etc/nginx/sites-enabled
		4.2 sudo ln -s ../sites-available/webapp
		4.3 remove the reference to the default project -  sudo rm default
 
Activating Environment
================================
 
Running gunicorn 
==================
Reference :  https://docs.djangoproject.com/en/1.4/howto/deployment/wsgi/gunicorn/

1. To run gunicorn  :  python manage.py run_gunicorn  (Note : go to your project home)
 

Running nginx 
==================
1. To run nginx  :  sudo service nginx restart
 
 
Testing
======================
 
1. Before you check if env is working or not in browser.wget the url and results in error free respose it is working fine
 
 wget "http://XXXXXXXXXXXXXXXX.us-west-2.compute.amazonaws.com/"

2. If you get 404 error then NGINX is not up and running
 
3. If you 500 error  then gunicorn is not up and running ,bring it up

4. If it is working fine through wget and not from browser,check your SecurityGroups
 
 4.1 go to your AWS :
  https://console.aws.amazon.com/ec2/home?region=us-west-2#s=SecurityGroups
 4.2  add 8001 or any port that you gunicorn running along with port 22 , 80 and 8080 to custom rules.

 5. If you get this message ,pat on your back and drop a message.
 
 It worked!
Congratulations on your first Django-powered page.
 





 
