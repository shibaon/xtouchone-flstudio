# name=Xtouch one DAW

import midi
import ui
import transport
import device
import mixer
import math

import xtouch_utils

CcIdPlay = 0x17
CcIdStop = 0x16
CcIdRec = 0x18
CcIdRew = 0x14
CcIdFwd = 0x15

CcIdTempo = 0x5A

def onInit():
    device.setHasMeters()

evt = False

def OnControlChange(event):
    global evt
    evt = event
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

once = False

def OnUpdateMeters():
    value = mixer.getLastPeakVol(midi.PEAK_LR_INV)
    global meter_value
    meter_value = xtouch_utils.convertToMeterValue(value)
    device.midiOutMsg(0xB0, 0, CcIdTempo, math.ceil(meter_value))

    global once, evt

    if not once and evt:
        print(evt.sysex)
        xtouch_utils.sendText(evt, 'green', 'Top', 'Bottom')
        once = True
