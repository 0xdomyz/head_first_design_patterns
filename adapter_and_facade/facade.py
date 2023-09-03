class Amplifier:
    def __init__(self):
        self.tuner = None
        self.player = None

    def on(self):
        print("Amplifier is on")

    def off(self):
        print("Amplifier is off")

    def set_stereo_sound(self):
        print("Amplifier stereo sound is set")

    def set_surround_sound(self):
        print("Amplifier surround sound is set")

    def set_volume(self, volume):
        print("Amplifier volume is set to", volume)


class Tuner:
    def __init__(self):
        self.amplifier = None

    def on(self):
        print("Tuner is on")

    def off(self):
        print("Tuner is off")

    def set_frequency(self, frequency):
        print("Tuner frequency is set to", frequency)


class StreamingPlayer:
    def __init__(self):
        self.amplifier = None

    def on(self):
        print("Streaming player is on")

    def off(self):
        print("Streaming player is off")

    def play(self, movie):
        print("Streaming player is playing", movie)

    def stop(self):
        print("Streaming player is stopped")

    def pause(self):
        print("Streaming player is paused")


class Projector:
    def __init__(self):
        self.player = None

    def on(self):
        print("Projector is on")

    def off(self):
        print("Projector is off")

    def tv_mode(self):
        print("Projector is in tv mode")

    def wide_screen_mode(self):
        print("Projector is in wide screen mode")


class Screen:
    def up(self):
        print("Screen is up")

    def down(self):
        print("Screen is down")


class PopcornPopper:
    def on(self):
        print("Popcorn popper is on")

    def off(self):
        print("Popcorn popper is off")

    def pop(self):
        print("Popcorn popper is popping popcorn")


class TheaterLights:
    def on(self):
        print("Theater lights are on")

    def off(self):
        print("Theater lights are off")

    def dim(self, level):
        print("Theater lights are dimmed to", level, "%")


class HomeTheaterFacade:
    def __init__(self, amp, tuner, player, projector, screen, lights, popper):
        self.amp = amp
        self.tuner = tuner
        self.player = player
        self.projector = projector
        self.screen = screen
        self.lights = lights
        self.popper = popper

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wide_screen_mode()
        self.amp.on()
        self.amp.set_surround_sound()
        self.amp.set_volume(5)
        self.player.on()
        self.player.play(movie)

    def end_movie(self):
        print("Shutting movie theater down...")
        self.popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.player.stop()
        self.player.off()


if __name__ == "__main__":
    # python3 07_the_adapter_and_facade_patterns/facade.py
    amp = Amplifier()
    tuner = Tuner()
    player = StreamingPlayer()
    projector = Projector()
    screen = Screen()
    lights = TheaterLights()
    popper = PopcornPopper()

    home_theater = HomeTheaterFacade(
        amp, tuner, player, projector, screen, lights, popper
    )
    home_theater.watch_movie("Raiders of the Lost Ark")
    home_theater.end_movie()
