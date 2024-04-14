DROP TABLE IF EXISTS  AlbumArtists, Albums, Artists, genreartists, keysignatures, 
marketcodes, playlists, trackartists, tracks, trackavailablemarkets CASCADE;

-- Albums Schema -- 
	CREATE TABLE Albums(
	album_id VARCHAR
	,album_name VARCHAR
	,total_tracks INTEGER
	,date_released VARCHAR
	,PRIMARY KEY (album_id)
);


-- Artists Schema -- 
CREATE TABLE Artists(
    artist_id VARCHAR
    ,artist_name VARCHAR
    ,nbr_of_followers INTEGER
    ,popularity INTEGER
    ,PRIMARY KEY (artist_id)
);

-- KeySignatures Schema --
CREATE TABLE KeySignatures(
    key_id INTEGER
    ,key_signature varchar(32)
    ,PRIMARY KEY (key_id)
);

-- MarketCodes Schema --
CREATE TABLE MarketCodes(
    country_code CHAR(2)
    ,country VARCHAR
    ,PRIMARY KEY (country_code)
);


-- Tracks Schema --
CREATE TABLE Tracks(
	track_id VARCHAR(32)
	,track_name VARCHAR
	,album_id VARCHAR(32)
	,duration_ms INTEGER
	,explicit BOOLEAN
	,current_popularity INTEGER
	,acousticness FLOAT
	,danceability FLOAT
	,instrumentalness FLOAT
	,key_signature INTEGER
	,mode CHAR(5)
	,tempo FLOAT
	,time_signature FLOAT
	,valence FLOAT
	,PRIMARY KEY  (track_id)
	,FOREIGN KEY  (album_id) REFERENCES Albums(album_id)
	,FOREIGN KEY (key_signature) REFERENCES KeySignatures(key_id)
);


-- AlbumArtists Schema --
CREATE TABLE AlbumArtists(
    album_id VARCHAR(32)
    ,artist_id VARCHAR(32)
    ,FOREIGN KEY (album_id) REFERENCES Albums(album_id)
    ,FOREIGN KEY (artist_id) REFERENCES Artists(artist_id)
);


-- GenreArtists Schema --
CREATE TABLE GenreArtists(
    artist_id VARCHAR(32)
    ,genre VARCHAR(32)
    ,FOREIGN KEY (artist_id) REFERENCES Artists(artist_id)
);


-- Playlists Schema --
CREATE TABLE Playlists(
	name VARCHAR(32)
	,track_id VARCHAR(32)
	,track_name VARCHAR
	,album_id VARCHAR(32)
	,album_name VARCHAR
	,FOREIGN KEY (track_id) REFERENCES Tracks(track_id)
	,FOREIGN KEY (album_id) REFERENCES Albums(album_id)
);


-- TrackArtists Schema --
CREATE TABLE TrackArtists(
    track_id VARCHAR(32)
    ,artist_id VARCHAR(32)
    ,FOREIGN KEY (track_id) REFERENCES Tracks(track_id)
    ,FOREIGN KEY (artist_id) REFERENCES Artists(artist_id)
);


-- TrackAvailableMarkets Schema --
CREATE TABLE TrackAvailableMarkets(
    track_id VARCHAR(32)
    ,country_code VARCHAR(32)
    ,FOREIGN KEY (track_id) REFERENCES Tracks(track_id)
    ,FOREIGN KEY (country_code) REFERENCES MarketCodes(country_code)
);


-- INSERT KeySignatures Data --
INSERT INTO KeySignatures (key_id, key_signature) VALUES
(-1, 'No Key')
,(0, 'C')
,(1, 'C Sharp or D Flat')
,(2, 'D')
,(3, 'D Sharp or E Flat')
,(4, 'E')
,(5, 'F')
,(6, 'F Sharp or G Flat')
,(7, 'G')
,(8, 'G Sharp or A Flat')
,(9, 'A')
,(10, 'A Sharp or B Flat')
,(11, 'B');

