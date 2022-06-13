# A LOGIN SYSTEM

#### Video Demo: https://youtu.be/PalT3JEktsA

#### Description:
This is a program which is replicates a login manager which is used to log in our computers. You can create an account or log in into the default ones.
All the accounts will be stored in the file 'user_pass.py'.
After login you will receive a nice welcome msg and it will play a cute video.
It has a 'user_pass.py' file which stores the login info (usernames and passwords) in a dictionary.
The 'project.py' then imports the dictionary and use it for login and for creating an account.
A new account is created by opening and editing 'user_pass.py' and adding the new login credentials.
Then it can log in into your account by matching the username and the password you input.
After login it will welcome you and play a cute video with the help of pywhatkit.
It also imports bcrypt which is used for hashing the passwords so that no one could see them.
If someone opens the 'user_pass.py' file the would only be able to see the usernames as the passwords would be hashed and there is no way to unhash a password or us a hashed password to reveal the real password.
This helps the user to secure their passwords. And when checking their passwords, it again uses the bcrypt library to match the hashed and the unhashed, newly inputted password.
It uses 4 to be installed python libraries:
(1)pywhatkit, (2)tkinter and (3)flask for the video
(4)bcrypt for password hashing

Functions:
1)login: It logs us in our account by prompting us for username and password. It checks the if the user already exists and also matches the hashed password with the unhashed password then returns a bool which remains True if the password matches

2)start: If the bool returned in login() remains true, it welcomes the user and starts the video

3)set_user: This function creates a new account with the username and password we input. It exits if the username already exits. It also hashes the password to secure it and then stores it in the 'user_pass.py' file

4)login_or_create: It asks the user if he/she wants to create a new account or login into an account

The main function calls login_or_create function which then calls other functions.

NOTE: THIS PROJECT WONT WORK IN THE CODESPACES AS IT REQUIRES TKINTER FOR IT TO WORK AND CODESPACES IS A CLOUD VM WHICH HAS NO GRAPHICAL INTERFACE AND TKINTER IS A GUI TOOL.

#### TODO:
1. Clone the repo: git clone https://github.com/ART3MISTICAL/cs50p-finalproject
2. cd /project
3. pip3 install -r requirements.txt
4. python project.py
5. Enjoy :)