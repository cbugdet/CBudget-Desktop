from datetime import *
import os
import sys
import shutil
import pickle
import re
import hashlib
from random import sample
import time
import threading
try: import wx
except Exception as message: print '\n',str(message.__class__)+':',str(message),'\n'
import ctypes
from make_uid import alpha_numeric_uid
import base64
try: app=wx.App(0)
except Exception as message: print '\n',str(message.__class__)+':',str(message),'\n'

class initialize():
	userList = []
	if os.name == 'nt': savedir = str(os.environ['APPDATA']+'\\CBudget\\')
	else: savedir = str(os.environ['HOME']+'/CBudget/')
	savefile = 'users.cbp'

	def addUser(self, name):
		self.userList.append(user(name))

	def removeUser(self, name):
		self.userList = [u for u in self.userList if name != u.name]

	def changeUser(self, name, password):
		self.userList[0] = user(name)
		self.userList[0].password = password

	def load(self):
		# print '\nin load...'
		# test_connect = self.test_connection_load()
		# mac_network_drives = test_connect[1]
		# # test_mac_connect = test_connect[2]
		# try:
			# if test_connect[0]: 
				# if os.name == 'nt': 
					# try: 
						# p = os.path.getmtime(self.savedir+self.savefile)
						# m = os.path.getmtime(mac_network_drives[test_mac_connect])
						# print 'p > m:', p > m
						# if p > m:
							# with open(mac_network_drives[test_mac_connect]) as f: self.userList = pickle.loads(base64.b64decode(f.read()))
						# else: 
							# with open(self.savedir+self.savefile) as f: self.userList = pickle.loads(base64.b64decode(f.read()))
					# except Exception as message: print '\nin load -> in test_connect for \'nt\'...',str(message.__class__)+':',str(message),'\n'
				# if os.name != 'nt': 
					# try:
						# os.system('osascript -e \'mount volume "smb://cary-pc.att.net;cary:M1ll3nIyouM@cary-pc/users/"\'')
						# m = os.path.getmtime(self.savedir+self.savefile)
						# p = os.path.getmtime('/volumes/users/cary/appdata/roaming/cbudget/users.cbp')
						# print 'm > p:', m > p
						# if m > p:
							# with open('/volumes/users/cary/appdata/roaming/cbudget/users.cbp') as f: self.userList = pickle.loads(base64.b64decode(f.read()))
						# else: 
							# with open(self.savedir+self.savefile) as f: self.userList = pickle.loads(base64.b64decode(f.read()))
						# print 'self.userList[0].s.mount_mac_volume:', self.userList[0].s.mount_mac_volume
					# except Exception as message: print '\nin load -> in test_connect for \'nt\'...',str(message.__class__)+':',str(message),'\n'
			# else:
				# with open(self.savedir+self.savefile) as f: self.userList = pickle.loads(base64.b64decode(f.read()))
			# for u in self.userList:
				# for i in u.incomeList:
					# for e in u.expenseList:
						# for s in u.savingsItemList:
							# if s.name == e.name and i.isPrimary:
								# s.set_expense_values_from_savingsItem(u, e)
		# except Exception as message: print '\nin load...',str(message.__class__)+':',str(message),'\n'
		try:
			with open(self.savedir+self.savefile) as f: self.userList = pickle.loads(base64.b64decode(f.read()))
			for u in self.userList:
				for i in u.incomeList:
					for e in u.expenseList:
						for s in u.savingsItemList:
							if s.name == e.name and i.isPrimary:
								s.set_expense_values_from_savingsItem(u, e)
		except Exception as message: print '\nin load...',str(message.__class__)+':',str(message),'\n'

	def save(self):
		# print '\nin save...'
		# test_connect = self.test_connection_save()
		# mac_network_drives = test_connect[1]
		# test_mac_connect = test_connect[2]
		users_file = base64.b64encode(pickle.dumps(self.userList))
		try:
			# if test_connect[0]:
				# if os.name == 'nt':
					# p = os.path.getmtime(self.savedir+self.savefile)
					# m = os.path.getmtime(mac_network_drives[test_mac_connect])
					# print 'p > m:', p > m
					# if p > m:
						# with open(mac_network_drives[test_mac_connect], 'w') as f: f.write(users_file)
						# print 'Success!'
				# if os.name != 'nt':
					# m = os.path.getmtime(self.savedir+self.savefile)
					# p = os.path.getmtime('/volumes/users/cary/appdata/roaming/cbudget/users.cbp')
					# print 'm > p:', m > p
					# if m > p:
						# with open('/volumes/users/cary/appdata/roaming/cbudget/users.cbp', 'w') as f: f.write(users_file)
						# print 'Success!'
			# self.save_local()
			with open(self.savedir+self.savefile, 'w') as f: f.write(users_file)
		except Exception as message: print '\n',str(message.__class__)+':',str(message),'\n'
		
	def save_local(self):
		users_file = base64.b64encode(pickle.dumps(self.userList))
		try:
			if os.path.exists(self.savedir) == False: os.makedirs(self.savedir)
			with open(self.savedir+self.savefile, 'w') as f: f.write(users_file)
		except Exception as message: print '\n',str(message.__class__)+':',str(message),'\n'
		
	def test_connection_load(self): 
		print 'in test_connection...'
		connecting_message_thread = threading.Thread(target=self.connecting_message)
		mount_message_thread = threading.Thread(target=self.mount_message)
		mac_network_drives = ('a:\\cbudget\\users.cbp', 'b:\\cbudget\\users.cbp')
		test_mac_connect = None
		pc_connected = None
		connected = None
		try:
			# if self.userList == []: connecting_message_thread.start()
			if os.name == 'nt':
				if self.userList != []: test_mac_connect = self.test_mac_connect()
				if test_mac_connect != None: connected = True
			if os.name != 'nt':
				if os.system('ping -c 1 cary-pc') == 0: 
					with open('/volumes/users/cary/appdata/roaming/cbudget/test_connection', 'w') as f: f.write('')
					pc_connected = True
					connected = True
		except Exception as message: print '\n',str(message.__class__)+':',str(message),'\n'
		if os.name != 'nt' and not pc_connected:
			mount_message_thread.start()
			os.system('osascript -e \'mount volume "smb://cary-pc.att.net;cary:M1ll3nIyouM@cary-pc/users/"\'')
		return (connected, mac_network_drives, test_mac_connect)
			
	def test_connection_save(self): 
		print 'in test_connection...'
		connecting_message_thread = threading.Thread(target=self.connecting_message)
		mac_message_thread = threading.Thread(target=self.mac_not_connected)
		pc_message_thread = threading.Thread(target=self.pc_not_connected)
		mount_message_thread = threading.Thread(target=self.mount_message)
		pc_connected = None
		mac_network_drives = (self.userList[0].s.mac_drive, 'a:\\cbudget\\users.cbp', 'b:\\cbudget\\users.cbp')
		connected = None
		test_mac_connect = None
		try:
			# if self.userList[0].s.show_connection_message: connecting_message_thread.start()
			if os.name == 'nt':
				if self.userList[0].s.test_mac_connect: test_mac_connect = self.test_mac_connect()
				if test_mac_connect != None: connected = True
			if os.name != 'nt':
				try: test_mac_connect = mac_network_drives.index(self.userList[0].s.mac_drive)
				except Exception as message: print '\ndebugging...',str(message.__class__)+':',str(message),'\n'
				if os.system('ping -c 1 cary-pc') == 0: 
					with open('/volumes/users/cary/appdata/roaming/cbudget/test_connection', 'w') as f: f.write('')
					pc_connected = True
					connected = True
			self.userList[0].s.show_connection_message = False
		except Exception as message: 
			print '\n',str(message.__class__)+':',str(message),'\n'
			if self.userList[0].s.show_connection_message: 
				if os.name != 'nt': pc_message_thread.start()
				pc_connected = False
		
		print 'in test_connection_save - this is being executed after the except'
		print 'self.userList[0].s.mount_mac_volume:', self.userList[0].s.mount_mac_volume
		if os.name != 'nt' and (self.userList[0].s.mount_mac_volume and pc_connected):
			mount_message_thread.start()
			os.system('osascript -e \'mount volume "smb://cary-pc.att.net;cary:M1ll3nIyouM@cary-pc/users/"\'')
		self.userList[0].s.mount_mac_volume = False
		self.userList[0].s.show_connection_message = False
		return (connected, mac_network_drives, test_mac_connect)
			
	def test_mac_connect(self):
		print 'entering test_mac_connect...'
		mac_message_thread = threading.Thread(target=self.mac_not_connected)
		test_mac_connect = None
		print 'self.userList:', self.userList	
		mac_network_drives = (self.userList[0].s.mac_drive, 'a:\\cbudget\\users.cbp', 'b:\\cbudget\\users.cbp')
		for m in mac_network_drives: 
			# print 'testing {0} in self.test_mac_connect'.format(m)
			try:
				if os.name == 'nt': 
					open(m)
					test_mac_connect = mac_network_drives.index(m)
					self.userList[0].s.mac_drive = mac_network_drives[test_mac_connect]
			except Exception as message: print '\nin test_mac_connect...',str(message.__class__)+':',str(message),'\n'
		if self.userList[0].s.test_mac_connnect: mac_message_thread.start()
		self.userList[0].s.test_mac_connnect = False
		return test_mac_connect
				
	def connecting_message(self): wx.MessageBox('Testing network connection. Please wait...', 'CBudget')
	def mac_not_connected(self): wx.MessageBox('The Mac is not connected!', 'Connection error')
	def pc_not_connected(self): wx.MessageBox('The PC is not connected!', 'Connection error')
	def mount_message(self): wx.MessageBox('Please wait for the drive to be mounted so the data file can be saved next attempt.', 'Mounting volume "Users/Cary" on Mac')
	
	def delete_install_folder(self): 
		install_dir = ''
		if os.name == 'nt':
			if os.path.exists(os.environ['APPDATA']+'\\CBudget\\remove_install.txt'):
				with open(os.environ['APPDATA']+'\\CBudget\\remove_install.txt', 'r') as f: 
					install_dir = f.read()
					if os.path.exists(install_dir+'\\install'): shutil.rmtree(install_dir+'\\install', True)
					if os.path.exists(install_dir+'\\install.lnk'): os.remove(install_dir+'\\install.lnk')
					#if os.path.exists(os.environ['APPDATA']+'\\CBudget\\remove_install.txt'): os.remove(os.environ['APPDATA']+'\\CBudget\\remove_install.txt')
		
	def end_process(self):
		print '\nin end_process...'
		if os.name == 'nt':
			k32 = ctypes.windll.kernel32
			handle = k32.OpenProcess(1, 0, os.getpid())
			return (0 != k32.TerminateProcess(handle, 0))
		quit()
		
	def window_timeout(self, frame, start_time):
		if time.time() - start_time > 600: 
			frame.Hide()
			try: wx.MessageBox('Your session has timed out due to inactivity. To continue managing your finances, reopen Cbudget and log back in.', 'CBudget has logged you out', wx.OK | wx.CENTRE | wx.ICON_WARNING) 
			except Exception as message: print '\n',str(message.__class__)+':',str(message),'\n'
			self.end_process()    


