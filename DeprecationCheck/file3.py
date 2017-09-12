"""
import address as address
from address.city import city as city
from lib.base import base as libBase

class A(object):
    def __init__(self, *args, **kw):
        super(A, self).__init__(*args, **kw)

    def method1(self):
        self.dut.whatever.call()

    def method2(self):
        if 3>4:
            self.dm3.DeviceContext(self.dut, some)
        else:
            self.dm3.DeviceContext(self.testInstance.dut, some)

    def method3(self):
        return self.testInstance.dut.Power.On()
"""

