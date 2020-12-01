#!/usr/bin/env python

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from re import sub
from os import system
import concurrent.futures

#? removes spaces and other special characters from the passed parameter
def remove_special(phrase):
    phrase = sub(r'\W+', '%20', phrase)
    return phrase

#? generate array of all songs in the given spotify link
def gen_track_list(spotify_link):
    track_list = []
    spotify_data = uReq(spotify_link).read()
    spotify_soup = soup(spotify_data, 'html.parser')
    
    raw_track_data = spotify_soup.findAll('div', {'class':'tracklist-col name'})
    for track in raw_track_data:
        turn_count = 0
        track_details = track.findAll('span', {'dir':'auto'})
        for single_detail in track_details:
            single_detail = str(single_detail)
            turn_count += 1
            if turn_count == 1:
                song_title = single_detail[36:-7]
            elif turn_count == 2:
                artist_name = single_detail[17:-7]
                track_info = song_title + '%20' + artist_name
                track_list.append(remove_special(track_info))

    return track_list

#? returns youtube link for single_track
def gen_download_link(single_track):
    ddg_link = r"https://duckduckgo.com/html?q=" + single_track + r"%20audio%20youtube%"
    ddg_data = uReq(ddg_link).read()
    ddg_soup = soup(ddg_data, 'html.parser')

    youtube_link = str(ddg_soup.findAll('a', {'class':'result__url'}, limit=1))
    start_index = youtube_link.find("www.youtube.com/watch?v=")
    return youtube_link[start_index:-24]

#? downloads the given link with youtube-dl
def download_list(track_list, index):
    if index <= len(track_list):
        youtube_link = gen_download_link(track_list[index])
        if len(youtube_link) > 5:
            download_command = "youtube-dl -f 140 " + youtube_link
            system(download_command)
        index += 3
    
    return index

def main():
    spotify_link = input("Spotify Playlist Link: ")
    track_list = gen_track_list(spotify_link)
    indexes = [0, 1, 2]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        while indexes[0] < len(track_list):
            process_0 = executor.submit(download_list, track_list, indexes[0])
            process_1 = executor.submit(download_list, track_list, indexes[1])
            process_2 = executor.submit(download_list, track_list, indexes[2])
            
            indexes[0] = process_0.result()
            indexes[1] = process_1.result()
            indexes[2] = process_2.result()
            
    print("playlist downloaded!")

main()
