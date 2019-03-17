#!/usr/bin/python
import spi_serial
s = spi_serial.SpiSerial()
s.reset()
s.write([8,1,1])
s.write([8,0,1])
