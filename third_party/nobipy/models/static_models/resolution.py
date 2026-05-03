from dataclasses import dataclass

@dataclass(frozen=True)
class Resolution:
    value : str
    int_value : int
    name : str


class Resolutions:
    M1 : Resolution = Resolution(value='1', int_value = 1, name='M1')
    M5 : Resolution = Resolution(value='5', int_value = 5, name='M5')
    M15 : Resolution = Resolution(value='15', int_value = 15, name='M15')
    M30 : Resolution = Resolution(value='30', int_value = 30, name='M30')
    H1 : Resolution = Resolution(value='60', int_value = 60, name='H1')
    H3 : Resolution = Resolution(value='180', int_value = 180, name='H3')
    H4 : Resolution = Resolution(value='240', int_value = 240, name='H4')
    H6 : Resolution = Resolution(value='360', int_value = 360, name='H6')
    H12 : Resolution = Resolution(value='720', int_value = 720, name='H12')
    D1 : Resolution = Resolution(value='D', int_value = 1440, name='Daily')
    D2 : Resolution = Resolution(value='2D', int_value = 2880, name='2 Days')
    D3 : Resolution = Resolution(value='3D', int_value = 34320, name='3 Days')

    @classmethod
    def get_all(cls):
        attrs = [
            getattr(cls,i)
            for i in cls.__annotations__
        ]
        resolutions_ = [i for i in attrs if isinstance(i,Resolution)]

        return resolutions_
