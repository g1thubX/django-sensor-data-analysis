from django.test import TestCase

# Create your tests here.
import unittest
from myapp.models import SensorData

class SensorDataTestCase(unittest.TestCase):
    def setUp(self):
        self.sensor_data = SensorData.objects.create(
            topic='sensor/temperature',
            value='37.0',
            timestamp=1680343756
        )
    
    def test_sensor_data_saved_to_database(self):
        saved_sensor_data = SensorData.objects.get(pk=self.sensor_data.pk)
        self.assertEqual(saved_sensor_data.topic, 'sensor/temperature')
        self.assertEqual(saved_sensor_data.value, '37.0')
        self.assertEqual(saved_sensor_data.timestamp, 1680343756)