class budget():
	monthlyIncome = 0.0
	annualIncome = 0.0
	monthlyExpenses = 0.0
	annualExpenses = 0.0

	def monthly_income(self, user):
		self.monthlyIncome = 0.0
		for i in user.incomeList: self.monthlyIncome += (30.45 / i.period_in_days()) * i.amount
		return round(self.monthlyIncome,2)

	def annual_income(self, user):
		self.annualIncome = 0.0
		for i in user.incomeList: self.annualIncome += (365.2422 / i.period_in_days()) * i.amount
		return round(self.annualIncome,2)
		
	def monthly_expenses(self, user):
		self.monthlyExpenses = 0.0
		for e in user.expenseList: self.monthlyExpenses += (30.45 / e.period_in_days()) * e.amount
		return round(self.monthlyExpenses,2)

	def annual_expenses(self, user):
		self.annualExpenses = 0.0
		for e in user.expenseList: self.annualExpenses += (365.2422 / e.period_in_days()) * e.amount
		return round(self.annualExpenses,2)

	def set_aside(self, user, income):
		setAside = 0.0
		for e in user.expenseList: setAside += e.amount / e.bill_period_divider(user)
		temp = income.amount / income.pay_period_total_earnings(user)
		setAside *= temp
		if setAside > income.amount: setAside = income.amount
		return round(setAside,2)

	def left_over(self, user, income):
		leftOver = 0.0
		set_aside = self.set_aside(user, income)
		leftOver = income.amount - set_aside
		return round(leftOver,2)
		
	def left_after_save_amount(self, user, income):
		leftAfterSaveAmount = self.left_over(user, income) - self.save_amount(user, income)
		return round(leftAfterSaveAmount,2)
		
	def income_to_expenses_ratio(self, user):
		incomeToExpensesRatio = self.monthly_expenses(user) / self.monthly_income(user)
		return incomeToExpensesRatio
	
	def save_percent(self, user):
		savePercent = 0.0
		try: savePercent = 1.0 - (self.monthly_expenses(user) / self.monthly_income(user))
		except Exception as message: print '\n',str(message.__class__)+':',str(message),'\n'
		if savePercent < 0.0: savePercent = 0.0
		return round(savePercent,4)
		
	def save_amount(self, user, income):
		saveAmount = 0.0
		saveAmount = self.left_over(user, income) * self.save_percent(user)
		return round(saveAmount,2)
		
	def monthly_savings(self, user):
		monthlySavings = 0.0
		monthlySavings = (self.monthly_income(user) - self.monthly_expenses(user)) * self.save_percent(user)
		return round(monthlySavings,2)
		
	def daily_allowance(self, user):
		dailyAllowance = 0.0
		dailyAllowance = ((self.monthly_income(user) - self.monthly_expenses(user)) - (self.monthly_income(user) - self.monthly_expenses(user)) * self.save_percent(user)) / 30.45
		return round(dailyAllowance,2)
	
	def weekly_allowance(self, user):
		weeklyAllowance = 0.0
		weeklyAllowance = self.daily_allowance(user) * 7
		return round(weeklyAllowance,2)
		
	def monthly_allowance(self, user):
		monthlyAllowance = 0.0
		monthlyAllowance = self.daily_allowance(user) * 30.45
		return round(monthlyAllowance,2)


