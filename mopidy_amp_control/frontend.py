import subprocess
import logging
import pykka
from mopidy.core import CoreListener, PlaybackState
from .repeating_timer import RepeatingTimer

logger = logging.getLogger(__name__)

def run_cmd(cmd):
    subprocess.run(cmd.strip(' "').split(), check=True)

class AmpControlFrontend(pykka.ThreadingActor, CoreListener):
    def __init__(self, config, core):
        super(AmpControlFrontend, self).__init__()

        self.core = core
        self.config = config["amp_control"]
        self.poweroff_timer = RepeatingTimer(
            self.config["unpower_in_minutes"]*60.0,
            self.unpower_amp,
            {"now":True})
        self.amp_on = False

    # my functions

    def power_amp(self):
        if not self.amp_on:
            self.poweroff_timer.cancel()
            run_cmd(self.config["cmd_power"])
            self.amp_on = True

    def unpower_amp(self, now=False):
        if self.amp_on:
            if now:
                run_cmd(self.config["cmd_unpower"])
                self.amp_on = False
            else:
                self.poweroff_timer.start()

    # event listeners

    def on_start(self):
        playback_state = self.core.playback.get_state()
        if playback_state == PlaybackState.PLAYING:
            self.power_amp()

    def on_stop(self):
        self.unpower_amp(now=True)

    def track_playback_started(self, tl_track):
        self.power_amp()

    def track_playback_resumed(self, tl_track, time_position):
        self.power_amp()

    def track_playback_paused(self, tl_track, time_position):
        self.unpower_amp()
