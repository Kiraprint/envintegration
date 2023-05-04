import unittest
from datetime import time
from envintegration.hygiene.physical_hygiene.light_mode import LightModes, light_mode_with_stress_index, light_mode_with_pai_and_hr


class TestLightModes(unittest.TestCase):

    def test_light_mode_with_stress_index(self):
        # when current_time is before 10 AM\n        current_time = time(hour=9, minute=30)
        sleep_duration = time(hour=7, minute=30)
        stress_index = 25
        expected_output = [
            LightModes(step=1, duration=time(minute=15),
                       light_temperature=4000, light_intensity=500),
            LightModes(step=2, duration=time(minute=15),
                       light_temperature=7000, light_intensity=1000),
            LightModes(step=3, duration=None,
                       light_temperature=4000, light_intensity=500)
        ]
        self.assertEqual(light_mode_with_stress_index(
            stress_index, sleep_duration, current_time), expected_output)

        # when current_time is between 10 AM and 3 PM and stress index is less than or equal to 39
        current_time = time(hour=12)
        sleep_duration = time(hour=5, minute=30)
        stress_index = 30
        expected_output = [
            LightModes(step=1, duration=time(minute=15),
                       light_temperature=6000, light_intensity=750),
            LightModes(step=2, duration=None,
                       light_temperature=4000, light_intensity=500)
        ]
        self.assertEqual(light_mode_with_stress_index(
            stress_index, sleep_duration, current_time), expected_output)

        # when current_time is between 10 AM and 3 PM and stress index is between 40 and 59
        current_time = time(hour=12)
        sleep_duration = time(hour=4)
        stress_index = 55
        expected_output = [LightModes(
            step=1, duration=None, light_temperature=4000, light_intensity=500)]
        self.assertEqual(light_mode_with_stress_index(
            stress_index, sleep_duration, current_time), expected_output)

        # when current_time is between 10 AM and 3 PM and stress index is between 60 and 79
        current_time = time(hour=12)
        sleep_duration = time(hour=7)
        stress_index = 75
        expected_output = [
            LightModes(step=1, duration=time(minute=30),
                       light_temperature=3500, light_intensity=350),
            LightModes(step=2, duration=None,
                       light_temperature=4000, light_intensity=500)
        ]
        self.assertEqual(light_mode_with_stress_index(
            stress_index, sleep_duration, current_time), expected_output)

        # when current_time is between 10 AM and 3 PM and stress index is between 80 and 100
        current_time = time(hour=12)
        sleep_duration = time(hour=7, minute=30)
        stress_index = 95
        expected_output = [
            LightModes(step=1, duration=time(
                minute=30), light_temperature=3500, light_intensity=350, need_to_rest=True),
            LightModes(step=2, duration=None,
                       light_temperature=4000, light_intensity=500)
        ]
        self.assertEqual(light_mode_with_stress_index(
            stress_index, sleep_duration, current_time), expected_output)

        # when current_time is between 3 PM and 8 PM and stress index is less than or equal to 39
        current_time = time(hour=17)
        sleep_duration = time(hour=5, minute=30)
        stress_index = 35
        expected_output = [LightModes(
            step=1, duration=None, light_temperature=4000, light_intensity=500)]
        self.assertEqual(light_mode_with_stress_index(
            stress_index, sleep_duration, current_time), expected_output)

        # when current_time is between 3 PM and 8 PM and stress index is between 40 and 59
        current_time = time(hour=17)
        sleep_duration = time(hour=4)
        stress_index = 50
        expected_output = [
            LightModes(step=1, duration=time(minute=15),
                       light_temperature=6000, light_intensity=750),
            LightModes(step=2, duration=None,
                       light_temperature=4000, light_intensity=500)
        ]
        self.assertEqual(light_mode_with_stress_index(
            stress_index, sleep_duration, current_time), expected_output)

        # when current_time is between 3 PM and 8 PM and stress index is between 60 and 79
        current_time = time(hour=17)
        sleep_duration = time(hour=7)
        stress_index = 70
        expected_output = [
            LightModes(step=1, duration=time(minute=30),
                       light_temperature=3500, light_intensity=350),
            LightModes(step=2, duration=None,
                       light_temperature=4000, light_intensity=500)
        ]
        self.assertEqual(light_mode_with_stress_index(
            stress_index, sleep_duration, current_time), expected_output)

        # when current_time is between 3 PM and 8 PM and stress index is between 80 and 100
        current_time = time(hour=17)
        sleep_duration = time(hour=7, minute=30)
        stress_index = 90
        expected_output = [
            LightModes(step=1, duration=time(minute=30),
                       light_temperature=3500, light_intensity=350, need_to_rest=True),
            LightModes(step=2, duration=None,
                       light_temperature=4000, light_intensity=500)
        ]
        self.assertEqual(light_mode_with_stress_index(
            stress_index, sleep_duration, current_time), expected_output)


