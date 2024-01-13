from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
import json
import os
from pathlib import Path

class TestFizzBuzz(APITestCase):

    base_dir = Path(__file__).resolve().parent
    test_data_json_file = os.path.join(base_dir, 'test_data.json')
    f = open(test_data_json_file) 
    test_data = json.load(f)

    def test_validation_check_of_request_parameters_missing_field(self):
        parameter = self.test_data["test_1_data"]
        desired_output = self.test_data["test_1_desired_output"]
        response = self.client.get(reverse('fizzbuzz'),parameter)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data,desired_output)
    
    def test_fizzbuzz_validation_check_of_request_parameters_type(self):
        parameter = self.test_data["test_2_data"]
        desired_output = self.test_data["test_2_desired_output"]
        response = self.client.get(reverse('fizzbuzz'),parameter)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data,desired_output)


    def test_fizzbuzz_success(self):
        parameter = self.test_data["test_3_data"]
        desired_output = self.test_data["test_3_desired_output"]
        response = self.client.get(reverse('fizzbuzz'),parameter)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data,desired_output)

    def test_statistics_success(self):
        test_parameters = self.test_data["test_4_data"]
        for par in test_parameters:
            self.client.get(reverse('fizzbuzz'),par)
        desired_output = self.test_data["test_4_desired_output"]
        response = self.client.get(reverse('statistics'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(list(response.data["max_used_parameter"]),desired_output["max_used_parameter"])