-- INSERT MarketCodes Data --
INSERT INTO MarketCodes (country_code, country) VALUES
('AD', 'Andorra')
,('AE', 'United Arab Emirates')
,('AF', 'Afghanistan')
,('AG', 'Antigua and Barbuda')
,('AI', 'Anguilla')
,('AL', 'Albania')
,('AM', 'Armenia')
,('AO', 'Angola')
,('AQ', 'Antarctica')
,('AR', 'Argentina')
,('AS', 'American Samoa')
,('AT', 'Austria')
,('AU', 'Australia')
,('AW', 'Aruba')
,('AX', 'Åland Islands')
,('AZ', 'Azerbaijan')
,('BA', 'Bosnia and Herzegovina')
,('BB', 'Barbados')
,('BD', 'Bangladesh')
,('BE', 'Belgium')
,('BF', 'Burkina Faso')
,('BG', 'Bulgaria')
,('BH', 'Bahrain')
,('BI', 'Burundi')
,('BJ', 'Benin')
,('BL', 'Saint Barthélemy')
,('BM', 'Bermuda')
,('BN', 'Brunei Darussalam')
,('BO', 'Bolivia, Plurinational State of')
,('BQ', 'Bonaire, Sint Eustatius and Saba')
,('BR', 'Brazil')
,('BS', 'Bahamas')
,('BT', 'Bhutan')
,('BV', 'Bouvet Island')
,('BW', 'Botswana')
,('BY', 'Belarus')
,('BZ', 'Belize')
,('CA', 'Canada')
,('CC', 'Cocos (Keeling) Islands')
,('CD', 'Congo, Democratic Republic of the Congo')
,('CF', 'Central African Republic')
,('CG', 'Congo')
,('CH', 'Switzerland')
,('CI', 'Côte d''Ivoire')
,('CK', 'Cook Islands')
,('CL', 'Chile')
,('CM', 'Cameroon')
,('CN', 'China')
,('CO', 'Colombia')
,('CR', 'Costa Rica')
,('CU', 'Cuba')
,('CV', 'Cabo Verde')
,('CW', 'Curaçao')
,('CX', 'Christmas Island')
,('CY', 'Cyprus')
,('CZ', 'Czechia')
,('DE', 'Germany')
,('DJ', 'Djibouti')
,('DK', 'Denmark')
,('DM', 'Dominica')
,('DO', 'Dominican Republic')
,('DZ', 'Algeria')
,('EC', 'Ecuador')
,('EE', 'Estonia')
,('EG', 'Egypt')
,('EH', 'Western Sahara')
,('ER', 'Eritrea')
,('ES', 'Spain')
,('ET', 'Ethiopia')
,('FI', 'Finland')
,('FJ', 'Fiji')
,('FK', 'Falkland Islands (Malvinas)')
,('FM', 'Micronesia, Federated States of Micronesia')
,('FO', 'Faroe Islands')
,('FR', 'France')
,('GA', 'Gabon')
,('GB', 'United Kingdom of Great Britain and Northern Ireland')
,('GD', 'Grenada')
,('GE', 'Georgia')
,('GF', 'French Guiana')
,('GG', 'Guernsey')
,('GH', 'Ghana')
,('GI', 'Gibraltar')
,('GL', 'Greenland')
,('GM', 'Gambia')
,('GN', 'Guinea')
,('GP', 'Guadeloupe')
,('GQ', 'Equatorial Guinea')
,('GR', 'Greece')
,('GS', 'South Georgia and the South Sandwich Islands')
,('GT', 'Guatemala')
,('GU', 'Guam')
,('GW', 'Guinea-Bissau')
,('GY', 'Guyana')
,('HK', 'Hong Kong')
,('HM', 'Heard Island and McDonald Islands')
,('HN', 'Honduras')
,('HR', 'Croatia')
,('HT', 'Haiti')
,('HU', 'Hungary')
,('ID', 'Indonesia')
,('IE', 'Ireland')
,('IL', 'Israel')
,('IM', 'Isle of Man')
,('IN', 'India')
,('IO', 'British Indian Ocean Territory')
,('IQ', 'Iraq')
,('IR', 'Iran, Islamic Republic of')
,('IS', 'Iceland')
,('IT', 'Italy')
,('JE', 'Jersey')
,('JM', 'Jamaica')
,('JO', 'Jordan')
,('JP', 'Japan')
,('KE', 'Kenya')
,('KG', 'Kyrgyzstan')
,('KH', 'Cambodia')
,('KI', 'Kiribati')
,('KM', 'Comoros')
,('KN', 'Saint Kitts and Nevis')
,('KP', 'Korea, Democratic People''s Republic of Korea')
,('KR', 'Korea, Republic of Korea')
,('KW', 'Kuwait')
,('KY', 'Cayman Islands')
,('KZ', 'Kazakhstan')
,('LA', 'Lao People''s Democratic Republic')
,('LB', 'Lebanon')
,('LC', 'Saint Lucia')
,('LI', 'Liechtenstein')
,('LK', 'Sri Lanka')
,('LR', 'Liberia')
,('LS', 'Lesotho')
,('LT', 'Lithuania')
,('LU', 'Luxembourg')
,('LV', 'Latvia')
,('LY', 'Libya')
,('MA', 'Morocco')
,('MC', 'Monaco')
,('MD', 'Moldova, Republic of Moldova')
,('ME', 'Montenegro')
,('MF', 'Saint Martin (French part)')
,('MG', 'Madagascar')
,('MH', 'Marshall Islands')
,('MK', 'North Macedonia')
,('ML', 'Mali')
,('MM', 'Myanmar')
,('MN', 'Mongolia')
,('MO', 'Macao')
,('MP', 'Northern Mariana Islands')
,('MQ', 'Martinique')
,('MR', 'Mauritania')
,('MS', 'Montserrat')
,('MT', 'Malta')
,('MU', 'Mauritius')
,('MV', 'Maldives')
,('MW', 'Malawi')
,('MX', 'Mexico')
,('MY', 'Malaysia')
,('MZ', 'Mozambique')
,('NA', 'Namibia')
,('NC', 'New Caledonia')
,('NE', 'Niger')
,('NF', 'Norfolk Island')
,('NG', 'Nigeria')
,('NI', 'Nicaragua')
,('NL', 'Netherlands, Kingdom of the Netherlands')
,('NO', 'Norway')
,('NP', 'Nepal')
,('NR', 'Nauru')
,('NU', 'Niue')
,('NZ', 'New Zealand')
,('OM', 'Oman')
,('PA', 'Panama')
,('PE', 'Peru')
,('PF', 'French Polynesia')
,('PG', 'Papua New Guinea')
,('PH', 'Philippines')
,('PK', 'Pakistan')
,('PL', 'Poland')
,('PM', 'Saint Pierre and Miquelon')
,('PN', 'Pitcairn')
,('PR', 'Puerto Rico')
,('PS', 'Palestine, State of')
,('PT', 'Portugal')
,('PW', 'Palau')
,('PY', 'Paraguay')
,('QA', 'Qatar')
,('RE', 'Réunion')
,('RO', 'Romania')
,('RS', 'Serbia')
,('RU', 'Russian Federation')
,('RW', 'Rwanda')
,('SA', 'Saudi Arabia')
,('SB', 'Solomon Islands')
,('SC', 'Seychelles')
,('SD', 'Sudan')
,('SE', 'Sweden')
,('SG', 'Singapore')
,('SH', 'Saint Helena, Ascension and Tristan da Cunha')
,('SI', 'Slovenia')
,('SJ', 'Svalbard and Jan Mayen')
,('SK', 'Slovakia')
,('SL', 'Sierra Leone')
,('SM', 'San Marino')
,('SN', 'Senegal')
,('SO', 'Somalia')
,('SR', 'Suriname')
,('SS', 'South Sudan')
,('ST', 'Sao Tome and Principe')
,('SV', 'El Salvador')
,('SX', 'Sint Maarten (Dutch part)')
,('SY', 'Syrian Arab Republic')
,('SZ', 'Eswatini')
,('TC', 'Turks and Caicos Islands')
,('TD', 'Chad')
,('TF', 'French Southern Territories')
,('TG', 'Togo')
,('TH', 'Thailand')
,('TJ', 'Tajikistan')
,('TK', 'Tokelau')
,('TL', 'Timor-Leste')
,('TM', 'Turkmenistan')
,('TN', 'Tunisia')
,('TO', 'Tonga')
,('TR', 'Türkiye')
,('TT', 'Trinidad and Tobago')
,('TV', 'Tuvalu')
,('TW', 'Taiwan, Province of China')
,('TZ', 'Tanzania, United Republic of Tanzania')
,('UA', 'Ukraine')
,('UG', 'Uganda')
,('UM', 'United States Minor Outlying Islands')
,('US', 'United States of America')
,('UY', 'Uruguay')
,('UZ', 'Uzbekistan')
,('VA', 'Holy See')
,('VC', 'Saint Vincent and the Grenadines')
,('VE', 'Venezuela, Bolivarian Republic of Venezeula')
,('VG', 'Virgin Islands (British)')
,('VI', 'Virgin Islands (U.S.)')
,('VN', 'Viet Nam')
,('VU', 'Vanuatu')
,('WF', 'Wallis and Futuna')
,('WS', 'Samoa')
,('YE', 'Yemen')
,('YT', 'Mayotte')
,('ZA', 'South Africa')
,('ZM', 'Zambia')
,('ZW', 'Zimbabwe')
,('XK', 'Kosovo')