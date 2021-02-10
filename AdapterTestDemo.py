import RPi.GPIO as gp
import os
import time

gp.setwarnings(False)
gp.setmode(gp.BOARD)

gp.setup(7, gp.OUT)
gp.setup(11, gp.OUT)
gp.setup(12, gp.OUT)

gp.setup(15, gp.OUT)
gp.setup(16, gp.OUT)
gp.setup(21, gp.OUT)
gp.setup(22, gp.OUT)

gp.output(11, True)
gp.output(12, True)
gp.output(15, True)
gp.output(16, True)
gp.output(21, True)
gp.output(22, True)

def main():
    times = []
    time1 = time.perf_counter()
    i2c = "i2cset -y 1 0x70 0x00 0x04"
    os.system(i2c)
    time2 = time.perf_counter()
    times.append(time2 - time1)
    time1 = time.perf_counter()
    gp.output(7, False)
    time2 = time.perf_counter()
    times.append(time2 - time1)
    time1 = time.perf_counter()
    gp.output(11, False)
    time2 = time.perf_counter()
    times.append(time2 - time1)
    time1 = time.perf_counter()
    gp.output(12, True)
    time2 = time.perf_counter()
    times.append(time2 - time1)
    time1 = time.perf_counter()
    capture(1)
    time2 = time.perf_counter()
    times.append(time2 - time1)
    i2c = "i2cset -y 1 0x70 0x00 0x05"
    os.system(i2c)
    gp.output(7, True)
    gp.output(11, False)
    gp.output(12, True)
    capture(2)
    i2c = "i2cset -y 1 0x70 0x00 0x06"
    os.system(i2c)
    gp.output(7, False)
    gp.output(11, True)
    gp.output(12, False)
    capture(3)
    i2c = "i2cset -y 1 0x70 0x00 0x07"
    os.system(i2c)
    gp.output(7, True)
    gp.output(11, True)
    gp.output(12, False)
    capture(4)
    print("os: " + times[0])
    print("gp7: " + times[1])
    print("gp11: " + times[2])
    print("gp12: " + times[3])
    print("cap: " + times[4])

def capture(cam):
    cmd = "raspistill -o capture_%d.jpg" % cam
    os.system(cmd)

if __name__ == "__main__":
    main()

    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)
