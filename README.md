# projects-vote 
## Author
Norah Waswala
## Project Description
 
## Demo
### Landing Page
![screen](/static/image/screen.png)
### Single Image
![screen](/static/image/screen1.png)
### API 
![screen](/static/image/screen1.png)
## User Story
  
* A user can view posted projects and their details.  
* A user can post a project to be rated/reviewed. 
* A user can rate/ review other users' projects.  
* Search for projects.  
* View projects overall score.
* A user can view their profile page.  
## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Get all projects, click on an image to view the full image page|
| Authentication | **Login/Register** |  Register for new users, otherwise login|
| Rating| **Rate project** |  A user is re-directed to ratings view|
|Search| **Search button**| A user can search projects by project's name|

## Requirements
The application requires the following installations to operate:
* SQL database
* pyperclip
* pip
* django
### Technologies Used
* Python3.8
* django
* Heroku
* Rest APIs
### Project Setup Instructions
* Open Terminal {Ctrl+Alt+T}
* Fork the repository
* Git clone https://github.com/Norah-Waswala/project-votes.git
* code . or atom . depending on the text editor of your choice
* * Move to the folder and install requirements
* cd my-gallery
* pip install -r requirements.txt
* Exporting Configurations
* export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
## Support and contact details
For more information, find me at my email (https://norah.waswala15@gmail.com)

## link to live site on heroku pages

## License and copyright information
[MIT LICENSE](LICENSE)
Copyright (C) [2022] [@ Norah-Waswala]
