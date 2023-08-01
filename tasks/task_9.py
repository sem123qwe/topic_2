byte_size: int = 1234567890  
kilo_size: float = int(byte_size) / 1024  # здесь Ваш код
mega_size: float = int(kilo_size) / 1024 # здесь Ваш код
giga_size: float = int(mega_size) / 1024 # здесь Ваш код

print(' Размер в байтах: ', byte_size, '\n' ' Размер в килобайтах: ', kilo_size, '\n' ' Размер в мегабайтах: ', mega_size, '\n' ' Размер в гигобайтах: ', giga_size )  # допишите код
