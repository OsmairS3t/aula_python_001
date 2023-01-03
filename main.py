
from datetime import date
import math as matematica
import matplotlib.pyplot as plt
def unpacking_experiment(*args):
	arg1 = args[0]
	arg2 = args[1]
	outroArg = args[2:]
	print(arg1)
	print(arg2)
	print(outroArg)

def unpacking(**kargs):
    print(kargs)

def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    #unpacking_experiment(1,2,3,4,5,6,7,8,9)
    #unpacking(named="Teste", other="Outro nome")
    #raiz = matematica.sqrt(20)
    #print(raiz)

	x = [1,2,3,4]
	y = [1,2,3,4]
	plt.plot(x,y);
	plt.show()


