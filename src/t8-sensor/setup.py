from setuptools import setup

setup(name='t8-sensor',
      version='0.1',
      description='Sensor management for the Thalabor8 project (Private project)',
      author='T8 - Chris Doherty',
      author_email='chris.doherty4@gmail.com',
      packages=[
          'Sensor', 
          'Sensor.Simulator', 
          'Sensor.Simulator.PIRSimulatorStates',
          'Sensor.Simulator.SensorDevices'
      ],
      install_requires=['RPi.GPIO'],
      zip_safe=False)