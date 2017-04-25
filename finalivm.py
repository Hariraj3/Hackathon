
import gtts
from gtts import gTTS
from moviepy.editor import *
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
	#return "<h1 style='color:blue'>Hello Hari</h1>"
	tts=gTTS(text='Demo for IVM', lang='en')
	tts.save("IVMAudio.mp3")
	tts=gTTS(text='Hello Rama, your bill amount is $19.99', lang='en')
	tts.save("IVMAudio2.mp3")

	#clip = VideoFileClip("http://10.74.22.223:5000/Wireless.mp4")
	fullvideoclip = VideoFileClip("Samsung.mp4")
	videoclip1 = fullvideoclip.subclip(0,5)
	videoclip2 = fullvideoclip.subclip(6,12)
	videoclip3 = fullvideoclip.subclip(13,fullvideoclip.duration)
	audioclip1 = AudioFileClip("IVMAudio.mp3")
	audioclip2 = AudioFileClip("IVMAudio2.mp3")

	txt_clip1 = (TextClip("Demo for IVM", font='Georgia-Regular',fontsize=70,color='red').set_duration(2))
	txt_clip2 = (TextClip("Hello Rama,\n your bill amount is $19.99", font='Arial Black',fontsize=40,color='black').set_position('center').set_duration(6))

	videoclip1 = videoclip1.set_audio(AudioFileClip("IVMAudio.mp3"))
	updateclip1 = CompositeVideoClip([videoclip1, txt_clip1.set_pos((100,200))])

	videoclip3 = videoclip3.set_audio(AudioFileClip("IVMAudio2.mp3"))
	updateclip2 = CompositeVideoClip([videoclip3, txt_clip2])

	finalclip = concatenate_videoclips([updateclip1, videoclip2, updateclip2])
	finalclip.to_videofile("IVMVideo.mp4")
	#clip = VideoFileClip("Wireless.mp4")
	#txt_clip = (TextClip("Demo for IVM", font='Georgia-Regular',fontsize=70,color='red').set_position('center').set_duration(5).set_start(5))
	#final_clip = CompositeVideoClip([clip, txt_clip])
	#final_clip.to_videofile("IVMVideo.mp4",fps=35)
	#final_clip.write_videofile("IVMVideo.mp4",fps=30,codec='libx264', audio="IVMAudio.mp3")
	return "<h1>testing" + str(fullvideoclip.duration) + "</h1>"

if __name__ == "__main__":
	application.run(host='0.0.0.0')
