# name=Xtouch one DAW

import midi
import ui
import transport

CcIdPlay = 0x17
CcIdStop = 0x16
CcIdRec = 0x18
CcIdRew = 0x14
CcIdFwd = 0x15

def OnControlChange(event):
    event.handled = False
    # print(event.data1)
    if event.data2 >= 0x40:
        if event.data1 == CcIdPlay:
            transport.start()
            event.handled = True
        elif event.data1 == CcIdStop:
            transport.stop()
            event.handled = True
        elif event.data1 == CcIdRec:
            transport.record()
            event.handled = True
        elif event.data1 == CcIdRew:
            # print("rew")
            ui.setFocused(midi.widPlaylist)
            ui.jog(-1)
            event.handled = True
        elif event.data1 == CcIdFwd:
            # print("fwd")
            ui.setFocused(midi.widPlaylist)
            ui.jog(1)
            event.handled = True
