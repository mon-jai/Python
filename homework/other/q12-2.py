from dataclasses import dataclass

@dataclass
class Plan:
    base: int
    chargeForVoiceInSameNetwork: float
    chargeForVoiceInDifferentNetwork: float
    chargeForVoiceCity: float
    chargeForMessageInSameNetwork: float
    chargeForMessageInDifferentNetwork: float

    def charge(self, voiceInSameNetwork: int,
               voiceInDifferentNetwork: int, voiceCity: int,
               messageInSameNetwork: int, messageInDifferentNetwork: int) -> float:
        return self.chargeForVoiceInSameNetwork * voiceInSameNetwork +\
            self.chargeForVoiceInDifferentNetwork * voiceInDifferentNetwork +\
            self.chargeForVoiceCity * voiceCity +\
            self.chargeForMessageInSameNetwork * messageInSameNetwork +\
            self.chargeForMessageInDifferentNetwork * messageInDifferentNetwork