class expenses_due():
	expensesDueDict = {}
	timeTillBillDueList = []

	def time_till_bill_due(self, user):
		self.timeTillBillDueList = [e.date-datetime.now() for e in user.expenseList]
		return self.timeTillBillDueList

	def expenses_due(self, user):
		income = user.get_primary_income()
		self.time_till_bill_due(user)
		self.expensesDueDict.clear()
		temp = {}
		for i in range(len(user.expenseList)): temp[i] = (user.expenseList, self.timeTillBillDueList)
		for t in temp: 
			#if temp[t][1][t].days <= income.period_in_days() and temp[t][0][t].partial_amount > 0: self.expensesDueDict[temp[t][0][t].name] = temp[t][0][t].partial_amount, temp[t][0][t].date.date()
			#if temp[t][1][t].days <= income.period_in_days() and temp[t][0][t].partial_amount == 0: self.expensesDueDict[temp[t][0][t].name] = temp[t][0][t].amount, temp[t][0][t].date.date()
			if temp[t][1][t].days <= income.period_in_days(): self.expensesDueDict[temp[t][0][t].name] = temp[t][0][t].amount, temp[t][0][t].date.date()
		return self.expensesDueDict

	def update_savings_item_amount(self, user, savingsItem):
		savingsItem.load_amount_saved()
		
	def record_payment(self, user, name, amount, date, conf, note, account):
		income = user.get_primary_income()
		trans = None
		self.expensesDueDict = self.expenses_due(user)
		for d in self.expensesDueDict:
			if name == d:
				for e in user.expenseList:
					if name == e.name:
						add_time = None
						note = None
						if int(amount)/int(e.amount) < 1: add_time = 1
						else: add_time = int(amount)/int(e.amount)
						if e.frequencyDesignator == 'month(s)': e.add_months(add_time)
						if e.frequencyDesignator != 'month(s)': e.date += timedelta(days=e.period_in_days()*add_time)
						e.amount = amount
						note = 'bill paid'
						trans = transaction(e.name, amount*-1, date, conf, note, 'expense')
						account.r.add_transaction(user, trans, account)
						for s in user.savingsItemList:
							if name == s.name:
								s.amount += amount*-1
								s.set_expense_values_from_savingsItem(user, e)
								if s.date <= datetime.now()+timedelta(days=income.period_in_days()) and s.amount == 0: user.removeExpense(e)

	def total(self, **kwargs): 
		return sum([e[0] for e in self.expensesDueDict.values()])


class finance():
	name = ''
	amount = 0.0
	date = datetime.min
	conf = ''
	note = ''
	state = None
	
	def change_values(self, name, amount, date, conf, note):
		self.name = name
		self.amount = amount
		self.date = date
		self.conf = conf
		self.note = note
		self.uid = alpha_numeric_uid(32)


class transaction(finance):
	type = None
	subtype = None
	
	def __init__(self, name, amount, date, conf, note, type):
		self.name = name
		self.amount = amount
		self.date = date
		self.conf = conf
		self.note = note
		self.type = type
		self.uid = alpha_numeric_uid(32)


class register():
	registerList = []
	search_criteria = []

	def __init__(self, regList):
		self.registerList = regList
		self.search_criteria = []

	def add_transaction(self, user, trans, account):
		self.registerList.append(trans)
		account.balance += trans.amount
		
	def remove_transaction(self, tlist, index):
		for r in self.registerList:
			if r.uid == tlist[index].uid:
				self.registerList.remove(r)

	def edit_transaction(self, tlist, index, name='', amount=0.0, date=datetime.min, conf='', note='', type=''):
		for r in self.registerList:
			if r.uid == tlist[index].uid:
				if name != '': r.name = name
				if amount != None: r.amount = amount
				if date != datetime.min: r.date = date
				if conf != '': r.conf = conf
				if note != '': r.note = note
				if type != '': r.type = type

	def add_search_criterion(self, string):
		self.search_criteria.append(string)
		return self.search_criteria
		
	def get_bofa_transactions(self, user, account):
		bofa = []
		try: 
			f = open('c:\\users\\cary\\downloads\\stmt.csv', 'rb')
			f.read()
			try: 
				for g in f: bofa.append(f.next())
			except Exception as message: print '\n',str(message.__class__)+':',str(message),'\n'
			print 'len(bofa):', len(bofa)
			# try: 
				# for i in range(6): bofa.remove(bofa[0])
			# except Exception as message: print '\n',str(message.__class__)+':',str(message),'\n'
			for i in range(len(bofa)): bofa[i] = bofa[i].split(',')
			for b in bofa: b[0] = b[0].split('/')
			temp_types = []
			for b in bofa: 
				if float(b[-2][1:-1]) >= 0: temp_types.append('credit')
				if float(b[-2][1:-1]) < 0: temp_types.append('debit')		
			print 'len(bofa):', len(bofa)
			print 'len(temp_types):', len(temp_types)
			count = 0
			for i in range(len(bofa)):
				trans = transaction(bofa[i][1], float(bofa[i][-2][1:-1]), datetime(int(bofa[i][0][2]),int(bofa[i][0][0]),int(bofa[i][0][1])),'','', temp_types[i])
				if trans not in account.r.registerList: 
					self.add_transaction(user, trans, account)
					count += 1
			print '{0} transactions were added'.format(count)
		except Exception as message: print '\n',str(message.__class__)+':',str(message),'\n'

	def filter_got_paid(self, name=''):
		tList = []
		if name == '':
			for t in self.registerList:
				if t.type == 'got_paid': tList.append(t)
		else:
			for t in self.registerList:
				if name == t.name:
					if t.type == 'got_paid': tList.append(t)
		return tList
		
	def filter_expense(self, name=''):
		tList = []
		if name == '':
			for t in self.registerList:
				if t.type == 'expense': tList.append(t)
		else:
			for t in self.registerList:
				if name == t.name:
					if t.type == 'expense': tList.append(t)
		return tList
		
	def filter_credit(self):
		tList = []
		for t in self.registerList:
			if t.type == 'credit' or t.type == '': tList.append(t)
		return tList
		
	def filter_debit(self):
		tList = []
		for t in self.registerList:
			if t.type == 'debit': tList.append(t)
		return tList
		
	def filter_transfer_credit(self):
		tList = []
		for t in self.registerList:
			if t.type == 'transfer_credit': tList.append(t)
		return tList
		
	def filter_transfer_debit(self):
		tList = []
		for t in self.registerList:
			if t.type == 'transfer_debit': tList.append(t)
		return tList
		
	def filter_by_type(self, user, type, tlist):
		return [t for t in tlist if t.type == type]
		
	def filter_by_search(self, user, string_value, tlist):
		sList = []
		for t in tlist:
			if re.search(string_value,t.name,re.I) != None or re.search(string_value,str(t.amount),re.I) != None or re.search(string_value,t.conf,re.I) != None or re.search(string_value,t.note,re.I) != None or re.search(string_value,t.type) != None: sList.append(t)
		return sList
		
	def filter_by_date_range(self, user, date1, date2, tlist):
		return [r for r in tlist if r.date.date() >= date1.date() and r.date.date() <= date2.date()]
		
	def average_income(self, name):
		dates = []
		diffs = []
		average_amount = 0.0
		average_frequencyNumber = 0.0
		count = 0
		incomeList = self.filter_got_paid(name)
		for i in incomeList:
			if name in i.name or name == i.name and i.amount != 0: 
				average_amount += i.amount
				count += 1
		if count: average_amount /= count
		for i in incomeList: dates.append(i.date)
		for i in range(1,len(dates)): diffs.append(dates[i]-dates[i-1])
		for d in diffs: average_frequencyNumber += d.days
		if len(diffs) > 0: average_frequencyNumber /= float(len(diffs))
		return (average_amount, average_frequencyNumber)
		
	def average_expense(self, name=''):
		dates = []
		diffs = []
		average_amount = 0.0
		average_frequencyNumber = 0.0
		count = 0
		expenseList = self.filter_expense(name)
		for e in expenseList:
			if name in e.name or name == e.name and e.amount != 0: 
				average_amount += abs(e.amount)
				count += 1
		if count: average_amount /= count
		for e in expenseList: dates.append(e.date)
		for i in range(1,len(dates)): diffs.append(dates[i]-dates[i-1])
		for d in diffs: average_frequencyNumber += d.days
		if len(diffs) > 0: average_frequencyNumber /= float(len(diffs))
		return (average_amount, int(average_frequencyNumber))
		
	def average_credits(self, user, name):
		dates = []
		diffs = []
		average_amount = 0.0
		average_frequencyNumber = 0.0
		creditList = self.filter_credit()
		if creditList == []: creditList = user.creditList
		for c in creditList:
			if name in c.name or name == c.name: average_amount += c.amount
		if len(creditList) > 0: average_amount /= len(creditList)
		for c in creditList: dates.append(c.date)
		for i in range(1,len(dates)): diffs.append(dates[i]-dates[i-1])
		for d in diffs: average_frequencyNumber += d.days
		if len(diffs) > 0: average_frequencyNumber /= len(diffs)
		return (average_amount, int(average_frequencyNumber))


