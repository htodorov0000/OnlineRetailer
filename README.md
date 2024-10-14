﻿# Starting the program
To start the program run the “online\_retailer.py” script. This is the only script which needs to be run to interface with the program.

The command line interface requires the user to input a number to navigate to the desired option. 

For example, on startup, you will be prompted to pick a security mode. Inputting 1 will turn security on, and inputting 2 will turn it off:

![](./Screenshots/Screenshot1.png)

The security setting cannot be changed after startup, the program will need to be turned off and back on to switch to a different security mode.
# Signing up and logging in
After picking the security setting, you will be placed onto the landing page, which is the main page of the software. To make a new account, select the Sign Up option. You will be prompted to input a username and a password. With security mode off, the username must be between 6 and 20 characters long, but there are no other restrictions, and the password can be any length, even empty. With security mode on, the username may not include any of the following characters: =+-@,;'" or spaces/tabs, while the password requires 12+ characters, a lowercase letter, an uppercase letter, a digit, and one of the following special symbols: #?!@$%^&\*-

Once signed up successfully, the account credentials will be written to the secure or insecure CSV database, depending on the chosen security setting. These files are located within the database folder:

![](./Screenshots/Screenshot2.png)

Following up, you must still log in even just after creating the account, by inputting the correct credentials. 
# User Features
Once the user has logged in, they will see this landing page:

![](./Screenshots/Screenshot3.png)

Account settings will allow the user to change password (with the same conditions as when first setting it), add payment details, remove payment details:

![](./Screenshots/Screenshot4.png)

Products will allow the user to browse products on the online retail store and purchase them:

![](./Screenshots/Screenshot5.png)

![](./Screenshots/Screenshot6.png)

In order for the user to purchase a product, they must first have inputted card details. This includes first and last name, card number (16 digits), expiration date (mm/yy), and CVC (3 digits). Once the purchase option is selected, the program will check if card details are available and allow purchase if so.
# Admin Features
The default admin account credentials are as follows:

USERNAME: Admin1

PASSWORD: Pas$w0rd12345

Once logged into an admin account, the User List option will be available in the landing page:

![](./Screenshots/Screenshot7.png)

![](./Screenshots/Screenshot8.png)

The admin will see a list of every user except for themselves (in order to prevent accidental deletion or demotion of own account).

Upon selection of user, there are the following options:

![](./Screenshots/Screenshot9.png)

This allows the admin to delete, promote and demote accounts from being admin. Every account with admin privileges is equal and has access to these options, allowing them to delete, promote or demote any other account.



Finally, tests can be accessed by running the script within the “test” folder. This contains several unittests used to test key functionality of the application.

Please note that no scripts are used to perform any of the hacker attacks, and that evidence of their performance is included in the main report.
