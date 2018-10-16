# coding: utf-8
import numpy as np
import console

def main():
	data = np.zeros(0)
	
	cope = input("スペース区切りで入力するときはyを、一つづつ入力する時は適当に入力してください:")
	
	if(cope == 'y'):
		list = [float(i) for i in input('>').split()]
		array = np.array(list)
		data = np.append(data,array)
	else:	
		while True:
			line = input('>')
			if line == '':
				break
			else:
				line = float(line)
				data = np.append(data,line)
		
	print(data)
	p = np.std(data)
	q = float(data.size)
	print ("要素数:%s" % int(q))
	print("平均:%s" % np.mean(data))
	print("標準偏差:%s" % p)
	q = np.sqrt(int(q)-1)
	r = p/q
	print("標準誤差:%s" % r)
	
	
if __name__ == '__main__':
    main()
