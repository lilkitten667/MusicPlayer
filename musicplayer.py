import pygame
import os
import time
from tkinter import *
from tkinter import ttk

class MusicPlayer:
    '''One object of this class represents a tkinter GUI application
    that plays audio files. '''

    def __init__(self, root):
        ''' Creates a tkinter GUI application that plays audio files.'''
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("1000x200+200+200")
        
        pygame.init()
        pygame.mixer.init()
        
        self.track = StringVar()
        
        self.status = StringVar()

        trackframe = LabelFrame(self.root, text = "song track", relief = GROOVE)
        trackframe.place(x = 0, y = 0, width = 600, height = 100)
        
        songtrack = Label(trackframe, 
                         textvariable = self.track).grid(row = 0, column = 0,
                                                         padx = 10, pady = 5)
        
        trackstatus = Label(trackframe, textvariable = self.status
                          ).grid(row = 0, column = 0, padx = 10, pady = 5)
        
        buttonframe = LabelFrame(
           self.root, text = "Control Panel", relief = GROOVE)
        buttonframe.place(x = 0, y = 100, width = 600, height = 100)
        
        Button(buttonframe, text="Play", command=self.playsong()).grid(row=0, column=0, padx=10, pady=5)
        Button(buttonframe, text="Pause", command=self.pausesong).grid(row=0, column=1, padx=10, pady=5)
        Button(buttonframe, text="Unpause", command=self.unpausesong).grid(row=0, column=2, padx=10, pady=5)
        Button(buttonframe, text="Stop", command=self.stopsong).grid(row=0, column=3, padx=10, pady=5)
    
    
        songsframe = LabelFrame(self.root, text = "Song Playlist", relief = GROOVE)
        songsframe.place(x = 600, y = 0, width = 400, height = 150)
        
        scrol_y = Scrollbar(songsframe, orient = VERTICAL)
        self.playlist = Listbox(songsframe, yscrollcommand = scrol_y.set,
                                selectbackground = "gold",
                                selectmode = SINGLE, relief = GROOVE)
        scrol_y.pack(side = RIGHT, fill = y)
        scrol_y.config(command = self.playlist.yview)
        self.playlist.pack(fill = BOTH)
        
        searchframe = LabelFrame(self.root, text = "Search", relief = GROOVE)
        searchframe.place(x = 600, y = 145, width = 400, height = 50)
        
        search_imput = Entry(searchframe, width = 30)
        self.inputVar = SringVar()
        search_input.config(textvariable = self.inputVar)
        search_input.grid(row = 1, column = 2, padx = 1, pady = 1)
        Button(searchframe, text = "Search",
                command = self.search).grid(row = 1, column = 1, padx = 1, pady = 1)

        olpath = os.getcwd()
        music = path("/Users/pipye/Downloads/Dancemusicplayer/Songs")
        dir = "Songs"
        PlayList = os.path.join(olpath, dir, music)

        print("Your New bopping tunes directory is: " + PlayList)
   
        self.refresh()

    def playlist(self):
        playlist = os.listdir()
        sound_track = playlist

    def search(self):
        templist = self.playlist.get(0, END)
        self.playlist.delet(0, END)
        query = self.inputVar.get().casefold().strip()

        try:
            for filename in templist:
                if query in filename.casefold():
                    self.playlist.insert(END, filename)
        except Exception as err:
            self.status.set(err)

    def playsong(self):
        songs = self.playlist.get(ACTIVES)
        self.status.set(" -Playing")
        self.track.set(songs)
        pygame.mixer.music.load(songs)
        pygame.mixer.music.play()

        
    def stopsong(self):
        self.status.set(" -Stopped")
        pygame.mixer.music.stop()

        
    def pausesong(self):
        self.status.set("Paused")
        self.mixer.music.pause()

        
    def unpausesong(self):
        self.status.set(" -Playing")
        pygame.mixer.music.unpause()

        
    def refresh(self):
        self.playlist.delete(0, 'end')
        file_type = ('mp3', '.ogg', '.wav')
        sound_track = os.listdir()

        try:
            for filename in sound_track:
                if filename[0] != ".":
                    if filename.endswith(file_type):
                        self.playlist.insert('end', filename)
        except Exception as err:
            self.status.set("Error" + str(err))

        print(self.playlist)


def main():
    root = Tk()
    app = MusicPlayer(root)
    root.mainloop()

if __name__ == "__main__":
    main()

    





        

    