class account(finance):
	balance = 0.0
	account_number = ''
	bank_name = ''
	isCurrent = False
	type = None
	r = None

	def __init__(self, name, balance, number, bank_name, type, regList):
		self.name = name
		self.balance = balance
		self.number = number
		self.bank_name = bank_name
		self.type = type
		self.r = register(regList)
		self.uid = alpha_numeric_uid(32)


class checking(account): pass


class savings(account): pass


class credit_card(account): 
	interest_rate = 0.0
	credit_limit = 0.0

	def __init__(self, name, balance, number, bank_name, rate, limit, type, regList):
		self.name = name
		self.balance = balance
		self.number = number
		self.interest_rate = rate
		self.credit_limit = limit
		self.type = type
		self.r = register(regList)
		self.uid = alpha_numeric_uid(32)
		
		
class settings():
	active_frame = None
	new_frame = None
	show_connection_message = True
	mount_mac_volume = True
	mac_drive = None
	test_mac_connection = False
	show_last_trasactions = None
		
	def __init__(self):
		self.savings_item_added = False
		self.credit_added = False
		self._home = home_window()
		self._accounts = accounts_window()
		self._incomes = incomes_window()
		self._credits = credits_window()
		self._expenses = expenses_window()
		self._savings_items = savings_items_window()
		self._budget = budget_window()
		self._expenses_due = expenses_due_window()
		self._transactions = transactions_window()
		
	def show_run_count(self):
		print 'Window access stats: \n'
		print 'Home window has been accessed {0} times'.format(self._home.run_count)
		print 'Accounts window has been accessed {0} times'.format(self._accounts.run_count)
		print 'Incomes window has been accessed {0} times'.format(self._incomes.run_count)
		print 'Credits window has been accessed {0} times'.format(self._credits.run_count)
		print 'Expenses window has been accessed {0} times'.format(self._expenses.run_count)
		print 'Savings Items window has been accessed {0} times'.format(self._savings_items.run_count)
		print 'Budget window has been accessed {0} times'.format(self._budget.run_count)
		print 'Expenses Due window has been accessed {0} times'.format(self._expenses_due.run_count)
		print 'Transactions window has been accessed {0} times'.format(self._transactions.run_count)
		
	def clear_run_count(self):
		self._home.run_count = 0
		self._accounts.run_count = 0
		self._incomes.run_count = 0
		self._credits.run_count = 0
		self._expenses.run_count = 0
		self._savings_items.run_count = 0
		self._budget.run_count = 0
		self._expenses_due.run_count = 0
		self._transactions.run_count = 0
		
		
		
class home_window():
	welcome_title = 'Getting Started'
	welcome_message = 'Welcome to CBudget and thank you for your purchase. It appears that this is your first time using CBudget. Congratulations!, you\'ve made ' \
							'the right choice! You\'ll soon see what I mean, but the first thing you need to do is create a username and password. This is for ' \
							'your security so no one can be nosy and take a peek into your financial life. Creating a username and password is a simple process ' \
							'and the prompts will guide you. Once you have a username and password, you\'ll see the [Accounts] button become active. CBudget works ' \
							'much like a powerful checkbook register that allows you to keep track of and record all of your personal finances. However, it does not ' \
							'access or change any of your bank or credit card accounts over the internet. To pay bills or transfer funds you still need to log in to ' \
							'your bank or credit card account online or go into your local bank branch. The advantage of this is security. Now that you\'ve made the ' \
							'purchase, the program is yours, you own it, it\'s stored on your computer only and is not accessed by any online servers, spyware, malware, ' \
							'bots or other privacy invading software. The only one who sees your finances is you. Now you can enjoy managing your finances with ease and ' \
							'peace of mind. Happy budgeting!'
								
	def __init__(self):
		self.run_first_time = True
		self.run_count = 0
							
class accounts_window():
	welcome_title = 'Getting Started with Accounts'
	welcome_message = 'The Accounts window will show in a moment. Accounts are what CBudget hinges on. You really can\'t do anything but log in unless you have at ' \
							'least one account. That\'s why you\'ll see most of the other buttons greyed out for now. If you\'ve entered more than one account, CBudget ' \
							'will total your account balances so you have an idea of the total amount of money you have at any given time. To get started with ' \
							'Accounts, the first thing you\'ll need to do is add an account. To do this, simply follow the prompts. Once you\'ve added your ' \
							'first account, you\'ll see most of the main buttons at the bottom become active. The only ones that won\'t activate right away are the ' \
							'[Budget] and [Expenses Due] buttons. You\'ll need at least one income and one expense for those buttons to activate. You\'ll learn ' \
							'how to add incomes and expenses soon. You can add as many checking, savings, and credit card accounts as you want.'
							
	def __init__(self):
		self.run_first_time = True
		self.run_count = 0
								
