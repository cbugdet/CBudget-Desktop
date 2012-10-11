#Boa:Frame:Home

import wx
import wx.gizmos
import time
import threading
from CBudgetP import *
import CBudgetP_Accounts
import CBudgetP_Incomes
import CBudgetP_Credits
import CBudgetP_Expenses
import CBudgetP_SavingsItems
import CBudgetP_Budget
import CBudgetP_ExpensesDue
import CBudgetP_Transactions


def create(parent):
	return Home(parent)

[wxID_HOME, wxID_HOMEBUTTONACCOUNTS, wxID_HOMEBUTTONBUDGET, 
 wxID_HOMEBUTTONCLOSE, wxID_HOMEBUTTONCREDITS, wxID_HOMEBUTTONENTERUSERNAME, 
 wxID_HOMEBUTTONEXPENSES, wxID_HOMEBUTTONEXPENSESDUE, wxID_HOMEBUTTONINCOMES, 
 wxID_HOMEBUTTONSAVINGSITEMS, wxID_HOMEBUTTONTRANSACTIONS, 
 wxID_HOMECHECKBOXCHANGEPASSWORD, wxID_HOMEPANEL1, 
 wxID_HOMESTATICTEXTUSERNAME, wxID_HOMETEXTCTRLUSERNAME, 
] = [wx.NewId() for _init_ctrls in range(15)]

