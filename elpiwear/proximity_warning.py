import Edison.i2c as I2C
import sharp2y0a21
import ads1015
import time
import thread

class proximity_warning:

    def __init__(self, sensorid, calibration, sensing_freq):
        self.sensing_freq = sensing_freq
        self.warning = []
        adc = ads1015.ads1015(I2C.i2c(1,0x48))
        adc.setchannel(sensorid, True)
        adc.setdatarate(ads1015.ADS1015_DR_128SPS)
        self.sensor = sharp2y0a21.sharp2y0a21(adc)
        self.sensor.loadcalibration(calibration)

    def add_warning(self, distance, warning):
        self.warning.append({'distance':distance, 'warning':warning})
        self.warning = sorted(self.warning, key=lambda k: k['distance'])

    def start(self):
        self.stop_flag = False
        self.thread = thread.start_new_thread( self.sensing_thread, () )

    def stop(self):
        self.stop_flag = True

    def detect_warning(self, distance):
        for warn in self.warnings:
            if distance < warn['distance']:
                return warn['warning']
        return None

    def sensing_thread(self):
        while not self.stop_flag:
            dist = self.sensor.distance()
            warn = self.detect_warning(dist)
            if warn is not None:
                warn(dist)

            time.sleep(self.sensing_freq)
