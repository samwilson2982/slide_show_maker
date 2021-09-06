import moviepy
import glob
import os
import moviepy.editor


class MovieManager(object):

    def join_paths(self,relative):
        return os.path.join(os.path.dirname(__file__),relative)

    def concat_images(self, clip_height,clip_duration):
        images = glob.glob(self.join_paths("../../../images/*.*"))
        clips = [moviepy.editor.ImageClip(m).set_duration(180) for m in images]
        clips = [clip.resize(height=clip_height) for clip in clips]
        return moviepy.editor.concatenate_videoclips(clips, method="compose")

    def concat_audio(self, duration):
        audio = glob.glob(self.join_paths("../../../audio/*.mp3"))
        audios = [moviepy.editor.AudioFileClip(m) for m in audio]
        max_audio = moviepy.editor.concatenate_audioclips([audio for audio in audios])
        looping = moviepy.editor.afx.audio_loop(max_audio, duration=duration)
        return looping

    def __init__(self, clip_height=720, clip_duration=10, use_audio=True,name="movie2.mp4"):
        if not name.endswith(".mp4"):
            name = name+".mp4"
        concat_clip = self.concat_images(clip_height, clip_duration)
        if use_audio == True:
            concat_clip.audio = (self.concat_audio(concat_clip.duration))



        concat_clip.write_videofile(name, threads = 8, fps=1)



