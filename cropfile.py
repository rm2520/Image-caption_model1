from moviepy.editor import VideoFileClip
from time import sleep
def main():


    full_video = "party.mp4"
    current_duration = VideoFileClip(full_video).duration
    #divide_into_count = 5
    #single_duration = current_duration / divide_into_count
    current_video = "p1.mp4"
    start=0
    current_duration="3600"
    clip = VideoFileClip(full_video).subclip(start, current_duration)

    clip.to_videofile(current_video, codec="libx264", temp_audiofile='temp-audio.m4a', remove_temp=True,
                      audio_codec='aac')

if __name__ == '__main__':
    main()