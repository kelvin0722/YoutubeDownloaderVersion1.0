input_value = raw_input('Enter the youtube url:')
myvid = pafy.new(str(input_value))
path = "/home/kelvin/youtubedownloads"
video_count = myvid.viewcount
title = myvid.title

print ("Title:%s"%(title))
print ("Total number of views:{:,}".format(myvid.viewcount))

try:
    best_vid = myvid.getbest()
    best_audio = myvid.getbestaudio(preftype="m4a",ftypestrict=True)
   
    best_vid.download(filepath=path,quiet=False)   
    best_audio.download(filepath=path,quiet=False) 
except:
    print("Check  the file  format")