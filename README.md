# django-cli-example
Using django-cli-example

## Features
1.**ADDING,UPDATING,DELETING,VIEWING CITY** 

2.**ADDING,UPDATING,DELETING,VIEWING BARANGGAY**

3.**ADDING,UPDATING,DELETING,VIEWING RESIDENT**

4.**SEARCHING RESIDENT BY LAST NAME, FIRST NAME, OR BARANGGAY**

5.**VIEWING THE RESIDENT ADDED ON CURRENT DATE**


## USAGE
Change into the outer mysite directory, if you haven’t already, and run the following commands(eg. **C:\Users\user_name\django-cli-sample\mysite>**)

**CITY**

**Adding new City**

Run this code on your command line:
```
$ python manage.py crud --add_city
```
You’ll see the following output on the command line:
```
Enter City Name:
```
Enter the city name you prefer to add hit enter and you'll see the following after:
```
City Saved Successfully
```

**Updating City**
Run this code on your command line:
```
$ python manage.py crud --update_city
```
You’ll see the following output on the command line:
```
All Cities
    ID    |   City   |Date Updated|
    1     |  SAMPLE CITY  | 06/14/18 |
Enter the City ID you want to update:
```
Choose the city you want to update by entering the ID, then you'll be asked to enter the new City name:
```
Enter new City Name:
```
Enter the city name you prefer to add hit enter and you'll see the following after:
```
Successfuly Update
```
