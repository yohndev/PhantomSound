from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np

class PhantomController():
    def __init__(self):
        # Initialize audio control(Basically telling the computer we want to control the audio and where)
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        self.volume = cast(interface, POINTER(IAudioEndpointVolume))

    def set_volume(self, hand_y):
        vol_scalar = np.interp(hand_y, [0.2, 0.8], [1.0, 0.0]) # handles the volume control to where is lower and where is higher
        vol_scalar = max(0.0, min(1.0, vol_scalar))#Ensures that its always between 0 and 1
        self.volume.SetMasterVolumeLevelScalar(vol_scalar, None)

