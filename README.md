# Tambua Kenya

## Author
#### By:
1. Joseph Nganga ; lead developer
1. Moringa TM's ; Mentors
1. Moringa Students ; Assistant designers

### Description  
This is an application that enables users to view different categories of images per locations and also able to copy the link and share it to other friends

### Deployed link


### Setup and Installation  
To get the project .......  
### BDD

| Behaviour | Input | Output |
| --------- | ------| ------ |
|On loading the app you see the landing page with a navbar at the left| Clicking `search`| You are redirected to the homepage if you had left the page or just loads the homepage again if you are still on the homepage|
|Clicking the `Locations` link on the navbar | Mouse click |Displays a drop-down menu for `Kisumu`, `Mombasa` and `Nakuru` locations.
|Clicking the `Kenya`,`kisumu` or `Nakuru`links from the drop-down menu | Mouse click | Redirects a page where you can view various photos from the location that you selected|
|Clicking the `Today's Images` link | Mouse click | Redirects to a page where you can view images of today|
|Clicking any image| Mouse click | A modal opens with the details of the image including the image itself.|
  
##### Cloning the repository:  

##### Navigate into the folder and install requirements  
 ```bash 
cd gallery pipenv  install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pipenv install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations gallery
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
  
  
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 2.2.9](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
* [Git](for version control)
  
  
## Known Bugs  
* There are no known bugs currently,though i encountered many of it during deployment,but i finally managed 
## Support and contact details
call me on

<img src="https://bit.ly/2H4L6UZ" width="109" style="border-radius:50%;">:0798734442

<img src="https://bit.ly/383xk0Z" width="109" style="border-radius:50%;">:0778378174
 
 <img src="https://bit.ly/2Smueyp" width="109" style="border-radius:50%;">:nungari100@gmail.com

## License

[MIT License](LICENSE.md)
Copyright (c) [2020] [Joseph Nganga]
</a>