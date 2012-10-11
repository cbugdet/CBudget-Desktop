#Boa:Frame:Expenses

import wx
import time
import CBudgetP
init = CBudgetP.initialize()
from datetime import datetime
import CBudgetP_Home
import CBudgetP_Accounts
import CBudgetP_Incomes
import CBudgetP_Credits
import CBudgetP_SavingsItems
import CBudgetP_Budget
import CBudgetP_ExpensesDue
import CBudgetP_Transactions

def create(parent):
	return Expenses(parent)

[wxID_EXPENSES, wxID_EXPENSESBUTTONACCOUNTS, wxID_EXPENSESBUTTONADDEXPENSE, 
 wxID_EXPENSESBUTTONAVERAGE, wxID_EXPENSESBUTTONBUDGET, 
 wxID_EXPENSESBUTTONCLOSE, wxID_EXPENSESBUTTONCREDITS, 
 wxID_EXPENSESBUTTONEDITEXPENSE, wxID_EXPENSESBUTTONEXPENSESDUE, 
 wxID_EXPENSESBUTTONHOME, wxID_EXPENSESBUTTONINCOMES, 
 wxID_EXPENSESBUTTONREMOVEEXPENSE, wxID_EXPENSESBUTTONSAVINGSITEMS, 
 wxID_EXPENSESBUTTONTRANSACTIONS, wxID_EXPENSESCHOICEFREQUENCYDESIGNATOR, 
 wxID_EXPENSESCHOICEFREQUENCYNUMBER, wxID_EXPENSESDATEPICKERCTRLDUEDATE, 
 wxID_EXPENSESLISTBOXEXPENSES, wxID_EXPENSESPANEL1, 
 wxID_EXPENSESSEARCHCTRLSEARCHEXPENSES, wxID_EXPENSESSTATICTEXBILLINTERVAL, 
 wxID_EXPENSESSTATICTEXT1ANNUALEXPENSES, wxID_EXPENSESSTATICTEXTAMOUNT, 
 wxID_EXPENSESSTATICTEXTDATE, wxID_EXPENSESSTATICTEXTEXPENSENAME, 
 wxID_EXPENSESSTATICTEXTMONTHLYEXPENSES, wxID_EXPENSESTEXTCTRLAMOUNT, 
 wxID_EXPENSESTEXTCTRLANNUALEXPENSES, wxID_EXPENSESTEXTCTRLEXPENSENAME, 
 wxID_EXPENSESTEXTCTRLMONTHLYEXPENSES, 
] = [wx.NewId() for _init_ctrls in range(30)]

