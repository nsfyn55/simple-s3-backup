simple-s3-backup
================

This repo contains a set of scripts for managing rudimentary backups and publishing them to s3. The first script is a shell script that moves a set of target directorys to the _/tmp_ folder, tars them with gzip compressions, appends the date, and pushes to s3. The second script is a python script that does pruning. It will simply prune based on the name of the backups such that only the five latest remain.

backups will populate in your target s3 bucket with a name similiar to ```backup_02_01_2012```. Note when the backups are pruned it will use the date in the name not the date on which the backup was uploaded.

## Dependencies ###
- Access id and secrect key to your Amazon Web Services account
- An s3 bucket that you can write to
- the http://s3tools.org/s3cmd binary installed
- a cron daemon 
- Python 2.7.3

## Usage ##
I use the tools with a cron job that zips up my ```src```,```docs```, and few other dot file directories. In there current form you will need to crack open the ```backup-box``` script and add the name of your s3 bucket. This script also assumes you have a ```.s3cmd``` file in the root of your cron owner's home directory with your ```access id``` and ```secret key ``` specified.

Similarly with the ```bak-cleaner.py``` script you will need to edit the script and supply your ```access id```, ```secret key```, and the s3 destination bucket

The final step is to create is to schedule a cron to run the whole thing. Below is my example cron entry. I am using a python virtual environment created through pythonbrew for the python script. If you do this you can run a ```pip install -r requirements.txt``` on the included requirements text. This will create a virtual environment in the canonical pythonbrew path with the necessary python dependencies. Then I just call the shell script and if the return code is 0 I execute the python script using the binary at the in the pythonbrew virtual environment path.

```
0 9 * * * /usr/local/bin/backup-box && /usr/local/pythonbrew/venvs/Python-2.7.3/backup/bin/python /usr/local/bin/bak-cleaner.py
```
