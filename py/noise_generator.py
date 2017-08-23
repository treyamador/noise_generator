import random
import wave
import math


class Vec2D:

    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y


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


'''

class Voices:

    def __init__(self):
        self.voices = []

    def __getitem__(self,key):
        pass

    def __setitem__(self,key,value):
        pass

    def __len__(self):
        pass

'''



class Voices:

    def __init__(self):
        self.voices = []
        self.keys = {}

    def __getitem__(self,key):
        val = self.keys[key]
        return self.voices[val]

    def __setitem__(self,key,value):
        if key in self.keys:
            self.voices[self.keys[key]] = value
        else:
            self.keys[key] = len(self.keys)
            self.voices.append(value)

    def __len__(self):
        return len(self.voices)

    def print(self):
        for key,val in self.keys.items():
            print(key,end=' ')
            print(self.voices[val])
        print('voices',len(self.voices))
        print('keys',len(self.keys))



class Music:

    def __init__(self):
        self.voices = {}
        self.notes = []

    def add_instrument(self,name):
        pass

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


def init_freq():
    return {
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
        

def driver():
    music = Music()
    freq = init_freq()
    notes = [
        Note(freq['A4'],5.0),
    ]
    music.add_notes(notes)
    music.write('sample.wav')

    # testing voices class
    voices = Voices()
    voices['A1'] = 'Hey there!'
    voices['B1'] = 'How it goes?'
    voices['C1'] = 'Life is a cruel joke.'
    voices['B1'] = 'Perhaps things will work out.'
    voices['C1'] = 'Yeah, I agree.'
    voices['D1'] = 'But there is more too it.'
    print('The len is',len(voices))
    voices.print()


if __name__ == '__main__':
    driver()