class Expenses(wx.Frame):
	def _init_ctrls(self, prnt):
		# generated method, don't edit
		wx.Frame.__init__(self, id=wxID_EXPENSES, name='Expenses', parent=prnt,
			  pos=wx.Point(389, 114), size=wx.Size(587, 499), style=wx.CAPTION,
			  title='Expenses')
		self.SetClientSize(wx.Size(571, 461))
		self.Center(wx.BOTH)
		self.Bind(wx.EVT_IDLE, self.OnExpensesIdle)

		self.panel1 = wx.Panel(id=wxID_EXPENSESPANEL1, name='panel1',
			  parent=self, pos=wx.Point(0, 0), size=wx.Size(571, 461),
			  style=wx.TAB_TRAVERSAL)
		self.panel1.SetToolTipString('Expenses Window')
		self.panel1.Bind(wx.EVT_MOTION, self.OnPanel1Motion)

		self.searchCtrlSearchExpenses = wx.SearchCtrl(id=wxID_EXPENSESSEARCHCTRLSEARCHEXPENSES,
			  name='searchCtrlSearchExpenses', parent=self.panel1,
			  pos=wx.Point(256, 160), size=wx.Size(127, 21), style=0, value='')
		self.searchCtrlSearchExpenses.SetToolTipString('Search for expenses in the list')
		self.searchCtrlSearchExpenses.Bind(wx.EVT_TEXT,
			  self.OnSearchCtrlSearchExpensesText,
			  id=wxID_EXPENSESSEARCHCTRLSEARCHEXPENSES)

		self.listBoxExpenses = wx.ListBox(choices=[],
			  id=wxID_EXPENSESLISTBOXEXPENSES, name='listBoxExpenses',
			  parent=self.panel1, pos=wx.Point(48, 24), size=wx.Size(352, 128),
			  style=0)
		self.listBoxExpenses.SetToolTipString('Expense List - You can add as many expenses here as you want. Just start by going to the Expense Name box and enter a expense name. Click Add Expenseif you need help')
		self.listBoxExpenses.Bind(wx.EVT_LISTBOX, self.OnListBoxExpensesListbox,
			  id=wxID_EXPENSESLISTBOXEXPENSES)

		self.textCtrlExpenseName = wx.TextCtrl(id=wxID_EXPENSESTEXTCTRLEXPENSENAME,
			  name='textCtrlExpenseName', parent=self.panel1, pos=wx.Point(408,
			  40), size=wx.Size(100, 21), style=wx.TE_CENTER, value='')
		self.textCtrlExpenseName.SetToolTipString('Enter the expense name here')
		self.textCtrlExpenseName.Bind(wx.EVT_KILL_FOCUS,
			  self.OnTextCtrlExpenseNameKillFocus)

		self.textCtrlAmount = wx.TextCtrl(id=wxID_EXPENSESTEXTCTRLAMOUNT,
			  name='textCtrlAmount', parent=self.panel1, pos=wx.Point(96, 160),
			  size=wx.Size(144, 21), style=wx.TE_CENTER, value='')
		self.textCtrlAmount.SetToolTipString('Enter the expense amount here')

		self.datePickerCtrlDueDate = wx.DatePickerCtrl(id=wxID_EXPENSESDATEPICKERCTRLDUEDATE,
			  name='datePickerCtrlDueDate', parent=self.panel1, pos=wx.Point(88,
			  208), size=wx.Size(144, 21), style=wx.DP_SHOWCENTURY)
		self.datePickerCtrlDueDate.SetToolTipString('Select the expense due date here')

		self.choiceFrequencyNumber = wx.Choice(choices=[],
			  id=wxID_EXPENSESCHOICEFREQUENCYNUMBER,
			  name='choiceFrequencyNumber', parent=self.panel1,
			  pos=wx.Point(272, 208), size=wx.Size(96, 21), style=0)
		self.choiceFrequencyNumber.SetToolTipString('If this bill is due every month, use this selector to choose a 1')
		self.choiceFrequencyNumber.Bind(wx.EVT_CHOICE,
			  self.OnChoiceFrequencyNumberChoice,
			  id=wxID_EXPENSESCHOICEFREQUENCYNUMBER)

		self.choiceFrequencyDesignator = wx.Choice(choices=[],
			  id=wxID_EXPENSESCHOICEFREQUENCYDESIGNATOR,
			  name='choiceFrequencyDesignator', parent=self.panel1,
			  pos=wx.Point(384, 208), size=wx.Size(130, 21), style=0)
		self.choiceFrequencyDesignator.SetToolTipString("If this bill is due every month, use this selector to choose month(s)'")
		self.choiceFrequencyDesignator.Bind(wx.EVT_CHOICE,
			  self.OnChoiceFrequencyDesignatorChoice,
			  id=wxID_EXPENSESCHOICEFREQUENCYDESIGNATOR)

		self.buttonAddExpense = wx.Button(id=wxID_EXPENSESBUTTONADDEXPENSE,
			  label='Add Expense', name='buttonAddExpense', parent=self.panel1,
			  pos=wx.Point(404, 72), size=wx.Size(110, 23), style=0)
		self.buttonAddExpense.Enable(True)
		self.buttonAddExpense.SetToolTipString('Add an expense to the list')
		self.buttonAddExpense.Bind(wx.EVT_BUTTON, self.OnButtonAddExpenseButton,
			  id=wxID_EXPENSESBUTTONADDEXPENSE)

		self.buttonRemoveExpense = wx.Button(id=wxID_EXPENSESBUTTONREMOVEEXPENSE,
			  label='Remove Expense', name='buttonRemoveExpense',
			  parent=self.panel1, pos=wx.Point(404, 100), size=wx.Size(110, 23),
			  style=0)
		self.buttonRemoveExpense.Enable(False)
		self.buttonRemoveExpense.SetToolTipString('Remove the selected expense from the list')
		self.buttonRemoveExpense.Bind(wx.EVT_BUTTON,
			  self.OnButtonRemoveExpenseButton,
			  id=wxID_EXPENSESBUTTONREMOVEEXPENSE)

		self.buttonEditExpense = wx.Button(id=wxID_EXPENSESBUTTONEDITEXPENSE,
			  label='Edit Expense', name='buttonEditExpense',
			  parent=self.panel1, pos=wx.Point(404, 128), size=wx.Size(110, 23),
			  style=0)
		self.buttonEditExpense.Enable(False)
		self.buttonEditExpense.SetToolTipString('Change values for the selected expense')
		self.buttonEditExpense.Bind(wx.EVT_BUTTON,
			  self.OnButtonEditExpenseButton,
			  id=wxID_EXPENSESBUTTONEDITEXPENSE)

		self.buttonAverage = wx.Button(id=wxID_EXPENSESBUTTONAVERAGE,
			  label='Average', name='buttonAverage', parent=self.panel1,
			  pos=wx.Point(404, 156), size=wx.Size(110, 23), style=0)
		self.buttonAverage.Enable(False)
		self.buttonAverage.SetToolTipString('Calculates the average amount for the selected expense in case the amount is not always the same and you want to use the average amount in your budget instead of the last amount you paid for this bill')
		self.buttonAverage.Bind(wx.EVT_BUTTON, self.OnButtonAverageButton,
			  id=wxID_EXPENSESBUTTONAVERAGE)

		self.textCtrlMonthlyExpenses = wx.TextCtrl(id=wxID_EXPENSESTEXTCTRLMONTHLYEXPENSES,
			  name='textCtrlMonthlyExpenses', parent=self.panel1,
			  pos=wx.Point(136, 256), size=wx.Size(128, 21), style=wx.TE_CENTER,
			  value='')
		self.textCtrlMonthlyExpenses.SetToolTipString('Shows your total monthly expenses. Each time you add, change, or remove an expense, this amount will be recalculated')

		self.textCtrlAnnualExpenses = wx.TextCtrl(id=wxID_EXPENSESTEXTCTRLANNUALEXPENSES,
			  name='textCtrlAnnualExpenses', parent=self.panel1,
			  pos=wx.Point(384, 258), size=wx.Size(128, 21), style=wx.TE_CENTER,
			  value='')
		self.textCtrlAnnualExpenses.SetToolTipString('Shows your total annual expenses. Each time you add, change, or remove an expense, this amount will be recalculated')

		self.buttonHome = wx.Button(id=wxID_EXPENSESBUTTONHOME, label='Home',
			  name='buttonHome', parent=self.panel1, pos=wx.Point(76, 296),
			  size=wx.Size(85, 48), style=0)
		self.buttonHome.SetToolTipString('Takes you back to the Home window. If you press this button you will have ')
		self.buttonHome.Bind(wx.EVT_BUTTON, self.OnButtonHomeButton,
			  id=wxID_EXPENSESBUTTONHOME)

		self.buttonAccounts = wx.Button(id=wxID_EXPENSESBUTTONACCOUNTS,
			  label='Accounts', name='buttonAccounts', parent=self.panel1,
			  pos=wx.Point(182, 296), size=wx.Size(85, 48), style=0)
		self.buttonAccounts.SetToolTipString('Takes you to the Accounts window')
		self.buttonAccounts.Bind(wx.EVT_BUTTON, self.OnButtonAccountsButton,
			  id=wxID_EXPENSESBUTTONACCOUNTS)

		self.buttonIncomes = wx.Button(id=wxID_EXPENSESBUTTONINCOMES,
			  label='Incomes', name='buttonIncomes', parent=self.panel1,
			  pos=wx.Point(288, 296), size=wx.Size(85, 48), style=0)
		self.buttonIncomes.SetToolTipString('Takes you to the Incomes window')
		self.buttonIncomes.Bind(wx.EVT_BUTTON, self.OnButtonIncomesButton,
			  id=wxID_EXPENSESBUTTONINCOMES)

		self.buttonCredits = wx.Button(id=wxID_EXPENSESBUTTONCREDITS,
			  label='Credits', name='buttonCredits', parent=self.panel1,
			  pos=wx.Point(392, 296), size=wx.Size(85, 48), style=0)
		self.buttonCredits.SetToolTipString('Takes you to the Credits window')
		self.buttonCredits.Bind(wx.EVT_BUTTON, self.OnButtonCreditsButton,
			  id=wxID_EXPENSESBUTTONCREDITS)

		self.buttonSavingsItems = wx.Button(id=wxID_EXPENSESBUTTONSAVINGSITEMS,
			  label='Savings Items', name='buttonSavingsItems',
			  parent=self.panel1, pos=wx.Point(76, 352), size=wx.Size(85, 48),
			  style=0)
		self.buttonSavingsItems.SetToolTipString('Takes you to the Savings Items window')
		self.buttonSavingsItems.Bind(wx.EVT_BUTTON,
			  self.OnButtonSavingsItemsButton,
			  id=wxID_EXPENSESBUTTONSAVINGSITEMS)

		self.buttonBudget = wx.Button(id=wxID_EXPENSESBUTTONBUDGET,
			  label='Budget', name='buttonBudget', parent=self.panel1,
			  pos=wx.Point(182, 352), size=wx.Size(85, 48), style=0)
		self.buttonBudget.SetToolTipString('Takes you to the Budget window')
		self.buttonBudget.Bind(wx.EVT_BUTTON, self.OnButtonBudgetButton,
			  id=wxID_EXPENSESBUTTONBUDGET)

		self.buttonExpensesDue = wx.Button(id=wxID_EXPENSESBUTTONEXPENSESDUE,
			  label='Expenses Due', name='buttonExpensesDue',
			  parent=self.panel1, pos=wx.Point(286, 352), size=wx.Size(85, 48),
			  style=0)
		self.buttonExpensesDue.SetHelpText('')
		self.buttonExpensesDue.SetToolTipString('Takes you to the Expenses Due window')
		self.buttonExpensesDue.Bind(wx.EVT_BUTTON,
			  self.OnButtonExpensesDueButton,
			  id=wxID_EXPENSESBUTTONEXPENSESDUE)

		self.buttonTransactions = wx.Button(id=wxID_EXPENSESBUTTONTRANSACTIONS,
			  label='Transactions', name='buttonTransactions',
			  parent=self.panel1, pos=wx.Point(392, 352), size=wx.Size(85, 48),
			  style=0)
		self.buttonTransactions.SetToolTipString('Takes you to the Transactions window')
		self.buttonTransactions.Bind(wx.EVT_BUTTON,
			  self.OnButtonTransactionsButton,
			  id=wxID_EXPENSESBUTTONTRANSACTIONS)

		self.staticTextDate = wx.StaticText(id=wxID_EXPENSESSTATICTEXTDATE,
			  label='Date:', name='staticTextDate', parent=self.panel1,
			  pos=wx.Point(56, 212), size=wx.Size(28, 13), style=0)

		self.staticTextExpenseName = wx.StaticText(id=wxID_EXPENSESSTATICTEXTEXPENSENAME,
			  label='Expense Name', name='staticTextExpenseName',
			  parent=self.panel1, pos=wx.Point(424, 24), size=wx.Size(72, 13),
			  style=0)

		self.staticText1AnnualExpenses = wx.StaticText(id=wxID_EXPENSESSTATICTEXT1ANNUALEXPENSES,
			  label='Annual Expenses', name='staticText1AnnualExpenses',
			  parent=self.panel1, pos=wx.Point(296, 262), size=wx.Size(83, 13),
			  style=0)

		self.staticTextMonthlyExpenses = wx.StaticText(id=wxID_EXPENSESSTATICTEXTMONTHLYEXPENSES,
			  label='Monthly Expenses', name='staticTextMonthlyExpenses',
			  parent=self.panel1, pos=wx.Point(48, 262), size=wx.Size(88, 13),
			  style=0)

		self.staticTextAmount = wx.StaticText(id=wxID_EXPENSESSTATICTEXTAMOUNT,
			  label='Amount:', name='staticTextAmount', parent=self.panel1,
			  pos=wx.Point(54, 163), size=wx.Size(42, 13), style=0)

		self.staticTexBillInterval = wx.StaticText(id=wxID_EXPENSESSTATICTEXBILLINTERVAL,
			  label='This expense is due every:', name='staticTexBillInterval',
			  parent=self.panel1, pos=wx.Point(318, 192), size=wx.Size(130, 13),
			  style=0)

		self.buttonClose = wx.Button(id=wxID_EXPENSESBUTTONCLOSE, label='Close',
			  name='buttonClose', parent=self.panel1, pos=wx.Point(242, 424),
			  size=wx.Size(75, 23), style=0)
		self.buttonClose.SetToolTipString('See you next time!')
		self.buttonClose.Bind(wx.EVT_BUTTON, self.OnButtonCloseButton,
			  id=wxID_EXPENSESBUTTONCLOSE)

	def __init__(self, parent):
		self._init_ctrls(parent)        
		init.load()
		self.user = init.userList[0]
		self.e = self.user.s._expenses
		self.e.run_count += 1
		self.add_expense_message = 'Start by entering the name of your first expense in the box below where it says \"Expense Name\" on the top right. ' \
						   'Then go to the box that says \"Amount\" and enter your expense amount. After that, you\'ll need to select the due date ' \
						   'next to where it says date on the left. Then you\'ll need to select how often the expense is due below where it says \"This expense is due every:\". ' \
						   'For example, if the bill you are entering is due every month, select 1 from the first selector and \"month(s)\" from the ' \
						   'second selector. You have to select one of each, or your budget will have trouble calculating. When you\'re all done, click ' \
						   '\"Add Expense\" and the new expense will be added to the list. Total monthly and annual expense amounts will be auto-calculated ' \
						   'for you each time you add, change, or remove an expense. Click \"Add Expense\" again if you need help.'
		self.message_count = 0
		if self.e.run_first_time: wx.MessageBox(self.e.welcome_message, self.e.welcome_title, wx.OK | wx.CENTRE)
		self.expenseList = self.user.expenseList
		self.frequencyNumber = 0
		self.frequencyDesignator = 'None'
		self.listBoxExpenses.InsertItems([e.name for e in self.user.expenseList],0) 
		for i in range(1,91):
			self.choiceFrequencyNumber.Append(str(i))
		self.choiceFrequencyDesignator.Append('day(s)')
		self.choiceFrequencyDesignator.Append('week(s)')
		self.choiceFrequencyDesignator.Append('month(s)')
		self.choiceFrequencyDesignator.Append('year(s)') 
		self.textCtrlMonthlyExpenses.WriteText('$'+str(round(self.user.b.monthly_expenses(self.user),2)))
		self.textCtrlAnnualExpenses.WriteText('$'+str(round(self.user.b.annual_expenses(self.user),2)))           
		if self.user.s.savings_item_added: 
			self.listBoxExpenses.SetSelection(len(self.expenseList)-1)
			self.user.s.savings_item_added = False           
			self.textCtrlExpenseName.WriteText(self.expenseList[self.listBoxExpenses.GetSelection()].name)
			self.textCtrlAmount.WriteText('$'+str(self.expenseList[self.listBoxExpenses.GetSelection()].amount))  
			self.choiceFrequencyNumber.SetStringSelection(str(int(self.expenseList[self.listBoxExpenses.GetSelection()].frequencyNumber)))
			self.choiceFrequencyDesignator.SetStringSelection(self.expenseList[self.listBoxExpenses.GetSelection()].frequencyDesignator)
			date = self.expenseList[self.listBoxExpenses.GetSelection()].date    
			self.datePickerCtrlDueDate.SetValue(wx.DateTimeFromDMY(date.day,date.month-1,date.year))
			self.e.run_first_time = False
			init.save()
		if self.user.expenseList == [] or self.user.incomeList == []: 
			self.buttonExpensesDue.Enabled = False       
			self.buttonBudget.Enabled = False
		self.start_time = time.time()
			
	def OnExpensesIdle(self, event):
		if self.e.run_first_time and self.message_count < 1: 
			wx.MessageBox(self.add_expense_message, 'To add an expense', wx.OK | wx.CENTRE)  
			self.set_backcolor_green(self.textCtrlExpenseName) 
			self.message_count += 1  
		init.window_timeout(self, self.start_time)
		
	def OnPanel1Motion(self, event):
		self.start_time = time.time()
			
	def OnTextCtrlExpenseNameKillFocus(self, event):
		self.set_backcolor_white([self.textCtrlExpenseName])

	def OnListBoxExpensesListbox(self, event):
		self.textCtrlExpenseName.Clear()      
		self.textCtrlAmount.Clear()
		self.textCtrlExpenseName.WriteText(self.expenseList[self.listBoxExpenses.GetSelection()].name)
		self.textCtrlAmount.WriteText('$'+str(self.expenseList[self.listBoxExpenses.GetSelection()].amount))
		self.choiceFrequencyNumber.SetStringSelection(str(int(self.expenseList[self.listBoxExpenses.GetSelection()].frequencyNumber)))
		self.choiceFrequencyDesignator.SetStringSelection(self.expenseList[self.listBoxExpenses.GetSelection()].frequencyDesignator)
		date = self.expenseList[self.listBoxExpenses.GetSelection()].date    
		self.datePickerCtrlDueDate.SetValue(wx.DateTimeFromDMY(date.day,date.month-1,date.year))
		self.buttonRemoveExpense.Enabled = True
		self.buttonEditExpense.Enabled = True
		self.buttonAverage.Enabled = True
					
	def OnSearchCtrlSearchExpensesText(self, event):
		self.expenseList = self.user.search_expenseList(self.searchCtrlSearchExpenses.GetValue())
		if len(self.expenseList) == 0: 
			self.expenseList = self.user.expenseList
			wx.MessageBox('Your search did not match any names in the expense list.','No matches found')
		print 'self.expenseList:', self.expenseList
		self.listBoxExpenses.Clear()
		self.listBoxExpenses.InsertItems([e.name for e in self.expenseList],0)
		self.textCtrlExpenseName.Clear()
		self.textCtrlAmount.Clear()   

	def OnButtonAddExpenseButton(self, event): 
		dt = self.datePickerCtrlDueDate.GetValue()
		date = datetime(dt.Year,dt.Month+1,dt.Day)
		if self.choiceFrequencyNumber.GetStringSelection() != '': self.frequencyNumber = int(self.choiceFrequencyNumber.GetStringSelection())
		if self.choiceFrequencyDesignator.GetStringSelection() != '': self.frequencyDesignator = self.choiceFrequencyDesignator.GetStringSelection()
		if self.textCtrlExpenseName.GetValue() == '' and self.textCtrlAmount.GetValue() == '' and (self.frequencyNumber == 0 or self.frequencyDesignator == 'None'): 
			wx.MessageBox(self.add_expense_message, 'To add an expense', wx.OK | wx.CENTRE)
			self.set_backcolor_green(self.textCtrlExpenseName)
		elif self.textCtrlExpenseName.GetValue() == '' and self.textCtrlAmount.GetValue() == '': 
			wx.MessageBox('In order to add an expense, it has to have a name. You can enter that below where it says \"Expense Name\".', 'Expense has no name', wx.OK | wx.CENTRE)        
			self.set_backcolor_red(self.textCtrlExpenseName) 
		elif self.textCtrlExpenseName.GetValue() == '' and self.textCtrlAmount.GetValue() != '': 
			wx.MessageBox('In order to add an expense, it has to have a name. You can enter that below where it says \"Expense Name\".', 'Expense has no name', wx.OK | wx.CENTRE)        
			self.set_backcolor_red(self.textCtrlExpenseName) 
			self.set_backcolor_white([self.textCtrlAmount])
		elif self.textCtrlExpenseName.GetValue() != '' and self.textCtrlAmount.GetValue() == '': 
			wx.MessageBox('In order to add an expense, it has to have an amount. You can enter that below where it says \"Amount\".', 'Expense has no amount', wx.OK | wx.CENTRE)
			self.set_backcolor_red(self.textCtrlAmount)            
			self.set_backcolor_white([self.textCtrlExpenseName])
		elif self.textCtrlExpenseName.GetValue() != '' and self.textCtrlAmount.GetValue() != '' and (self.frequencyNumber == 0 or self.frequencyDesignator == 'None'): 
			wx.MessageBox('In order to add an expense, CBudget needs to know how often this bill is due. You can select that below where it says \"This bill is due every:\"', 'Expense has no cycle', wx.OK | wx.CENTRE)
			self.set_backcolor_red(self.staticTexBillInterval)
			self.set_backcolor_white([self.textCtrlExpenseName, self.textCtrlAmount])
		else:
			self.set_backcolor_white([self.textCtrlExpenseName, self.textCtrlAmount])
			self.set_backcolor_grey(self.staticTexBillInterval)
			if self.textCtrlExpenseName.GetValue() not in self.listBoxExpenses.GetStrings(): 
				amount = 0.0
				try: 
					if '$' in self.textCtrlAmount.GetValue(): amount = float(self.textCtrlAmount.GetValue()[1:])                    
					else: amount = float(self.textCtrlAmount.GetValue())              
					self.user.addExpense(self.textCtrlExpenseName.GetValue(), amount, date, int(self.choiceFrequencyNumber.GetStringSelection()),self.choiceFrequencyDesignator.GetStringSelection())
					self.e.run_first_time = False
					self.textCtrlExpenseName.SetFocus()
					init.save()
					wx.MessageBox('The expense \"{0}\" has been to your expenses list.'.format(self.textCtrlExpenseName.GetValue()), 'Expense added', wx.OK | wx.CENTRE)                    
					self.set_backcolor_white([self.textCtrlAmount])
					self.listBoxExpenses.Clear()
					self.listBoxExpenses.InsertItems([e.name for e in self.expenseList],0)        
					self.textCtrlMonthlyExpenses.Clear()
					self.textCtrlAnnualExpenses.Clear() 
					self.textCtrlMonthlyExpenses.WriteText('$'+str(round(self.user.b.monthly_expenses(self.user),2)))
					self.textCtrlAnnualExpenses.WriteText('$'+str(round(self.user.b.annual_expenses(self.user),2)))
					self.textCtrlExpenseName.Clear()
					self.textCtrlAmount.Clear()
					self.buttonRemoveExpense.Enabled = False
					self.buttonEditExpense.Enabled = False
					self.buttonAverage.Enabled = False  
					self.textCtrlExpenseName.SetFocus()  
					if self.user.incomeList != []: 
						self.buttonExpensesDue.Enabled = True      
						self.buttonBudget.Enabled = True 
					if len(self.user.expenseList) > 3 and self.user.s._budget.run_first_time == True:
						result = wx.MessageBox('Now that you have some expenses, you might want to take a look at your budget, or you can stay here and add more expenses. Would you like to view your budget?', 'View budget?', wx.YES_NO | wx.CENTRE)
						if result == wx.YES: self.OnButtonBudgetButton(event)
				except ValueError: 
					wx.MessageBox('The amount you are entering has to be a number. You\'ve probably entered some letters, symbols, or a word. Make sure it\'s a number.', 'Amount is not a number', wx.OK | wx.CENTRE)
					self.set_backcolor_red(self.textCtrlAmount)    
			else: 
				wx.MessageBox('Sorry, you can\'t add an expense with that name. It\'s already in the list. To add another expense, you\'ll need to change the name.', 'Duplicate expense', wx.OK | wx.CENTRE)                    
				self.set_backcolor_red(self.textCtrlExpenseName)    

	def OnButtonEditExpenseButton(self, event):
		print 'self.listBoxExpenses.GetSelection():', self.listBoxExpenses.GetSelection()
		print 'self.expenseList[self.listBoxExpenses.GetSelection()].name:', self.expenseList[self.listBoxExpenses.GetSelection()].name
		print 'self.expenseList[self.listBoxExpenses.GetSelection()].amount:', self.expenseList[self.listBoxExpenses.GetSelection()].amount
		if self.textCtrlExpenseName.GetValue() != '': self.expenseList[self.listBoxExpenses.GetSelection()].name = self.textCtrlExpenseName.GetValue()
		amount = 0.0
		try: 
			if '$' in self.textCtrlAmount.GetValue(): amount = float(self.textCtrlAmount.GetValue()[1:])
			else: amount = float(self.textCtrlAmount.GetValue())  
			self.expenseList[self.listBoxExpenses.GetSelection()].amount = amount
		except ValueError: wx.MessageBox('The amount you are entering has to be a number and can\'t be blank. You\'ve probably entered some letters, symbols, or a word. Make sure it\'s a number.', 'Amount is not a number', wx.OK | wx.CENTRE)   
		dt = self.datePickerCtrlDueDate.GetValue()
		date = datetime(dt.Year,dt.Month+1,dt.Day)        
		self.expenseList[self.listBoxExpenses.GetSelection()].date = date
		if self.choiceFrequencyNumber.GetStringSelection() != '': self.expenseList[self.listBoxExpenses.GetSelection()].frequencyNumber = int(self.choiceFrequencyNumber.GetStringSelection())
		if self.choiceFrequencyDesignator.GetStringSelection() != '': self.expenseList[self.listBoxExpenses.GetSelection()].frequencyDesignator = self.choiceFrequencyDesignator.GetStringSelection()
		self.textCtrlMonthlyExpenses.Clear() 
		self.textCtrlAnnualExpenses.Clear() 
		self.textCtrlMonthlyExpenses.WriteText('$'+str(round(self.user.b.monthly_expenses(self.user),2)))
		self.textCtrlAnnualExpenses.WriteText('$'+str(round(self.user.b.annual_expenses(self.user),2)))          
		init.save()
		self.buttonRemoveExpense.Enabled = False
		self.buttonEditExpense.Enabled = False
		self.buttonAverage.Enabled = False
		self.listBoxExpenses.Clear()
		self.listBoxExpenses.InsertItems([e.name for e in self.expenseList],0)

	def OnButtonRemoveExpenseButton(self, event):
		result = wx.MessageBox('You are about to remove the expense: {0}. Is this what you really want to do?'.format(self.expenseList[self.listBoxExpenses.GetSelection()].name), 'Remove expense?', wx.YES_NO | wx.CENTRE)
		if result == wx.YES:
			self.user.removeExpense(self.expenseList[self.listBoxExpenses.GetSelection()])
			init.save()
			self.listBoxExpenses.Clear()
			self.listBoxExpenses.InsertItems([e.name for e in self.user.expenseList],0)
			self.textCtrlMonthlyExpenses.Clear() 
			self.textCtrlAnnualExpenses.Clear() 
			self.textCtrlMonthlyExpenses.WriteText('$'+str(round(self.user.b.monthly_expenses(self.user),2)))
			self.textCtrlAnnualExpenses.WriteText('$'+str(round(self.user.b.annual_expenses(self.user),2)))  
			self.textCtrlExpenseName.Clear()
			self.textCtrlAmount.Clear()        
			self.buttonRemoveExpense.Enabled = False
			self.buttonEditExpense.Enabled = False
			self.buttonAverage.Enabled = False
			self.choiceFrequencyNumber.SetSelection(-1)
			self.choiceFrequencyDesignator.SetSelection(-1)   
			self.frequencyNumber = 0
			self.frequencyDesignator = 'None'   

	def OnButtonAverageButton(self, event):
		elist = self.user.get_current_account().r.filter_expense(self.expenseList[self.listBoxExpenses.GetSelection()].name)
		average = self.user.get_current_account().r.average_expense(self.expenseList[self.listBoxExpenses.GetSelection()].name)
		index = self.listBoxExpenses.GetSelection()        
		if len(elist) > 0:
			result = wx.MessageBox('The average amount for this expense is ${0}. Click [Yes] to set this as the new amount for this expense'.format(round(average[0],2)), 'Use Average?', wx.YES_NO | wx.CENTRE)
			if result == wx.YES:
				self.textCtrlAmount.Clear()
				self.textCtrlAmount.WriteText('$'+str(round(average[0],2)))
				self.expenseList[index].amount = round(average[0],2)
				if average[1] != 0:
					self.choiceFrequencyNumber.SetStringSelection(str(int(average[1])))
					self.choiceFrequencyDesignator.SetStringSelection('day(s)')                 
					self.expenseList[index].frequencyNumber = average[1]
					self.expenseList[index].frequencyDesignator = 'day(s)'
					self.textCtrlMonthlyExpenses.Clear() 
					self.textCtrlAnnualExpenses.Clear() 
					self.textCtrlMonthlyExpenses.WriteText('$'+str(round(self.user.b.monthly_expenses(self.user),2)))
					self.textCtrlAnnualExpenses.WriteText('$'+str(round(self.user.b.annual_expenses(self.user),2)))        
				self.listBoxExpenses.Clear()
				self.listBoxExpenses.InsertItems([e.name for e in self.expenseList],0)
				init.save()
			else: 
				self.listBoxExpenses.Clear()
				self.listBoxExpenses.InsertItems([e.name for e in self.expenseList],0)
		else: wx.MessageBox('To get an average for this expense, you need to have at least two records of it in your transaction list that were not entered on the same day. There are no records yet.', 'No expense history for this item', wx.OK | wx.CENTRE)        
		
	def OnChoiceFrequencyNumberChoice(self, event):
		self.frequencyNumber = int(self.choiceFrequencyNumber.GetStringSelection())  

	def OnChoiceFrequencyDesignatorChoice(self, event):
		self.frequencyDesignator = self.choiceFrequencyDesignator.GetStringSelection()
	
	def clear_boxes(self):
		self.textCtrlExpenseName.Clear()
		self.textCtrlAmount.Clear() 
		self.textCtrlMonthlyExpenses.Clear() 
		self.textCtrlAnnualExpenses.Clear()  
		self.choiceFrequencyNumber.SetSelection(-1)          
		self.choiceFrequencyDesignator.SetSelection(-1)
		
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
		
	def set_backcolor_white(self, ctrls):
		for c in ctrls:
			c.SetBackgroundColour(wx.Colour(255, 255, 255))
			c.Refresh()
		
	def set_backcolor_grey(self, ctrl):
		ctrl.SetBackgroundColour(wx.Colour(240, 240, 240))
		ctrl.Refresh()     
		
	def OnButtonHomeButton(self, event):
		self.Hide()
		self.Close()
		self.main = CBudgetP_Home.create(None)
		self.main.Show()
		
	def OnButtonAccountsButton(self, event):
		self.Hide()
		self.Close()
		self.main = CBudgetP_Accounts.create(None)
		self.main.Show()
		
	def OnButtonIncomesButton(self, event):
		self.Hide()
		self.Close()
		self.main = CBudgetP_Incomes.create(None)
		self.main.Show() 
		
	def OnButtonCreditsButton(self, event):
		self.Hide()
		self.Close()
		self.main = CBudgetP_Credits.create(None)
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
		self.user.s.show_expenses_due = True
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
		if self.e.run_count <= 10: init.delete_install_folder()
		self.Close()         
		init.end_process()  