class incomes_window():
	welcome_title = 'Getting Started with Incomes'
	welcome_message = 'The Incomes window will show in a moment. To get started with Incomes, you\'ll need to add your first income. The prompts will guide you. Some of us have just one source of income. If that\'s you' \
							', no problem. You\'ll only need to add that one income. If you have more than one source of income say, from two or more jobs, or you and your spouse are using CBudget ' \
							'to manage your household finances together, no worries! CBudget takes into account every income you have. That\'s the easy part. But what really makes CBudget your best friend on payday ' \
							'is that it uses the combined amounts and pay periods for all incomes and determines how much you need to set aside for bills, savings, and spending money from each one. For ' \
							'example, if you and your spouse both work, but you get paid on the 1st and 15th of the month and he or she gets paid every week, then it can be challenging to know precisely how much to ' \
							'set aside from each income to make sure all expenses are covered, and to make sure money is being saved for emergencies or other important stuff, and ensure that there\'s some left over to blow off some ' \
							'steam on the weekends. Wouldn\'t you love to have that peaceful, confident feeling every time you get paid, that you know exactly what to do with every last penny of your hard ' \
							'earned money? Now you can with CBudget! I assure you, you make more money than you think you do, but if it\'s not going to the right places each paycheck, you\'re probably wasting more than ' \
							'you think. But don\'t worry, even if you aren\'t that good at managing your money, you will soon become a pro. Changing your spending habits is not as ' \
							'hard as you think when you have a simple, but accurate guide in front of you.'
	def __init__(self):
		self.run_first_time = True
		self.run_count = 0
		self.record_income_payment = False
								
class credits_window():
	welcome_title = 'Getting Started with Credits'
	welcome_message = 'The Credits window will show in a moment. To get started with Credits, you\'ll need to add a credit. The prompts will guide you. A credit is a type of income that doesn\'t have a regular ' \
							'cycle. A credit may be a one-time income like a cash gift, an inheritance check, or a form of pay that doesn\'t come on a regular basis such as income ' \
							'from a small business. If you\'ve entered a credit three or more times (not on the same day) with the same name, you can choose to add that credit to ' \
							'your income list as a regular income. CBudget will automatically assign an average amount and pay cycle to the new income. The new income can then be used in the Budget ' \
							'window to let you know how much to set aside for expenses, how much to save, and how much is left for spending money, just like any other regular income.'
	def __init__(self):
		self.run_first_time = True
		self.run_count = 0
								
class expenses_window():
	welcome_title = 'Getting Started with Expenses'
	welcome_message = 'The Expenses window will show in a moment. To get started with Expenses you\'ll need to add each of your expenses to the list. The prompts will guide you. This is the only part of CBudget that ' \
							'that will take some time initially, but once you\'re done with that, you\'re done. You won\'t ever have to worry about it again unless you need to add a new expense, ' \
							'change one that\'s already there, or remove one from the list. And once you\'ve paid off a bill like a credit card, you\'ll have fun removing that one from the list. ' \
							'Just for clarification, an expense in CBudget is any regular, recurring bill such as your rent/mortgage, car payment, car insurance, phone bill, and other things like that. ' \
							'It can be any type of bill that you have to pay on a regular basis. Entering these bills allows CBudget to calculate an amount for you to set aside each paycheck ' \
							'so you can start building up a \"pool\" of money to always have on hand for paying bills. With this method of budgeting, you never need to break your money down into individual ' \
							'percentages or use envelopes for each category of expense. It\'s all pre-calculated and accurate to within a few pennies (for your entire budget). The envelope method works, but ' \
							'what if there was something that worked just as well, if not better, without all the mess and clutter? The only catch is that for CBudget to work for you, you have to maintain enough ' \
							'discipline not to go into the \"pool\" and take money out when there\'s an emergency. But then, you have to have the same level of discipline with the envelope system. CBudget ' \
							'is also designed to help you begin setting aside another \"pool\" of money that\'s just for emergencies or even things you want to save for like vacations or other things you may ' \
							'think you can\'t afford.'
	def __init__(self):
		self.run_first_time = True
		self.run_count = 0
								
class savings_items_window():
	welcome_title = 'Getting Started with Savings Items'
	welcome_message = 'The Savings Items window will show in a moment. To get started with Savings Items, you\'ll need to add your first Savings Item. The prompts will guide you. A Savings Item ' \
							'is an item that allows you to keep track of things you want to save money for such as that trip to Europe, the kids\' college or a new car. It can be ' \
							'anything you want to save money for. Once you\'ve entered a Savings Item, you can just use it to keep of track of the amount and date you want to have ' \
							'that money saved by, or you can add it as a regular recurring bill to your expenses list. This is where Savings Items become very powerful. When you add ' \
							'it as a regular expense, CBudget will calculate the amount you need to save for that item every time you get paid for any of your incomes, if you have more than one. ' \
							'It is recommended that you put this money aside in a seperate savings account that you don\'t touch so when it comes time for that trip to Europe, the kids\'s college, the new car, ' \
							'or whatever you\'re saving for, you\'ll have the money already set aside specifically for that. Don\'t worry, if you\'re using CBudget to it\'s full potential, ' \
							'you\'ll already have an emergency fund building, so you won\'t need to go into that account for anything else.'
	def __init__(self):
		self.run_first_time = True
		self.run_count = 0
									 
class budget_window():
	welcome_title = 'Getting Started with your Budget'
	welcome_message = 'The Budget window will show in a moment. To get started with your Budget, there are a few things you need to know. One of them is that CBudget does not break your finances down into ' \
							'individual amounts for each of your bills. In our experience, while well intentioned, that method just makes things more complicated. ' \
							'Most budgets try to break everything down into categories and then attempt to tell you how much money to spend for each category. If you\'ve been using a budget like that, no problem, but we\'ve found that the simpler budgeting ' \
							'is, the more effective. As a result, we\'ve come up with a way to make budgeting just as powerful (if not more) than the traditional method by telling you ' \
							'three simple things on payday. 1) How much money to set aside for all of your bills, 2) how much you can realistically afford to save and 3) how much you can ' \
							'afford to keep on hand as spending cash until your next paycheck. So, while your financial health improves using CBudget, your mental health doesn\'t have to suffer. Getting on top of ' \
							'your finances doesn\'t have to be painful. In fact we\'ve seen many people fail at budgeting simply because they get discouraged and end up feeling that the whole process is ' \
							'just too difficult. If you\'ve been living paycheck to paycheck, then CBudget is going to start helping you where you\'re at - paycheck to paycheck. If you\'re reading this now, ' \
							'then you\'ve been pointed in the right direction. You can succeed with finances and still have fun. It\'s called balance. With that said, a word of caution:  the worse you\'ve been ' \
							'at spending your money without any feeling of consequence ' \
							'the more likely you are to feel some failure at first while trying to change your spending habits. Again, don\'t worry. Even if you fail over and over again at saving ' \
							'the money CBudget says you can save, or if you put that money into your savings account on payday only to go and deplete it again when you get to the end of your paycheck, because the ' \
							'amount left for spending cash just doesn\'t seem to be enough, you\'re really not failing at all. Persistence is key. Just keep putting the money where CBudget tells you to ' \
							'each time you get paid. You will get better at this because you have a system now and that system has structure that you didn\'t have before, if you keep at it, before long you\'ll ' \
							'begin to notice that you\'re paying all of your bills on time, your debts are decreasing, you\'re more aware of your spending habits, and you\'re savings account is starting to stack up. ' \
							'This is the power of CBudget, not that it does everything for you, but that it provides a system that empowers you, even changes you through your own discipline to become a different person ' \
							'in the way you manage your finances. In order for this budgeting process to be most effective, we recommend that you have at a minimum 3 bank accounts: 2 checking accounts and 1 savings account. ' \
							'The reason for this is that it\'s much easier to keep things in the right place if you divide your money in reality, not just in your head or in the CBudget Accounts window. If you can\'t, for some reason, get ' \
							'more than one bank account right now, don\'t worry, you can still use CBudget to keep track of the funds you should have in seperate \"pools\" (or accounts) in the Accounts window, but keep trying to get those other ' \
							'accounts. It\'ll be much easier.'
	def __init__(self):
		self.run_first_time = True
		self.run_count = 0
									