def test_light_mode_with_pai_and_hr(self):
    # when current_time is before 10 AM
    current_time = time(hour=9)
    sleep_duration = time(hour=7, minute=30)
    pai = 25
    hr = 60
    expected_output = [
        LightModes(step=1, duration=time(minute=15),
                   light_temperature=4000, light_intensity=500),
        LightModes(step=2, duration=time(minute=15),
                   light_temperature=7000, light_intensity=1000),
        LightModes(step=3, duration=None,
                   light_temperature=4000, light_intensity=500)
    ]
    self.assertEqual(light_mode_with_pai_and_hr(
        pai, hr, sleep_duration, current_time), expected_output)

    # when current_time is between 10 AM and 3 PM and pai is less than or equal to 2.9 and HR is less than or equal to 89
    current_time = time(hour=12)
    sleep_duration = time(hour=5, minute=30)
    pai = 2.5
    hr = 80
    expected_output = [LightModes(
        step=1, duration=None, light_temperature=4000, light_intensity=500)]
    self.assertEqual(light_mode_with_pai_and_hr(
        pai, hr, sleep_duration, current_time), expected_output)

    # when current_time is between 10 AM and 3 PM and pai is less than or equal to 2.9 and HR is between 90 and 139
    current_time = time(hour=12)
    sleep_duration = time(hour=4)
    pai = 2.5
    hr = 120
    expected_output = [
        LightModes(step=1, duration=time(minute=15),
                   light_temperature=6000, light_intensity=750),
        LightModes(step=2, duration=None,
                   light_temperature=4000, light_intensity=500)
    ]
    self.assertEqual(light_mode_with_pai_and_hr(
        pai, hr, sleep_duration, current_time), expected_output)


    # when current_time is between 10 AM and 3 PM and pai is less than or equal to 2.9 and HR is greater than 140
    current_time = time(hour=12)
    sleep_duration = time(hour=5)
    pai = 2.5
    hr = 150
    expected_output = [
        LightModes(step=1, duration=time(minute=15),
                   light_temperature=6000, light_intensity=750),
        LightModes(step=2, duration=None,
                   light_temperature=4000, light_intensity=500)
    ]
    self.assertEqual(light_mode_with_pai_and_hr(
        pai, hr, sleep_duration, current_time), expected_output)
    
    # when current_time is between 10 AM and 3 PM and pai is between 3 and 3.9 and HR is less than or equal to 89
    current_time = time(hour=12)
    sleep_duration = time(hour=4, minute=30)
    pai = 3.5
    hr = 70
    expected_output = [
        LightModes(step=1, duration=time(minute=20),
                   light_temperature=6500, light_intensity=850),
        LightModes(step=2, duration=None,
                   light_temperature=4000, light_intensity=500)
    ]
    self.assertEqual(light_mode_with_pai_and_hr(
        pai, hr, sleep_duration, current_time), expected_output)
    