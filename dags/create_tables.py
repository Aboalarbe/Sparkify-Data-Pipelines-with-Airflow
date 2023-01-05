staging_events_table_create= "CREATE TABLE IF NOT EXISTS staging_events \
  ( \
     artist VARCHAR, \
     auth VARCHAR, \
     firstName VARCHAR, \
     gender CHAR(1), \
     itemSession INT, \
     lastName VARCHAR, \
     length NUMERIC, \
     level VARCHAR, \
     location  VARCHAR, \
     method VARCHAR, \
     page VARCHAR, \
     registeration NUMERIC, \
     sessionId INT, \
     song VARCHAR, \
     status INT, \
     ts NUMERIC, \
     userAgent VARCHAR, \
     userId INT \
  );"

staging_songs_table_create = "CREATE TABLE IF NOT EXISTS staging_songs \
  ( \
     num_songs INT, \
     artist_id VARCHAR, \
     artist_latitude NUMERIC, \
     artist_longitude NUMERIC, \
     artist_location VARCHAR, \
     artist_name VARCHAR, \
     song_id VARCHAR, \
     title VARCHAR, \
     duration  NUMERIC, \
     year INT \
  );"

songplay_table_create = "CREATE TABLE IF NOT EXISTS songplays \
  ( \
     songplay_id INT IDENTITY(0,1) PRIMARY KEY, \
     start_time  NUMERIC NOT NULL, \
     user_id     INT, \
     level       VARCHAR NOT NULL, \
     song_id     VARCHAR, \
     artist_id   VARCHAR, \
     session_id  INT NOT NULL, \
     location    VARCHAR, \
     user_agent  VARCHAR NOT NULL \
  );"

user_table_create = "CREATE TABLE IF NOT EXISTS users \
( \
user_id INT, \
first_name VARCHAR, \
last_name VARCHAR, \
gender CHAR(1), \
level VARCHAR \
);"

song_table_create = "CREATE TABLE IF NOT EXISTS songs ( \
song_id VARCHAR PRIMARY KEY, \
title VARCHAR NOT NULL, \
artist_id VARCHAR NOT NULL, \
year INT NOT NULL, \
duration NUMERIC NOT NULL \
);"

artist_table_create = "CREATE TABLE IF NOT EXISTS artists ( \
artist_id VARCHAR PRIMARY KEY, \
name VARCHAR NOT NULL, \
location VARCHAR, \
latitude VARCHAR, \
longitude VARCHAR \
);"

time_table_create = "CREATE TABLE IF NOT EXISTS time ( \
start_time TIMESTAMP PRIMARY KEY, \
hour INT, \
day INT, \
week INT, \
month INT, \
year INT, \
weekday INT \
);"
