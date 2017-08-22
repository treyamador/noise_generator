import wave
import math



class WAV:

    def __init__(self,filename,nchannels=2,sampwidth=2,framerate=44100,nframes=441000):
        ''' init new wav file '''
        self.wav = self._init_wav(filename)
        self.set_attr(nchannels,sampwidth,framerate,nframes)

    def set_attr(self,nchannels,sampwidth,framerate,nframes):
        self.nchannels = nchannels
        self.sampwidth = sampwidth
        self.framerate = framerate
        self.nframes = nframes
        self.wav.setnchannels(nchannels)
        self.wav.setsampwidth(sampwidth)
        self.wav.setframerate(framerate)
        self.wav.setnframes(nframes)

    def set_data(self,data):
        if isinstance(data,list):
            self.wav.writeframesraw(bytes(data))

    def _init_wav(self,filename):
        return wave.open(filename,'wb')

    def __del__(self):
        self.wav.close()


def create_wave(filename):
    wav = WAV(filename)
    frames = [int(math.sin(x)) for x in range(44100*10)]
    wav.set_data(frames)



def driver():
    create_wave('sample.wav')
    




if __name__ == '__main__':
    driver()

