# encoding: utf-8
# module RTIMU
# from /usr/lib/python3/dist-packages/RTIMU.cpython-34m-arm-linux-gnueabihf.so
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class RTHumidity(object):
    """ RTIMU.RTHumidity object """
    def humidityInit(self, *args, **kwargs): # real signature unknown
        """ Set up the humidity sensor """
        pass

    def humidityName(self, *args, **kwargs): # real signature unknown
        """ Get the name of the humidity sensor """
        pass

    def humidityRead(self, *args, **kwargs): # real signature unknown
        """ Get current values """
        pass

    def humidityType(self, *args, **kwargs): # real signature unknown
        """ Get the type code of the humidity sensor """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class RTIMU(object):
    """ RTIMU.RTIMU object """
    def getAccel(self, *args, **kwargs): # real signature unknown
        """ Return the accel readings """
        pass

    def getAccelCalibrationValid(self, *args, **kwargs): # real signature unknown
        """ Return true if the compass is using ellipsoid calibration """
        pass

    def getAccelResiduals(self, *args, **kwargs): # real signature unknown
        """ Return the accel residual readings """
        pass

    def getCompass(self, *args, **kwargs): # real signature unknown
        """ Return the compass readings """
        pass

    def getCompassCalibrationEllipsoidValid(self, *args, **kwargs): # real signature unknown
        """ Return true if the compass is using ellipsoid calibration """
        pass

    def getCompassCalibrationValid(self, *args, **kwargs): # real signature unknown
        """ Return true if the compass is using min/max calibration """
        pass

    def getFusionData(self, *args, **kwargs): # real signature unknown
        """ Return true if valid bias """
        pass

    def getGyro(self, *args, **kwargs): # real signature unknown
        """ Return the gyro readings """
        pass

    def getIMUData(self, *args, **kwargs): # real signature unknown
        """ Return true if valid bias """
        pass

    def getMeasuredPose(self, *args, **kwargs): # real signature unknown
        """ Return the measured pose """
        pass

    def getMeasuredQPose(self, *args, **kwargs): # real signature unknown
        """ Return the measured QPose """
        pass

    def IMUGetPollInterval(self, *args, **kwargs): # real signature unknown
        """ Get the recommended poll interval in mS """
        pass

    def IMUGyroBiasValid(self, *args, **kwargs): # real signature unknown
        """ Return true if valid bias """
        pass

    def IMUInit(self, *args, **kwargs): # real signature unknown
        """ Set up the IMU """
        pass

    def IMUName(self, *args, **kwargs): # real signature unknown
        """ Get the name of the IMU """
        pass

    def IMURead(self, *args, **kwargs): # real signature unknown
        """ Get a sample """
        pass

    def IMUType(self, *args, **kwargs): # real signature unknown
        """ Get the type code of the IMU """
        pass

    def resetFusion(self, *args, **kwargs): # real signature unknown
        """ Return true if valid bias """
        pass

    def setAccelCalibrationMode(self, *args, **kwargs): # real signature unknown
        """ Turn on accel calibration mode """
        pass

    def setAccelEnable(self, *args, **kwargs): # real signature unknown
        """ Enable or disable the Accelerometer reading """
        pass

    def setCompassCalibrationMode(self, *args, **kwargs): # real signature unknown
        """ Turn on compass calibration mode """
        pass

    def setCompassEnable(self, *args, **kwargs): # real signature unknown
        """ Enable or disable the Compass reading """
        pass

    def setExtIMUData(self, *args, **kwargs): # real signature unknown
        """ Inject data from external IMU """
        pass

    def setGyroEnable(self, *args, **kwargs): # real signature unknown
        """ Enable or disable Gyro reading """
        pass

    def setSlerpPower(self, *args, **kwargs): # real signature unknown
        """ Enable or disable Gyro reading """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class RTPressure(object):
    """ RTIMU.RTPressure object """
    def pressureInit(self, *args, **kwargs): # real signature unknown
        """ Set up the pressure sensor """
        pass

    def pressureName(self, *args, **kwargs): # real signature unknown
        """ Get the name of the pressure sensor """
        pass

    def pressureRead(self, *args, **kwargs): # real signature unknown
        """ Get current values """
        pass

    def pressureType(self, *args, **kwargs): # real signature unknown
        """ Get the type code of the pressure sensor """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class Settings(object):
    """ RTIMU.Settings object """
    def discoverIMU(self, *args, **kwargs): # real signature unknown
        """ Try do discover and auto-set a connected IMU """
        pass

    def load(self, *args, **kwargs): # real signature unknown
        """ Load settings from a file """
        pass

    def save(self, *args, **kwargs): # real signature unknown
        """ Save settings to a file """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    AccelCalMax = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AccelCalMin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    AccelCalValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CompassCalEllipsoidCorr11 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CompassCalEllipsoidCorr12 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CompassCalEllipsoidCorr13 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CompassCalEllipsoidCorr21 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CompassCalEllipsoidCorr22 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CompassCalEllipsoidCorr23 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CompassCalEllipsoidCorr31 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CompassCalEllipsoidCorr32 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CompassCalEllipsoidCorr33 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CompassCalEllipsoidOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CompassCalEllipsoidValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CompassCalMax = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CompassCalMin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CompassCalValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    FusionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    GD20HM303DAccelFsr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    GD20HM303DAccelLpf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    GD20HM303DAccelSampleRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    GD20HM303DCompassFsr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    GD20HM303DCompassSampleRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    GD20HM303DGyroBW = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    GD20HM303DGyroFsr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    GD20HM303DGyroHpf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    GD20HM303DGyroSampleRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    GD20HM303DLHCAccelFsr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    GD20HM303DLHCAccelSampleRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    GD20HM303DLHCCompassFsr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    GD20HM303DLHCCompassSampleRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    GD20HM303DLHCGyroBW = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    GD20HM303DLHCGyroFsr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    GD20HM303DLHCGyroHpf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    GD20HM303DLHCGyroSampleRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    GD20M303DLHCAccelFsr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    GD20M303DLHCAccelSampleRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    GD20M303DLHCCompassFsr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    GD20M303DLHCCompassSampleRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    GD20M303DLHCGyroBW = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    GD20M303DLHCGyroFsr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    GD20M303DLHCGyroHpf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    GD20M303DLHCGyroSampleRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    GyroBias = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    GyroBiasValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    I2CAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    I2CBus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IMUType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    LSM9DS0AccelFsr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    LSM9DS0AccelLpf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    LSM9DS0AccelSampleRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    LSM9DS0CompassFsr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    LSM9DS0CompassSampleRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    LSM9DS0GyroBW = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    LSM9DS0GyroFsr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    LSM9DS0GyroHpf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    LSM9DS0GyroSampleRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    LSM9DS1AccelFsr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    LSM9DS1AccelLpf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    LSM9DS1AccelSampleRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    LSM9DS1CompassFsr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    LSM9DS1CompassSampleRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    LSM9DS1GyroBW = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    LSM9DS1GyroFsr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    LSM9DS1GyroHpf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    LSM9DS1GyroSampleRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    MPU9150AccelFsr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    MPU9150CompassSampleRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    MPU9150GyroAccelLpf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    MPU9150GyroAccelSampleRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    MPU9150GyroFst = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    MPU9250AccelFsr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    MPU9250AccelLpf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    MPU9250CompassSampleRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    MPU9250GyroAccelSampleRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    MPU9250GyroFsr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    MPU9250GyroLpf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

