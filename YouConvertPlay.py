from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re

import time
import wx
import os
import sys
import logging
import traceback
import webbrowser

from threading import Thread
from time import sleep, perf_counter


def Download(line):

    playlist = Playlist(line)
    #folder = 'C:/Users/maxim/Desktop/Programmes/YouConvertPlay/musics'
    file = open('destination.txt', "r")
    SAVE_PATH = file.readline()
    file.close()

    folder = SAVE_PATH
    #prints each video url, which is the same as iterating through 
    playlist.video_urls

    print("Searching ...")
    number = 0
    for url in playlist:
       
        number = number + 1
            #prints address of each YouTube object in the playlist
    print("System found " + str(number) + " musics.\n" )
    print("Dowloading...\n")
    for url in playlist:
    	try:
    		author = YouTube(url).author
    		title = YouTube(url).title
    		splitAuthor = author.split(' - ')[0]

    		print("\nMusic : " + str(splitAuthor) + " - " + str(title))
    		if os.path.exists(SAVE_PATH + "/" + str(splitAuthor)+ ' - ' + str(title)+'.mp3') == False:
	    		YouTube(url).streams.filter(only_audio=True).first().download(SAVE_PATH)

	    		for file in os.listdir(folder):
	    			if re.search('mp4', file):
	    				mp4_path = os.path.join(folder,file)
	    				mp3_path = os.path.join(folder,str(splitAuthor)+ ' - ' + str(title)+'.mp3')
	    				new_file = mp.AudioFileClip(mp4_path)
	    				new_file.write_audiofile(mp3_path)
	    				os.remove(mp4_path)
	    	else:
	    		print("The music already exists !")
    	except:
    		print("A problem occurred for : " + str(YouTube(url).title)) 
    		try:
    			os.remove(mp4_path)
    		except:
    			print("An error occured !")

 


def run():

    numberOfLink = 0
    Downloaded = 1
    # Ouvrir le fichier en lecture seule
    file = open('list.txt', "r")
    # utilisez readline() pour lire la première ligne
    line = file.readline()
    while line:
        line = file.readline()
        numberOfLink = numberOfLink+1
    file.close()
    print ("\n\nNumber of playlist : " + str(numberOfLink)+ " 🎵\n")

    # Ouvrir le fichier en lecture seule
    if(numberOfLink != 0):
        file = open('list.txt', "r")
        # utilisez readline() pour lire la première ligne
        line = file.readline()
        print("Downloading ... \n\n")


        while line:  
            Download(line)

            print ("Download completed : " + str(Downloaded) + "/" + str(numberOfLink) + " ✔️\n")
            Downloaded = Downloaded+1
            line = file.readline()


        file.close()
        
        f = open("list.txt","w")
        f.close()
    else:
        print("An error has occurred ❌\n")
        print("No link for download\n")



class RedirectText(object):
    def __init__(self,aWxTextCtrl):
        self.out = aWxTextCtrl
    
    def flush(self):
        """
        does nothing for this handler
        """

    def write(self,string):
        self.out.WriteText(string)


