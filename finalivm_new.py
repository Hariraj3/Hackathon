import gtts
from gtts import gTTS
from moviepy.editor import *
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
	#return "<h1 style='color:blue'>Hello Hari</h1>"
	tts=gTTS(text='Hello Rama, Upgrade to iPhone7 Plus and get 10% discount in your first month bill.', lang='en')
	tts.save("IVMAudio.mp3")

	#clip = VideoFileClip("http://10.74.22.223:5000/Wireless.mp4")
	fullvideoclip = VideoFileClip("template.mp4")
	videoclip1 = fullvideoclip.subclip(0,4)
	videoclip2 = fullvideoclip.subclip(5,fullvideoclip.duration)
	audioclip1 = AudioFileClip("IVMAudio.mp3")

	txt_clip = (TextClip("Hello Rama,", font='Arial Black',fontsize=40,color='black').set_pos((5,10)).set_duration(6))
	txt_clip2 = (TextClip("Upgrade to iPhone7 Plus and get 10% discount in your first month bill.", font='Arial Black',fontsize=40,color='black').set_pos((5,60)).set_duration(6))
	#txt_clip = (TextClip("Hello Rama,\n Upgrade to iPhone7 Plus and get 10% discount in your first month bill.", font='Arial Black',fontsize=40,color='black').set_duration(6))
	#txt_clip = (TextClip("Hari\n Raju",fontsize=40).set_position('center').set_duration(6))

	videoclip2 = videoclip2.set_audio(AudioFileClip("IVMAudio.mp3"))
	updateclip2 = CompositeVideoClip([videoclip2, txt_clip, txt_clip2])

	finalclip = concatenate_videoclips([videoclip1, updateclip2])
	finalclip.to_videofile("IVMVideov2.mp4")
	return "<h1>testing" + str(fullvideoclip.duration) + "</h1>"

if __name__ == "__main__":
	application.run(host='0.0.0.0')

