### Logicaldoc-CE migration handler


Logicaldoc-CE is a pretty open source document management system. Compared to commercial version useful features are 
deactivated. For instance, you can´t migrate to a new version of Logicaldoc-CE. You can´t back up your data unless you 
have scripts that do it for you. Even with backing up the database and saving Logicaldoc´s repository, it won´t be 
possible to migrate to a new version of Logicaldoc-CE.

This tool helps you to migrate your data to a new version. It uses Logicaldoc´s Api to achieve it. 

#### Requirements
* requests
* Python3.5+

#### Settings
Every Logicaldoc installation should have an account with high privileges that have access to everything. Adjust these 
credentials in the configuration file. In most cases `api_entry` shouldn´t be modified. It is the entrypoint of 
Logicaldoc-CE´s Api.
* ./config/connection.ini

#### Logging
You can find information what the handler logs. 
* ./log/logicaldoc.log

#### Data
Here you find you exported data. I will be used for importing as well. The metadata files contain information of every 
file and folder your Logicaldo-CE has.
* ./data/file_metadata.json
* ./data/folder_metadata.json

#### Run
It does not matter if you use Windows or Linux. The tool doesn´t require OS related stuff
```shell
python run.py [export|import]
```

