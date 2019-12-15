# FinalProject
Student record keeping system

1. Project type: A
2. Robert Clasemann (clase06) and Charlie Splittstoser (split022)
3. https://nameless-sands-47707.herokuapp.com/
4. https://github.com/charlieSplittstoser/FinalProject/tree/master/app
5. Bootstrap, JQuery, SQLite, Google Library API. 
6. 
    Our project is a student record keeping system. 

    Upon loading the home page, you'll be shown three links with a short description.

    The first option is to look at their course schedule. If you click on this link and aren't signed into your account,
    you'll see an error message. Otherwise if no account information is found within the database, you must register for a new
    account. Once registration is completed, a message will indicate that you've successfully created an account. 

    After you log in, you can access your course schedule. The default selection Spring 2020 won't have any classes to show.       But the Fall and Spring 2019 semesters will display four classes with their respective grades earned. 

    The second option is the course catalog link. When you click this link, you'll will be shown a list of classes you can   
    potentially enroll for. Each selection displays the course's ID, title, instructor, and number of credits. To enroll in a 
    class, click on the blue (+) icon, and it'll bring up the enrollment page. This page confirms your enrollment for the 
    chosen course. If you cancel your enrollment, you'll be brought back to the course catalog page. If you enroll, a 
    confirmation message will display stating you've successfully enrolled in the course. Now in your course schedule for 
    Spring 2020 term, you'll see the class has been added to your schedule.

    Last is the Library link. Upon loading up this page, a list of books pertaining to "Internet Programming" will display on 
    your screen. Each book contains data such as the title, author, and availability. You can search for any book that you may 
    be intereted in. Overall, this page is to simply showcase books that may or may not be available at the school library.


7.
    Log-in verification: Checks if credentials match that within the database. If so, access is given.
  
    Register an account: Information entered is inserted into the database.
  
    Course schedule drop-down window: Displays data from database matching the term selected.
  
    Enroll in course: Inserts enrolled course into the currently selected term course schedule.
  
   Library: Calls Google Library API, extracts data from json, and returns specific information about each book.
  
8.
    Log-in Page: Displays fields to enter user email and password. 
    
    Registration Page: Displays account information fields such as name and email.
    
    Catalog Page: Displays a list of classes that the user could enroll for.
    
    Enroll Page: Displays a box confirming enrollment for the class.
  
    Library Page: Displays a list of books that are potentially available at the library.
    
    Index Page: Displays links to other views with their description.
    
    Schedule Page: Displays a list of classes with information pertaining to each class including the name of the professor and number of credits. 
  
9. 
    User (Student) Table: It's primary key is ID and it contains the student's first name, last name, and password hash. Each student is uniquely identified with their email address. It's used to check if the person is a current user or to add said person as a registered user.
    
    Course Table: It's primary key is ID and it contiains the course's ID, title, instructor, and number of credits. Each course is uniquely identified with its course ID. This table's contents is shown on the course catalog page.
    
    Enrollment Table: It's primary key is ID and it contains a student ID, a course ID, the term of enrollment, and the grade receieved. This is a bridge table that is used to correlate data between a student and a specific course. 
10.
