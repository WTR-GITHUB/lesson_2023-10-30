import logging

def move_to_end(listas:list, a:int):
    new_list = []
    new_list.append(listas.pop(a-1))
    listas = listas + new_list
    logging.debug(new_list)
    logging.warning(listas)
    return listas

logging.basicConfig(level=logging.DEBUG, filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

my_list = [1, 3, 2, 4, 4, 1]
logging.info(my_list)
poz = 1

move_to_end(my_list, poz)

