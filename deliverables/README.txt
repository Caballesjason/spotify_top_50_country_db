---- SPOTIFY TOP 50 COUNTRY PLAYLISTS DATABASE DESIGN ----
---- Deliverables ----
All deliverable as per the project documentation is in the directory `deliverables`

---- MOTIVATION ----
Spotify generates a variety of playlists that their users can listen to. This database stores information on the top 50 songs of 67 countries. Spotify creates their own playlists for the top 50 most popular songs, and this database stores information on 67 different countries and their most popular songs. This would allow researchers to understand what kind of musical characteristics countries like listening to.

Music is deeply rooted in cultures across the globe. Another goal for this database is to help us better understand cultures based on the music popular in their respective countries.


---- HOW ARE WE OBTAINING THE DATA? ----
The Spotify API is a public API we used to pull Spotify's song data from its top 50 countries playlists. Each playlist's URL is contained in countries_top_fifty.txt. Our script sends a request to the Spotify API and pulls each song's information for our Playlist table. Any entity, i.e. (Artist, Playlist, Album, Track) is an object in the form of a python dictionary. The scripts parses the data so that we can obtain tuples to populate our tables. The one issue that arised is that these objects would create non-atomic values and therefore violate 2NF. For example, an album could have multiple artists featured in it, therefore we needed to create tuples for each artist in the album. Our script will create atomic tuples for each object that has an attribute containing multiple values. Once tuples are created, we use embedded SQL to execute our insert queries.

scripts.data_pull_functions.py is a python script that contains a function to pull the data for each relation we have in our database. To upload our data we use scripts.insert_data.py. Each function in scripts.insert_data.py uses the data created in the functions of scripts.data_pull_functions.py as an argument to upload the data to our database.


---- RUNNING THE CODE ----
In order to run the code, it is required that you have the following three things

A local postgres SQL server on your computer
A spotify account
A spotify Client ID and Client Secret


---- INSTRUCTIONS ----
---- GETTING CLIENT ID AND CLIENT SECRET ----
Log into the spotify developers page
On the top right side of the page, click the drop down and enter your project dashboard
Click "Create App"
Enter the required information and create your app
Onces the app is created, click the app settings buttion on the top right
From there you should see your client ID
Click "View Client Secret" to view your client secret


---- SETTING UP CONFIGURATIONS ----
In the credential_example_files directory, create a copy of both files (database.ini, project_credentials.yaml) in the super directory of the project. Afterward, enter your spotify cilent ID and client secret in project_credentials.yaml. In database.ini, please enter your database system's username and password, along with the name of the database you want to store the spotify data


---- POPULATING THE DATABASE ----
To populate the database, just simply run main!


---- Directory Descriptions ----
`credential_example_files` - This directory contains the sample config files to access the spotify API and your local postgreSQL via python!

`database_design` - This directory contains the EL diagram and  `create.sql`, `drop.sql`, and `insert.sql`.  It also contains `all.sql`, which is used to to create, drop, and insert data when our scripts run.

`deliverables` - This directory contains all files required for our report

`pdfs` - This directory contains our data dictionary, report documentaiton, and a copy of our project report.

`scripts` - This directory contains all scripts used to pull out data from the Spotify API.

`sql_queries` - This directory the 9 sql queries requested for the project
