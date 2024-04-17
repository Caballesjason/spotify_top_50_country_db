# Data Sources
Our team __SeaQewL__ have used the following as data sources.

## Spotify API
Our team uses music data from the [Spotify API](https://developer.spotify.com/documentation/web-api). This API allows us to pull music data that is available in Spotify's application. The spotify API also utilizes data for market codes and musical key signatrue encodings. The API's documentation provides wiki pages to show how they source the data for market codes and key signature encodings and we also use the data from those wiki pages as well!

Here are the following wiki pages:

[__Market Codes:__ ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

[__Key Signature Encodings:__ Standard Pitch Class Notation](https://en.wikipedia.org/wiki/Pitch_class)


# Data Dictionary
## Artists
`artist_id` __(PRIMARY KEY)__ - The unique ID for an Artist

`artist_name` - The name of the artist

`nbr_of_followers` - The number of people currently following the artist

`popularity` -  The popularity of the artist. The value will be between 0 and 100, with 100 being the most popular. The artist's popularity is calculated from the popularity of all the artist's tracks.

## Tracks
`track_id` __(PRIMARY KEY)__ - The ID for a track 

`track_name` - The name of the track

`album_id` __(FOREIGN KEY)__ - The ID of the album that the track is a part of 

`duration_ms` - The duration of the track in milliseconds

`explcit` - A boolean indicating if a track contains explicit content

`current_popularity` - The popularity of a track is a value between 0 and 100, with 100 being the most popular. The popularity is calculated by an algorithm and is based, in the most part, on the total number of plays the track has had and how recent those plays are.  Typically, songs that are frequently played today have a higher popularity than songs that were played a lot in the past. Duplicate tracks (e.g. the same track from a single and an album) are rated independently. Artist and album popularity is derived mathematically from track popularity. 

__Note:__ The popularity value may lag actual popularity by a few days: the value is not updated in real time.

`acousticness` - A confidence measure between 0.0 and 1.0 of whether a track is acoustic.  1.0 represents high confidence that the track is acoustic

`danceability` - Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.

`instrumentalness` - Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0

`key_signatures` __(FOREIGN KEY)__ - The key the track is in. Integers map to pitches using standard [Pitch Class notation](https://en.wikipedia.org/wiki/Pitch_class). E.g. 0 = C, 1 = C Sharp/D Flat, 2 = D, and so on. If no key was detected, the value is -1

`mode` - Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0

`tempo` - The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration

`time_signature` - An estimated time signature. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure). The time signature ranges from 3 to 7 indicating time signatures of "3/4", to "7/4"

`valence` - A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry)


## Albums
`album_id` __(PRIMARY KEY)__ - The ID for a album

`album_name` - The name for an album

`total_tracks` - The number of tracks in the album

`date_released` - The date the album is released.  If no month or day for the release date can be provided, the Spotify API gives only the year.


## AlbumArtists
`album_id` __(FOREIGN KEY)__ - The ID for an album

`artist_id` __(FOREIGN KEY)__ -  The ID for an artist


## GenreArtists
`artist_id` __(FOREIGN KEY)__ - The ID for an artist

`genre` - The genre that the artist is categorized as


## KeySignatures
`key_id` __(PRIMARY KEY)__ - The ID for a key signature

`key_signature` - The actual key signature

## MarketCodes
`country_code` __(PRIMARY KEY)__ - A two character country code

`country` - The name of a country

## Playlists
`name` - The name of the playlist we pulled a track from 

`track_id` __(FOREIGN KEY)__ - The ID of the track

`track_name` - The name of the track

`album_id` __(FOREIGN KEY)__ - The album ID of the track

`album_name` - The album name of the track


## TrackArtists
`track_id` __(FOREIGN KEY)__ - The ID of a track

`artist_id` __(FOREIGN KEY)__ - The ID of an artist 

## TrackAvailableMarkets
`track_id` __(FOREIGN KEY)__ - The ID of a track

`country_code` - The country code of where a track is available