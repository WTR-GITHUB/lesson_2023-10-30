import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


number = input(f"Enter a number: ")
if number.isnumeric():
    logging.info(f"The number '{number}' is integer.")
else:
    logging.error(f"The number '{number}' is not integer.")