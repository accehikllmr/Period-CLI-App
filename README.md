Command line interface application to track and predict menstrual cycles based on historical user data.

*** User data is NOT securely stored, as it is in an unencrypted text file. ***

This application was implemented before I learned about object oriented programming, so it does not implement any of its concepts. However, the project functions are separated into modules.

Menu option #1 is full proof as far as I can tell, in terms of rejecting bad input from the user wihtout crashing the application. Namely, it only allows the user to type valid characters for the required date format. The same goes for the home interface.

Menu option #2 has been fully implemented, except that it crashes the application when the database (text file) has less than two dates. Hence, the default text file in this project has two recent dates.

Menu option #3 has not been implemented. In fact, trying to implement this option led to the work done on the Anrdoid mobile application version (see the Period_App_01 repository).

Menu option #4 works exits the app.
