
Number = int | float

StandardPitchSign: tuple[str, ...] = ('A', '#A', 'B', 'C', '#C', 'D', '#D', 'E', '#E', 'F', '#F', 'G', '#G')

def PitchTableGenerator(*, PitchSignTable: tuple[str, ...] | list[str] = StandardPitchSign, arange: tuple[int, int] = (-36, 60), A4: int = 4):
    '''
    生成一个科学音调记号对照表

    [In] `PitchSignTable` 一个八度内的所有音调记号

    [In] `arange` 范围(闭区间)，生成的表的音调范围

    [In] `A4` A4所在八度区间(当然也可能不叫A4)
    '''
    octave = len(PitchSignTable)
    for pitch_pow in range(arange[0], arange[1] + 1, 1):
        octave_level = A4 + pitch_pow // octave
        sign_index = pitch_pow % octave
        yield (pitch_pow, PitchSignTable[sign_index]+str(octave_level))

def pitch2freq(value_of_pitch: Number, *, A4: Number = 440, octave: int = 12) -> float:
    '''
    将音调记号表的音高值转换为频率

    [In] `value_of_pitch` 音高数值, 一般默认以A4作为0

    [In] `A4` A4的音高, 默认为440Hz

    [In] `octave` 一个八度内音调记号的数量, 默认12
    '''
    return A4 * 2 ** (value_of_pitch / octave)

