from CBudgetP import *

class console_display():
	''' Displays the program information in a console window 
		using a main menu and a series of submenus. '''
	init = initialize()
	user = user('')
	income = income('',0.0,datetime.min,0,'')

	def welcome(self):
		print "***************************************"
		print "********* Welcome To CBudget **********"
		print "***************************************"

	def main_menu(self):
		print '\nMain Menu:'
		print '************'
		print '(1): Users'
		print '(2): Accounts'
		print '(3): Incomes'
		print '(4): Expenses'
		print '(5): Savings Items'
		print '(6): Budget'
		print '(7): Expenses Due'
		print '(8): Transactions\n'
		print 'Press [Enter] to exit\n'
		s = raw_input()
		return s
		
	def user_menu(self):
		print '\nUser Menu'
		print '***********'
		print '(1): Add a user'
		print '(2): Remove a user'
		print '(3): Show current user'
		print '(4): Switch user'
		print '(5): Show user info'
		print '(6): Got paid'
		print '(7): Add a credit'
		print '(8): Return to main menu\n'
		s = raw_input()
		return s
		
	def account_menu(self):
		print '\nAccount Menu'
		print '*************'
		print '(1): View account balances'
		print '(2): Change an account balance'
		print '(3): Return to main menu\n'
		s = raw_input()
		return s
		
	def change_account_menu(self):
		print '\nChange account Menu'
		print '*********************'
		print '(1): Change Income in balance'
		print '(2): Change Bills out balance'
		print '(3): Change Savings balance'
		print '(4): Return to account menu\n'
		s = raw_input()
		return s
		
	def income_menu(self):
		print '\nIncome Menu'
		print '*************'
		print '(1): Add an income'
		print '(2): Remove an income'
		print '(3): Show current income values'
		print '(4): Change income values (name, amount, interval)'
		print '(5): Switch income'
		print '(6): Set primary'
		print '(7): Show primary'
		print '(8): Average income'
		print '(9): Return to main menu\n'
		s = raw_input()
		return s
	
	def expense_menu(self):
		print '\nExpense Menu'
		print '**************'
		print '(1): Add an expense'
		print '(2): Remove an expense'
		print '(3): Show expense values'
		print '(4): Change expense values (name, amount, due date, interval)'
		print '(5): Average expense'
		print '(6): Return to main menu\n'
		s = raw_input()
		return s
		
	def savings_item_menu(self):
		print '\nSavings Item Menu'
		print '*******************'
		print '(1): Add a savings item'
		print '(2): Remove a savings item'
		print '(3): Show savings item values'
		print '(4): Change savings item values'
		print '(5): Add savings item to expense list'
		print '(6): Return to main menu\n'
		s = raw_input()
		return s
		
	def budget_menu(self):
		print '\nBudget Menu'
		print '*******************'
		print '(1): Show budget'
		print '(2): Return to main menu\n'
		s = raw_input()
		return s
		
	def expenses_due_menu(self):
		print '\nExpenses Due Menu'
		print '*******************'
		print '(1): Show expenses due'
		print '(2): Record a payment'
		print '(3): Return to main menu\n'
		s = raw_input()
		return s
		
	def transaction_menu(self):
		print '\nTransaction Menu'
		print '*******************'
		print '(1): Add a transaction'
		print '(2): Show income payments'
		print '(3): Show expense payments'
		print '(4): Show credits'
		print '(5): Show debits'
		print '(6): Search for a transaction'
		print '(7): Edit a transaction'
		print '(8): Delete a transaction'
		print '(9): Return to main menu\n'
		s = raw_input()
		return s
		
	def test_users_exist(self):
		if len(self.init.userList) == 0:
			return False
		else: return True
			
	def display(self):
		self.welcome()
		self.init.load()
		try:
			self.user = self.init.userList[0]
			os.system('title Current user is '+self.user.name)
		except:
			pass
		self.income = self.user.get_primary_income()
		sel = self.main_menu()
		while sel:
			if sel == '1':
				subsel = self.user_menu()
				while subsel:
					if subsel == '1':
						print 'What is the user''s name to add?'
						name = raw_input()
						self.init.addUser(name)
						self.init.save()
						for u in self.init.userList:
							if name == u.name:
								self.user = u
						subsel = self.user_menu()
					elif subsel == '2':
						print '\n'
						count = 0
						for u in self.init.userList:
							print '('+str(count+1)+'):', u.name
							count += 1
						print '\nEnter the number of the user you would like to remove:'
						index = raw_input()
						if index == '':
							index = 0
						else: index = int(index)
						try:
							print '\n', self.init.userList[index-1].name, 'has been removed'
							self.init.removeUser(self.init.userList[index-1].name)
						except:
							print '\nThere are no users yet or the index you selected is out of range.'
						subsel = self.user_menu()
					elif subsel == '3':
						print 'Current user is: ', self.user.name
						subsel = self.user_menu()
					elif subsel == '4':
						print '\n'
						count = 0
						for u in self.init.userList:
							print '('+str(count+1)+'):', u.name
							count += 1
						print '\nEnter the number of the user you would like to switch to:'
						index = raw_input()
						if index == '':
							index = 0
						else: index = int(index)
						try:
							self.user = self.init.userList[index-1]
							self.income = self.user.get_primary_income()
							print '\nYou selected the user:', self.user.name
							os.system('title Current user is '+self.user.name)
						except:
							print '\nThere are no users yet or the index you selected is out of range. '
							print 'Try creating a new user or select one from the list, option (1)\n'
						subsel = self.user_menu()
					elif subsel == '5':
						self.user.info()
						subsel = self.user_menu()
					elif subsel == '6':
						if len(self.user.incomeList) > 0:
							print '\n'
							count = 0
							for i in self.user.incomeList:
								print '('+str(count+1)+'):', i.name
								count += 1
							print '\nEnter the number of the income this payment came from:'
							index = raw_input()
							if index == '':
								index = 0
							else: index = int(index)
							print '\nEnter the amount you got paid:'
							amount = raw_input()
							if amount == '':
								amount = 0
							else: amount = float(amount)
							self.user.got_paid(self.user.incomeList[index-1], amount)
							os.system('title transfer amounts: income_in: '+str(round(self.user.b.left_after_save_amount(self.user, self.user.incomeList[index-1]), 2))+' bills_out: '+str(round(self.user.b.set_aside(self.user, self.user.incomeList[index-1]), 2))+' savings: '+str(round(self.user.b.save_amount(self.user, self.user.incomeList[index-1]), 2)))
							os.startfile('http:\\\www.bankofamerica.com')
						else:
							print '\nYou have no incomes to choose from at this time'
						subsel = self.user_menu()
					elif subsel == '7':
						print '\nWhat is the name of the credit?'
						name = raw_input()
						print '\nWhat is the credit amount?'
						amount = raw_input()
						if amount == '':
							amount = 0
						else: amount = float(amount)
						self.user.savings.r.add_transaction(self.user, transaction(name, amount, datetime.now(), '', '', 'credit'), self.user.savings)
						c = credit(name, amount, datetime.now())
						print '\nAdd this credit to the income list as a regular income (y or n)?'
						answer = raw_input()
						if answer == 'y' or answer == 'Y':
							for i in self.user.incomeList:
								if c.name in i.name or c.name == i.name:
									self.user.removeIncome(i.name)
							c.add_to_incomeList(self.user, c)
							self.init.save()
						subsel = self.user_menu()
					elif subsel == '8':
						self.init.save()
						sel = self.main_menu()
						break
					else:
						print 'You did not enter a valid selection. Please try again.\n'
						subsel = self.user_menu()
			elif sel == '2' and self.test_users_exist() == True:
				subsel = self.account_menu()
				while subsel:
					if subsel == '1':
						print '\nIncome in balance =', round(self.user.income_in.balance, 2)
						print '\nBills out balance =', round(self.user.bills_out.balance, 2)
						print '\nSavings balance =', round(self.user.savings.balance, 2)
						print '\nTotal balance =', round((self.user.income_in.balance+self.user.bills_out.balance+self.user.savings.balance), 2)
						subsel = self.account_menu()
					if subsel == '2':
						subsubsel = self.change_account_menu()
						while subsubsel:
							if subsubsel == '1':
								print '\nEnter the new amount'
								amount = raw_input()
								if amount == '':
									amount = 0
								else: amount = float(amount)
								self.user.income_in.balance = amount
								print '\nNew Income in balance is:', self.user.income_in.balance, '\n'
								subsubsel = self.change_account_menu()
							elif subsubsel == '2':
								print '\nEnter the new amount'
								amount = raw_input()
								if amount == '':
									amount = 0
								else: amount = float(amount)
								self.user.bills_out.balance = amount
								print '\nNew Bills out balance is:', self.user.bills_out.balance, '\n'
								subsubsel = self.change_account_menu()
							elif subsubsel == '3':
								print '\nEnter the new amount'
								amount = raw_input()
								if amount == '':
									amount = 0
								else: amount = float(amount)
								self.user.savings.balance = amount
								print '\nNew Savings balance is:', self.user.savings.balance, '\n'
								subsubsel = self.change_account_menu()
							elif subsubsel == '4':
								subsel = self.account_menu()
								break
							else:
								print '\nYou did not enter a valid selection. Please try again.'
								subsubsel = self.change_account_menu()
					elif subsel == '3':
						self.init.save()
						sel = self.main_menu()
						break
					else:
						print '\nYou did not enter a valid selection. Please try again.'
						subsel = self.account_menu()
			elif sel == '3' and self.test_users_exist() == True:
				subsel = self.income_menu()
				while subsel:
					if subsel == '1':
						print '\nWhat is the name of the income to add?'
						name = raw_input()
						print '\nWhat is the income amount(not the amount per hour,'
						print 'but the amount you make each paycheck)?.'
						amount = raw_input()
						if amount == '':
							amount = 0
						else: amount = float(amount)
						if amount == '':
							amount = 0
						else: amount = float(amount)
						print '\nHow often are you paid? Example: I get paid every 1 week.'
						print '\nI would enter 1 for the first value, and w for the second value'
						print '\nfirst value: '
						number = int(raw_input())
						print '\nsecond value: '
						designator = raw_input()
						try:
							self.user.addIncome(name,amount,number,designator)
							self.income = income(name,amount,number,designator)
							self.init.save()
						except:
							print '\nUser does not exist, you must add this user'
						subsel = self.income_menu()
					elif subsel == '2':
						print '\n'
						count = 0
						for i in self.user.incomeList:
							print '('+str(count+1)+'):', i.name
							count += 1
						print '\nEnter the number of the income you would like to remove:'
						index = raw_input()
						if index == '':
							index = 0
						else: index = int(index)
						self.user.removeIncome(self.user.incomeList[index-1].name)
						subsel = self.income_menu()
					elif subsel == '3':
						if len(self.user.incomeList) > 0:
							print '\nIncome name:', self.income.name
							print '\nIncome amount:', self.income.amount
							des = ''
							if self.income.frequencyDesignator == 'd':
								des = 'days'
							elif self.income.frequencyDesignator == 'w':
								des = 'weeks'
							elif self.income.frequencyDesignator == 'm':
								des = 'months'
							elif self.income.frequencyDesignator == 'y':
								des = 'years'
							print '\nIncome is paid every', self.income.frequencyNumber, des,'\n'
						else:
							print '\nYou have no incomes to view at this time'
						subsel = self.income_menu()
					elif subsel == '4':
						print '\n'
						count = 0
						for i in self.user.incomeList:
							print '('+str(count+1)+'):', i.name
							count += 1
						print '\nEnter the number of the income you would like to change values for:'
						index = raw_input()
						if index == '':
							index = 0
						else: index = int(index)
						print '\nIncome name:', self.income.name
						print '\nIncome amount:', self.income.amount
						des = ''
						if self.income.frequencyDesignator == 'd':
							des = 'days'
						elif self.income.frequencyDesignator == 'w':
							des = 'weeks'
						elif self.income.frequencyDesignator == 'm':
							des = 'months'
						elif self.income.frequencyDesignator == 'y':
							des = 'years'
						print '\nIncome is paid every', self.income.frequencyNumber, des
						print '\nChange name? (y or n):'
						change = raw_input()
						if change == 'y'  or change == 'Y':
							print '\nEnter name: '
							name = raw_input()
						else:
							name = self.user.incomeList[index-1].name
						print '\nChange amount? (y or n)'
						change = raw_input()
						if change == 'y'  or change == 'Y':
							print '\nEnter amount: '
							amount = raw_input()
							if amount == '':
								amount = 0
							else: amount = float(amount)
						else:
							amount = self.user.incomeList[index-1].amount
						print '\nChange date? (y or n)'
						change = raw_input()
						if change == 'y'  or change == 'Y':
							print '\nEnter the year first, then the month, then the day'
							print 'year: '
							year = int(raw_input())
							print 'month: '
							month = int(raw_input())
							print 'day: '
							day = int(raw_input())
							date = datetime(year,month,day)
						else:
							date = self.user.incomeList[index-1].date
						print '\nChange pay interval? (y or n)'
						change = raw_input()
						if change == 'y'  or change == 'Y':
							print '\nHow often are you paid? Example: I get paid every 1 week.'
							print '\nI would enter 1 for the first value, and w for the second value'
							print '\nfirst value: '
							print change
							number = int(raw_input())
							print '\nsecond value: '
							designator = raw_input()
						else:
							number = self.user.incomeList[index-1].frequencyNumber
							designator = self.user.incomeList[index-1].frequencyDesignator
						self.user.incomeList[index-1].change_values(name, amount, date, number, designator)
						subsel = self.income_menu()
					elif subsel == '5':
						print '\n'
						count = 0
						for i in self.user.incomeList:
							print '('+str(count+1)+'):', i.name
							count += 1
						print '\nEnter the number of the income you would like to switch to:'
						index = raw_input()
						if index == '':
							index = 0
						else: index = int(index)
						try:
							self.income = self.user.incomeList[index-1]
							print '\nYou selected the income: ', self.income.name
						except:
							print '\nThere are no incomes yet or the index you selected is out of range. '
							print '\nTry creating a new income or select one from the list, option (1)'
						subsel = self.income_menu()
					elif subsel == '6':
						print '\nThis option allows you to designate which income you want to be your primary income'
						print '\nEnter the name of the income you would like to set as primary.'
						print '\n'
						count = 0
						for i in self.user.incomeList:
							print '('+str(count+1)+'):', i.name
							count += 1
						print '\nEnter the number of the income you would like to set as primary:'
						index = raw_input()
						if index == '':
							index = 0
						else: index = int(index)
						try:
							self.income = self.user.incomeList[index-1]
							self.user.set_primary_income(self.user.incomeList[index-1].name)
							print '\nYour primary income has been set to:', self.income.name
						except:
							print '\nThere are no incomes yet or the index you selected is out of range. '
							print '\nTry creating a new income or select one from the list, option (1)\n'
						subsel = self.income_menu()
					elif subsel == '7':
						if len(self.user.incomeList) > 0:
							print '\nYour primary income has been set to:', self.user.get_primary_income().name
						else: print '\nYou must have an income to use this selection. Please enter an income.'
						subsel = self.income_menu()
					elif subsel == '8':
						print '\n'
						count = 0
						for i in self.user.incomeList:
							print '('+str(count+1)+'):', i.name
							count += 1
						print '\nEnter the number of the income you would like to see average info for:'
						index = raw_input()
						if index == '':
							index = 0
						else: index = int(index)
						print '\nIncome history:\n'
						for i in self.user.income_in.r.filter_got_paid(self.user.incomeList[index-1].name):
							print i.name, i.amount, i.date
						if len(self.user.income_in.r.filter_got_paid()) == 0:
							print 'There is no income history yet'
						print '\nThe average amount for this income is:', self.user.income_in.r.average_income(self.user.incomeList[index-1].name)
						print '\nWould you like to use this average amount in your budget? (y or n)'
						answer = raw_input()
						if answer == 'y' or answer == 'Y':
							self.user.incomeList[index-1].amount = self.user.income_in.r.average_income(self.user.incomeList[index-1].name)
						subsel = self.income_menu()
					elif subsel == '9':
						self.init.save()
						sel = self.main_menu()
						break
					else:
						print '\nYou did not enter a valid selection. Please try again.'
						subsel = self.income_menu()
			elif sel == '4' and self.test_users_exist() == True:
				subsel = self.expense_menu()
				while subsel:
					if subsel == '1':
						print '\nWhat is the name of the expense to add?'
						name = raw_input()
						print '\nWhat is the expense amount?'
						amount = raw_input()
						if amount == '':
							amount = 0
						else: amount = float(amount)
						print '\nWhat is the due date of this expense?'
						print '\nEnter the year first, then the month, then the day'
						print 'year: '
						year = raw_input()
						print 'month: '
						month = raw_input()
						print 'day: '
						day = raw_input()
						if year == '' or month == '' or day == '':
							date = datetime.now()
						else:
							year = int(year)
							month = int(month)
							day = int(day)
							date = datetime(year,month,day)
						print '\nHow often is this bill due? Example: I pay this bill every month.'
						print '\nI would enter 1 for the first value, and m for the second value\n'
						print 'first value: '
						number = int(raw_input())
						print 'second value: '
						designator = raw_input()
						try:
							self.user.addExpense(name,amount,date,number,designator)
						except:
							print '\nUser is not in the list, you must add this user'
						subsel = self.expense_menu()
					elif subsel == '2':
						print '\n'
						count = 0
						for e in self.user.expenseList:
							print '('+str(count+1)+'):', e.name
							count += 1
						print '\nEnter the number of the expense you would like to remove:'
						index = raw_input()
						if index == '':
							index = 0
						else: index = int(index)
						self.user.removeExpense(self.user.expenseList[index-1].name)
						subsel = self.expense_menu()
					elif subsel == '3':
						if len(self.user.expenseList) > 0:
							print '\n'
							count = 0
							for e in self.user.expenseList:
								print '('+str(count+1)+'):', e.name
								count += 1
							print '\nEnter the number of the expense you would like see info for:'
							index = raw_input()
							if index == '':
								index = 0
							else: index = int(index)
							print '\nExpense name:', self.user.expenseList[index-1].name
							print '\nExpense amount:', self.user.expenseList[index-1].amount
							print '\nExpense due date:', self.user.expenseList[index-1].date.date()
							des = ''
							if self.user.expenseList[index-1].frequencyDesignator == 'd':
								des = 'days'
							elif self.user.expenseList[index-1].frequencyDesignator == 'w':
								des = 'weeks'
							elif self.user.expenseList[index-1].frequencyDesignator == 'm':
								des = 'months'
							elif self.user.expenseList[index-1].frequencyDesignator == 'y':
								des = 'years'
							print '\nExpense is paid every', self.user.expenseList[index-1].frequencyNumber, des,'\n'
						else:
							print '\nYou have no expenses at this time'
						subsel = self.expense_menu()
					elif subsel == '4':
						print '\n'
						count = 0
						for e in self.user.expenseList:
							print '('+str(count+1)+'):', e.name
							count += 1
						print '\nEnter the number of the expense you would like to change values for:'
						index = raw_input()
						if index == '':
							index = 0
						else: index = int(index)
						print '\nExpense name:', self.user.expenseList[index-1].name
						print '\nExpense amount:', self.user.expenseList[index-1].amount
						print '\nExpense date:', self.user.expenseList[index-1].date.date()
						des = ''
						if self.user.expenseList[index-1].frequencyDesignator == 'd':
							des = 'days'
						elif self.user.expenseList[index-1].frequencyDesignator == 'w':
							des = 'weeks'
						elif self.user.expenseList[index-1].frequencyDesignator == 'm':
							des = 'months'
						elif self.user.expenseList[index-1].frequencyDesignator == 'y':
							des = 'years'
						print '\nExpense is due every', self.user.expenseList[index-1].frequencyNumber, des
						print '\nChange name? (y or n):'
						change = raw_input()
						if change == 'y'  or change == 'Y':
							print '\nEnter name: '
							name = raw_input()
						else:
							name = self.user.expenseList[index-1].name
						print '\nChange amount? (y or n)'
						change = raw_input()
						if change == 'y'  or change == 'Y':
							print '\nEnter amount: '
							amount = raw_input()
							if amount == '':
								amount = 0
							else: amount = float(amount)
						else:
							amount = self.user.expenseList[index-1].amount
						print '\nChange date? (y or n)'
						change = raw_input()
						if change == 'y'  or change == 'Y':
							print '\nEnter the year first, then the month, then the day'
							print 'year: '
							year = int(raw_input())
							print 'month: '
							month = int(raw_input())
							print 'day: '
							day = int(raw_input())
							date = datetime(year,month,day)
						else:
							date = self.user.expenseList[index-1].date
						print '\nChange interval? (y or n)'
						change = raw_input()
						if change == 'y'  or change == 'Y':
							print '\nHow often is this bill due? Example: This bill is due every 1 month.'
							print '\nI would enter 1 for the first value, and m for the second value'
							print '\nfirst value: '
							print change
							number = int(raw_input())
							print '\nsecond value: '
							designator = raw_input()
						else:
							number = self.user.expenseList[index-1].frequencyNumber
							designator = self.user.expenseList[index-1].frequencyDesignator
						self.user.expenseList[index-1].change_values(name, amount, date, number, designator)
						subsel = self.expense_menu()
					elif subsel == '5':
						print '\n'
						count = 0
						for e in self.user.expenseList:
							print '('+str(count+1)+'):', e.name
							count += 1
						print '\nEnter the number of the expense you would like to see average info for:'
						index = raw_input()
						if index == '':
							index = 0
						else: index = int(index)
						print '\nExpense history:\n'
						for e in self.user.bills_out.r.filter_expense(self.user.expenseList[index-1].name):
							print e.name, e.amount, e.date
						if len(self.user.bills_out.r.filter_expense()) == 0:
							print 'There is no expense history yet'
						print '\nThe average amount for this expense is:', self.user.bills_out.r.average_expense(self.user.expenseList[index-1].name)
						print '\nWould you like to use this average amount in your budget? (y or n)'
						answer = raw_input()
						if answer == 'y' or answer == 'Y':
							self.user.expenseList[index-1].amount = self.user.bills_out.r.average_expense(self.user.expenseList[index-1].name)
						subsel = self.expense_menu()
					elif subsel == '6':
						self.init.save()
						sel = self.main_menu()
						break
					else:
						print '\nYou did not enter a valid selection. Please try again.\n'
						subsel = self.expense_menu()
			elif sel == '5' and self.test_users_exist() == True:
				subsel = self.savings_item_menu()
				while subsel:
					if subsel == '1':
						print '\nWhat is the name of the savings item to add?'
						name = raw_input()
						print '\nWhat is the savings item amount?'
						amount = raw_input()
						if amount == '':
							amount = 0
						else: amount = float(amount)
						print '\nWhat is the due date of this savings item?'
						print '\nEnter the year first, then the month, then the day'
						print 'year: '
						year = raw_input()
						print 'month: '
						month = raw_input()
						print 'day: '
						day = raw_input()
						if year == '' or month == '' or day == '':
							date = datetime.now()
						else:
							year = int(year)
							month = int(month)
							day = int(day)
							date = datetime(year,month,day)
						try:
							self.user.addSavingsItem(name,amount,date)
						except:
							print '\nUser is not in the list, you must add this user'
						subsel = self.savings_item_menu()
					elif subsel == '2':
						print '\n'
						count = 0
						for s in self.user.savingsItemList:
							print '('+str(count+1)+'):', s.name
							count += 1
						print '\nEnter the number of the savings item you would like to remove:'
						index = raw_input()
						if index == '':
							index = 0
						else: index = int(index)
						self.user.removeSavingsItem(self.user.savingsItemList[index-1].name)
						subsel = self.savings_item_menu()
					elif subsel == '3':
						if len(self.user.savingsItemList) > 0:
							print '\n'
							count = 0
							for s in self.user.savingsItemList:
								print '('+str(count+1)+'):', s.name
								count += 1
							print '\nEnter the number of the savings item you would like see info for:'
							index = raw_input()
							if index == '':
								index = 0
							else: index = int(index)
							print '\nSavings item name:', self.user.savingsItemList[index-1].name
							print '\nSavings item amount:', self.user.savingsItemList[index-1].amount
							print '\nSavings item due date:', self.user.savingsItemList[index-1].date.date()
						else:
							print '\nYou have no savings items at this time'
						subsel = self.savings_item_menu()
					elif subsel == '4':
						print '\n'
						count = 0
						for s in self.user.savingsItemList:
							print '('+str(count+1)+'):', s.name
							count += 1
						print '\nEnter the number of the savings item you would like to change values for:'
						index = raw_input()
						if index == '':
							index = 0
						else: index = int(index)
						print '\nSavings item name:', self.user.savingsItemList[index-1].name
						print '\nSavings item amount:', self.user.savingsItemList[index-1].amount
						print '\nSavings item date:', self.user.savingsItemList[index-1].date.date()
						print '\nChange name? (y or n):'
						change = raw_input()
						if change == 'y' or change == 'Y':
							print '\nEnter name: '
							name = raw_input()
						else:
							name = self.user.savingsItemList[index-1].name
						print '\nChange amount? (y or n)'
						change = raw_input()
						if change == 'y' or change == 'Y':
							print '\nEnter amount: '
							amount = raw_input()
							if amount == '':
								amount = 0
							else: amount = float(amount)
						else:
							amount = self.user.savingsItemList[index-1].amount
						print '\nChange date? (y or n)'
						change = raw_input()
						if change == 'y' or change == 'Y':
							print '\nEnter the year first, then the month, then the day'
							print 'year: '
							year = int(raw_input())
							print 'month: '
							month = int(raw_input())
							print 'day: '
							day = int(raw_input())
							date = datetime(year,month,day)
						else:
							date = self.user.savingsItemList[index-1].date
						self.user.savingsItemList[index-1].change_values(self.user, name, amount, date)
						subsel = self.savings_item_menu()
					elif subsel == '5':
						print '\n'
						count = 0
						for s in self.user.savingsItemList:
							print '('+str(count+1)+'):', s.name
							count += 1
						print '\nEnter the number of the savings item you would like to add to the expense list:'
						index = raw_input()
						if index == '':
							index = 0
						else: index = int(index)
						if len(self.user.incomeList) > 0:
							self.user.savingsItemList[index-1].add_to_expenseList(self.user)
						else: print '\nYou must have an income to use this selection. Please enter an income.'
						subsel = self.savings_item_menu()
					elif subsel == '6':
						self.init.save()
						sel = self.main_menu()
						break
					else:
						print '\nYou did not enter a valid selection. Please try again.\n'
						subsel = self.savings_item_menu()
			elif sel == '6' and self.test_users_exist() == True:
				print 'save percent: ', str(round(self.user.b.save_percent(self.user), 4)*100)+'%'
				print 'monthly savings: ', round(self.user.b.monthly_savings(self.user), 2)
				print 'daily allowance: ', round(self.user.b.daily_allowance(self.user), 2)
				print 'weekly allowance: ', round(self.user.b.weekly_allowance(self.user), 2)
				print 'monthly allowance: ', round(self.user.b.monthly_allowance(self.user), 2), '\n'
				print 'incomes:\n'
				for i in self.user.incomeList:
					print 'name: ', i.name+';', 'amount: ', str(i.amount)+';', 'date: ', str(i.date.date())+';', 'frequencyNumber: ', str(i.frequencyNumber)+';', 'frequencyDesignator: ', i.frequencyDesignator
					print 'set aside: ', round(self.user.b.set_aside(self.user, i), 2), ' -----> This gets put into bills_out account'
					print 'save amount: ', round(self.user.b.save_amount(self.user, i), 2), ' -----> This gets put into savings'
					print 'left after save amount: ', round(self.user.b.left_after_save_amount(self.user, i), 2), ' -----> This stays in income_in account\n'
				print '\nexpenses:\n'
				for e in self.user.expenseList:
					print 'name: ', e.name+';', 'amount: ', str(e.amount)+';', 'date: ', str(e.date.date())+';', 'frequencyNumber: ', str(e.frequencyNumber)+';', 'frequencyDesignator: ', e.frequencyDesignator
				print '\nsavings items:\n'
				for s in self.user.savingsItemList:
					print 'name: ', s.name+';', 'amount: ', str(s.amount)+';', 'date: ', s.date.date()
				print '\n'
				sel = self.main_menu()
			elif sel == '7' and self.test_users_exist() == True:
				subsel = self.expenses_due_menu()
				while subsel:
					if subsel == '1':
						self.user.show_expenses_due()
						subsel = self.expenses_due_menu()
					elif subsel == '2':
						edDict = self.user.ed.expenses_due(self.user)
						nameList = []
						for n in edDict:
							nameList.append(n)
						if len(edDict) > 0:
							self.user.show_expenses_due()
							print '\n'
							count = 0
							for e in self.user.ed.expenses_due(self.user):
								print '('+str(count+1)+'):', e
								count += 1
							print '\nEnter the number of the expense you would like to record a payment for:'
							index = raw_input()
							if index == '':
								index = 0
							else: index = int(index)
							name = nameList[index-1]
							print '\nWhat is the amount of the item?'
							amount = raw_input()
							if amount == '':
								amount = 0
							else: amount = float(amount)
							print '\nIs there a confirmation # for this payment? (y or n)'
							answer = raw_input()
							if answer == 'y' or answer == 'Y':
								print '\nEnter the confirmation number: '
								conf = raw_input()
							else:
								conf = ''
							print '\nWould you like to add a note or memo for this payment? (y or n)'
							answer = raw_input()
							if answer == 'y' or answer == 'Y':
								print '\nEnter the note or memo: '
								note = raw_input()
							else:
								note = ''
							self.user.ed.record_payment(self.user, name, amount*-1, conf, note)
						else: print 'There are no bills to pay at this time' 
						subsel = self.expenses_due_menu()
					elif subsel == '3':
						self.init.save()
						sel = self.main_menu()
						break
					else:
						print '\nYou did not enter a valid selection. Please try again.\n'
						subsel = self.expenses_due_menu()
			elif sel == '8' and self.test_users_exist() == True:
				subsel = self.transaction_menu()
				while subsel:
					total = 0.0
					if subsel == '1':
						print '\nWhich account will this transaction coming be involving?'
						print '\n(1): Income in'
						print '(2): Bills out'
						print '(3): Savings\n'
						account = raw_input()
						if account == '1':
							account = self.user.income_in
						elif account == '2':
							account = self.user.bills_out
						elif account == '3':
							account = self.user.savings
						print '\nWhat is the name of the transaction?'
						name = raw_input()
						print '\nWhat is the amount of the transaction?'
						amount = raw_input()
						if amount == '':
							amount = 0
						else: amount = float(amount)
						print '\nIs there a confirmation # for this payment? (y or n)'
						answer = raw_input()
						if answer == 'y' or answer == 'Y':
							print '\nEnter the confirmation number: '
							conf = raw_input()
						else:
							conf = ''
							print 'in conf else'
						print '\nWould you like to add a note or memo for this payment? (y or n)'
						answer = raw_input()
						if answer == 'y' or answer == 'Y':
							print '\nEnter the note or memo: '
							note = raw_input()
						else:
							note = ''
							print 'in note else'
						print '\nWhat type of transaction is this? Credit or Debit (c or d)'
						type = raw_input()
						if type == 'c' or type == 'C':
							type = 'credit'
							account.r.add_transaction(self.user, transaction(name, amount, datetime.now(), conf, note, type), account)
							self.init.save()
						elif type == 'd' or type == 'D':
							type = 'debit'
							amount *= -1
							account.r.add_transaction(self.user, transaction(name, amount, datetime.now(), conf, note, type), account)
							self.init.save()
						else: 
							type = 'debit'
							amount *= -1
							account.r.add_transaction(self.user, transaction(name, amount, datetime.now(), conf, note, type), account)
							self.init.save()
						subsel = self.transaction_menu()
					elif subsel == '2':
						print '\nIncome payments:\n'
						t = self.user.income_in.r.filter_got_paid()
						for g in t:
							print g.name, g.amount, g.date.date(), g.conf, g.note
							total += g.amount
						print '\nTotal = ', total
						total = 0
						subsel = self.transaction_menu()
					elif subsel == '3':
						print '\nExpense payments:\n'
						t = self.user.bills_out.r.filter_expense()
						for e in t:
							print e.name, e.amount, e.date.date(), e.conf, e.note
							total += e.amount
						print '\nTotal = ', total
						total = 0
						subsel = self.transaction_menu()
					elif subsel == '4':
						print '\nCredits to income_in account not including income payments:\n'
						t = self.user.savings.r.filter_credit()
						for c in t:
							print c.name, c.amount, c.date.date(), c.conf, c.note
							total += c.amount
						for cr in self.user.get_credits():
							print cr.name, cr.amount, cr.date.date(), cr.conf, cr.note
							total += cr.amount
						print '\nTotal = ', total
						total = 0
						subsel = self.transaction_menu()
					elif subsel == '5':
						print '\nDebits from income_in account not including expense payments:\n'
						t = self.user.income_in.r.filter_debit()
						for d in t:
							print d.name, d.amount, d.date.date(), d.conf, d.note
							total += d.amount
						print '\nTotal = ', total
						total = 0
						subsel = self.transaction_menu()
					elif subsel == '6':
						total = 0
						tlist = self.user.get_all_transactions()
						search_results = []
						print '\nEnter the search string you would like to find:'
						search = raw_input()
						print '\n'
						if search != '':
							search_results = [t for t in tlist if re.search(search, t.name, re.I) or re.search(search, t.note, re.I)]
							for s in search_results:
								print s.name, s.amount, s.date.date(), s.conf, s.note
								total += s.amount
							if len(search_results) == 0:
								print '\nThere are no transactions that match that criteria\n'
							else:
								print '\nTotal is: ', total
						else:
							search_results = tlist
							for s in search_results:
								print s.name, s.amount, s.date.date(), s.conf, s.note
								total += s.amount
							if len(search_results) == 0:
								print '\nThere are no transactions that match that criteria\n'
							else:
								print '\nTotal is: ', total
						subsel = self.transaction_menu()
					elif subsel == '7':
						tempTList = self.user.get_all_transactions()
						print '\n'
						count = 0
						try:
							for t in tempTList:
								print '('+str(count+1)+'):', t.name, t.amount, t.date, t.conf, t.note
								count += 1
							print '\nEnter the number of the transaction you would like to edit:'
							index = raw_input()
							if index == '':
								index = 0
							else: index = int(index)
							print '\nChange name? (y or n):'
							change = raw_input()
							if change == 'y' or change == 'Y':
								print '\nEnter name: '
								name = raw_input()
							else:
								name = tempTList[index-1].name
							print '\nChange amount? (y or n)'
							change = raw_input()
							if change == 'y' or change == 'Y':
								print '\nEnter amount: '
								amount = raw_input()
								if amount == '':
									amount = 0
								else: amount = float(amount)
							else:
								amount = tempTList[index-1].amount
							print '\nChange date? (y or n)'
							change = raw_input()
							if change == 'y' or change == 'Y':
								print '\nEnter the year first, then the month, then the day'
								print 'year: '
								year = int(raw_input())
								print 'month: '
								month = int(raw_input())
								print 'day: '
								day = int(raw_input())
								date = datetime(year,month,day)
							else:
								date = tempTList[index-1].date
							print '\nChange confirmation #? (y or n)'
							answer = raw_input()
							if answer == 'y' or answer == 'yes' or answer == 'Yes' or answer == 'Y':
								print '\nEnter the confirmation number: '
								conf = raw_input()
							else:
								conf = ''
							print '\nChange note/memo? (y or n)'
							answer = raw_input()
							if answer == 'y' or answer == 'yes' or answer == 'Yes' or answer == 'Y':
								print '\nEnter the note or memo: '
								note = raw_input()
							else:
								note = ''
							self.user.get_all_transactions()[index-1].name = name
							self.user.get_all_transactions()[index-1].amount = amount
							self.user.get_all_transactions()[index-1].date = date
							self.user.get_all_transactions()[index-1].conf = conf
							self.user.get_all_transactions()[index-1].note = note
						except IOError as message: print message
						subsel = self.transaction_menu() 
					elif subsel == '8':
						tempTList = self.user.get_all_transactions()
						print '\n'
						count = 0
						try:
							for t in tempTList:
								print '('+str(count+1)+'):', t.name, t.amount, t.date, t.conf, t.note
								count += 1
							print '\nEnter the number of the transaction you would like to delete:'
							index = raw_input()
							if index == '':
								index = 0
							else: index = int(index)
							if tempTList[index-1] in self.user.income_in.r.registerList: self.user.income_in.r.remove_transaction(index-1)
							if tempTList[index-1] in self.user.bills_out.r.registerList: self.user.bills_out.r.remove_transaction(index-1)
							if tempTList[index-1] in self.user.savings.r.registerList: self.user.savings.r.remove_transaction(index-1)
						except IOError as message: print message
						subsel = self.transaction_menu()
					elif subsel == '9':
						self.init.save()
						sel = self.main_menu()
						break
					else:
						print '\nYou did not enter a valid selection. Please try again.\n'
						subsel = self.transaction_menu()
			else:
				print '\nYou did not enter a valid selection or no users have been created yet. Please try again.\n'
				sel = self.main_menu()


c = console_display()
c.display()