class Home(wx.Frame):
	def _init_ctrls(self, prnt):
		# generated method, don't edit
		wx.Frame.__init__(self, id=wxID_HOME, name='Home', parent=prnt,
			  pos=wx.Point(382, 139), size=wx.Size(601, 449), style=wx.CAPTION,
			  title='Welcome to CBudget')
		self.SetClientSize(wx.Size(585, 411))
		self.Center(wx.BOTH)
		self.Bind(wx.EVT_ACTIVATE, self.OnHomeActivate)
		self.Bind(wx.EVT_IDLE, self.OnHomeIdle)

		self.panel1 = wx.Panel(id=wxID_HOMEPANEL1, name='panel1', parent=self,
			  pos=wx.Point(0, 0), size=wx.Size(585, 411),
			  style=wx.TAB_TRAVERSAL)
		self.panel1.Show(True)
		self.panel1.SetThemeEnabled(True)
		self.panel1.SetToolTipString('Welcome to CBudget')
		self.panel1.SetAutoLayout(False)
		self.panel1.SetBackgroundStyle(wx.BG_STYLE_SYSTEM)
		self.panel1.Bind(wx.EVT_MOTION, self.OnPanel1Motion)

		self.textCtrlUserName = wx.TextCtrl(id=wxID_HOMETEXTCTRLUSERNAME,
			  name='textCtrlUserName', parent=self.panel1, pos=wx.Point(150,
			  88), size=wx.Size(200, 21), style=wx.TE_CENTER, value='')
		self.textCtrlUserName.SetToolTipString('Enter User Name or Password')
		self.textCtrlUserName.Bind(wx.EVT_TEXT, self.OnTextCtrlUserNameText,
			  id=wxID_HOMETEXTCTRLUSERNAME)

		self.buttonEnterUserName = wx.Button(id=wxID_HOMEBUTTONENTERUSERNAME,
			  label='Enter', name='buttonEnterUserName', parent=self.panel1,
			  pos=wx.Point(352, 87), size=wx.Size(75, 23), style=0)
		self.buttonEnterUserName.Enable(False)
		self.buttonEnterUserName.SetToolTipString('Enter User Name or Password')
		self.buttonEnterUserName.Bind(wx.EVT_BUTTON,
			  self.OnButtonEnterUserNameButton,
			  id=wxID_HOMEBUTTONENTERUSERNAME)

		self.checkBoxChangePassword = wx.CheckBox(id=wxID_HOMECHECKBOXCHANGEPASSWORD,
			  label='Change Password', name='checkBoxChangePassword',
			  parent=self.panel1, pos=wx.Point(198, 112), size=wx.Size(112, 13),
			  style=0)
		self.checkBoxChangePassword.SetValue(True)
		self.checkBoxChangePassword.Show(False)
		self.checkBoxChangePassword.SetToolTipString('This option allows you to change your password, if you have entered the correct old password in the box. It is a good idea to write down your password and keep it in a safe place. If you lose your password, the only way to reset it is to change users which will delete all of your data.')

		self.buttonAccounts = wx.Button(id=wxID_HOMEBUTTONACCOUNTS,
			  label='Accounts', name='buttonAccounts', parent=self.panel1,
			  pos=wx.Point(96, 168), size=wx.Size(85, 65), style=0)
		self.buttonAccounts.SetToolTipString('Accounts allows you to create, delete, and manage your bank accounts and credit card accounts')
		self.buttonAccounts.Bind(wx.EVT_BUTTON, self.OnButtonAccountsButton,
			  id=wxID_HOMEBUTTONACCOUNTS)

		self.buttonIncomes = wx.Button(id=wxID_HOMEBUTTONINCOMES,
			  label='Incomes', name='buttonIncomes', parent=self.panel1,
			  pos=wx.Point(200, 168), size=wx.Size(85, 65), style=0)
		self.buttonIncomes.SetToolTipString('Incomes allows you to create, delete, and manage your regular recurring incomes')
		self.buttonIncomes.Bind(wx.EVT_BUTTON, self.OnButtonIncomesButton,
			  id=wxID_HOMEBUTTONINCOMES)

		self.buttonCredits = wx.Button(id=wxID_HOMEBUTTONCREDITS,
			  label='Credits', name='buttonCredits', parent=self.panel1,
			  pos=wx.Point(304, 168), size=wx.Size(85, 65), style=0)
		self.buttonCredits.SetToolTipString('Credits allows you to create, delete, and manage credits that are not regular recurring income ')
		self.buttonCredits.Bind(wx.EVT_BUTTON, self.OnButtonCreditsButton,
			  id=wxID_HOMEBUTTONCREDITS)

		self.buttonExpenses = wx.Button(id=wxID_HOMEBUTTONEXPENSES,
			  label='Expenses', name='buttonExpenses', parent=self.panel1,
			  pos=wx.Point(408, 168), size=wx.Size(85, 65), style=0)
		self.buttonExpenses.SetToolTipString('Expenses allows you to create, delete, and manage your regular recurring expenses')
		self.buttonExpenses.Bind(wx.EVT_BUTTON, self.OnButtonExpensesButton,
			  id=wxID_HOMEBUTTONEXPENSES)

		self.buttonSavingsItems = wx.Button(id=wxID_HOMEBUTTONSAVINGSITEMS,
			  label='SavingsItems', name='buttonSavingsItems',
			  parent=self.panel1, pos=wx.Point(96, 248), size=wx.Size(85, 65),
			  style=0)
		self.buttonSavingsItems.SetToolTipString('Savings Items allows you to create, delete, and manage savings items that are not regular recurring expenses')
		self.buttonSavingsItems.Bind(wx.EVT_BUTTON,
			  self.OnButtonSavingsItemsButton, id=wxID_HOMEBUTTONSAVINGSITEMS)

		self.buttonBudget = wx.Button(id=wxID_HOMEBUTTONBUDGET, label='Budget',
			  name='buttonBudget', parent=self.panel1, pos=wx.Point(200, 248),
			  size=wx.Size(85, 65), style=0)
		self.buttonBudget.SetToolTipString('Budget is where you view how much you need to set aside for bills, amount to save, and left over spending money')
		self.buttonBudget.Bind(wx.EVT_BUTTON, self.OnButtonBudgetButton,
			  id=wxID_HOMEBUTTONBUDGET)

		self.buttonExpensesDue = wx.Button(id=wxID_HOMEBUTTONEXPENSESDUE,
			  label='Expenses Due', name='buttonExpensesDue',
			  parent=self.panel1, pos=wx.Point(304, 248), size=wx.Size(85, 65),
			  style=0)
		self.buttonExpensesDue.SetToolTipString('Expenses Due shows which regular recurring expenses are due for this paycheck and allows you to record bills paid in your transaction register')
		self.buttonExpensesDue.Bind(wx.EVT_BUTTON,
			  self.OnButtonExpensesDueButton, id=wxID_HOMEBUTTONEXPENSESDUE)

		self.buttonTransactions = wx.Button(id=wxID_HOMEBUTTONTRANSACTIONS,
			  label='Transactions', name='buttonTransactions',
			  parent=self.panel1, pos=wx.Point(408, 248), size=wx.Size(85, 65),
			  style=0)
		self.buttonTransactions.SetToolTipString('Transactions shows a comprehensive list of recorded transactions such as income payments, expense payments, non-regular income credits, and daily debit and credit transactions for all your accounts')
		self.buttonTransactions.Bind(wx.EVT_BUTTON,
			  self.OnButtonTransactionsButton, id=wxID_HOMEBUTTONTRANSACTIONS)

		self.buttonClose = wx.Button(id=wxID_HOMEBUTTONCLOSE, label='Close',
			  name='buttonClose', parent=self.panel1, pos=wx.Point(258, 364),
			  size=wx.Size(75, 23), style=0)
		self.buttonClose.SetToolTipString('See you next time!')
		self.buttonClose.Bind(wx.EVT_BUTTON, self.OnButtonCloseButton,
			  id=wxID_HOMEBUTTONCLOSE)

		self.staticTextUserName = wx.StaticText(id=wxID_HOMESTATICTEXTUSERNAME,
			  label="Enter User's Name:", name='staticTextUserName',
			  parent=self.panel1, pos=wx.Point(204, 72), size=wx.Size(93, 13),
			  style=0)

	def __init__(self, parent):
		self._init_ctrls(parent) 
		# self.checkBoxChangeUser.SetValue(False)
		self.checkBoxChangePassword.SetValue(False)
		self.enable_buttons(False)
		self.enter_user_name_message = True
		self.message_count = 0
		self.user = None
		if init.userList == []:    
			self.h = home_window()
			wx.MessageBox(self.h.welcome_message, self.h.welcome_title, wx.OK | wx.CENTRE)                     
			self.staticTextUserName.Label = "Create a username:"        
			self.set_backcolor_green(self.textCtrlUserName)          
		else: 
			self.user = init.userList[0]
			self.i = self.user.s._incomes
			init.userList[0].s.show_connection_message = True
			init.userList[0].s.test_mac_connection = True
			init.userList[0].s.mout_mac_volume = True
			init.userList[0].s.active_frame = str(self)._formatter_field_name_split()[0][1:]
			self.h = init.userList[0].s._home
			self.h.run_count += 1    
			self.Title = '{0}, {1}'.format(init.userList[0].name,'welcome to CBudget')            
			self.staticTextUserName.Label = 'Enter your password:'
			# self.checkBoxChangeUser.Shown = True
			self.checkBoxChangePassword.Shown = True 
			init.save()    
		self.goto_accounts = False   
		self.goto_incomes = False 
		self.goto_expenses = False 
		self.start_time = time.time()
			
	def OnHomeActivate(self, event):
		self.event = event
		
	def OnHomeIdle(self, event):
		#print time.time() - self.start_time
		if self.enter_user_name_message and self.h.run_first_time and self.message_count < 1: 
			wx.MessageBox('Enter a username in the box below where it says, \"Create a username:\". This username cannot be changed in the future without ' \
						  'erasing all of your data, so make sure it\'s the one you want to keep.', 'Enter your name', wx.OK | wx.CENTRE)             
			self.enter_user_name_message = False
			self.message_count += 1
		if self.goto_accounts:
			if init.userList[0].accountList == []:
				wx.MessageBox('{0}, you have no accounts set up yet. Let\'s go to the Accounts window and add some accounts.'.format(init.userList[0].name), 'Let\'s go to Accounts', wx.OK | wx.CENTRE)
				self.OnButtonAccountsButton(event)
				self.goto_accounts = False
		if self.goto_incomes:
			if init.userList[0].incomeList == []:
				wx.MessageBox('{0}, you have no incomes set up yet. Let\'s go to the Incomes window and add some incomes.'.format(init.userList[0].name), 'Let\'s go to Incomes', wx.OK | wx.CENTRE)
				self.OnButtonIncomesButton(event)
			self.goto_incomes = False
		if self.goto_expenses:
			if init.userList[0].expenseList == [] and init.userList[0].incomeList != []:
				wx.MessageBox('{0}, you have no expenses set up yet. Let\'s go to the Expenses window and add some expenses.'.format(init.userList[0].name), 'Let\'s go to Expenses', wx.OK | wx.CENTRE)
				self.OnButtonExpensesButton(event)
			self.goto_expenses = False
		init.window_timeout(self, self.start_time)
		
	def OnPanel1Motion(self, event):
		self.start_time = time.time()

	def OnButtonEnterUserNameButton(self, event): 
		if init.userList == []:    
			self.buttonClose.Enabled = False
			if self.textCtrlUserName.GetValue() != '':
				init.addUser(self.textCtrlUserName.GetValue())
				self.set_backcolor_white([self.textCtrlUserName])
				self.Title = '{0}, {1}'.format(init.userList[0].name,'welcome to CBudget')
				self.textCtrlUserName.Clear()
				self.staticTextUserName.Label = 'Create a password:'
				wx.MessageBox('Great job, {0}!, Now, enter a password in the box below where it says, \"Create a password:\". ' \
								'You\'ll be able to change the password any time you want in the future.'.format(init.userList[0].name), 'Create a password', wx.OK | wx.CENTRE)                                            
				self.set_backcolor_green(self.textCtrlUserName)
				self.buttonEnterUserName.Enabled = False
				self.enter_user_name_message = False
				self.h = init.userList[0].s._home
				init.save()                
			else: wx.MessageBox('You need to enter a username (one that has doesn\'t have any empty spaces) to create a new user.', 'Need a User name', wx.OK | wx.CENTRE)
		else:    
			if self.h.run_first_time:                 
				wx.MessageBox('{0}, excellent work! Now, you\'re ready to go to the Accounts window.'.format(init.userList[0].name), 'You\'re done!', wx.OK | wx.CENTRE)
				self.set_backcolor_white([self.textCtrlUserName])            
				self.h.run_first_time = False  
				init.save()
				self.buttonClose.Enabled = True
				self.OnButtonAccountsButton(event)
			if init.userList[0].password != '': 
				if not self.checkBoxChangePassword.IsChecked():
					if init.userList[0].password == self.textCtrlUserName.GetValue():
						self.goto_accounts = True
						if init.userList[0].accountList != []: self.goto_incomes = True
						if init.userList[0].incomeList != []:self.goto_expenses = True
						self.start_time = time.time()
						if len(init.userList[0].incomeList) > 0 and len(init.userList[0].expenseList) > 0:
							result = wx.MessageBox('Is today your payday? If so, would you like to go to Incomes and record your income payment. To do that, click \"Yes\" below.', 'Is is payday?', wx.YES_NO | wx.CENTRE)
							if result == wx.YES: 
								init.userList[0].s._incomes.record_income_payment = True
								init.save()
								self.OnButtonIncomesButton(event)
							if result == wx.NO: 
								if init.userList[0].s._accounts.run_count > init.userList[0].s._transactions.run_count: self.OnButtonAccountsButton(event)
								else: self.OnButtonTransactionsButton(event)
						self.staticTextUserName.Label = '' 
						# self.checkBoxChangeUser.Shown = False
						self.checkBoxChangePassword.Shown = False
						self.textCtrlUserName.Clear() 
						self.textCtrlUserName.Enabled = False
						self.buttonEnterUserName.Enabled = False
						self.buttonClose.Enabled = True
						self.enable_buttons(True)
						if init.userList[0].accountList == []:
							self.enable_buttons(False)
							self.buttonAccounts.Enabled = True
						self.set_backcolor_white([self.textCtrlUserName])
					else: 
						wx.MessageBox('Please enter the correct password.', 'Wrong Password', wx.OK | wx.CENTRE)  
						self.set_backcolor_red(self.textCtrlUserName)
				# elif self.checkBoxChangeUser.IsChecked():
					# if init.userList[0].password == self.textCtrlUserName.GetValue():
						# result = wx.MessageBox('This action will erase all the previous user\'s data. Are you sure you want to continue?', 'Erase all data?', wx.YES_NO | wx.CENTRE)
						# if result == wx.YES: 
							# init.removeUser(init.userList[0].name)
							# init.save()
							# self.Title = 'Welcome to CBudget'
							# self.staticTextUserName.Label = "Enter User's Name:" 
							# self.checkBoxChangeUser.Shown = False
							# self.checkBoxChangePassword.Shown = False
							# self.checkBoxChangeUser.SetValue(False) 
							# self.textCtrlUserName.Clear()     
							# self.enable_buttons(False)    
							# self.buttonClose.Enabled = False      
							# wx.MessageBox('Enter a username in the box below where it says, \"Create a username:\". This username cannot be changed in the future without ' \
										  # 'erasing all of your data, so make sure it\'s the one you want to keep.', 'Enter your name', wx.OK | wx.CENTRE)                   
						# if result == wx.NO:
							# self.checkBoxChangeUser.SetValue(False) 
							# self.textCtrlUserName.Clear()           
					# else: 
						# wx.MessageBox('Please enter the correct password.', 'Password does not match', wx.OK | wx.CENTRE)                                                                                      
				elif self.checkBoxChangePassword.IsChecked():
					if init.userList[0].password == self.textCtrlUserName.GetValue() and not(self.staticTextUserName.Label == 'Enter the new password:' or self.staticTextUserName.Label == 'Re-enter the new password:'):
						result = wx.MessageBox('Are you sure you want to change your password?', 'Change password?', wx.YES_NO | wx.CENTRE)
						if result == wx.YES: 
							self.staticTextUserName.Label = 'Enter the new password:'
							# self.checkBoxChangeUser.Shown = False
							self.checkBoxChangePassword.Shown = False  
							self.textCtrlUserName.Clear() 
						if result == wx.NO: 
							self.checkBoxChangePassword.SetValue(False) 
							# self.checkBoxChangeUser.SetValue(False) 
							self.textCtrlUserName.Clear()     
					elif init.userList[0].password == self.textCtrlUserName.GetValue() and (self.staticTextUserName.Label == 'Enter the new password:' or self.staticTextUserName.Label == 'Re-enter the new password:'):
						result = wx.MessageBox('The new password you entered is the same as the old password. Do you want to leave the password unchanged?', 'Keep same password?', wx.YES_NO | wx.CENTRE) 
						if result == wx.YES:
							self.staticTextUserName.Label = '' 
							# self.checkBoxChangeUser.Shown = False
							self.checkBoxChangePassword.Shown = False
							self.textCtrlUserName.Clear() 
							self.textCtrlUserName.Enabled = False
							self.buttonEnterUserName.Enabled = False
							self.enable_buttons(True)                            
						if result == wx.NO:
							self.staticTextUserName.Label = 'Re-enter the new password:'
							self.textCtrlUserName.Clear() 
					elif init.userList[0].password != self.textCtrlUserName.GetValue() and not(self.staticTextUserName.Label == 'Enter the new password:' or self.staticTextUserName.Label == 'Re-enter the new password:'):
						wx.MessageBox('Please enter the correct password.', 'Password does not match', wx.OK | wx.CENTRE) 
						self.textCtrlUserName.Clear() 
					elif init.userList[0].password != self.textCtrlUserName.GetValue() and (self.staticTextUserName.Label == 'Enter the new password:' or self.staticTextUserName.Label == 'Re-enter the new password:'):
						init.userList[0].password = self.textCtrlUserName.GetValue()
						init.save()  
						self.checkBoxChangePassword.SetValue(False) 
						self.checkBoxChangePassword.Shown = True  
						# self.checkBoxChangeUser.Shown = True               
						self.password_changed = False
						self.staticTextUserName.Label = ''
						wx.MessageBox('Your password has been changed.', 'Success!', wx.OK | wx.CENTRE)  
						self.staticTextUserName.Label = '' 
						# self.checkBoxChangeUser.Shown = False
						self.checkBoxChangePassword.Shown = False
						self.textCtrlUserName.Clear() 
						self.textCtrlUserName.Enabled = False
						self.buttonEnterUserName.Enabled = False
						self.enable_buttons(True)
			else:
				init.userList[0].password = self.textCtrlUserName.GetValue()
				init.save()
				self.staticTextUserName.Label = ''
				self.textCtrlUserName.Clear() 
				self.textCtrlUserName.Enabled = False
				self.buttonEnterUserName.Enabled = False
				self.textCtrlUserName.Clear()
				self.buttonEnterUserName.Enabled = False
				self.enable_buttons(True) 
							  
	def OnTextCtrlUserNameText(self, event):
		self.buttonEnterUserName.Enabled = True     
				
	def enable_buttons(self, enable):
		if enable:
			self.buttonAccounts.Enabled = True         
			if init.userList[0].accountList != []: self.buttonIncomes.Enabled = True
			if init.userList[0].accountList == []: self.buttonIncomes.Enabled = False              
			if init.userList[0].accountList != []: self.buttonCredits.Enabled = True
			if init.userList[0].accountList == []: self.buttonCredits.Enabled = False              
			if init.userList[0].accountList != []: self.buttonExpenses.Enabled = True
			if init.userList[0].accountList == []: self.buttonExpenses.Enabled = False                
			if init.userList[0].accountList != [] and init.userList[0].expenseList != [] and init.userList[0].incomeList != []: self.buttonBudget.Enabled = True
			else: self.buttonBudget.Enabled = False                     
			if init.userList[0].accountList != []: self.buttonSavingsItems.Enabled = True
			if init.userList[0].accountList == []: self.buttonSavingsItems.Enabled = False                  
			if init.userList[0].accountList != [] and init.userList[0].expenseList != [] and init.userList[0].incomeList != []: self.buttonExpensesDue.Enabled = True
			if init.userList[0].accountList != [] and init.userList[0].expenseList != [] and init.userList[0].incomeList != []: self.buttonExpensesDue.Enabled = True
			else: self.buttonExpensesDue.Enabled = False            
			if init.userList[0].accountList != []: self.buttonTransactions.Enabled = True
			if init.userList[0].accountList == []: self.buttonTransactions.Enabled = False
		else:
			self.buttonAccounts.Enabled = False
			self.buttonIncomes.Enabled = False
			self.buttonCredits.Enabled = False
			self.buttonExpenses.Enabled = False
			self.buttonBudget.Enabled = False
			self.buttonSavingsItems.Enabled = False
			self.buttonExpensesDue.Enabled = False
			self.buttonTransactions.Enabled = False   
			
	def set_backcolor_red(self, ctrl):
		ctrl.SetBackgroundColour(wx.Colour(255, 128, 128))
		ctrl.Refresh()
		ctrl.SetFocus()
		if 'TextCtrl' in str(ctrl.__str__):
			ctrl.SetSelection(0,-1)
						
	def set_backcolor_green(self, ctrl):
		ctrl.SetBackgroundColour(wx.Colour(0, 255, 0))
		ctrl.Refresh()
		ctrl.SetFocus()
		if 'TextCtrl' in str(ctrl.__str__):
			ctrl.SetSelection(0,-1)
		
	def set_backcolor_white(self, ctrls):
		for c in ctrls:
			c.SetBackgroundColour(wx.Colour(255, 255, 255))
			c.Refresh()

	def OnButtonAccountsButton(self, event):
		self.Hide()
		self.Close()
		self.main = CBudgetP_Accounts.create(None)
		self.main.Show()

	def OnButtonIncomesButton(self, event):
		self.Hide()
		#self.Close()
		self.main = CBudgetP_Incomes.create(None)
		self.main.Show()
		
	def OnButtonCreditsButton(self, event):
		self.Hide()
		self.Close()
		self.main = CBudgetP_Credits.create(None)
		self.main.Show()  

	def OnButtonExpensesButton(self, event):
		self.Hide()
		self.Close()
		self.main = CBudgetP_Expenses.create(None)
		self.main.Show()

	def OnButtonSavingsItemsButton(self, event):
		self.Hide()
		self.Close()
		self.main = CBudgetP_SavingsItems.create(None)
		self.main.Show()

	def OnButtonBudgetButton(self, event):
		self.Hide()
		self.Close()
		self.main = CBudgetP_Budget.create(None)
		self.main.Show()

	def OnButtonExpensesDueButton(self, event):
		init.userList[0].s.show_expenses_due = True
		init.save()
		self.Hide()
		self.Close()
		self.main = CBudgetP_ExpensesDue.create(None)
		self.main.Show()

	def OnButtonTransactionsButton(self, event):
		self.Hide()
		self.Close()
		self.main = CBudgetP_Transactions.create(None)
		self.main.Show()
		
	def OnButtonCloseButton(self, event):
		if self.h.run_count <= 10: init.delete_install_folder()
		self.Close()
		init.end_process()
