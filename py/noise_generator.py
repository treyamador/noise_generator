import random
import wave
import math


class WAV:

    def __init__(self,nchannels=1,sampwidth=1,framerate=44100,nframes=4410000):
        self.set_nchannels(nchannels)
        self.set_sampwidth(sampwidth)
        self.set_framerate(framerate)
        self.set_nframes(nframes)

    def set_attr(self,wav,nchannels,sampwidth,framerate,nframes):
        wav.setnchannels(nchannels)
        wav.setsampwidth(sampwidth)
        wav.setframerate(framerate)
        wav.setnframes(nframes)
        return wav

    def set_nchannels(self,nchannels):
        self.nchannels = nchannels

    def set_sampwidth(self,sampwidth):
        self.sampwidth = sampwidth

    def set_framerate(self,framerate):
        self.framerate = framerate
        
    def set_nframes(self,nframes):
        self.nframes = nframes

    def set_data(self,data):
        self.data = data

    def write_file(self,path):
        with wave.open(path,'wb') as wav:
            wav = self.set_attr(wav,
                self.nchannels,self.sampwidth,
                self.framerate,self.nframes)
            wav.writeframesraw(bytes(self.data))

    def read_file(self,path):
        pass


class Note:
    
    def __init__(self,tone,length):
        self.tone = tone
        self.length = length


class Music:

    def __init__(self):
        self.instruments = {}
        self.notes = []

    def add_instrument(self,name):
        self.instruments[name] = []

    def add_notes(self,notes):
        if isinstance(notes,list):
            for note in notes:
                self.notes.append(note)
        elif isinstance(notes,Note):
            self.notes.append(notes)

    def create_sinusoid(self,tone,frames):
        return [int(math.sin(tone*2*math.pi*x/44100)*127+128) for x in range(int(44100*frames))]

    def write(self,filename):
        sinusoid = []
        for note in self.notes:
            sinusoid.extend(self.create_sinusoid(note.tone,note.length))
        wav = WAV()
        wav.set_data(sinusoid)
        wav.write_file(filename)
        

def driver():
    music = Music()
    
    freq = {
        
        'C4':261.63,
        'D4':293.66,
        'E4':329.63,
        'F4':349.23,
        'G4':392.00,
        'A4':440.00,
        'B4':493.88,
        
        'C5':523.25,
        'D5':587.33,
        'E5':659.25,
        'F5':698.46,
        'G5':783.99,
        'A5':880.00,
        'B5':987.77,
        
        'C6':1046.50,
        'D6':1174.66,
        'E6':1318.51,
        'F6':1396.91,
        'G6':1567.98,
        'A6':1760.00,
        'B6':1975.53

    }


    notes = [
        
        Note(freq['E4'],5.0),
    
    ]
    


    music.add_notes(notes)
    music.write('sample.wav')


if __name__ == '__main__':
    driver()