class expenses_due_window():
	welcome_title = 'Getting Started with Expenses Due'
	welcome_message = 'The Expenses Due window will show in a moment. To get started with Expenses Due, simply take a look the list of expenses that are due. But what exactly are you looking at? This is a list made ' \
							'up of the bills that are due ONLY in the pay period you are in now. In other words, if you get paid every week and the due date for one or more of your bills falls between now ' \
							'and the next pay day, those bills will show up in the list. If no bills are due, a popup will tell you that too. How does CBudget figure this out? A little ' \
							'magic with math and some practical life experience have brought about a process we use to keep you worry free. Again, if you are setting aside the amount to cover bills that it says in the Budget window each paycheck, then ' \
							'you won\'t even have to think (much less worry) about being able to cover your bills or even when they\'re due. They will just show up in the Expenses Due list. Simple! You will also see a total ' \
							'amount due for all the bills that are shown in the list. This is just so you know what you\'re working with overall. Don\'t let this amount scare you. If you\'ve just started using CBudget and haven\'t had ' \
							'time to build up enough of a pool to cover regular expenses, you will soon. It may take somewhere around three months to build enough of a pool to cover all bills that are due at any given time, ' \
							'but if you\'re new to CBudget and your habit hasn\'t been one of saving money, then really you\'re no worse off than you were before by changing where you put your money, and believe me, the change will be worth it. ' \
							'You have nothing to lose except stress about your finances. One last thing, you will see a button that says [Record Payment]. Its says, "Record" because, if you recall, CBudget does not change your bank ' \
							'accounts or any other accounts online. This button simply allows you to record that you\'ve made the payment. The payment will be recorded in your transaction list and the due date of the bill ' \
							'will be pushed forward by the amount of time it occurs regularly. In other words, if it\'s due every month, the due date will be pushed forward by a month, or by two weeks if it\'s due every two weeks. That way, it won\'t show up ' \
							'in the list again until the next time it\'s due.'
	def __init__(self):
		self.run_first_time = True
		self.run_count = 0
									
class transactions_window():
	welcome_title = 'Getting Started with Transactions'
	welcome_message = 'The Transactions window will show in a moment. To get started with Transactions, the first thing you need to know is that you can use the selector near the ' \
						'bottom right corner of the window to switch between your accounts. This will allow you to view all transactions for the account you have selected. You ' \
						'can also add new transactions, change information for transactions already in the list, and delete transactions entered by mistake or that you just don\'t ' \
						'want to see anymore. You also have at your fingertips a powerful search function as well as the ability to filter transactions by date or by transaction ' \
						'type. For example, in filtering by date, if you are paid every two weeks you may only want to see what you did with your money in that two week period. ' \
						'With the date filter, you can. The search function allows you to enter a search string to find transactions either by their name, amount, confirmation ' \
						'number, or a note or memo recorded with the transaction. Filtering by type allow you to view only transactions of a certain type such as income payments, ' \
						'bills paid, credits, debits, and account transfers. You can even use any combination of the three filters together or all of them at the same time! You may ' \
						'be saying to yourself, \"Wow, this is a really cool feature, but since CBudget doesn\'t automatically go into my bank account and download all my ' \
						'transactions, that means I have to enter each one by hand\". That\'s true, but if you use Transactions to record all your financial activity for each ' \
						'account, I think you\'ll begin to see the benefit of entering it by hand. While you\'re in the process of learning how to manage money better, it can be ' \
						'very helpful to have to enter each transaction by hand. Doing this will force you to become more aware of how much you\'re spending and will keep you ahead ' \
						'of your bank and what they say you have left in your account. Sound like a traditional checkbook register? That\'s exaclty what it is, but since it\'s ' \
						'electronic, it\'s a bit easier to enter and much easier to find information than the old hand-written way. For those of you who like keeping track of things ' \
						'and are good with checkbook registers, this may just end up being your favorite aspect of using CBudget.'
	def __init__(self):
		self.run_first_time = True
		self.run_count = 0


