# name=Xtouch one DAW

import midi
import ui
import transport
import device
import mixer
import math

CcIdPlay = 0x17
CcIdStop = 0x16
CcIdRec = 0x18
CcIdRew = 0x14
CcIdFwd = 0x15

CcIdTempo = 0x5A

def onInit():
    device.setHasMeters()

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

def __ConvertToMeterValue(value: float):
    """ Converts an FL Studio meter float value to an MCU compatible value (one char hex) """
    
    value_max = 1.3 # FL Studio max value
    meter_value = int(value / value_max * 127) # 127 — max value in X touch one

    # If there's any activity, make sure the meter shows it
    if (value > 0.001 and meter_value == 0):
        meter_value = 1

    # If there's no activity, clear the meter (15)
    if value == 0:
        meter_value = 0

    return meter_value;

meter_value = 0;

def OnUpdateMeters():
    value = mixer.getLastPeakVol(midi.PEAK_LR_INV)
    global meter_value
    meter_value = __ConvertToMeterValue(value)
    device.midiOutMsg(0xB0, 0, CcIdTempo, math.ceil(meter_value))
