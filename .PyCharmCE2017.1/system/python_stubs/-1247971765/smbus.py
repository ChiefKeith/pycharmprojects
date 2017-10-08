# encoding: utf-8
# module smbus calls itself SMBus
# from /usr/lib/python3/dist-packages/smbus.cpython-34m-arm-linux-gnueabihf.so
# by generator 1.145
"""
This module defines an object type that allows SMBus transactions
on hosts running the Linux kernel.  The host kernel must have I2C
support, I2C device interface support, and a bus adapter driver.
All of these can be either built-in to the kernel, or loaded from
modules.

Because the I2C device interface is opened R/W, users of this
module usually must have root permissions.
"""
# no imports

# no functions
# classes

class SMBus(object):
    """
    SMBus([bus]) -> SMBus
    
    Return a new SMBus object that is (optionally) connected to the
    specified I2C device interface.
    """
    def block_process_call(self, addr, cmd, vals=None): # real signature unknown; restored from __doc__
        """
        block_process_call(addr, cmd, [vals]) -> results
        
        Perform SMBus Block Process Call transaction.
        """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """
        close()
        
        Disconnects the object from the bus.
        """
        pass

    def open(self, bus): # real signature unknown; restored from __doc__
        """
        open(bus)
        
        Connects the object to the specified SMBus.
        """
        pass

    def process_call(self, addr, cmd, val): # real signature unknown; restored from __doc__
        """
        process_call(addr, cmd, val)
        
        Perform SMBus Process Call transaction.
        """
        pass

    def read_block_data(self, addr, cmd): # real signature unknown; restored from __doc__
        """
        read_block_data(addr, cmd) -> results
        
        Perform SMBus Read Block Data transaction.
        """
        pass

    def read_byte(self, addr): # real signature unknown; restored from __doc__
        """
        read_byte(addr) -> result
        
        Perform SMBus Read Byte transaction.
        """
        pass

    def read_byte_data(self, addr, cmd): # real signature unknown; restored from __doc__
        """
        read_byte_data(addr, cmd) -> result
        
        Perform SMBus Read Byte Data transaction.
        """
        pass

    def read_i2c_block_data(self, addr, cmd, len=32): # real signature unknown; restored from __doc__
        """
        read_i2c_block_data(addr, cmd, len=32) -> results
        
        Perform I2C Block Read transaction.
        """
        pass

    def read_word_data(self, addr, cmd): # real signature unknown; restored from __doc__
        """
        read_word_data(addr, cmd) -> result
        
        Perform SMBus Read Word Data transaction.
        """
        pass

    def write_block_data(self, addr, cmd, vals=None): # real signature unknown; restored from __doc__
        """
        write_block_data(addr, cmd, [vals])
        
        Perform SMBus Write Block Data transaction.
        """
        pass

    def write_byte(self, addr, val): # real signature unknown; restored from __doc__
        """
        write_byte(addr, val)
        
        Perform SMBus Write Byte transaction.
        """
        pass

    def write_byte_data(self, addr, cmd, val): # real signature unknown; restored from __doc__
        """
        write_byte_data(addr, cmd, val)
        
        Perform SMBus Write Byte Data transaction.
        """
        pass

    def write_i2c_block_data(self, addr, cmd, vals=None): # real signature unknown; restored from __doc__
        """
        write_i2c_block_data(addr, cmd, [vals])
        
        Perform I2C Block Write transaction.
        """
        pass

    def write_quick(self, addr): # real signature unknown; restored from __doc__
        """
        write_quick(addr)
        
        Perform SMBus Quick transaction.
        """
        pass

    def write_word_data(self, addr, cmd, val): # real signature unknown; restored from __doc__
        """
        write_word_data(addr, cmd, val)
        
        Perform SMBus Write Word Data transaction.
        """
        pass

    def __init__(self, bus=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    pec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if Packet Error Codes (PEC) are enabled"""



# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

