-- TrackAvailableMarkets Schema --
CREATE TABLE TrackAvailableMarkets(
    track_id VARHCAR(32)
    ,country_code VARCHAR(32)
    ,FOREIGN KEY (track_id) REFERENCES Tracks(track_id)
    ,FOREIGN KEY (country_code) REFERENCES MarketCodes(country_code)
);