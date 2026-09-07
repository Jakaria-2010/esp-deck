import board
import busio

spi = busio.SPI(
    clock=board.GPIO12,
    MOSI=board.GPIO11,
    MISO=board.GPIO13
)