class MyFrame(wx.Frame): 
    def __init__(self):

        super().__init__(parent=None, title='𝚈𝚘𝚞𝙲𝚘𝚗𝚟𝚎𝚛𝚝Play', size=(500,300))
        
        self.SetMaxSize(wx.Size(500,300))
        self.SetMinSize(wx.Size(500,300))

        panel = wx.Panel(self)        
        my_sizer = wx.BoxSizer(wx.VERTICAL) 

        self.SetBackgroundColour((255, 255, 255))
        ico = wx.Icon('icone.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)

        title = wx.StaticText(panel, label="𝚈𝚘𝚞𝙲𝚘𝚗𝚟𝚎𝚛𝚝PLay", pos=(175, 45))
        title.SetFont(wx.Font(20, wx.FONTFAMILY_SWISS  , wx.NORMAL, wx.NORMAL, 0, ""))
        title.SetForegroundColour(wx.Colour(160, 160, 160))

        link = wx.StaticText(panel, label="🔗 Playlist", pos=(20, 100))
        link.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS  , wx.NORMAL, wx.NORMAL, 0, ""))
        link.SetForegroundColour(wx.Colour(160, 160, 160))


        notes = wx.StaticText(panel, label="♫ ♪ ♫ ♪", pos=(275, 70))
        notes.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS  , wx.NORMAL, wx.NORMAL, 0, ""))
        #notes.SetForegroundColour(wx.Colour(253, 254, 255))
        

        btnPlaylist = wx.Button(panel, label='➕',size =(50, 25),  name ="Playlist",pos=(420, 125))
        #btnPlaylist.SetForegroundColour(wx.Colour(0, 167, 50))
        btnPlaylist.Bind(wx.EVT_BUTTON, self.on_pressPlaylist)
        
        btnDownload = wx.Button(panel, label='Download ✔️',size =(145, 30),  name ="button",pos=(250, 185))
        btnDownload.SetForegroundColour(wx.Colour(0, 167, 50))
        btnDownload.SetBackgroundColour(wx.Colour(203, 255, 186))
        btnDownload.Bind(wx.EVT_BUTTON, self.on_pressDownload)

        btnAlbum = wx.Button(panel, label='Album 📁',size =(145, 30),  name ="button",pos=(90, 185))
        btnAlbum.SetForegroundColour(wx.Colour(0, 141, 255))
        btnAlbum.SetBackgroundColour(wx.Colour(200, 225, 246, 0.8))

        btnAlbum.Bind(wx.EVT_BUTTON, self.on_pressAlbum)

        btnList = wx.Button(panel, label='📝',size =(30, 30),  name ="📝",pos=(15, 15))
        btnList.SetForegroundColour(wx.Colour(0, 0, 0))
        btnList.Bind(wx.EVT_BUTTON, self.on_pressList)

        btnHelp = wx.Button(panel, label='❓',size =(30, 30),  name ="?",pos=(438, 15))
        btnHelp.SetForegroundColour(wx.Colour(255, 0, 0))
        btnHelp.Bind(wx.EVT_BUTTON, self.on_pressHelp)
        btnHelp.SetBackgroundColour((212, 213, 217, 1))

        btnClear = wx.Button(panel, label='🧽',size =(30, 30),  name ="?",pos=(408, 15))
        btnClear.SetForegroundColour(wx.Colour(255, 153, 0))
        btnClear.Bind(wx.EVT_BUTTON, self.on_pressClear)
        btnClear.SetBackgroundColour((212, 213, 217, 1))

        btnSettings= wx.Button(panel, label='📂',size =(30, 30),  name ="folder",pos=(45, 15))
        btnSettings.SetForegroundColour(wx.Colour(0, 0, 0))
        btnSettings.Bind(wx.EVT_BUTTON, self.on_pressDirectory)

        #btnSettings.SetBackgroundColour((93, 89, 89, 1))

        signature = wx.StaticText(panel, label="by M. Momin   ", pos=(435, 250))
        signature.SetFont(wx.Font(6, wx.FONTFAMILY_SWISS  , wx.ITALIC, wx.NORMAL, 0, ""))

        self.log = wx.TextCtrl(panel, -1, size=(395, 25), pos=(20, 125), style=wx.TE_PROCESS_ENTER)
        font1 = wx.Font(10, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
        self.log.SetFont(font1)
        self.log.SetBackgroundColour((255, 255, 255))

        my_sizer.Add((0,0), 1, wx.EXPAND)
        #my_sizer.Add(self.log, 0, wx.ALL | wx.CENTER, 0)
        my_sizer.Add((0,0), 1, wx.EXPAND)

        cmd = 'color 8F' 
        os.system(cmd)
        cmd = 'mode 70, 20'
        os.system(cmd)
        print(" \n              ▄ █ ▄ █ ▄ █    YᴏᴜCᴏɴᴠᴇʀᴛPlay    █ ▄ █ ▄ █ ▄      \n ")

        
        panel.SetSizer(my_sizer)        
        self.Show()



    def on_pressDownload(self, event):
        t = Thread(target=run, args=())
        t.start()

    def on_pressPlaylist(self, event):
        destFile = r"list.txt"
        with open(destFile, 'a') as f:
            link = self.log.GetValue() + str("\n")
            f.write(link)
            self.log.SetBackgroundColour((147, 230, 146))
            self.log.SetValue("")

    def on_pressAlbum(self, event):
        file = open('destination.txt', "r")
        line = file.readline()
        file.close()
        SAVE_PATH = line
        os.system("start " + SAVE_PATH)
    
    def on_pressHelp(self, event):
        os.system("start " + "ReadMe_fr.txt")

    def on_pressList(self, event):
        os.system("start " + "list.txt")
    
    def on_pressDirectory(self, event):
        dialog = wx.DirDialog(None, "Choose a directory 📂",style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            f = open("destination.txt","w")
            f.close()
            destFile = r"destination.txt"
            with open(destFile, 'a') as f:
                f.write(dialog.GetPath() + '/')
                print ("\n\nDirectory changed with succes 📂✔️")
        dialog.Destroy()
    
    def on_pressClear(self, event):
        os.system('cls')
        print(" \n              ▄ █ ▄ █ ▄ █    YᴏᴜCᴏɴᴠᴇʀᴛ    █ ▄ █ ▄ █ ▄      \n ")
        print(" \n──────────────────────────────────────────────────────────────────────\n ")


if __name__=='__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()