class user():
	name = ''
	password = ''
	b = None
	ed = None
	s = None
	account_paid_into = None
	states = {
				'APP_RUNNING':None, 
				'LOGGED_IN':None, 
				'PASSWORD_VALID':None, 
				'IDLE':False, 
				'GOT_PAID':'ask', 
				'EXPENSES_DUE':'ask'
			 }

	def __init__(self, name):
		self.name = name
		self.incomeList = []
		self.creditList = []
		self.expenseList = []
		self.debitList = []
		self.savingsItemList = []
		self.accountList = []
		self.b = budget()
		self.ed = expenses_due()
		self.s = settings()

	def addIncome(self, name, amount, date, number, designator): 
		self.incomeList.append(income(name, amount, date, number, designator))
		temp = []
		for i in self.incomeList:
			temp.append(i.isPrimary)
		if True not in temp: self.incomeList[0].isPrimary = True
	def addExpense(self, name, amount, date, number, designator): self.expenseList.append(expense(name, amount, date, number, designator))
	def addCredit(self, name, amount, date, conf, note): self.creditList.append(credit(name, amount, date, conf, note))
	def addDebit(self, name, amount, date, cnf, note): self.debitList.append(debit(name, amount, date))
	def addSavingsItem(self, name, amount, date): self.savingsItemList.append(savings_item(name, amount, date)) 
	def addCheckingAccount(self, name, balance, account_number, bank_name, type): 
		self.accountList.append(checking(name, balance, account_number, bank_name, type, []))
		temp = []
		for a in self.accountList:
			temp.append(a.isCurrent)
		if True not in temp: self.accountList[0].isCurrent = True	
	def addSavingsAccount(self, name, balance, account_number, bank_name, type): 
		self.accountList.append(savings(name, balance, account_number, bank_name, type, []))
		temp = []
		for a in self.accountList:
			temp.append(a.isCurrent)
		if True not in temp: self.accountList[0].isCurrent = True
	def addCreditCardAccount(self, name, balance, account_number, bank_name, rate, limit, type): 
		self.accountList.append(credit_card(name, balance, account_number, bank_name, rate, limit, type, []))
		temp = []
		for a in self.accountList:
			temp.append(a.isCurrent)
		if True not in temp: self.accountList[0].isCurrent = True
	def removeIncome(self, income): 
		temp = self.get_primary_income()
		temp1 = self.incomeList[0]
		self.incomeList = [i for i in self.incomeList if i.uid != income.uid]
		if income == temp and self.incomeList != []:
			self.set_primary_income(self.incomeList[0])
			return 'success'
		else: return 'fail'
	def removeCredit(self, credit): self.creditList = [c for c in self.creditList if c.uid != credit.uid]
	def removeExpense(self, expense): self.expenseList = [e for e in self.expenseList if e.uid != expense.uid]
	def removeDebit(self, debit): self.debitList = [d for d in self.debitList if d.name != debit.uid]
	def removeSavingsItem(self, savingsItem):
		self.expenseList = [e for e in self.expenseList if e.name != savingsItem.name]
		self.savingsItemList = [s for s in self.savingsItemList if s.uid != savingsItem.uid]
	def removeAccount(self, account): 
		temp = self.get_current_account()
		temp1 = self.accountList[0]
		self.accountList = [a for a in self.accountList if a.uid != account.uid]
		if account == temp and self.accountList != []:
			self.set_current_account(self.accountList[0])
			return 'success'
		else: return 'fail'

	def got_paid(self, income, amount, account):
		income.amount = amount
		income.date = datetime.now()
		income.state = 'paid'
		print 'in user.got_paid and income.state is:', income.state
		account.r.add_transaction(self, transaction(income.name, amount, datetime.now(), '', 'income payment', 'got_paid'), account)
		self.account_paid_into = account
		
	def get_primary_income(self):
		for i in self.incomeList:
			if i.isPrimary: return i
		
	def set_primary_income(self, income):
		for i in self.incomeList:
			if i.uid == income.uid: i.isPrimary = True
			else: i.isPrimary = False
			
	def get_current_account(self):
		for a in self.accountList:
			if a.isCurrent: return a
		
	def set_current_account(self, account):
		for a in self.accountList:
			if a.uid == account.uid: a.isCurrent = True
			else: a.isCurrent = False
			
	def get_total_accounts_balance(self, with_credit_card=False):
		total = 0.0
		if with_credit_card: 
			total = sum([a.balance for a in self.accountList if a.type != 'Credit Card'])
			total -= sum([a.balance for a in self.accountList if a.type == 'Credit Card'])
		else: total = sum([a.balance for a in self.accountList if a.type != 'Credit Card'])
		return total

	def get_credits(self):
		cList = []
		cList = [c for c in self.creditList]
		return cList
	
	def get_average_from_creditList(self):
		average = 0.0
		cList = self.get_credits()
		for c in cList: average += c.amount
		average /= len(clist)
		return average

	def search_expenseList(self, search_string):
		elist = [e for e in self.expenseList if re.search(search_string,e.name,re.I) != None]
		return elist

	def get_all_transactions(self):
		rlist = []
		for a in self.accountList: rlist.extend(a.r.registerList)
		return rlist
		
	def sort_transactions_by_date(self, tlist):
		dates = []
		for t in tlist: dates.append(t.date)
		dates.sort()
		temp = []
		for d in dates:
			for t in tlist: 
				if t.date == d and t not in temp: temp.append(t)
		return temp
		
	def get_most_frequent_income_payment_account(self):
		income_payment_type_list = []
		count = 0
		for a in self.accountList:
			for t in a.r.registerList: 
				if t.type == 'got_paid': count += 1
			income_payment_type_list.append(count)
			count = 0
		return self.accountList[income_payment_type_list.index(max(income_payment_type_list))]
		
	def get_most_frequent_expense_payment_account(self):
		expense_payment_type_list = []
		count = 0
		for a in self.accountList:
			for t in a.r.registerList: 
				if t.type == 'expense': count += 1
			expense_payment_type_list.append(count)
			count = 0
		return self.accountList[expense_payment_type_list.index(max(expense_payment_type_list))]

	def info(self):
		print 'username: ', self.name, '\n'
		print 'monthly income: ', round(self.b.monthly_income(self), 2)
		print 'annual income: ', round(self.b.annual_income(self), 2)
		print 'monthly expenses: ', round(self.b.monthly_expenses(self), 2)
		print 'annual expenses: ', round(self.b.annual_expenses(self), 2), '\n'
		print 'save percent: ', str(round(self.b.save_percent(self), 4)*100)+'%'
		print 'monthly savings: ', round(self.b.monthly_savings(self), 2)
		print 'daily allowance: ', round(self.b.daily_allowance(self), 2)
		print 'weekly allowance: ', round(self.b.weekly_allowance(self), 2)
		print 'monthly allowance: ', round(self.b.monthly_allowance(self), 2)
		print '\nincomes:\n'
		for i in self.incomeList:
			print 'name: ', i.name+';', 'amount: ', str(i.amount)+';', 'date: ', str(i.date.date())+';', 'frequencyNumber: ', str(i.frequencyNumber)+';', 'frequencyDesignator: ', i.frequencyDesignator
			print 'set aside: ', round(self.b.set_aside(self, i), 2), ' -----> This gets put into bills_out account'
			print 'save amount: ', round(self.b.save_amount(self, i), 2), ' -----> This gets put into savings'
			print 'left after save amount: ', round(self.b.left_after_save_amount(self, i), 2), ' -----> This stays in income_in account\n'
		print '\nexpenses:\n'
		for e in self.expenseList:
			print 'name: ', e.name+';', 'amount: ', str(round(e.amount, 2))+';', 'date: ', str(e.date.date())+';', 'frequencyNumber: ', str(e.frequencyNumber)+';', 'frequencyDesignator: ', e.frequencyDesignator
		print '\nsavings items:\n'
		for s in self.savingsItemList:
			print 'name: ', s.name+';', 'amount: ', str(round(s.amount, 2))+';', 'date: ', s.date.date()
		print '\n'
		self.s.show_run_count()
		
	def show_expenses_due(self):
		income = self.get_primary_income()
		total = 0.0
		print '\n'
		for k, v in self.ed.expenses_due(self).items():
			print k, 'is due in the amount of', v[0], 'on', v[1], '\n'
			total += v[0]
		if total > 0:
			print 'Total amount due is: ', total
		else:
			print 'There are no items due at this time'
		print '\n'
		

