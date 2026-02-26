class audiofile:
    def __init__(self,filename):
        self.filename=filename
    def play(self):
        return f"Playing Audio:{self.filename}(Using MP3 codec)"
class videofile:
    def __init__(self,filename):
        self.filename=filename
    def play(self):
        return f"playing video:{self.filename}(Rendering 1080p)"
a1=audiofile("taatu.mp3")
a2=videofile("pulu.mp4")
a3=audiofile("tuttu.mp3")
a4=videofile("tulu.mp4")
playlist=[a1,a2,a3,a4]
print(a1.play())
print(a2.play())
print(a3.play())
print(a4.play())
for a in playlist:
    print(a.play())


