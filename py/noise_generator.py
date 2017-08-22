import random
import wave
import math


class WAV:

    def __init__(self,nchannels=1,sampwidth=1,framerate=44100,nframes=4410000):
        ''' args: path, nchannels, sampwidth, framerate, nframes, data '''
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


def create_single_tone_wave(filename):
    # WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))
    wav = WAV()
    frames = [int(math.sin(x/100)*128)+127 for x in range(44100*100)]
    wav.set_data(frames)
    wav.write_file(filename)

def create_a_note_wav(filename):
    sinusoid = [int(math.sin(880*math.pi*x/44100)*128+128) for x in range(4410000)]
    wav = WAV()
    wav.set_data(sinusoid)
    wav.write_file(filename)


def driver():
    create_a_note_wav('sample.wav')
    

if __name__ == '__main__':
    driver()


