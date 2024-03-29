import os
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from sphero_sdk import SpheroRvrObserver

rvr = SpheroRvrObserver()


def main():
    """ This program has RVR drive around in different directions using the function drive_with_yaw_normalized.
        This is a newer command, and uses some different conventions from what you may be accustomed to if you
        have used the initial release of this SDK.

        In Sphero conventions, "heading" is CCW positive, matching a compass, while "yaw" is CW positive, as a
        rotation around the (vertical) Z axis of the robot following the right hand rule.  This yaw convention
        was selected to match the ISO 8855 standard:
        "Road Vehicles - Vehicle dynamics and road-holding ability -- Vocabulary"

        Because of this difference between heading and yaw, headings will need to be converted into yaw angles
        IF you want to switch commands in existing projects.

        To eliminate the flags field, unsigned scalar speed values have been replaced in newer commands with
        signed linear velocity values.  The value is still a single byte, and is now normalized between +/-127
        instead of 0-255 (though -128 can be used - it will be clamped to -127).
    """
    try:
        rvr.wake()

        # Give RVR time to wake up
        time.sleep(2)

        rvr.reset_yaw()

        rvr.drive_with_yaw_normalized(
            linear_velocity=32,  # Valid linear_velocity values are in the range [-127..+127]
            yaw_angle=0  # Valid yaw values are traditionally [-179..+180], but will continue wrapping outside of that range
        )

        # Delay to allow RVR to drive
        time.sleep(1)

        rvr.drive_with_yaw_normalized(
            linear_velocity=32,  # Valid linear_velocity values are in the range [-127..+127]
            yaw_angle=90  # Valid yaw values are traditionally [-179..+180], but will continue wrapping outside of that range
        )

        # Delay to allow RVR to drive
        time.sleep(1)

        rvr.drive_with_yaw_normalized(
            linear_velocity=32,  # Valid linear_velocity values are in the range [-127..+127]
            yaw_angle=180  # Valid yaw values are traditionally [-179..+180], but will continue wrapping outside of that range
        )

        # Delay to allow RVR to drive
        time.sleep(1)

        rvr.drive_with_yaw_normalized(
            linear_velocity=32,  # Valid linear_velocity values are in the range [-127..+127]
            yaw_angle=270,  # Valid yaw values are traditionally [-179..+180], but will continue wrapping outside of that range
        )

        # Delay to allow RVR to drive
        time.sleep(1)

        # This will bring RVR to a stop facing a yaw angle of zero.
        rvr.drive_with_yaw_normalized(
            linear_velocity=0,  # Valid linear_velocity values are in the range [-127..+127]
            yaw_angle=0,  # Valid yaw values are traditionally [-179..+180], but will continue wrapping outside of that range
        )
       
        # Delay to allow RVR to drive
        time.sleep(2)

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

    finally:
        rvr.close()


if __name__ == '__main__':
    main()
