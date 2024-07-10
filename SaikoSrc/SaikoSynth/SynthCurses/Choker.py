'''
（由于暂时找不到地方写了，就写在这里罢（笑）
音色的格式大改
{
    "<音色名>" : [
        {"freq": <频率>, "real": <实部>, "imag": <虚部>},
        ...
    ],
    ...
}
'''
import numba
import numpy as np
from typing import Any

SoundTrackType = np.ndarray[np.float32, Any]

synthesizer_name = 'ChokerSynthesizer'

#import matplotlib.pyplot as plt

@numba.njit
def __SynthCurse(length: int, volume: float, freq: SoundTrackType, resl: SoundTrackType, imag: SoundTrackType, sr: int | float = 64000)-> SoundTrackType:
    samples = np.arange(start=0, stop=length, step=1, dtype=np.float32) * 2 * np.pi / sr
    fs = np.kron(samples, freq.T).reshape(1000, len(freq))
    r = resl.T * np.cos(fs)
    i = imag.T * np.sin(fs)
    result = volume * (r + i)
    return np.sum(result, axis=1)

#@numba.njit
def __SynthCurseNOJIT(length: int, volume: float, freq: SoundTrackType, resl: SoundTrackType, imag: SoundTrackType, sr: int | float = 64000)-> SoundTrackType:
    samples = np.arange(start=0, stop=length, step=1, dtype=np.float32) * 2 * np.pi / sr
    fs = np.kron(samples, freq.T).reshape(1000, len(freq))
    r = resl.T * np.cos(fs)
    i = imag.T * np.sin(fs)
    result = volume * (r + i)
    return np.sum(result, axis=1)


class Synth(object):
    def __init__(self, voice_table: dict[str, list[dict[str, float]]]):
        self.voice_table: dict[str, tuple[SoundTrackType, SoundTrackType, SoundTrackType]] = {}
        for voice_name, voice_data in voice_table.items():
            freq_num = len(voice_data)
            freq = [0.0] * freq_num
            resl = [0.0] * freq_num
            imag = [0.0] * freq_num

            for i in range(freq_num):
                freq[i] = voice_data[i]['freq']
                resl[i] = voice_data[i]['real']
                imag[i] = voice_data[i]['imag']
            
            self.voice_table[voice_name] = (np.array(freq, np.float32), np.array(resl, np.float32), np.array(imag, np.float32))
    
    def __call__(self, length: int, vol: float, voice_name: str, sr: int | float = 64000):
        return __SynthCurseNOJIT(length, vol, *self.voice_table[voice_name], sr=sr)
    

if __name__ == '__main__':

    import matplotlib.pyplot as plt
    import time

    t1 = time.time()
    n = __SynthCurseNOJIT(1000, 0.8, np.array([1], np.float32), np.array([0.2], np.float32), np.array([0.8], np.float32), 1000)
    t2 = time.time()
    p = __SynthCurseNOJIT(1000, 0.8, np.array([1], np.float32), np.array([0.8], np.float32), np.array([0.2], np.float32), 1000)
    t3 = time.time()
    
    print(t2-t1, t3, t2)

    plt.plot(n)
    plt.show()

