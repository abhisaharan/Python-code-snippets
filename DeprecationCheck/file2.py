"""
import address as address

import lib.base as libBase

class A(libBase):
    def __init__(self, testInstance):
        super(A, self).__init__(testInstance)

    def method1(self):
        self.dut.whatever.call()

    def method2(self):
        if 3>4:
            self.dm3.DeviceContext(self.dut, some)
        else:
            self.dm3.DeviceContext(self.dut, some)

    def method3(self):
        return self.dut.Power.On()
"""

