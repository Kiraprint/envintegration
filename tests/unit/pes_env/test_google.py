import asyncio
import unittest
from unittest.mock import MagicMock

from .google_fit_api import GoogleFitApi


class TestGoogleFitApi(unittest.TestCase):
    def setUp(self):
        self.token = "test_token"
        self.google_fit = MagicMock()
        self.google_fit_api = GoogleFitApi(self.token)
        self.google_fit_api.fit = self.google_fit

    def test_get_sleeps_and_phases_by_time(self):
        self.google_fit.get_sleeps.return_value = [
            {"start_time": 1632430800, "end_time": 1632434400}]
        self.google_fit.get_sleep_phases.return_value = [
            {"phase": "deep", "duration": 100}]
        start_data_time = 1632430000
        end_data_time = 1632435000
        expected_result = [{"start_time": 1632430800, "end_time": 1632434400, "phases": [
            {"phase": "deep", "duration": 100}]}]
        actual_result = asyncio.run(self.google_fit_api.get_sleeps_and_phases_by_time(
            start_data_time, end_data_time))
        self.assertEqual(actual_result, expected_result)

    def test_get_steps_from_walks(self):
        self.google_fit.get_walks.return_value = [{"start_time": 1632340800, "end_time": 1632344400}]
        self.google_fit.get_steps.return_value = [{"value": [{"fpVal": 100.0}]}]
        expected_result = 100
        actual_result = asyncio.run(self.google_fit_api.get_steps_from_walks())
        self.assertEqual(actual_result, expected_result)

    def test_get_heights(self):
        self.google_fit.get_data_sources.return_value = [
            {"dataStreamId": "test_id"}]
        self.google_fit.get_data_point_changes.return_value = {
            "insertedDataPoint": [{"value": [{"fpVal": 1.75}]}]}
        expected_result = [{"value": 175}]
        actual_result = asyncio.run(self.google_fit_api.get_heights())
        self.assertEqual(actual_result, expected_result)

    def test_get_weights(self):
        self.google_fit.get_data_sources.return_value = [
            {"dataStreamId": "test_id"}]
        self.google_fit.get_data_point_changes.return_value = {"insertedDataPoint": [{"value": [{"fpVal": 70.0}]}]}
        expected_result = [{"value": 70}]
        actual_result = asyncio.run(self.google_fit_api.get_weights())
        self.assertEqual(actual_result, expected_result)
