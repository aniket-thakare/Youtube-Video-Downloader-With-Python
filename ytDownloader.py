import ffmpeg    #to merge audio/video streaams
import pytube    #to download video from YouTube
import time      #to measure download time
import os
import sys


print(50*"*")
print("-|-|-|-|-|-|-YOUTUBE VIDEO DOWNLOADER-|-|-|-|-|-|-")
print(50*"*")
print()


def clean_filename(name):
        forbidden_chars = '|'
        filename = (''.join([x if x not in forbidden_chars else '#' for x in name])).replace('  ', ' ').strip()
        if len(filename) >= 176:
            filename = filename[:170] + '...'
        return filename 
    
def download_video(link, res_level='FHD'):
    ti = time.time()
    yt = pytube.YouTube(link, use_oauth=True, allow_oauth_cache=True)
    print(yt.title, '|', yt.author, '|', yt.publish_date.strftime("%Y-%m-%d"), '|', yt.views, '|', yt.length, 'sec')
    
    choice = 0
    while choice !=4:
        print(" (1) >> Download in 4k \n")
        print(" (2) >> Download in 2k \n")
        print(" (3) >> Download in 1080p \n")
        print(" (4) >> Download in 720p \n")
        print(" (5) >> Download in 480p \n")
        print(" (6) >> Quit\n")

        choice = int(input(" Enter Which Quality You Want To Download  -->>  "))

        if choice == 1:
            res_level == '4K'
            print('Downloading in 4k')
            dynamic_streams = ['2160p|160kbps', '1440p|160kbps', '1080p|160kbps', '720p|160kbps', '720p|128kbps', '480p|160kbps', '480p|128kbps']
            
        if choice == 2:
            res_level == '2K'
            print('Downloading in 2k')
            dynamic_streams = ['1440p|160kbps', '1080p|160kbps', '720p|160kbps', '720p|128kbps', '480p|160kbps', '480p|128kbps']

        if choice == 3:
            res_level == 'FHD'
            print('Downloading in 1080p')
            dynamic_streams = ['1080p|160kbps', '720p|160kbps', '720p|128kbps', '480p|160kbps', '480p|128kbps']

        if choice == 4:
            res_level == 'HD'
            print('Downloading in 720p')
            dynamic_streams = ['720p|160kbps', '720p|128kbps', '480p|160kbps', '480p|128kbps']

        if choice == 5:
            res_level == '480p'
            print('Downloading in 480p')
            dynamic_streams = ['480p|160kbps', '480p|128kbps']
        
        if choice == 6:
            print("\n----Program Terminated----\n")
            sys.exit()   
    
        for ds in dynamic_streams:
            try:
                yt.streams.filter(res=ds.split('|')[0], progressive=False).first().download(filename='video.mp4')
                yt.streams.filter(abr=ds.split('|')[1], progressive=False).first().download(filename='audio.mp3')
                break
            except:
                continue
        
        audio = ffmpeg.input('audio.mp3')
        video = ffmpeg.input('video.mp4')
        filename = 'C:\\Users\\91788\\Desktop\\Youtube\\' + clean_filename(yt.title) + '.mp4'
        ffmpeg.output(audio, video,filename).run(overwrite_output=True)
        

    # Removing audio and video file after merging them into one video

        os.remove('C:\\Users\\91788\\Desktop\\Youtube\\video.mp4')
        os.remove('C:\\Users\\91788\\Desktop\\Youtube\\audio.mp3')

        print(ds, 'video successfully downloaded from', link)
        print('Time taken: {:.0f} sec'.format(time.time() - ti))
        print(" \n\n----VIDEO DOWNLOADED----")
        print("\n----PROGRAM TERMINATED----\n")

        sys.exit()

link = input(" ENTER LINK OF VIDEO -->> ")
download_video(link, '4K')