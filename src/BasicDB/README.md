Programming Assignment 5
================================

**Fundamentals of Modern Software**  
**Fall 2019**  
**Due 11:59 PM, Friday October 11**

Introduction
------------


**REMINDERS**

1. **When you are done, be sure to submit your work.**
2. **You must adhere to the collaboration policy in the syllabus. You MAY NOT copy the code of someone else in the class or allow someone else to copy your code.**
3. **Be sure to test your programs thoroughly. We will.**
4. **Your output should match the output in the samples EXACTLY, to the letter.**

This assignment may be submitted for full credit by 11:59 PM on Friday, October 11, or with a 20% late submission penalty by 11:59 PM on Sunday, October 13.


zipcode-queries.py
--------

Using the basicdb package and the `geo.json` database, write the following functions. **Your functions should never attempt to read `geo.json` or `geozipcodes.csv` directly. All access to the data must be through the functions defined in `basicdb.py`.**

`state_of(zipcode)`: Returns the name of the state in which `zipcode` is located.

`northernmost(state)`: Returns the northernmost zipcode in `state`.

`zipcodes_in_city(city_name)`: Returns the total number of zip codes in the City `city_name`.

`states_by_size()`: Returns a list of state names, sorted in order from the state containing the fewest zip codes to the state containing the most. _This cannot be done solely using the basicdb interface. You will need to embed your calls to basicdb inside some additional Python code._



classlist.py
--------

Using the basicdb package and the `registrar.json` database, write a program that takes a single command-line argument and prints out a report on a specified course:

    $ python classlistSOLUTION.py 3
    Introduction to Asian History meets TH10 in Lecture Hall A
    Albert Aziz
    Derek Dortmund
    Eustace Ennis
    Frances Fan
    Current enrollment: 4
    Remaining capacity: 21

**Your program should never attempt to read the CSV files or the database schema directory. All access to the data must be through the functions defined in `basicdb.py`.** You are welcome to use as many or as few queries as you like and to embed them in any additional Python code you wish.  Do _not_ assume that the database contents are the same as in the sample files provided.  We will not change the schema, but we will test your program with a version of the database loaded with different or additional rooms, courses, and students.