class ongoing(finance):
	frequencyNumber = 0
	frequencyDesignator = ''
	periodInDays = 0.0
	periodDivider = 0.0
	
	def __init__(self, name, amount, date, number, designator):
		self.name = name
		self.amount = amount
		self.date = date
		self.frequencyNumber = number
		self.frequencyDesignator = designator
		self.uid = alpha_numeric_uid(32)
		
	def change_values(self, name, amount, date, number, designator):
		self.name = name
		self.amount = amount
		self.date = date
		self.frequencyNumber = number
		self.frequencyDesignator = designator
	
	def period_in_days(self):
		''' \n\n Calculates the pay cycle and returns how many days are in it '''
		if self.frequencyDesignator == 'day(s)': self.periodInDays = self.frequencyNumber * 1.0
		if self.frequencyDesignator == 'week(s)': self.periodInDays = self.frequencyNumber * 7.0
		if self.frequencyDesignator == 'month(s)': self.periodInDays = self.frequencyNumber * 30.45
		if self.frequencyDesignator == 'year(s)': self.periodInDays = self.frequencyNumber * 365.2422
		return self.periodInDays
		
	def add_months(self, late_catchup=1):
		if self.date.month == 1 or self.date.month == 3 or self.date.month == 5 or self.date.month == 7 or self.date.month == 8 or self.date.month == 10 or self.date.month == 12: self.date += timedelta((31*self.frequencyNumber)*late_catchup)
		elif self.date.month == 4 or self.date.month == 6 or self.date.month == 9 or self.date.month == 11: self.date += timedelta((30*self.frequencyNumber)*late_catchup)
		else: self.date += timedelta((28*self.frequencyNumber)*late_catchup)


class one_time(finance):
	storeAmountSaved = 0.0
	days_till_transaction = 0.0
	amount_to_save = 0.0

	def add_store_amount(self, amount):
		self.storeAmountSaved += amount

	def calc_days_till_transaction(self):
		self.days_till_transaction = self.date - datetime.now()
		return self.days_till_transaction.days

	def calc_amount_to_save(self, user):
		income = user.get_primary_income()
		self.amount_to_save = (self.amount / self.calc_days_till_transaction()) * income.period_in_days()
		if self.amount_to_save > self.amount:
			self.amount_to_save = self.amount
		return self.amount_to_save

	def divide_days_into_wmy(self, days):
		number_designator = ()
		if days > 90 and days <= 730: number_designator = (days/7, 'week(s)')
		elif days > 730: number_designator = (days/31, 'month(s)')
		else: number_designator = (days, 'day(s)')
		return number_designator

	def change_values(self, user, name, amount, date):
		self.name = name
		self.amount = amount
		self.date = date
		self.calc_new_expense_amount(user)            

class income(ongoing):
	periodTotalEarnings = 0.0
	isPrimary = False

	def __init__(self, name, amount, date, number, designator):
		self.name = name
		self.amount = amount
		self.date = date
		self.frequencyNumber = number
		self.frequencyDesignator = designator
		self.isPrimary = False
		self.uid = alpha_numeric_uid(32)

	def pay_period_divider(self, user):
		income = user.get_primary_income()
		self.periodDivider = income.period_in_days() / self.period_in_days()
		return self.periodDivider
		
	def pay_period_total_earnings(self, user):
		income = user.get_primary_income()
		self.periodTotalEarnings = 0
		for i in user.incomeList:
			self.periodTotalEarnings += i.amount * i.pay_period_divider(user)
		return self.periodTotalEarnings


class expense(ongoing):
	partial_amount = 0.0
	partial_payment = 0.0
	partial_paid = False
	states = {'PAID':'ask'}

	def __init__(self, name, amount, date, number, designator):
		self.name = name
		self.amount = amount
		partial_payment = 0.0
		self.partial_payment = 0.0
		self.date = date
		self.frequencyNumber = number
		self.frequencyDesignator = designator
		self.isPrimary = False
		self.uid = alpha_numeric_uid(32)
		
	def bill_period_divider(self, user):
		income = user.get_primary_income()
		self.periodDivider = self.period_in_days() / income.period_in_days()
		return self.periodDivider


class credit(one_time):
	def __init__(self, name, amount, date, conf, note):
		self.name = name
		self.amount = amount
		self.date = date
		self.conf = conf
		self.note = note
		self.uid = alpha_numeric_uid(32)

	def add_store_amount(self, amount):
		print 'this function is not available in this class and has no effect'

	def store_amount_saved(self):
		print 'this function is not available in this class and has no effect'

	def load_amount_saved(self):
		print 'this function is not available in this class and has no effect'
		
	def add_to_incomeList(self, user, credit):
		average_credits = user.get_current_account().r.average_credits(user, credit.name)
		number_designator = self.divide_days_into_wmy(average_credits[1])
		if average_credits[1] != 0:
			user.addIncome(credit.name, round(average_credits[0], 2), credit.date, number_designator[0], number_designator[1])
			return 'success'
		else:
			print '\nYou may not use this feature with 2 or less credits, but the credit amount has been added to your credit list'
			return 'fail'


class debit(one_time):
	def __init__(self, name, amount, date):
		self.name = name
		self.amount = amount
		self.date = date
		self.uid = alpha_numeric_uid(32)
		

class savings_item(one_time):
	def __init__(self, name, amount, date):
		self.name = name
		self.amount = amount
		self.date = date
		self.uid = alpha_numeric_uid(32)

	def add_to_expenseList(self, user):
		amount_to_save = self.calc_amount_to_save(user)
		income = user.get_primary_income()
		number_designator = self.divide_days_into_wmy(int(income.period_in_days()))
		if amount_to_save > 0: 
			user.addExpense(self.name, round(amount_to_save, 2), datetime.now()+timedelta(int(income.period_in_days())), number_designator[0] , number_designator[1])
			return 'success'
		else: return 'fail'

	def set_expense_values_from_savingsItem(self, user, expense):
		if expense.name == self.name:
			number_designator = self.divide_days_into_wmy(user.get_primary_income().period_in_days())
			expense.amount = round(self.calc_amount_to_save(user), 2)
			expense.frequencyNumber = number_designator[0]
			expense.frequencyDesignator = number_designator[1]
			return 'success'
		else: return 'fail'
		
		
##########################################################################################
################################### End of CBugdet Code ##################################
##########################################################################################
 

# If I double click the CBudgetP.py file or run from command line...
if __name__ == '__main__': 
	init=initialize()
	init.load()
	if init.userList != []: u=init.userList[0]
	if sys.argv[-1] == 'info' or sys.argv[-1] == '-i': u.info()
	elif sys.argv[-1] == 'mod' or sys.argv[-1] == '-m': print help('__main__')
	elif sys.argv[-1] == '-r': u.s.show_run_count()
	elif sys.argv[-1] == '-c': 
		try: 
			reply=wx.MessageBox('Are you sure you want to clear the run count?', 'Clear run count?', wx.YES_NO | wx.ICON_QUESTION)
			if reply == wx.YES: 
				u.s.clear_run_count()
				init.save()
		except Exception as message: print '\n',str(message.__class__)+':',str(message),'\n'
	else:
		print '\nCommand line options: \n'
		print '-i for info'
		print '-m for module help'
		print '-r for run count'
		print '-c to clear run count'
	
# If I import CBudgetP...
else: 
	init = initialize()
	init.load()
	if init.userList != []: u=init.userList[0]