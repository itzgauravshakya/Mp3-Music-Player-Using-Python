def unmutemusic():
    global currentvol
    root.unmuteButton.grid_remove()
    root.muteButton.grid()
    mixer.music.set_volume(currentvol)
    
def mutemusic():
    global currentvol
    root.muteButton.grid_remove()
    root.unmuteButton.grid()
    currentvol = mixer.music.get_volume()
    mixer.music.set_volume(0)
    
def resumemusic():
    root.ResumeButton.grid_remove()
    root.PauseButton.grid()
    mixer.music.unpause()
    AudioStatusLabel.configure(text='Playing.......')
    
def volumeup():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol+0.05)
    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value'] = mixer.music.get_volume()*100
    
def volumedown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol-0.05)
    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value'] = mixer.music.get_volume()*100
    
def stopmusic():
    mixer.music.stop()
    AudioStatusLabel.configure(text='Stopped.......')
    
def pausemusic():
    mixer.music.pause()
    root.PauseButton.grid_remove()
    root.ResumeButton.grid()
    AudioStatusLabel.configure(text='Paused......')
    
def playmusic():
    ad = audiotrack.get()
    mixer.music.load(ad)
    ProgressbarLabel.grid()
    root.muteButton.grid()
    ProgressbarMusicLabel.grid()
    mixer.music.set_volume(0.4)
    ProgressbarVolume['value'] = 40
    ProgressbarVolumeLabel['text'] = '40%'
    mixer.music.play()
    AudioStatusLabel.configure(text='Playing.......')
    
    Song = MP3(ad)
    totalsonglength = int(Song.info.length)
    ProgressbarMusic ['maximum'] = totalsonglength
    ProgressbarMusicEndTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=totalsonglength))))
    def Progressbarmusictick():
        CurrenSongLength = mixer.music.get_pos()//1000
        ProgressbarMusic['value'] = CurrenSongLength
        ProgressbarMusicStartTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=CurrenSongLength))))
        ProgressbarMusic.after(2,Progressbarmusictick)
    Progressbarmusictick()
    
def musicurl():
    dd  = filedialog.askopenfilename()
    audiotrack.set(dd)
    
