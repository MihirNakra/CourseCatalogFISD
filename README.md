# Course Catalog FISD

By Mihir Nakra

nakramihir@gmail.com

# I. Introduction / Purpose

The idea for this project came directly from my day to day life. When I was a Junior in high school and it came time to pick our courses for the following year, I took a peek at my school district's course catalog to find courses. That process proved to be tedious, as the course catalog was a multiple hundred page long PDF document that was hard to traverse. At the same time I was taking Harvard's CS50 class, and after learning basic web development with flask and database management with sqlite3, I decided to solve this problem. 

One thing I want to note is that my data collection methods weren't perfect due to the somewhat unpredictable nature of how courses are layed out on the course catalog PDF. I am currently in the process of manually editing the data and creating more categories to allow for an even easier way to search courses. 

# II. Methodology

As I mentioned in the introduction, I used flask and sqlite3 to create this website. The app.py file contains the logic for the website and serves as the backend. It directly accesses the catalog.db database and sends data to the front end, where it is displayed dynamically either using javascript or jinja2's template capabilities. App.py also responds to certain routes of the website, displaying certain html files in correspondence.

The /static folder contains the non-html static files, which include the Frisco ISD icon and my custom css file

The /templates folder contains every html file I wrote for this project, including the template html files as well

I also have uploaded this project onto Heroku servers, which allows me to actually run the website on the internet and not just locally. Unfortunately, at this time I am unable to keep the website running 24/7.
