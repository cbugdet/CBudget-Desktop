import random
import string

def alpha_numeric_symbol_uid(length, ulm='lower'):
	''' \n\nreturns a unique identifier alpha-numeric string based on the length given. \nMax value for param length is 2048
		ulm stands for upper_lower_mixed case '''
	if ulm == 'mixed': a=string.ascii_letters
	if ulm == 'upper': a=string.ascii_uppercase
	if ulm == 'lower': a=string.ascii_lowercase
	a*=30
	s=string.punctuation
	s*=100
	n=range(10)
	n*=100
	n=[str(elem) for elem in n]
	n=''.join(n)
	n=n+a+s
	#print 'len(n):', len(n)
	return ''.join(random.sample(n, length))

def alpha_numeric_uid(length, ulm='lower'):
	''' \n\nreturns a unique identifier alpha-numeric string based on the length given. \nMax value for param length is 2048'''
	if ulm == 'mixed': a=string.ascii_letters
	if ulm == 'upper': a=string.ascii_uppercase
	if ulm == 'lower': a=string.ascii_lowercase
	a*=20
	a+=a[0:8]
	n=range(10)
	n*=100
	n=[str(elem) for elem in n]
	n=''.join(n)
	n+=a
	return ''.join(random.sample(n, length))
	
def alpha_uid(length, ulm='lower'):
	''' \n\nreturns a unique identifier alpha-only string based on the length given. \nMax value for param length is 2080'''
	if ulm == 'mixed': a=string.ascii_letters
	if ulm == 'upper': a=string.ascii_uppercase
	if ulm == 'lower': a=string.ascii_lowercase
	a*=40
	a+=a[0:8]
	return ''.join(random.sample(a, length))
	
def numeric_uid(length):
	''' \n\nreturns a unique identifier numeric-only string based on the length given. \nMax value for param length is 2080'''
	n=range(10)
	n*=208
	n=[str(elem) for elem in n]
	n=''.join(n)
	return ''.join(random.sample(n, length))
	
def make_uid_list(key_length, list_length, func, case='lower', save_to_file=False):
	''' Returns a list of len(list_length) uids based on the key_length for each uid.
	If save_to_file is true, asks for a file path and appends uid list to the file)'''
	uids=[]
	for i in range(int(list_length)): uids.append(func(key_length,case))
	if save_to_file: 
		file_location = raw_input('Enter the file location: ')
		try: 
			with open(file_location, 'a') as u:
				for i in uids: 
					u.write(','+i+'\n')
		except IOError as message: print message
	return uids

def test_uniqueness(strlen, num_uids, func): 
	uids = []
	for i in range(num_uids):
		uids.append(func(strlen))
	print (len(set(uids))/float(len(uids)))*100,'% uids are unique out of {0}'.format(num_uids)
	
def test_symbol_quantity(strlen, num_uids):
	has_sym = []
	add = ''
	sym = False
	for i in range(num_uids):
		add=alpha_numeric_symbol_uid(strlen)
		sym = False
		for a in add:
			if not a.isalnum(): sym = True
		if sym: has_sym.append(add)
	print (len(has_sym)/float(num_uids))*100.0,'% of uids with a length of {0} have symbols out of {1}'.format(strlen, num_uids)


if __name__ == '__main__':
	print alpha_numeric_symbol_uid(8)
	print alpha_numeric_symbol_uid(64)
	print alpha_numeric_symbol_uid(64,'upper')
	print alpha_numeric_symbol_uid(64,'mixed'), '\n'
	print alpha_numeric_uid(64)
	print alpha_numeric_uid(64,'upper')
	print alpha_numeric_uid(64,'mixed'), '\n'
	print alpha_uid(64)
	print alpha_uid(64,'upper')
	print alpha_uid(64,'mixed'), '\n'
	print numeric_uid(64)
	raw_input()
	
anu = alpha_numeric_uid