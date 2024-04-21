# Spotify Top 50 Country Playlists Database Design
## Motivation
[Spotify](https://open.spotify.com/) generates a variety of playlists that their users can listen to.  This database stores information on the top 50 songs of 67 countries. Spotify creates their own playlists for the top 50 most popular songs,  and this database stores information of 67 different countries and their most popular songs.   This would allow researchers to understand what kind of musical characteristics countries like listening to.

Music is deeply rooted in cultures across the globe. Another goal for this database is to help us better understand cultures based on the music popular in their respective countries.

## Running the Code Locally
In order to run the code, it is required that you have the following three things

1. A local PostGres SQL server on your computer
2. A spotify account
3. A spotify Client ID and Client Secret

# Instructions
## Getting Client ID and Client Secret
 1. Log into the [spotify developers page](https://developer.spotify.com/)
 2. On the top right side of the page, click the drop down and enter your project dashboard
 3. Click "Create App"
 4. Enter the required information and create your app
 5. Onces the app is created, click the app settings buttion on the top right
 6. From there you should see your client ID
 7. Click "View Client Secret" to view your client secret

## Setting Up Configurations
In the `credential_example_files` directory, create a copy of both files (`database.ini`, `project_credentials.yaml`) in the super directory of the project.  Afterward, enter your spotify cilent ID and client secret in `project_credentials.yaml`.   In `database.ini`, please enter your database system's username and password, along with the name of the database you want to store the spotify data

## Populating the Databases
We have written the code to create a `.db` file, along with updating the data into PostgreSQL.  In `database_design.master_sql_scripts`, you will see two directories.  The files in the directories are exactly the same, however they have different file extentions to compensate for the different versions of SQL.  We do this because we also created a `.db` file that utilizes a different version of SQL.

To create the relation schemas, please run `all.pgsql` and `all.sql`.  This allows you to create all scehmas and populate the __KeySignatures__ and __MarketCodes__ relations as the API is not required to populate these relations.

Once the 