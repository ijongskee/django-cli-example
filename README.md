# django-cli-example
Using django-cli-example

## Features
1.**ADDING,UPDATING,DELETING CITY** 

2.**ADDING,UPDATING,DELETING BARANGGAY**

3.**ADDING,UPDATING,DELETING RESIDENT**

4.**SEARCHING RESIDENT BY LAST NAME, FIRST NAME, OR BARANGGAY**

5.**VIEWING THE RESIDENT ADDED ON CURRENT DATE**


##USAGE

Change into the outer mysite directory, if you haven’t already, and run the following commands(eg. **C:\Users\user_name\django-cli-sample\mysite>**)

## CITY

**ADDING NEW CITY**

Run this code on your command line:
```
$ python manage.py crud --add_city
```
You’ll see the following output on the command line:
```
Enter City Name:
```
Enter the city name you prefer to add, hit enter and you'll see the following after:
```
City Saved Successfully
```

**UPDATING CITY**

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
Successfuly Updated
```

**DELETING CITY**

Run this code on your command line:
```
$ python manage.py crud --delete_city
```
You’ll see the following output on the command line:
```
All Cities
    ID    |   City   |Date Updated|
    1     |SAMPLE CITY | 06/14/18 |
Enter the ID of the City you wish to delete :
```
Choose the city you want to delete by entering the ID, then you'll see the following after:
```
Successfully Deleted SAMPLE CITY
```

## BARANGGAY

**ADDING NEW CITY**

Run this code on your command line:
```
$ python manage.py crud --add_baranggay
```
You’ll see the following output on the command line:
```
All Cities
    ID    |   City   |Date Updated|
    1     |SAMPLE CITY | 06/14/18 |
Enter the City ID  :
```
Enter the the ID of the city where the baranggay belong in, then you'll see the following after:
```
Please Enter baranggay Name:
```
Enter the baranggay name you prefer to add, hit enter and you'll see the following after:
```
Baranggay saved Successfully
```

**UPDATING BARANGGAY**

Run this code on your command line:
```
$ python manage.py crud --update_baranggay
```
You’ll see the following output on the command line:
```
All Baranggay
    ID    |   City   |Baranggay |Date Updated|
    1     |   SAMPLE CITY | SAMPLE_B | 06/14/18 |
Enter the Baranggay ID you want to update :
```
Enter the Baraggay ID you wish to update, then you'll see the following:
```
All Cities
    ID    |   City   |Date Updated|
    2     |   SAMPLE CITY    | 06/14/18 |
Enter City ID :
```
After entering the city ID you'll see
```
Please Enter new baranggay Name:
```
After Entering the new baranggay name you'll see:
```
Baranggay saved Successfully
```
**DELETING BARANGGAY**

Run this code on your command line:
```
$ python manage.py crud --delete_baranggay
```
You’ll see the following output on the command line:
```
All Baranggay
    ID    |   City   |Baranggay |Date Updated|
    1     |   SAMPLECITY   |  SAMPLE_B  | 06/14/18 |
Enter the ID of the baranggay you wish to delete :
```
After choosing the ID you'll see:
```
Successfully Deleted asdasd
```

## RESIDENT

**ADDING NEW RESIDENT**
Run this code on your command line:
```
python manage.py crud --add_resident
```
You’ll see the following output on the command line:
```
All Cities
    ID    |   City   |Date Updated|
    2     |SAMPLE CITY | 06/14/18 |
Enter the ID of your city :
```
After choosing the CITY ID you'll see:
```
Baranggays from city 
    ID    |   City   |Baranggay |Date Updated|
    2     |   asd    | SAMPLE_b | 06/14/18 |
Enter the ID of your Baranggay : 
```
After choosing the baranggay ID you'll see:
```
Enter street:
Enter House Number 
Enter your First Name:
Enter you Middle Name : 
Enter your Last Name :
```
After Entering date needed you'll see:
```
Successfully saved the data
```
**UPDATING RESIDENT**
Run this code on your command line:
```
python manage.py crud --update_resident
```

You’ll see the following output on the command line:
```
         ID         |     First Name     |    Middle Name     |     Last Name      |        City        |     Baranggay      |       Street       |    House Number    |    Date Updated    |
         1          | SAMPLE FIRST NAME  | SAMPLE MIDDLE NAME |  SAMPLE LAST NAME  |        asd         |      SAMPLE_b      |   SAMPLE STREET    |   SAMPLE HOUSE NO  |      06/14/18      |
