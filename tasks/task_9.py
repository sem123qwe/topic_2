byte_size: int = 1234567890  
kilo_size: float = int(byte_size) / 1024
mega_size: float = int(kilo_size) / 1024
giga_size: float = int(mega_size) / 1024

print(' Размер в байтах: ', byte_size, '\n' ' Размер в килобайтах: ', kilo_size, '\n' ' Размер в мегабайтах: ', mega_size, '\n' ' Размер в гигобайтах: ', giga_size )  # допишите код

# TODO: Необходимо улучшить
