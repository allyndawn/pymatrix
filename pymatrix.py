import sys
import time

from rgbmatrix import RGBMatrix, RGBMatrixOptions

if __name__ == "__main__":
    options = RGBMatrixOptions()
    # See https://github.com/hzeller/rpi-rgb-led-matrix/blob/master/bindings/python/samples/samplebase.py
    options.rows = 32
    options.cols = 64
    options.chain_length = 1
    options.parallel = 1
    options.hardware_mapping = 'regular'
    options.gpio_slowdown = 2
    options.disable_hardware_pulsing = True

    matrix = RGBMatrix(options = options)

    try:
        print("Press CTRL-C to stop")
        matrix.SetPixel(4, 4, 100, 100, 100)

        while True:
            time.sleep(100)

    except KeyboardInterrupt:
        print("Done")
        sys.exit(0)