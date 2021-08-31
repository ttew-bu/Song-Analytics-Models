import os
import pandas as pd
import numpy as np
import lyricsgenius
import time
import re

doc_path = "C:/Users/trist/Balanced_genres_data.csv"

#Create empty df to store all songs in
df = pd.read_csv(doc_path, encoding="utf-8")

#Create variable 
total_rows = len(df)

#Create chunks to go through the data process
chunksize = 15

#Define Genius object by getting API permission via token
genius = lyricsgenius.Genius(access_token='FBtxHhzd75FAj2Xu34ObFLXEvuWODdWugXHkA2e2c2SIBXuqBvesDuWb0bKOR6tD')

#For each array in the dataframe, take the 
for n in range(1590,len(df),chunksize):
    print(n)

    df_chunk = pd.read_csv(doc_path, encoding="utf-8",nrows=chunksize,skiprows=n)

    #Turn df into arrays so we can pull from the subsequent lists with ease
    arrayed_df = df_chunk.to_numpy()

    for row in range(0,chunksize):
        try:
            #Create blank cell for lyrics
            lyrics = ""

            #Set a round start time to track API performance
            round_start = time.perf_counter()

            #Define the singer within the array
            song = str((arrayed_df[row][1]))

            #Define the song name within the array
            singer = str(arrayed_df[row][0])

            print(song)

            #Use Genius API/Python package to query the database; this step takes 0.7-2.5 seconds and anything consistently outside this range is troubling
            genius_results = genius.search_song(song,singer)
            time.sleep(8)

        except UnicodeEncodeError:
            genius_results = np.nan
            time.sleep(8)
         

        #If blank query, create a null and a continue running down the list
        try:
            
        
            if genius_results == None or genius_results == np.nan:
                lyrics = np.nan

            else:
                result_artist = str(genius_results.primary_artist.name)

                if result_artist in singer:
                    lyrics = genius_results.lyrics
                else:
                    lyrics=np.nan

        except AttributeError:
            lyrics=np.nan


        df_chunk.loc[df_chunk.index[row], 'lyrics'] = lyrics
   
    df_chunk.to_csv("lyrics.csv",mode='a',header=False,encoding="utf-8")
    time.sleep(5)