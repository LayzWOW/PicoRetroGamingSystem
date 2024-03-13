class Resources:
    # Tunes
    WIN_TUNE = [
        (262, 4),
        (196, 8),
        (196, 8),
        (220, 4),
        (196, 4),
        (0, 4),
        (247, 4),
        (262, 4)
        ]
    
    GAME_OVER_TUNE = [
        (262, 4),
        (220, 4),
        (196, 4),
        (0, 4),
        (110, 2)
        ]
    
    
    # Sprites graphics definition
    A_0_W = 16    # width and height of the sprite in pixels
    A_0_H = 16
    A_0 = bytearray([
        0b01111111, 0b11111110,
        0b10000000, 0b00000001,
        0b10000000, 0b00000001,
        0b10000000, 0b00000001,
        0b10000000, 0b00000001,
        0b10000000, 0b00000001,
        0b10000000, 0b00000001,
        0b10000000, 0b00000001,
        0b10000000, 0b00000001,
        0b10000000, 0b00000001,
        0b10000000, 0b00000001,
        0b10000000, 0b00000001,
        0b10000000, 0b00000001,
        0b10000000, 0b00000001,
        0b10000000, 0b00000001,
        0b01111111, 0b11111110
        ])

    A_2_W = 16    # width and height of the sprite in pixels
    A_2_H = 16
    A_2 = bytearray([
        0b01111111, 0b11111110,
        0b10000000, 0b00000001,
        0b10000011, 0b11000001,
        0b10001111, 0b11110001,
        0b10011100, 0b00111001,
        0b10000000, 0b00111001,
        0b10000000, 0b00111001,
        0b10000011, 0b11111001,
        0b10000111, 0b11100001,
        0b10011100, 0b00000001,
        0b10011100, 0b00000001,
        0b10011111, 0b11111001,
        0b10011111, 0b11111001,
        0b10011111, 0b11111001,
        0b10000000, 0b00000001,
        0b01111111, 0b11111110
        ])

    A_4_W = 16    # width and height of the sprite in pixels
    A_4_H = 16
    A_4 = bytearray([
        0b01111111, 0b11111110,
        0b10000000, 0b00000001,
        0b10000001, 0b11110001,
        0b10000011, 0b11110001,
        0b10001110, 0b01110001,
        0b10011100, 0b01110001,
        0b10011100, 0b01110001,
        0b10011111, 0b11111001,
        0b10011111, 0b11111001,
        0b10000000, 0b01110001,
        0b10000000, 0b01110001,
        0b10000000, 0b11111001,
        0b10000000, 0b11111001,
        0b10000000, 0b11111001,
        0b10000000, 0b00000001,
        0b01111111, 0b11111110
        ])
    
    A_8_W = 16    # width and height of the sprite in pixels
    A_8_H = 16
    A_8 = bytearray([
        0b01111111, 0b11111110,
        0b10000000, 0b00000001,
        0b10001111, 0b11111001,
        0b10001111, 0b11111001,
        0b10001100, 0b00111001,
        0b10001100, 0b00111001,
        0b10011111, 0b11111001,
        0b10011111, 0b11111001,
        0b10011100, 0b00111001,
        0b10011100, 0b00111001,
        0b10011100, 0b00111001,
        0b10011111, 0b11111001,
        0b10011111, 0b11111001,
        0b10011111, 0b11111001,
        0b10000000, 0b00000001,
        0b01111111, 0b11111110
        ])
    
    A_16_W = 16    # width and height of the sprite in pixels
    A_16_H = 16
    A_16 = bytearray([
        0b01111111, 0b11111110,
        0b10000000, 0b00000001,
        0b10011000, 0b00000001,
        0b10011000, 0b00000001,
        0b10011000, 0b00000001,
        0b10011000, 0b00000001,
        0b10011000, 0b00000001,
        0b10011000, 0b11111001,
        0b10011001, 0b10001101,
        0b10000001, 0b10000001,
        0b10000001, 0b11111101,
        0b10000001, 0b10001101,
        0b10000001, 0b11111101,
        0b10000000, 0b11111001,
        0b10000000, 0b00000001,
        0b01111111, 0b11111110
        ])
    A_32_W = 16    # width and height of the sprite in pixels
    A_32_H = 16
    A_32 = bytearray([
        0b01111111, 0b11111110,
        0b10000000, 0b00000001,
        0b10111110, 0b00000001,
        0b10000110, 0b00000001,
        0b10011110, 0b00000001,
        0b10000110, 0b00000001,
        0b10000110, 0b00000001,
        0b10111110, 0b01111001,
        0b10111110, 0b11001101,
        0b10000000, 0b00011101,
        0b10000000, 0b00111001,
        0b10000000, 0b11100001,
        0b10000000, 0b11111101,
        0b10000000, 0b11111101,
        0b10000000, 0b00000001,
        0b01111111, 0b11111110
        ])
    A_64_W = 16    # width and height of the sprite in pixels
    A_64_H = 16
    A_64 = bytearray([
        0b01111111, 0b11111110,
        0b10000000, 0b00000001,
        0b10011110, 0b00000001,
        0b10110011, 0b00000001,
        0b10110000, 0b00000001,
        0b10111111, 0b00000001,
        0b10110011, 0b00000001,
        0b10011111, 0b00000001,
        0b10000000, 0b00111101,
        0b10000000, 0b01101101,
        0b10000000, 0b11001101,
        0b10000000, 0b11111101,
        0b10000000, 0b00001101,
        0b10000000, 0b00001101,
        0b10000000, 0b00000001,
        0b01111111, 0b11111110
        ])
    A_128_W = 16    # width and height of the sprite in pixels
    A_128_H = 16
    A_128 = bytearray([
        0b01111111, 0b11111110,
        0b10000000, 0b00000001,
        0b10110000, 0b00000001,
        0b10110000, 0b00000001,
        0b10110000, 0b00000001,
        0b10110000, 0b00000001,
        0b10110111, 0b10000001,
        0b10000001, 0b10000001,
        0b10000111, 0b10000001,
        0b10000110, 0b00011101,
        0b10000111, 0b10010101,
        0b10000000, 0b00111101,
        0b10000000, 0b00100101,
        0b10000000, 0b00111101,
        0b10000000, 0b00000001,
        0b01111111, 0b11111110
        ])
    A_256_W = 16    # width and height of the sprite in pixels
    A_256_H = 16
    A_256 = bytearray([
        0b01111111, 0b11111110,
        0b10000000, 0b00000001,
        0b10111000, 0b00000001,
        0b10001000, 0b00000001,
        0b10111000, 0b00000001,
        0b10100000, 0b00000001,
        0b10111011, 0b10000001,
        0b10000010, 0b00000001,
        0b10000011, 0b10000001,
        0b10000000, 0b10100001,
        0b10000011, 0b10100001,
        0b10000000, 0b00111001,
        0b10000000, 0b00101001,
        0b10000000, 0b00111001,
        0b10000000, 0b00000001,
        0b01111111, 0b11111110
        ])
    A_512_W = 16    # width and height of the sprite in pixels
    A_512_H = 16
    A_512 = bytearray([
        0b01111111, 0b11111110,
        0b10000000, 0b00000001,
        0b10111100, 0b00000001,
        0b10110000, 0b00000001,
        0b10111100, 0b00000001,
        0b10001101, 0b10000001,
        0b10111101, 0b10000001,
        0b10111101, 0b10000001,
        0b10000001, 0b10111101,
        0b10000001, 0b10001101,
        0b10000001, 0b10111101,
        0b10000000, 0b00110001,
        0b10000000, 0b00111101,
        0b10000000, 0b00111101,
        0b10000000, 0b00000001,
        0b01111111, 0b11111110
        ])
    A_1024_W = 16    # width and height of the sprite in pixels
    A_1024_H = 16
    A_1024 = bytearray([
        0b01111111, 0b11111110,
        0b10000000, 0b00000001,
        0b10011100, 0b00000001,
        0b10111100, 0b00000001,
        0b10011100, 0b00000001,
        0b10011100, 0b00000001,
        0b10011100, 0b00000001,
        0b10111110, 0b11001101,
        0b10111110, 0b11001101,
        0b10000000, 0b11011001,
        0b10000000, 0b11110001,
        0b10000000, 0b11011001,
        0b10000000, 0b11001101,
        0b10000000, 0b11001101,
        0b10000000, 0b00000001,
        0b01111111, 0b11111110
        ])
    A_2048_W = 16    # width and height of the sprite in pixels
    A_2048_H = 16
    A_2048 = bytearray([
        0b01111111, 0b11111110,
        0b10000000, 0b00000001,
        0b10011100, 0b00000001,
        0b10100110, 0b00000001,
        0b10000110, 0b00000001,
        0b10011100, 0b00000001,
        0b10110000, 0b00000001,
        0b10111110, 0b11001101,
        0b10111110, 0b11001101,
        0b10000000, 0b11011001,
        0b10000000, 0b11110001,
        0b10000000, 0b11011001,
        0b10000000, 0b11001101,
        0b10000000, 0b11001101,
        0b10000000, 0b00000001,
        0b01111111, 0b11111110
        ])
