"""
import address.state.city
from address import state as state

from lib import libBase as MistBase

class A(MistBase):
    def __init__(self, testInstance):
        super(A, self).__init__(testInstance)

    def method1(self):
        return self.dm3.DeviceContext(self.testInstance.dut, whatever)

    def method2(self):
        self.dut.Power.Off()
        self.dm3.Context(self.dut, something1)
        self.dm3.Context(self.dut, something2)
"""
