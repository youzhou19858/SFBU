from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, barcode: str = '', productName: str = '') -> None:
        super().__init__()
        self.__barcode = barcode
        self.__productName = productName

    @abstractmethod
    def scanner(self) -> None:
        pass

    @abstractmethod
    def printer(self) -> None:
        pass


class PrepackedFood(Product):
    def __init__(self, barcode: str = '', productName: str = '', unitPrice: float = 0.0) -> None:
        super().__init__(barcode, productName)
        self.__unitPrice = unitPrice

    def scanner(self) -> None:
        while True:
            try:
                op: int = int(input(
                    'Please choose one of the attributes?\n1.Barcode\n2.Product Name\n3.Unit Price\nPlease enter 1/2/3:'))
                if op == 1:
                    self.__barcode = input('Please enter the barcode: ')
                    break
                elif op == 2:
                    self.__productName = input(
                        'Please enter the product name: ')
                    break
                elif op == 3:
                    while True:
                        try:
                            self.__unitPrice = float(
                                input('Please enter the unit price: '))
                            if (self.__unitPrice <= 0):
                                raise ValueError
                            break
                        except ValueError:
                            print('Please enter a valid positive float number.')
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Please enter valid digit only -- 1/2/3')

    def printer(self) -> None:
        while True:
            try:
                op: int = int(input(
                    'Please choose one of the attributes?\n1.Barcode\n2.Product Name\n3.Unit Price\nPlease enter 1/2/3:'))
                if op == 1:
                    print(f'Barcode: {self.__barcode}')
                    break
                elif op == 2:
                    print(f'Product Name: {self.__productName}')
                    break
                elif op == 3:
                    print(f'Unit Price: {self.__unitPrice}')
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Please enter valid digit only -- 1/2/3')


class FreshFood(Product):
    def __init__(self, barcode: str = '', productName: str = '', weight: float = 0.0, pricePerKg: float = 0.0) -> None:
        super().__init__(barcode, productName)
        self.__weight = weight
        self.__pricePerKg = pricePerKg

    def scanner(self) -> None:
        while True:
            try:
                op: int = int(input(
                    'Please choose one of the attributes?\n1.Barcode\n2.Product Name\n3.weight\n4.price per kilogram\nPlease enter 1/2/3/4:'))
                if op == 1:
                    self.__barcode = input('Please enter the barcode: ')
                    break
                elif op == 2:
                    self.__productName = input(
                        'Please enter the product name: ')
                    break
                elif op == 3:
                    while True:
                        try:
                            self.__weight = float(
                                input('Please enter the weight: '))
                            if (self.__weight <= 0):
                                raise ValueError
                            break
                        except ValueError:
                            print('Please enter a valid positive float number.')
                    break
                elif op == 4:
                    while True:
                        try:
                            self.__pricePerKg = float(
                                input('Please enter the price per kilogram: '))
                            if (self.__pricePerKg <= 0):
                                raise ValueError
                            break
                        except ValueError:
                            print('Please enter a valid positive float number.')
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Please enter valid digit only -- 1/2/3/4')

    def printer(self) -> None:
        while True:
            try:
                op: int = int(input(
                    'Please choose one of the attributes?\n1.Barcode\n2.Product Name\n3.weight\n4.Price per Kilogram\nPlease enter 1/2/3/4:'))
                if op == 1:
                    print(f'Barcode: {self.__barcode}')
                    break
                elif op == 2:
                    print(f'Product Name: {self.__productName}')
                    break
                elif op == 3:
                    print(f'Weight: {self.__weight}')
                    break
                elif op == 4:
                    print(f'Price per Kilogram: {self.__pricePerKg}')
                else:
                    raise ValueError
            except ValueError:
                print('Please enter valid digit only -- 1/2/3')


if __name__ == '__main__':
    p1: PrepackedFood = PrepackedFood('1', 'p1', 10.0)
    p2: PrepackedFood = PrepackedFood()
    print('Let\'s set uninitialized p2.')
    while True:
        p2.scanner()
        if input('Do you want to set any other attributes? (Y/N): ').strip().lower() == 'n':
            break
    print('let\'s get set p2.')
    while True:
        p2.printer()
        if input('Do you want to get any other attributes? (Y/N): ').strip().lower() == 'n':
            break
    p3: FreshFood = FreshFood('1', 'p3', 10.0)
    p4: FreshFood = FreshFood()
    print('Let\'s set uninitialized p4.')
    while True:
        p4.scanner()
        if input('Do you want to set any other attributes? (Y/N): ').strip().lower() == 'n':
            break
    print('let\'s get set p4.')
    while True:
        p4.printer()
        if input('Do you want to get any other attributes? (Y/N): ').strip().lower() == 'n':
            break
