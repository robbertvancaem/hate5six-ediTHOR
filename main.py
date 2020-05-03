from pynput.keyboard import Key, Controller
import time
import random

keyboard = Controller()

startup = 1


def get_closest(n, i):
    # Smaller multiple
    a = n // i * i

    b = a + i

    return b if n - a > b - n else a


def get_angle(current, amount_of_cameras):
    angles = list(range(amount_of_cameras))  # Create a list with all cameras
    # Remove the current camera from the list (it is 1-based)
    angles.remove(current - 1)
    new_angle = random.choice(angles)  # Pick a random camera from the list

    return new_angle + 1  # Since a list is 0 based, add 1 so that it starts at 1


def get_duration(min, max, bpm):
    bps = bpm / 60  # The amount of beats per second

    duration_interval = (1 / bps) * 1000

    # Pick a random duration (in ms)
    random_duration = random.randint(min * 1000, max * 1000)

    # Round it to a duration that matches the BPM
    duration = get_closest(random_duration, duration_interval)

    print("Duration (%s)ms, bps (%s), interval (%s)ms " %
          (duration, bps, duration_interval))
    return duration / 1000  # Return it in seconds


def delay():
    # Give some time to think or get ready, please
    print("Start in %s seconds..." % (startup))
    time.sleep(startup)  # Not sure why this is needed
    # This probably is needed to start the sequence in Premiere
    keyboard.press(Key.space)
    keyboard.release(Key.space)


def run():
    current_angle = 1
    amount_of_cameras = 4
    min_duration = 2  # (in seconds)
    max_duration = 4  # (in seconds)
    bpm = 120  # This will influence the speed of the cuts

    delay()  # Initiate startup
    time.sleep(1)

    while True:
        angle = get_angle(current_angle, amount_of_cameras)

        duration = get_duration(min_duration, max_duration, bpm)
        # keyboard.press('%s' % angle)
        # keyboard.release('%s' % angle)
        print("Cutting to Camera %s, hold %s s" % (angle, duration))
        time.sleep(duration)
        current_angle = angle


if __name__ == '__main__':
    run()
