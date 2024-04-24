# Spotify Top 50 Country Playlists Database Design
## Motivation
[Spotify](https://open.spotify.com/) generates a variety of playlists that their users can listen to.  This database stores information on the top 50 songs of 67 countries. Spotify creates their own playlists for the top 50 most popular songs,  and this database stores information on 67 different countries and their most popular songs.   This would allow researchers to understand what kind of musical characteristics countries like listening to.

Music is deeply rooted in cultures across the globe. Another goal for this database is to help us better understand cultures based on the music popular in their respective countries.


## How Are We Obtaining the Data?
The [Spotify API](https://developer.spotify.com/documentation/web-api) is a public API we used to pull Spotify's song data from its top 50 countries playlists.  Each playlist's URL is contained in `countries_top_fifty.txt`.  Our script sends a request to the Spotify API and pulls each song's information for our Playlist table.  Any entity, i.e. (Artist, Playlist, Album, Track) is an object in the form of a python dictionary.  The scripts parses the data so that we can obtain tuples to populate our tables.  The one issue that arised is that these objects would create non-atomic values and therefore violate 2NF.  For example, an album could have multiple artists featured in it, therefore we needed to create tuples for each artist in the album.  Our script will create atomic tuples for each object that has an attribute containing multiple values.  Once tuples are created, we use embedded SQL to execute our insert queries.

`scripts.data_pull_functions.py` is a python script that contains a function to pull the data for each relation we have in our database.  To upload our data we use `scripts.insert_data.py`.  Each function in `scripts.insert_data.py` uses the data created in the functions of `scripts.data_pull_functions.py` as an argument to upload the data to our database.


## Running the Code
In order to run the code, it is required that you have the following three things

1. A local postgres SQL server on your computer
2. A spotify account
3. A spotify Client ID and Client Secret

### Instructions
#### Getting Client ID and Client Secret
 1. Log into the [spotify developers page](https://developer.spotify.com/)
 2. On the top right side of the page, click the drop down and enter your project dashboard
 3. Click "Create App"
 4. Enter the required information and create your app
 5. Onces the app is created, click the app settings buttion on the top right
 6. From there you should see your client ID
 7. Click "View Client Secret" to view your client secret

#### Setting Up Configurations
In the `credential_example_files` directory, create a copy of both files (`database.ini`, `project_credentials.yaml`) in the super directory of the project.  Afterward, enter your spotify cilent ID and client secret in `project_credentials.yaml`.   In `database.ini`, please enter your database system's username and password, along with the name of the database you want to store the spotify data

#### Populating the Database
To populate the database, just simply run `main`!