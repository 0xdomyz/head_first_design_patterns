# python3 remote_control.py

from abc import ABC, abstractmethod


class RemoteControl:
    def __init__(self):
        self._on_commands = [None] * 7
        self._off_commands = [None] * 7

        no_command = NoCommand()

        for i in range(7):
            self._on_commands[i] = no_command
            self._off_commands[i] = no_command

    def set_command(self, slot, on_command, off_command):
        self._on_commands[slot] = on_command
        self._off_commands[slot] = off_command

    def on_button_was_pushed(self, slot):
        self._on_commands[slot].execute()

    def off_button_was_pushed(self, slot):
        self._off_commands[slot].execute()

    def __str__(self):
        string_buff = []
        string_buff.append("\n------ Remote Control -------\n")

        max_left_nme_len = 0
        for i in range(len(self._on_commands)):
            left_nme = self._on_commands[i].__class__.__name__
            max_left_nme_len = max(max_left_nme_len, len(left_nme))

        for i in range(len(self._on_commands)):
            left_nme = self._on_commands[i].__class__.__name__
            right_nme = self._off_commands[i].__class__.__name__
            string_buff.append(
                f"[slot {i}] {left_nme:{max_left_nme_len+4}}    {right_nme}\n"
            )

        return "".join(string_buff)


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class NoCommand(Command):
    def execute(self):
        pass


class LightOnCommand(Command):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.on()


class LightOffCommand(Command):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.off()


class Light:
    def __init__(self, location):
        self._location = location

    def on(self):
        print(self._location + " light is on")

    def off(self):
        print(self._location + " light is off")


class StereoOnWithCDCommand(Command):
    def __init__(self, stereo):
        self._stereo = stereo

    def execute(self):
        self._stereo.on()
        self._stereo.set_cd()
        self._stereo.set_volume(11)


class StereoOffCommand(Command):
    def __init__(self, stereo):
        self._stereo = stereo

    def execute(self):
        self._stereo.off()


class Stereo:
    def __init__(self, location):
        self._location = location

    def on(self):
        print(self._location + " stereo is on")

    def set_cd(self):
        print(self._location + " stereo is set for CD input")

    def set_volume(self, volume):
        print(self._location + " stereo volume set to " + str(volume))

    def off(self):
        print(self._location + " stereo is off")


class CeilingFanOnCommand(Command):
    def __init__(self, ceiling_fan):
        self._ceiling_fan = ceiling_fan

    def execute(self):
        self._ceiling_fan.high()


class CeilingFanOffCommand(Command):
    def __init__(self, ceiling_fan):
        self._ceiling_fan = ceiling_fan

    def execute(self):
        self._ceiling_fan.off()


class CeilingFan:
    def __init__(self, location):
        self._location = location
        self._level = 0

    def high(self):
        self._level = 2
        print(self._location + " ceiling fan is on high")

    def off(self):
        self._level = 0
        print(self._location + " ceiling fan is off")


def romote_loader():
    remote_control = RemoteControl()

    living_room_light = Light("Living Room")
    kitchen_light = Light("Kitchen")
    ceiling_fan = CeilingFan("Living Room")
    stereo = Stereo("Living Room")

    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)
    kitchen_light_on = LightOnCommand(kitchen_light)
    kitchen_light_off = LightOffCommand(kitchen_light)

    ceiling_fan_on = CeilingFanOnCommand(ceiling_fan)
    ceiling_fan_off = CeilingFanOffCommand(ceiling_fan)

    stereo_on = StereoOnWithCDCommand(stereo)
    stereo_off = StereoOffCommand(stereo)

    remote_control.set_command(0, living_room_light_on, living_room_light_off)
    remote_control.set_command(1, kitchen_light_on, kitchen_light_off)
    remote_control.set_command(2, ceiling_fan_on, ceiling_fan_off)
    remote_control.set_command(3, stereo_on, stereo_off)

    print(remote_control)

    remote_control.on_button_was_pushed(0)
    remote_control.off_button_was_pushed(0)
    remote_control.on_button_was_pushed(1)
    remote_control.off_button_was_pushed(1)
    remote_control.on_button_was_pushed(2)
    remote_control.off_button_was_pushed(2)
    remote_control.on_button_was_pushed(3)
    remote_control.off_button_was_pushed(3)


if __name__ == "__main__":
    romote_loader()