def createwidthes():
    global imbrowse,implay,impause,imstop,imvolumedown,imvolumeup,imresume,immute,imunmute
    global AudioStatusLabel,ProgressbarVolumeLabel,ProgressbarLabel,ProgressbarVolume,ProgressbarMusicLabel,ProgressbarMusic,ProgressbarMusicEndTimeLabel,ProgressbarMusic,ProgressbarMusicStartTimeLabel
    #########################   IMAGE REGISTER  ########################### 
    
    implay = PhotoImage(file='play_img.png')
    imstop = PhotoImage(file='stop_img.png')
    imresume = PhotoImage(file='resume.png')
    impause = PhotoImage(file='pause_img.png')
    imvolumeup = PhotoImage(file='vup.png')
    imvolumedown = PhotoImage(file='vdown.png')
    imbrowse = PhotoImage(file='browse.png')
    immute = PhotoImage(file='mute.png')
    imunmute = PhotoImage(file='unmute.png')
    
    ###################   CHANGE SIZE OF ICONS   ######################## 
    
    imbrowse = imbrowse.subsample(2,2)
    implay = implay.subsample(2,2)
    imstop = imstop.subsample(2,2)
    imresume = imresume.subsample(2,2)
    impause = impause.subsample(2,2)
    imvolumeup = imvolumeup.subsample(2,2)
    imvolumedown = imvolumedown.subsample(2,2)
    immute = immute.subsample(2,2)
    imunmute = imunmute.subsample(2,2)
     
    #####################   LABELS   ############################### 
    TrackLabel = Label(root,text='select audio track : ',background='lightskyblue',font=('arial',15,'italic bold'))
    TrackLabel.grid(row=0,column=0,padx=20,pady=20)
    
    AudioStatusLabel = Label(root,text='',background='lightskyblue',font=('bell mt',15,'italic bold'),width=20)
    AudioStatusLabel.grid(row=2,column=1)
    
    #########################  ENTRY BOX   ########################## 
    
    TrackLabelEntry = Entry(root,font=('arial',16,'italic bold'),width=35,textvariable=audiotrack)
    TrackLabelEntry.grid(row=0,column=1,padx=20,pady=20)
    
    ##########################  BUTTONS     #########################
    
    BrowseButton = Button(root,text='Search',background='yellow',font=('arial',12,'italic bold'),width=200,bd=10,
                          activebackground='red',image=imbrowse,compound=RIGHT,command=musicurl)
    BrowseButton.grid(row=0,column=2,padx=20,pady=20)
    
    PlayButton = Button(root,text='Play',background='grey',font=('arial',12,'italic bold'),width=200,bd=10,
                        activebackground='red',image=implay,compound=RIGHT,command=playmusic)
    PlayButton.grid(row=1,column=1,padx=20,pady=20)
    
    root.PauseButton = Button(root,text='Pause',background='lightgreen',font=('arial',12,'italic bold'),width=200,bd=10,
                         activebackground='red',image=impause,compound=RIGHT,command=pausemusic)
    root.PauseButton.grid(row=1,column=0,padx=20,pady=20)
    
    root.ResumeButton = Button(root,text='Resume',background='lightgreen',font=('arial',12,'italic bold'),width=200,bd=10,
                         activebackground='red',image=imresume,compound=RIGHT,command=resumemusic)
    root.ResumeButton.grid(row=1,column=0,padx=20,pady=20)
    root.ResumeButton.grid_remove()
    
    root.muteButton = Button(root,text='Mute',width=75,bg='yellow',activebackground='red',bd=5,
                             image=immute,compound=RIGHT,command=mutemusic)
    root.muteButton.grid(row=3,column=3)
    root.muteButton.grid_remove()
    
    root.unmuteButton = Button(root,text='Unmute',width=75,bg='yellow',activebackground='red',bd=5,
                             image=imunmute,compound=RIGHT,command=unmutemusic)
    root.unmuteButton.grid(row=3,column=3)
    root.unmuteButton.grid_remove()
    
    VolumeUpButton = Button(root,text='VolumeUp',background='lightpink',font=('arial',12,'italic bold'),width=200,bd=10,
                            activebackground='red',image=imvolumeup,compound=RIGHT,command=volumeup)
    VolumeUpButton.grid(row=2,column=0,padx=20,pady=20)
    
    StopButton = Button(root,text='Stop',background='lightgreen',font=('arial',12,'italic bold'),width=200,bd=10,
                        activebackground='red',image=imstop,compound=RIGHT,command=stopmusic)
    StopButton.grid(row=1,column=2,padx=20,pady=20)
    
    VolumeDownButton = Button(root,text='VolumeDown',background='lightpink',font=('arial',12,'italic bold'),width=200,bd=10,
                              activebackground='red',image=imvolumedown,compound=RIGHT,command=volumedown)
    VolumeDownButton.grid(row=2,column=2,padx=20,pady=20)
    
    ###############  PROGRESS BAR VOLUME #######################
    ProgressbarLabel = Label(root,text='',bg='red')
    ProgressbarLabel.grid(row=0,column=3,rowspan=3,padx=20,pady=20)
    ProgressbarLabel.grid_remove()
    
    ProgressbarVolume = Progressbar(ProgressbarLabel,orient=VERTICAL,mode='determinate',
                                    value=0,length=190)
    ProgressbarVolume.grid(row=0,column=0,ipadx=5)
    
    ProgressbarVolumeLabel = Label(ProgressbarLabel,text='0%',bg='lightgrey',width=3)
    ProgressbarVolumeLabel.grid(row=0,column=0)
    
    #############  PROGRESS BAR MUSIC ###################
    ProgressbarMusicLabel = Label(root,text='',bg='red')
    ProgressbarMusicLabel.grid(row=3,column=0,columnspan=3,padx=20,pady=20)
    ProgressbarMusicLabel.grid_remove()
    
    ProgressbarMusicStartTimeLabel = Label(ProgressbarMusicLabel,text='',bg='red',width=4)
    ProgressbarMusicStartTimeLabel.grid(row=0,column=0)
    
    ProgressbarMusic = Progressbar(ProgressbarMusicLabel,orient=HORIZONTAL,mode='determinate',value=0)
    ProgressbarMusic.grid(row=0,column=1,ipadx=370,ipady=3)
    
    ProgressbarMusicEndTimeLabel = Label(ProgressbarMusicLabel,text='0:00:0',bg='red')
    ProgressbarMusicEndTimeLabel.grid(row=0,column=2)




###################################################################
from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3
root = Tk()
root.geometry('1100x500+200+50')
root.title('MUSIC PLAYER')
root.iconbitmap('music_audio_7173.ico')
root.configure(bg='lightskyblue')

#####################    GLOBAL VARIABLE  ##########################

audiotrack = StringVar()
currentvol = 0
totalsonglength = 0

####################   CREATE SLIDER    ###############################
  
ss =' Enjoy The   V i b e s '
#count = 0   ###
#text = ''     ##
SliderLabel = Label(root,text=ss,bg='lightskyblue',font=('bell mt',10,'bold'))
SliderLabel.grid(row=4,column=1,padx=20,pady=20)#,columnspan=3) ##
# def IntroLabelTRick():  ####
#     global count,text
#     if(count>=len(ss)):
#         count = -1
#         text= ''
#         SliderLabel.configure(text=text)
#     else:
#         text = text+ss[count]
#         SliderLabel.configure(text=text)
#     count += 1
#     SliderLabel.after(200,IntroLabelTRick)
    
#IntroLabelTRick()    #####
mixer.init()
createwidthes()
root.mainloop()