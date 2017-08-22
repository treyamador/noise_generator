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
        return [int(math.sin(tone*math.pi*x/44100)*127+128) for x in range(int(44100*frames))]

    def write(self,filename):
        sinusoid = []
        for note in self.notes:
            sinusoid.extend(self.create_sinusoid(note.tone,note.length))
        wav = WAV()
        wav.set_data(sinusoid)
        wav.write_file(filename)
        

def driver():
    music = Music()
    #notes = [
    #    Note(880,0.25),Note(1100,0.25),Note(1320,0.25),Note(1760,0.25),
    #    Note(880,0.25),Note(1100,0.25),Note(1320,0.25),Note(1760,0.25),
    #    Note(880,0.25),Note(1100,0.25),Note(1320,0.25),Note(1760,0.25),
    #    Note(880,0.25),Note(1100,0.25),Note(1320,0.25),Note(1760,0.25),
    #]

    freq = {

        'A4':440.00,
        'B4':493.88,
        
        'C5':523.25,
        'E5':659.25,
        'G5':783.99,
        'A5':880.00,
        'B5':987.77,
        
        'C6':1046.50

    }

    notes = [
        Note(freq['C5'],0.25),Note(freq['E5'],0.25),Note(freq['G5'],0.25),Note(freq['C6'],0.25),
        Note(freq['C5'],0.25),Note(freq['E5'],0.25),Note(freq['G5'],0.25),Note(freq['C6'],0.25),
        Note(freq['C5'],0.25),Note(freq['E5'],0.25),Note(freq['G5'],0.25),Note(freq['C6'],0.25),
        Note(freq['B4'],0.25),Note(freq['E5'],0.25),Note(freq['G5'],0.25),Note(freq['B5'],0.25),
        
        Note(freq['C5'],0.25),Note(freq['E5'],0.25),Note(freq['A5'],0.25),Note(freq['C6'],0.25),
        Note(freq['C5'],0.25),Note(freq['E5'],0.25),Note(freq['A5'],0.25),Note(freq['C6'],0.25),
        Note(freq['C5'],0.25),Note(freq['E5'],0.25),Note(freq['A5'],0.25),Note(freq['C6'],0.25),
        Note(freq['C5'],0.25),Note(freq['E5'],0.25),Note(freq['A5'],0.25),Note(freq['C6'],0.25),
        

    ]
    music.add_notes(notes)
    music.write('sample.wav')

if __name__ == '__main__':
    driver()

