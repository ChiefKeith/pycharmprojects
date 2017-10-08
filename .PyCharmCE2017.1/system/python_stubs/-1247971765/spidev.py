# encoding: utf-8
# module spidev
# from /usr/lib/python3/dist-packages/spidev.cpython-34m-arm-linux-gnueabihf.so
# by generator 1.145
"""
This module defines an object type that allows SPI transactions
on hosts running the Linux kernel. The host kernel must have SPI
support and SPI device interface support.
All of these can be either built-in to the kernel, or loaded from
modules.

Because the SPI device interface is opened R/W, users of this
module usually must have root permissions.
"""
# no imports

# no functions
# classes

class SpiDev(object):
    """
    SpiDev([bus],[client]) -> SPI
    
    Return a new SPI object that is (optionally) connected to the
    specified SPI device interface.
    """
    def close(self): # real signature unknown; restored from __doc__
        """
        close()
        
        Disconnects the object from the interface.
        """
        pass

    def fileno(self): # real signature unknown; restored from __doc__
        """
        fileno() -> integer "file descriptor"
        
        This is needed for lower-level file interfaces, such as os.read().
        """
        return 0

    def open(self, bus, device): # real signature unknown; restored from __doc__
        """
        open(bus, device)
        
        Connects the object to the specified SPI device.
        open(X,Y) will open /dev/spidev-X.Y
        """
        pass

    def readbytes(self, *args, **kwargs): # real signature unknown
        """
        read(len) -> [values]
        
        Read len bytes from SPI device.
        """
        pass

    def writebytes(self, *args, **kwargs): # real signature unknown
        """
        write([values]) -> None
        
        Write bytes to SPI device.
        """
        pass

    def xfer(self, values=None): # real signature unknown; restored from __doc__
        """
        xfer([values]) -> [values]
        
        Perform SPI transaction.
        CS will be released and reactivated between blocks.
        delay specifies delay in usec between blocks.
        """
        pass

    def xfer2(self, values=None): # real signature unknown; restored from __doc__
        """
        xfer2([values]) -> [values]
        
        Perform SPI transaction.
        CS will be held active between blocks.
        """
        pass

    def __init__(self, bus=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    bits_per_word = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """bits per word
"""

    cshigh = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """CS active high
"""

    loop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """loopback configuration
"""

    lsbfirst = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """LSB first
"""

    max_speed_hz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """maximum speed in Hz
"""

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """SPI mode as two bit pattern of 
Clock Polarity  and Phase [CPOL|CPHA]
min: 0b00 = 0 max: 0b11 = 3
"""

    threewire = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """SI/SO signals shared
"""



# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

