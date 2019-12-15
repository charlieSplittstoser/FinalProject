# FinalProject
Student record keeping system

1. Project type: A
2. Robert Clasemann (clase06) and Charlie Splittstoser (split022)
3. https://nameless-sands-47707.herokuapp.com/
4. https://github.com/charlieSplittstoser/FinalProject/tree/master/app
5. Bootstrap, JQuery, SQLite, Google Library API. 
6. Our project is a student record keeping system. Upon loading the page, the user is shown three links with a short description.
The first option is to look at their course schedule. If the user clicks on this link and isn't signed onto their account,
they're prompted to do so. Otherwise if no account information is found within the database, they must register for a new
account. Once registration is completed, a message will indicate that they've successfully created an account. After they log in,
they're brought back to the home screen. Now when they click
7.
    -Log-in verification: Checks if credentials match that within the database. If so, access is given.
  
    -Register an account: Information entered is inserted into the database.
  
    -Course schedule drop-down window: Displays data from database matching the term selected.
  
    -Enroll in course: Inserts enrolled course into the currently selected term course schedule.
  
   -Library: Calls Google Library API, extracts data from json, and returns specific information about each book.
  
8.
    -Log-in Page: Displays fields to enter user email and password. 
    
    -Registration Page: Displays account information fields such as name and email.
    
    -Catalog Page: Displays a list of classes that the user could enroll for.
    
    -Enroll Page: Displays a box confirming enrollment for the class.
  
    -Library Page: Displays a list of books that are potentially available at the library.
    
    -Index Page: Displays links to other views with their description.
    
    -Schedule Page: Displays a list of classes with information pertaining to each class including the name of the professor and number of credits. 
  
9.
10.