Enter resident ID to update :
```
Now pick the resident you want to edit by entering its ID, after picking you'll see:
```
All Cities
    ID    |   City   |Date Updated|
    2     |SAMPLE CITY | 06/14/18 |
Enter the ID of your city :
```
After choosing the CITY ID you'll see:
```
Baranggays from city 
    ID    |   City   |Baranggay |Date Updated|
    2     |   asd    | SAMPLE_b | 06/14/18 |
Enter the ID of your Baranggay : 
```
After choosing the baranggay ID you'll see:
```
Enter street:
Enter House Number 
Enter your First Name:
Enter you Middle Name : 
Enter your Last Name :
```
After Entering date needed you'll see:
```
Successfully saved the data
```
**DELETING RESINDENT**

Run this code on your command line:
```
python manage.py crud --delete_resident
```

You’ll see the following output on the command line:
```
         ID         |     First Name     |    Middle Name     |     Last Name      |        City        |     Baranggay      |       Street       |    House Number    |    Date Updated    |
         1          |       sdasd        |       asdas        |       dasda        |        asd         |      SAMPLE_b      |        asd         |   SAMPLE HOUSE NO  |      06/14/18      |
Enter resident ID to update :
```
After choosing the ID you'll see:
```
Successfully deleted resident
```
**GET RESIDENT(S) UPDATE TODAY/CURRENT DAY**

```
python manage.py crud --get_resident_updated_today
```
You’ll see the following output
```
    ID    |First Name|Middle Name|Last Name |   City   |Baranggay |  Street  |House Number|Date Updated|
    2     |SAMPLE FIRSTNAME|SAMPLE MIDDLE NAME|SAMPLE LAST NAME|SAMPLE CITY|SAMPLE BARANGGAY|SAMPLE STREET|SAMPLE STREET| 06/14/18 |
```

**SEARCHING RESIDENT(S) BY  LAST NAME**

Run this code on your command line (NOTE: sample is a data encoded by user):
```
python manage.py search --get_resident_by_last_name sample
```
You’ll see the following output that contains "sample" in First Name:

```
         ID         |     First Name     |    Middle Name     |     Last Name      |        City        |     Baranggay      |       Street       |    House Number    |    Date Updated    |
         2          |  SAMPLE FIRSTNAME  | SAMPLE MIDDLE NAME |  SAMPLE LAST NAME  |    SAMPLE CITY     |  SAMPLE BARANGGAY  |   SAMPLE STREET    |   SAMPLE STREET    |      06/14/18      |
```
**SEARCHING RESIDENT(S) BY FIRST NAME**

Run this code on your command line (NOTE: sample is a data encoded by user):

```
python manage.py search --get_resident_by_first_name sample
```
You’ll see the following output that contains "sample" text/string in First Name:
```
         ID         |     First Name     |    Middle Name     |     Last Name      |        City        |     Baranggay      |       Street       |    House Number    |    Date Updated    |
         2          |  SAMPLE FIRSTNAME  | SAMPLE MIDDLE NAME |  SAMPLE LAST NAME  |    SAMPLE CITY     |  SAMPLE BARANGGAY  |   SAMPLE STREET    |   SAMPLE STREET    |      06/14/18      |
```
**SEARCHING RESIDENT(S) BY BARANGGAY**

Run this code on your command line (NOTE: sample is a data encoded by user):

```
python manage.py search --get_resident_by_baranggay sample
```
You’ll see the following output that contains "sample" text/string in baranggay:
```
         ID         |     First Name     |    Middle Name     |     Last Name      |        City        |     Baranggay      |       Street       |    House Number    |    Date Updated    |
         2          |  SAMPLE FIRSTNAME  | SAMPLE MIDDLE NAME |  SAMPLE LAST NAME  |    SAMPLE CITY     |  SAMPLE BARANGGAY  |   SAMPLE STREET    |   SAMPLE STREET    |      06/14/18      |
```

**SEARCHING RESIDENT(S) BY CITY**

Run this code on your command line (NOTE: sample is a data encoded by user):

```
python manage.py search --get_resident_by_city sample
```
You’ll see the following output that contains "sample" text/string in city:
```
         ID         |     First Name     |    Middle Name     |     Last Name      |        City        |     Baranggay      |       Street       |    House Number    |    Date Updated    |
         2          |  SAMPLE FIRSTNAME  | SAMPLE MIDDLE NAME |  SAMPLE LAST NAME  |    SAMPLE CITY     |  SAMPLE BARANGGAY  |   SAMPLE STREET    |   SAMPLE STREET    |      06/14/18      |
```
