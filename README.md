# Awards
By Agnes Okutoyi
  
## Description  
This project allows users to post their projects for other users to rate according to design, usability and content 

## User Story  
  
* A user can view posted projects and their details.  
* A user can post a project to be rated/reviewed. 
* A user can rate/ review other users' projects.  
* Search for projects.  
* View projects overall score.
* A user can view their profile page.  
  
  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 git@github.com:Ag-nes/Awards.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Awwwards pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv env - source env/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations awards
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  

### Technology used  
  
* Python3.8.10
* Django 4.0.2
* Html
* Css


### Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
### Contact Information   
* If you have any question or contributions, please email me at [faithagnes2@gmail.com]  
  

### MIT LICENCE
 * Copyright (c) 2022 Agnes Nafula


