from machine import UART

STA_BYTE = 0x7E
VER_BYTE = 0xFF
LEN_BYTE = 0x06
FDB_BYTE = 0x00
END_BYTE = 0xEF


class GORILLA_MP3PLAYER:
    #     player_volume = 20
    #     is_mute = False

    def __init__(self, tx, rx):
        self.uart = UART(2, baudrate=9600, tx=tx, rx=rx)
        self.player_volume = 30
        self.is_mute = True
        self.setVolume(self.player_volume)

    def command(self, cmd, hbyte_data, lbyte_data):
        self.uart.write(bytes([STA_BYTE]))
        self.uart.write(bytes([VER_BYTE]))
        self.uart.write(bytes([LEN_BYTE]))
        self.uart.write(bytes([cmd]))
        self.uart.write(bytes([FDB_BYTE]))
        self.uart.write(bytes([hbyte_data]))
        self.uart.write(bytes([lbyte_data]))
        self.uart.write(bytes([END_BYTE]))

    def playNext(self):
        self.command(0x01, 0, 0)

    def playPrevious(self):
        self.command(0x02, 0, 0)

    def playIndex(self, index):
        self.command(0x03, 0, index)

    def volumeUp(self):
        if self.player_volume < 30:
            self.player_volume += 1
            self.command(0x04, 0, 0)
            print("Current volume: {}".format(self.player_volume))
        else:
            print("Max volume set\r\n")

    def volumeDown(self):
        if self.player_volume != 0:
            self.player_volume -= 1
            self.command(0x05, 0, 0)
            print("Current volume: {}".format(self.player_volume))
        else:
            print("Volume set to MUTE\r\n")

    def setVolume(self, volume):
        self.player_volume = volume
        self.command(0x06, 0, volume)

    def sleep(self):
        self.command(0x0A, 0, 0)

    def wakeUp(self):
        self.command(0x0B, 0, 0)

    def reset(self):
        self.command(0x0C, 0, 0)

    def play(self):
        self.command(0x0D, 0, 1)
        self.is_mute = False

    def pause(self):
        self.command(0x0E, 0, 0)

    def playFolder(self, folder, file):
        self.command(0x0F, folder, file)

    def playStop(self):
        self.command(0x16, 0, 0)

    def playMute(self):
        curr_vol = self.player_volume
        if self.is_mute:
            self.setVolume(curr_vol)
            self.is_mute = False
        else:
            self.setVolume(0)
            self.is_mute = True
        self.player_volume = curr_vol


mp3 = GORILLA_MP3PLAYER(rx=22, tx=17)

mp3.play()
