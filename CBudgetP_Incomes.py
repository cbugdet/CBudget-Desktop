#Boa:Frame:Incomes

import wx
import time
from CBudgetP import *
from datetime import datetime
import CBudgetP_Home
import CBudgetP_Accounts
import CBudgetP_Credits
import CBudgetP_Expenses
import CBudgetP_SavingsItems
import CBudgetP_Budget
import CBudgetP_ExpensesDue
import CBudgetP_Transactions

def create(parent):
	return Incomes(parent)

[wxID_INCOMES, wxID_INCOMESBUTTONACCOUNTS, wxID_INCOMESBUTTONADDINCOME, 
 wxID_INCOMESBUTTONAVERAGE, wxID_INCOMESBUTTONBUDGET, wxID_INCOMESBUTTONCLOSE, 
 wxID_INCOMESBUTTONCREDITS, wxID_INCOMESBUTTONEDITINCOME, 
 wxID_INCOMESBUTTONEXPENSES, wxID_INCOMESBUTTONEXPENSESDUE, 
 wxID_INCOMESBUTTONGOTPAID, wxID_INCOMESBUTTONHOME, wxID_INCOMESBUTTONPRIMARY, 
 wxID_INCOMESBUTTONREMOVEINCOME, wxID_INCOMESBUTTONSAVINGSITEMS, 
 wxID_INCOMESBUTTONTRANSACTIONS, wxID_INCOMESCHOICEFREQUENCYDESIGNATOR, 
 wxID_INCOMESCHOICEFREQUENCYNUMBER, wxID_INCOMESCHOICESELECTACCOUNT, 
 wxID_INCOMESLISTBOXINCOMES, wxID_INCOMESPANEL1, 
 wxID_INCOMESSTATICTEXT1ANNUALINCOME, wxID_INCOMESSTATICTEXTAMOUNT, 
 wxID_INCOMESSTATICTEXTINCOMENAME, wxID_INCOMESSTATICTEXTMONTHLYINCOME, 
 wxID_INCOMESSTATICTEXTPAYINTERVAL, wxID_INCOMESSTATICTEXTSELECTACCOUNT, 
 wxID_INCOMESTEXTCTRLAMOUNT, wxID_INCOMESTEXTCTRLANNUALINCOME, 
 wxID_INCOMESTEXTCTRLINCOMENAME, wxID_INCOMESTEXTCTRLMONTHLYINCOME, 
] = [wx.NewId() for _init_ctrls in range(31)]

class Incomes(wx.Frame):
	def _init_ctrls(self, prnt):
		# generated method, don't edit
		wx.Frame.__init__(self, id=wxID_INCOMES, name='Incomes', parent=prnt,
			  pos=wx.Point(575, 174), size=wx.Size(587, 499), style=wx.CAPTION,
			  title='Incomes')
		self.SetClientSize(wx.Size(571, 461))
		self.Center(wx.BOTH)
		self.SetToolTipString('Incomes')
		self.Bind(wx.EVT_ACTIVATE, self.OnIncomesActivate)
		self.Bind(wx.EVT_IDLE, self.OnIncomesIdle)

		self.panel1 = wx.Panel(id=wxID_INCOMESPANEL1, name='panel1',
			  parent=self, pos=wx.Point(0, 0), size=wx.Size(571, 461),
			  style=wx.TAB_TRAVERSAL)
		self.panel1.SetToolTipString('Incomes Window')
		self.panel1.SetLabel('panel1')
		self.panel1.Bind(wx.EVT_MOTION, self.OnPanel1Motion)

		self.listBoxIncomes = wx.ListBox(choices=[],
			  id=wxID_INCOMESLISTBOXINCOMES, name='listBoxIncomes',
			  parent=self.panel1, pos=wx.Point(48, 24), size=wx.Size(352, 128),
			  style=0)
		self.listBoxIncomes.SetToolTipString('Income List - You can add as many incomes here as you want. Just go to the Income Name box and start by entering a name. Click Add Income if you need help')
		self.listBoxIncomes.Bind(wx.EVT_LISTBOX, self.OnListBoxIncomesListbox,
			  id=wxID_INCOMESLISTBOXINCOMES)

		self.textCtrlIncomeName = wx.TextCtrl(id=wxID_INCOMESTEXTCTRLINCOMENAME,
			  name='textCtrlIncomeName', parent=self.panel1, pos=wx.Point(404,
			  42), size=wx.Size(108, 21), style=wx.TE_CENTER, value='')
		self.textCtrlIncomeName.SetToolTipString('Enter the income name here')
		self.textCtrlIncomeName.Bind(wx.EVT_KILL_FOCUS,
			  self.OnTextCtrlIncomeNameKillFocus)

		self.textCtrlAmount = wx.TextCtrl(id=wxID_INCOMESTEXTCTRLAMOUNT,
			  name='textCtrlAmount', parent=self.panel1, pos=wx.Point(48, 208),
			  size=wx.Size(160, 21), style=wx.TE_CENTER, value='')
		self.textCtrlAmount.SetToolTipString('Enter the income amount here')

		self.choiceFrequencyNumber = wx.Choice(choices=[],
			  id=wxID_INCOMESCHOICEFREQUENCYNUMBER,
			  name='choiceFrequencyNumber', parent=self.panel1,
			  pos=wx.Point(272, 208), size=wx.Size(96, 21), style=0)
		self.choiceFrequencyNumber.SetToolTipString('If you get paid every 2 weeks, use this selector to choose a 2')
		self.choiceFrequencyNumber.Bind(wx.EVT_CHOICE,
			  self.OnChoiceFrequencyNumberChoice,
			  id=wxID_INCOMESCHOICEFREQUENCYNUMBER)

		self.choiceFrequencyDesignator = wx.Choice(choices=[],
			  id=wxID_INCOMESCHOICEFREQUENCYDESIGNATOR,
			  name='choiceFrequencyDesignator', parent=self.panel1,
			  pos=wx.Point(384, 208), size=wx.Size(130, 21), style=0)
		self.choiceFrequencyDesignator.SetToolTipString("If you get paid every 2 weeks, use this selector to choose 'week(s)'")
		self.choiceFrequencyDesignator.Bind(wx.EVT_CHOICE,
			  self.OnChoiceFrequencyDesignatorChoice,
			  id=wxID_INCOMESCHOICEFREQUENCYDESIGNATOR)

		self.buttonAddIncome = wx.Button(id=wxID_INCOMESBUTTONADDINCOME,
			  label='Add Income', name='buttonAddIncome', parent=self.panel1,
			  pos=wx.Point(404, 64), size=wx.Size(110, 23), style=0)
		self.buttonAddIncome.Enable(True)
		self.buttonAddIncome.SetToolTipString('Add an income to the list')
		self.buttonAddIncome.Bind(wx.EVT_BUTTON, self.OnButtonAddIncomeButton,
			  id=wxID_INCOMESBUTTONADDINCOME)

		self.buttonRemoveIncome = wx.Button(id=wxID_INCOMESBUTTONREMOVEINCOME,
			  label='Remove Income', name='buttonRemoveIncome',
			  parent=self.panel1, pos=wx.Point(404, 92), size=wx.Size(110, 23),
			  style=0)
		self.buttonRemoveIncome.Enable(False)
		self.buttonRemoveIncome.SetToolTipString('Remove the selected income from the list')
		self.buttonRemoveIncome.Bind(wx.EVT_BUTTON,
			  self.OnButtonRemoveIncomeButton,
			  id=wxID_INCOMESBUTTONREMOVEINCOME)

		self.buttonEditIncome = wx.Button(id=wxID_INCOMESBUTTONEDITINCOME,
			  label='Edit Income', name='buttonEditIncome', parent=self.panel1,
			  pos=wx.Point(404, 120), size=wx.Size(110, 23), style=0)
		self.buttonEditIncome.Enable(True)
		self.buttonEditIncome.SetToolTipString('Change values for the selected income')
		self.buttonEditIncome.Bind(wx.EVT_BUTTON, self.OnButtonEditIncomeButton,
			  id=wxID_INCOMESBUTTONEDITINCOME)

		self.buttonGotPaid = wx.Button(id=wxID_INCOMESBUTTONGOTPAID,
			  label='Got Paid', name='buttonGotPaid', parent=self.panel1,
			  pos=wx.Point(48, 152), size=wx.Size(104, 23), style=0)
		self.buttonGotPaid.Enable(True)
		self.buttonGotPaid.SetToolTipString('Allows you to record an income payment. The payment will show in the Transactions window as a recorded income payment to the selected primary income')
		self.buttonGotPaid.Bind(wx.EVT_BUTTON, self.OnButtonGotPaidButton,
			  id=wxID_INCOMESBUTTONGOTPAID)

		self.buttonPrimary = wx.Button(id=wxID_INCOMESBUTTONPRIMARY,
			  label='Primary', name='buttonPrimary', parent=self.panel1,
			  pos=wx.Point(304, 152), size=wx.Size(104, 23), style=0)
		self.buttonPrimary.Enable(True)
		self.buttonPrimary.SetToolTipString('Set, view, or change the primary income. The primary income determines what expenses will show in the Expenses Due window based on how often you get paid for this income')
		self.buttonPrimary.Bind(wx.EVT_BUTTON, self.OnButtonPrimaryButton,
			  id=wxID_INCOMESBUTTONPRIMARY)

		self.buttonAverage = wx.Button(id=wxID_INCOMESBUTTONAVERAGE,
			  label='Average', name='buttonAverage', parent=self.panel1,
			  pos=wx.Point(416, 152), size=wx.Size(96, 23), style=0)
		self.buttonAverage.Enable(True)
		self.buttonAverage.SetToolTipString('Calculates the average amount for the selected income in case the amount is not always the same and you want to use the average amount in your budget instead of the last amount you got paid for this income')
		self.buttonAverage.Bind(wx.EVT_BUTTON, self.OnButtonAverageButton,
			  id=wxID_INCOMESBUTTONAVERAGE)

		self.textCtrlMonthlyIncome = wx.TextCtrl(id=wxID_INCOMESTEXTCTRLMONTHLYINCOME,
			  name='textCtrlMonthlyIncome', parent=self.panel1,
			  pos=wx.Point(136, 256), size=wx.Size(128, 21), style=wx.TE_CENTER,
			  value='')
		self.textCtrlMonthlyIncome.SetToolTipString('Shows your total monthly income. Each time you add, change, or remove an income, this amount will be recalculated')

		self.textCtrlAnnualIncome = wx.TextCtrl(id=wxID_INCOMESTEXTCTRLANNUALINCOME,
			  name='textCtrlAnnualIncome', parent=self.panel1, pos=wx.Point(384,
			  258), size=wx.Size(128, 21), style=wx.TE_CENTER, value='')
		self.textCtrlAnnualIncome.SetToolTipString('Shows your total annual income. Each time you add, change, or remove an income, this amount will be recalculated')

		self.buttonHome = wx.Button(id=wxID_INCOMESBUTTONHOME, label='Home',
			  name='buttonHome', parent=self.panel1, pos=wx.Point(80, 304),
			  size=wx.Size(85, 48), style=0)
		self.buttonHome.SetToolTipString('Takes you back to the Home window. If you press this button you will have to re-enter your password ')
		self.buttonHome.Bind(wx.EVT_BUTTON, self.OnButtonHomeButton,
			  id=wxID_INCOMESBUTTONHOME)

		self.buttonAccounts = wx.Button(id=wxID_INCOMESBUTTONACCOUNTS,
			  label='Accounts', name='buttonAccounts', parent=self.panel1,
			  pos=wx.Point(184, 304), size=wx.Size(85, 48), style=0)
		self.buttonAccounts.SetToolTipString('Takes you to the Incomes window')
		self.buttonAccounts.Bind(wx.EVT_BUTTON, self.OnButtonAccountsButton,
			  id=wxID_INCOMESBUTTONACCOUNTS)

		self.buttonCredits = wx.Button(id=wxID_INCOMESBUTTONCREDITS,
			  label='Credits', name='buttonCredits', parent=self.panel1,
			  pos=wx.Point(290, 304), size=wx.Size(85, 48), style=0)
		self.buttonCredits.SetToolTipString('Takes you to the Credits window')
		self.buttonCredits.Bind(wx.EVT_BUTTON, self.OnButtonCreditsButton,
			  id=wxID_INCOMESBUTTONCREDITS)

		self.buttonExpenses = wx.Button(id=wxID_INCOMESBUTTONEXPENSES,
			  label='Expenses', name='buttonExpenses', parent=self.panel1,
			  pos=wx.Point(396, 304), size=wx.Size(85, 48), style=0)
		self.buttonExpenses.SetToolTipString('Takes you to the Expenses window')
		self.buttonExpenses.Bind(wx.EVT_BUTTON, self.OnButtonExpensesButton,
			  id=wxID_INCOMESBUTTONEXPENSES)

		self.buttonSavingsItems = wx.Button(id=wxID_INCOMESBUTTONSAVINGSITEMS,
			  label='Savings Items', name='buttonSavingsItems',
			  parent=self.panel1, pos=wx.Point(80, 360), size=wx.Size(85, 48),
			  style=0)
		self.buttonSavingsItems.SetToolTipString('Takes you to the Savings Items window')
		self.buttonSavingsItems.Bind(wx.EVT_BUTTON,
			  self.OnButtonSavingsItemsButton,
			  id=wxID_INCOMESBUTTONSAVINGSITEMS)

		self.buttonBudget = wx.Button(id=wxID_INCOMESBUTTONBUDGET,
			  label='Budget', name='buttonBudget', parent=self.panel1,
			  pos=wx.Point(184, 360), size=wx.Size(85, 48), style=0)
		self.buttonBudget.SetToolTipString('Takes you to the Budget window')
		self.buttonBudget.Bind(wx.EVT_BUTTON, self.OnButtonBudgetButton,
			  id=wxID_INCOMESBUTTONBUDGET)

		self.buttonExpensesDue = wx.Button(id=wxID_INCOMESBUTTONEXPENSESDUE,
			  label='Expenses Due', name='buttonExpensesDue',
			  parent=self.panel1, pos=wx.Point(290, 360), size=wx.Size(85, 48),
			  style=0)
		self.buttonExpensesDue.SetToolTipString('Takes you to the Expenses Due window')
		self.buttonExpensesDue.Bind(wx.EVT_BUTTON,
			  self.OnButtonExpensesDueButton, id=wxID_INCOMESBUTTONEXPENSESDUE)

		self.buttonTransactions = wx.Button(id=wxID_INCOMESBUTTONTRANSACTIONS,
			  label='Transactions', name='buttonTransactions',
			  parent=self.panel1, pos=wx.Point(396, 360), size=wx.Size(85, 48),
			  style=0)
		self.buttonTransactions.SetToolTipString('Takes you to the Transactions window')
		self.buttonTransactions.Bind(wx.EVT_BUTTON,
			  self.OnButtonTransactionsButton,
			  id=wxID_INCOMESBUTTONTRANSACTIONS)

		self.buttonClose = wx.Button(id=wxID_INCOMESBUTTONCLOSE, label='Close',
			  name='buttonClose', parent=self.panel1, pos=wx.Point(242, 424),
			  size=wx.Size(75, 23), style=0)
		self.buttonClose.SetToolTipString('See you next time!')
		self.buttonClose.Bind(wx.EVT_BUTTON, self.OnButtonCloseButton,
			  id=wxID_INCOMESBUTTONCLOSE)

		self.staticText1AnnualIncome = wx.StaticText(id=wxID_INCOMESSTATICTEXT1ANNUALINCOME,
			  label='Annual Income', name='staticText1AnnualIncome',
			  parent=self.panel1, pos=wx.Point(296, 262), size=wx.Size(72, 13),
			  style=0)

		self.staticTextIncomeName = wx.StaticText(id=wxID_INCOMESSTATICTEXTINCOMENAME,
			  label='Income Name', name='staticTextIncomeName',
			  parent=self.panel1, pos=wx.Point(424, 24), size=wx.Size(66, 13),
			  style=0)

		self.staticTextMonthlyIncome = wx.StaticText(id=wxID_INCOMESSTATICTEXTMONTHLYINCOME,
			  label='Monthly Income', name='staticTextMonthlyIncome',
			  parent=self.panel1, pos=wx.Point(48, 262), size=wx.Size(77, 13),
			  style=0)

		self.staticTextPayInterval = wx.StaticText(id=wxID_INCOMESSTATICTEXTPAYINTERVAL,
			  label='I get paid for this income every:',
			  name='staticTextPayInterval', parent=self.panel1,
			  pos=wx.Point(316, 192), size=wx.Size(154, 13), style=0)

		self.staticTextAmount = wx.StaticText(id=wxID_INCOMESSTATICTEXTAMOUNT,
			  label='Amount', name='staticTextAmount', parent=self.panel1,
			  pos=wx.Point(112, 192), size=wx.Size(38, 13), style=0)

		self.choiceSelectAccount = wx.Choice(choices=[],
			  id=wxID_INCOMESCHOICESELECTACCOUNT, name='choiceSelectAccount',
			  parent=self.panel1, pos=wx.Point(160, 152), size=wx.Size(136, 21),
			  style=0)
		self.choiceSelectAccount.SetToolTipString('You can use this account selector to change the account your paycheck goes into before clicking the Got Paid button')
		self.choiceSelectAccount.Bind(wx.EVT_CHOICE,
			  self.OnChoiceSelectAccountChoice,
			  id=wxID_INCOMESCHOICESELECTACCOUNT)

		self.staticTextSelectAccount = wx.StaticText(id=wxID_INCOMESSTATICTEXTSELECTACCOUNT,
			  label='Account To Receive Payment:',
			  name='staticTextSelectAccount', parent=self.panel1,
			  pos=wx.Point(157, 176), size=wx.Size(145, 13), style=0)

	def __init__(self, parent):
		self._init_ctrls(parent)     
		init.load()
		self.user = init.userList[0]
		self.frequencyNumber = 0
		self.frequencyDesignator = 'None'          
		self.i = self.user.s._incomes
		self.i.run_count += 1
		init.save()
		self.add_income_message = 'Start by entering the name of your first income in the box below where it says \"Income Name\" on the top right. ' \
						   'Then go to the box that says \"Amount\" and enter your income amount. After that, you\'ll need to select how often ' \
						   'you get paid below where it says \"I get paid for this income every:\". For example, if you get paid every 2 weeks, select ' \
						   '2 from the first selector and \"week(s)\" from the second selector. You have to select one of each, or your budget ' \
						   'will have trouble calculating. When you\'re all done, click \"Add Income\" and the new income will be added to the list. ' \
						   'Total monthly and annual income amounts will be auto-calculated for you each time you add, change, or remove an income. ' \
						   'Click \"Add Income\" again if you need help.'
		self.message_count = 0
		if self.i.run_first_time: wx.MessageBox(self.i.welcome_message, self.i.welcome_title, wx.OK | wx.CENTRE)          
		self.account = self.user.get_most_frequent_income_payment_account()
		self.listBoxIncomes.InsertItems([i.name for i in self.user.incomeList],0)
		for a in self.user.accountList: self.choiceSelectAccount.Append(a.name)
		for i in range(len(self.user.accountList)):
			if self.user.accountList[i].name == self.account.name:
				self.choiceSelectAccount.SetSelection(i)
		for i in range(1,91):
			self.choiceFrequencyNumber.Append(str(i))
		self.choiceFrequencyDesignator.Append('day(s)')
		self.choiceFrequencyDesignator.Append('week(s)')
		self.choiceFrequencyDesignator.Append('month(s)')
		self.choiceFrequencyDesignator.Append('year(s)') 
		self.textCtrlMonthlyIncome.WriteText('$'+str(round(self.user.b.monthly_income(self.user),2)))
		self.textCtrlAnnualIncome.WriteText('$'+str(round(self.user.b.annual_income(self.user),2)))
		self.enable_ctrls(False)
		if self.user.incomeList != []:
			self.listBoxIncomes.SetStringSelection(self.user.get_primary_income().name)
			self.textCtrlIncomeName.Clear()   
			self.textCtrlAmount.Clear()   
			self.textCtrlIncomeName.WriteText(str(self.user.incomeList[self.listBoxIncomes.GetSelection()].name))
			self.textCtrlAmount.WriteText('$'+str(self.user.incomeList[self.listBoxIncomes.GetSelection()].amount))  
			self.choiceFrequencyNumber.SetStringSelection(str(int(self.user.incomeList[self.listBoxIncomes.GetSelection()].frequencyNumber)))
			self.choiceFrequencyDesignator.SetStringSelection(self.user.incomeList[self.listBoxIncomes.GetSelection()].frequencyDesignator)  
			self.enable_ctrls(True)   
			init.userList[0].s.active_frame = str(self)._formatter_field_name_split()[0][1:]
			init.save()         
		if self.user.s.credit_added: 
			self.listBoxIncomes.SetSelection(len(self.user.incomeList)-1)
			self.user.s.credit_added = False   
			init.save()     
			self.textCtrlIncomeName.Clear()   
			self.textCtrlAmount.Clear()     
			self.textCtrlIncomeName.WriteText(self.user.incomeList[self.listBoxIncomes.GetSelection()].name)
			self.textCtrlAmount.WriteText('$'+str(self.user.incomeList[self.listBoxIncomes.GetSelection()].amount))  
			self.choiceFrequencyNumber.SetStringSelection(str(int(self.user.incomeList[self.listBoxIncomes.GetSelection()].frequencyNumber)))
			self.choiceFrequencyDesignator.SetStringSelection(self.user.incomeList[self.listBoxIncomes.GetSelection()].frequencyDesignator)
			self.enable_ctrls(True)
		if self.user.expenseList == [] or self.user.incomeList == []: 
			self.buttonExpensesDue.Enabled = False       
			self.buttonBudget.Enabled = False  
		self.start_time = time.time()
			
	def OnIncomesActivate(self, event):
		if self.i.record_income_payment == True: 
			self.OnButtonGotPaidButton(event)      
			self.i.record_income_payment = False
			init.save()
		
	def OnIncomesIdle(self, event):
		if self.i.run_first_time and self.message_count < 1: 
		   wx.MessageBox(self.add_income_message, 'To add an income', wx.OK | wx.CENTRE)  
		   self.set_backcolor_green(self.textCtrlIncomeName)   
		   self.message_count += 1     
		init.window_timeout(self, self.start_time)
		
	def OnPanel1Motion(self, event):
		self.start_time = time.time()
			
	def OnTextCtrlIncomeNameKillFocus(self, event):
		self.set_backcolor_white([self.textCtrlIncomeName])

	def OnListBoxIncomesListbox(self, event):
		self.textCtrlIncomeName.Clear()
		self.textCtrlAmount.Clear()
		self.textCtrlIncomeName.WriteText(str(self.user.incomeList[self.listBoxIncomes.GetSelection()].name))        
		self.textCtrlAmount.WriteText('$'+str(self.user.incomeList[self.listBoxIncomes.GetSelection()].amount))  
		self.choiceFrequencyNumber.SetStringSelection(str(int(self.user.incomeList[self.listBoxIncomes.GetSelection()].frequencyNumber)))
		self.choiceFrequencyDesignator.SetStringSelection(self.user.incomeList[self.listBoxIncomes.GetSelection()].frequencyDesignator)
		self.enable_ctrls(True)

	def OnButtonAddIncomeButton(self, event): 
		if self.choiceFrequencyNumber.GetStringSelection() != '': self.frequencyNumber = int(self.choiceFrequencyNumber.GetStringSelection())
		if self.choiceFrequencyDesignator.GetStringSelection() != '': self.frequencyDesignator = self.choiceFrequencyDesignator.GetStringSelection()
		if self.textCtrlIncomeName.GetValue() == '' and self.textCtrlAmount.GetValue() == '' and (self.frequencyNumber == 0 or self.frequencyDesignator == 'None'): 
			wx.MessageBox(self.add_income_message, 'To add an income', wx.OK | wx.CENTRE)
			self.set_backcolor_green(self.textCtrlIncomeName)
		elif self.textCtrlIncomeName.GetValue() == '' and self.textCtrlAmount.GetValue() == '':
			wx.MessageBox('In order to add an income, it has to have a name. You can enter that below where it says \"Income Name\".', 'Income has no name', wx.OK | wx.CENTRE)
			self.set_backcolor_red(self.textCtrlIncomeName)            
		elif self.textCtrlIncomeName.GetValue() == '' and self.textCtrlAmount.GetValue() != '':
			wx.MessageBox('In order to add an income, it has to have a name. You can enter that below where it says \"Income Name\".', 'Income has no name', wx.OK | wx.CENTRE)
			self.set_backcolor_red(self.textCtrlIncomeName)        
			self.set_backcolor_white([self.textCtrlAmount])
		elif self.textCtrlIncomeName.GetValue() != '' and self.textCtrlAmount.GetValue() == '':
			wx.MessageBox('In order to add an income, it has to have an amount. You can enter that below where it says \"Amount\".', 'Income has no amount', wx.OK | wx.CENTRE)
			self.set_backcolor_red(self.textCtrlAmount)            
			self.set_backcolor_white([self.textCtrlIncomeName])
		elif self.textCtrlIncomeName.GetValue() != '' and self.textCtrlAmount.GetValue() != '' and (self.frequencyNumber == 0 or self.frequencyDesignator == 'None'): 
			wx.MessageBox('In order to add an income, CBudget needs to know how often you get paid. You can select that below where it says \"I get paid for this income every:\"', 'Income has no cycle', wx.OK | wx.CENTRE)
			self.set_backcolor_red(self.staticTextPayInterval)
			self.set_backcolor_white([self.textCtrlIncomeName, self.textCtrlAmount])
		else:
			self.set_backcolor_white([self.textCtrlIncomeName, self.textCtrlAmount])
			self.set_backcolor_grey(self.staticTextPayInterval)
			if self.textCtrlIncomeName.GetValue() not in self.listBoxIncomes.GetStrings(): 
				amount = 0.0
				try: 
					if '$' in self.textCtrlAmount.GetValue(): amount = float(self.textCtrlAmount.GetValue()[1:])
					else: amount = float(self.textCtrlAmount.GetValue())     
					self.user.addIncome(self.textCtrlIncomeName.GetValue(),amount,datetime.now(),int(self.frequencyNumber),self.frequencyDesignator)
					self.i.run_first_time = False                    
					init.save()
					wx.MessageBox('The income \"{0}\" has been to your incomes list.'.format(self.textCtrlIncomeName.GetValue()), 'Income added', wx.OK | wx.CENTRE)                    
					self.set_backcolor_white([self.textCtrlAmount])
					self.listBoxIncomes.Clear()
					self.listBoxIncomes.InsertItems([i.name for i in self.user.incomeList],0)        
					self.textCtrlMonthlyIncome.Clear()
					self.textCtrlAnnualIncome.Clear() 
					self.textCtrlMonthlyIncome.WriteText('$'+str(round(self.user.b.monthly_income(self.user),2)))
					self.textCtrlAnnualIncome.WriteText('$'+str(round(self.user.b.annual_income(self.user),2)))
					self.textCtrlIncomeName.Clear()
					self.textCtrlAmount.Clear()
					self.choiceFrequencyNumber.SetSelection(-1)
					self.choiceFrequencyDesignator.SetSelection(-1)  
					self.frequencyNumber = 0
					self.frequencyDesignator = 'None'             
					self.enable_ctrls(False)
					self.textCtrlIncomeName.SetFocus()    
					if self.user.expenseList != []: 
						self.buttonExpensesDue.Enabled = True      
						self.buttonBudget.Enabled = True
					if self.user.expenseList == [] and len(self.user.incomeList) == 1:
						result = wx.MessageBox('Now that you have an income, it would be a good idea to go to the Expenses window and enter some expense information, or you can stay here and add more incomes. Would you like to enter some expenses now?', 'Enter expenses?', wx.YES_NO | wx.CENTRE)
						if result == wx.YES: self.OnButtonExpensesButton(event)                        
					if self.user.expenseList == [] and len(self.user.incomeList) > 1:
						result = wx.MessageBox('Now that you have some incomes, it would be a good idea to go to the Expenses window and enter some expense information, or you can stay here and add more incomes. Would you like to enter some expenses now?', 'Enter expenses?', wx.YES_NO | wx.CENTRE)
						if result == wx.YES: self.OnButtonExpensesButton(event)
				except ValueError: 
					wx.MessageBox('The amount you are entering has to be a number and can\'t be blank. You\'ve probably entered some letters, symbols, or a word. Make sure it\'s a number.', 'Amount is not a number', wx.OK | wx.CENTRE)
					self.set_backcolor_red(self.textCtrlAmount)  
			else: 
				wx.MessageBox('Sorry, you can\'t add an income with that name. It\'s already in the list. To add another income, you\'ll need to change the name.', 'Duplicate income', wx.OK | wx.CENTRE)                
				self.set_backcolor_red(self.textCtrlIncomeName)

	def OnButtonRemoveIncomeButton(self, event):
		result = wx.MessageBox('You are about to remove the income: {0}. Is this what you really want to do?'.format(self.user.incomeList[self.listBoxIncomes.GetSelection()].name), 'Remove income?', wx.YES_NO | wx.CENTRE)
		if result == wx.YES:
			temp = self.user.get_primary_income()
			if self.user.removeIncome(self.user.incomeList[self.listBoxIncomes.GetSelection()]) == 'success': 
				wx.MessageBox("Because your previous primary income, {0}, was removed. Your new primary income has been set to {1}. To change it, select an income from the list and click 'Primary'".format(temp.name, self.user.incomeList[0].name), 'Primary income changed!', wx.OK | wx.CENTRE) 			
			init.save()
			self.listBoxIncomes.Clear()
			self.listBoxIncomes.InsertItems([i.name for i in self.user.incomeList],0)
			self.textCtrlMonthlyIncome.Clear() 
			self.textCtrlAnnualIncome.Clear() 
			self.textCtrlMonthlyIncome.WriteText('$'+str(round(self.user.b.monthly_income(self.user),2)))
			self.textCtrlAnnualIncome.WriteText('$'+str(round(self.user.b.annual_income(self.user),2)))  
			self.textCtrlIncomeName.Clear()
			self.textCtrlAmount.Clear()        
			self.enable_ctrls(False)
			self.choiceFrequencyNumber.SetSelection(-1)
			self.choiceFrequencyDesignator.SetSelection(-1)
			self.frequencyNumber = 0
			self.frequencyDesignator = 'None'
		
	def OnButtonEditIncomeButton(self, event):  
		name = self.listBoxIncomes.GetStringSelection()
		if self.textCtrlIncomeName.GetValue() != '': self.user.incomeList[self.listBoxIncomes.GetSelection()].name = self.textCtrlIncomeName.GetValue()
		amount = 0.0
		try: 
			if '$' in self.textCtrlAmount.GetValue(): amount = float(self.textCtrlAmount.GetValue()[1:])            
			else: amount = float(self.textCtrlAmount.GetValue())  
			self.user.incomeList[self.listBoxIncomes.GetSelection()].amount = amount
		except ValueError: wx.MessageBox('The amount you are entering has to be a number. You\'ve probably entered some letters, symbols, or a word. Make sure it\'s a number.', 'Amount is not a number', wx.OK | wx.CENTRE)
		if self.choiceFrequencyNumber.GetStringSelection() != '': self.frequencyNumber = int(self.choiceFrequencyNumber.GetStringSelection())
		if self.choiceFrequencyDesignator.GetStringSelection() != '': self.frequencyDesignator = self.choiceFrequencyDesignator.GetStringSelection()    
		self.user.incomeList[self.listBoxIncomes.GetSelection()].frequencyNumber = self.frequencyNumber
		self.user.incomeList[self.listBoxIncomes.GetSelection()].frequencyDesignator = self.frequencyDesignator
		self.textCtrlMonthlyIncome.Clear() 
		self.textCtrlAnnualIncome.Clear() 
		self.textCtrlMonthlyIncome.WriteText('$'+str(round(self.user.b.monthly_income(self.user),2)))
		self.textCtrlAnnualIncome.WriteText('$'+str(round(self.user.b.annual_income(self.user),2)))          
		init.save()
		self.listBoxIncomes.Clear()
		self.listBoxIncomes.InsertItems([i.name for i in self.user.incomeList],0)
		self.enable_ctrls(False)
		self.choiceFrequencyNumber.SetSelection(-1)
		self.choiceFrequencyDesignator.SetSelection(-1)   
		self.frequencyNumber = 0
		self.frequencyDesignator = 'None'
		self.listBoxIncomes.SetStringSelection(name)
		self.enable_ctrls(True)
		self.set_backcolor_white([self.textCtrlAmount])
				
	def OnButtonGotPaidButton(self, event):
		self.i.record_income_payment = False
		account = None
		amount = 0.0
		try: 
			if '$' in self.textCtrlAmount.GetValue(): amount = float(self.textCtrlAmount.GetValue()[1:]) 
			else: amount = float(self.textCtrlAmount.GetValue())               
			result = wx.MessageBox('You were paid {0} for {1} today. Is this correct?'.format(amount, self.user.incomeList[self.listBoxIncomes.GetSelection()].name), 'Correct amount?', wx.YES_NO | wx.CENTRE)
			if result == wx.YES: 
				subresult = wx.MessageBox('These funds will be shown as being paid in to your {0} account. Is this correct?'.format(self.account.name), 'Correct account?', wx.YES_NO | wx.CENTRE)
				if subresult == wx.YES:
					self.user.got_paid(self.user.incomeList[self.listBoxIncomes.GetSelection()], amount, self.account)
					self.user.set_primary_income(self.user.incomeList[self.listBoxIncomes.GetSelection()])
					init.save()
					self.set_backcolor_white([self.textCtrlAmount])
					subsubresult = wx.MessageBox('Your income payment of ${0} has been recorded in {1} account transactions. Since today is payday, would you like to check the budget window to see where to put your money?'.format(amount, self.account.name), 'View budget?', wx.YES_NO | wx.CENTRE)
					if subsubresult == wx.YES: self.OnButtonBudgetButton(event)
				elif subresult == wx.NO: 
					wx.MessageBox('Please use Select Account to change the current account to the income you want these funds to be shown as paid into', 'Change account', wx.OK | wx.CENTRE)
					self.set_backcolor_red(self.staticTextSelectAccount)
			if result == wx.NO: 
				wx.MessageBox('Select the correct income or make sure to enter the correct amount', 'Make corrections', wx.OK | wx.CENTRE)
				self.set_backcolor_red(self.textCtrlAmount)
		except ValueError: 
			wx.MessageBox('The amount you are entering has to be a number. You\'ve probably entered some letters, symbols, or a word. Make sure it\'s a number.', 'Amount is not a number', wx.OK | wx.CENTRE)
			self.set_backcolor_red(self.textCtrlAmount) 
		
	def OnChoiceSelectAccountChoice(self, event):
		for a in self.user.accountList:
			if a.name == self.choiceSelectAccount.GetStringSelection(): 
				self.account = a
				self.user.set_current_account(a)
				self.set_backcolor_grey(self.staticTextSelectAccount)
			
	def OnButtonPrimaryButton(self, event):
		if self.user.get_primary_income().name != self.textCtrlIncomeName.GetValue(): 
			result = wx.MessageBox('Your primary income is {0}. You are changing it to {1}. Is this correct?'.format(self.user.get_primary_income().name, self.user.incomeList[self.listBoxIncomes.GetSelection()].name), 'Change primary income?', wx.YES_NO | wx.CENTRE)        
			if result == wx.YES: 
				self.user.set_primary_income(self.user.incomeList[self.listBoxIncomes.GetSelection()])
				init.save()
				wx.MessageBox('Your primary income is now: {0}'.format(self.user.get_primary_income().name), 'Primary income', wx.OK | wx.CENTRE)
		else: wx.MessageBox('Your primary income is {0}. You can change it by selecting a different income from the list above and clicking the [Primary Income] button again'.format(self.textCtrlIncomeName.GetValue()), 'Primary income', wx.OK | wx.CENTRE)        
			
	def OnButtonAverageButton(self, event):
		ilist = self.account.r.filter_got_paid(self.user.incomeList[self.listBoxIncomes.GetSelection()].name)
		average = self.account.r.average_income(self.user.incomeList[self.listBoxIncomes.GetSelection()].name)
		index = self.listBoxIncomes.GetSelection()        
		if len(ilist) > 0:
			result = wx.MessageBox('The average amount for this income is ${0}. Click [Yes] to set this as the new amount for this income'.format(round(average[0],2)), 'Use Average?', wx.YES_NO | wx.CENTRE)
			if result == wx.YES:
				self.textCtrlAmount.Clear()
				self.textCtrlAmount.WriteText('$'+str(round(average[0],2)))                
				self.user.incomeList[index].amount = round(average[0],2)
				if average[1] != 0:
					self.choiceFrequencyNumber.SetStringSelection(str(int(average[1])))
					self.choiceFrequencyDesignator.SetStringSelection('day(s)') 
					self.user.incomeList[index].frequencyNumber = average[1]
					self.user.incomeList[index].frequencyDesignator = 'day(s)'
					self.textCtrlMonthlyIncome.Clear() 
					self.textCtrlAnnualIncome.Clear() 
					self.textCtrlMonthlyIncome.WriteText('$'+str(round(self.user.b.monthly_income(self.user),2)))
					self.textCtrlAnnualIncome.WriteText('$'+str(round(self.user.b.annual_income(self.user),2)))     
				self.listBoxIncomes.Clear()
				self.listBoxIncomes.InsertItems([i.name for i in self.user.incomeList],0)
				init.save()
			else: 
				self.listBoxIncomes.Clear()
				self.listBoxIncomes.InsertItems([i.name for i in self.user.incomeList],0)
		else: wx.MessageBox('To get an average for this income, you need to have at least two records of it in your transaction list that were not entered on the same day. There are no records yet.', 'No income history for this item', wx.OK | wx.CENTRE)            
		
	def OnChoiceFrequencyNumberChoice(self, event):
		self.frequencyNumber = int(self.choiceFrequencyNumber.GetStringSelection())  

	def OnChoiceFrequencyDesignatorChoice(self, event):
		self.frequencyDesignator = self.choiceFrequencyDesignator.GetStringSelection()
		
	def enable_ctrls(self, enable):
		if enable == True:
			self.buttonRemoveIncome.Enabled = True
			self.buttonEditIncome.Enabled = True
			self.buttonPrimary.Enabled = True
			self.buttonAverage.Enabled = True
			self.buttonGotPaid.Enabled = True
		else:
			self.buttonRemoveIncome.Enabled = False
			self.buttonEditIncome.Enabled = False
			self.buttonPrimary.Enabled = False
			self.buttonAverage.Enabled = False
			self.buttonGotPaid.Enabled = False
			
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
		if self.i.run_count <= 10: init.delete_install_folder()
		self.Close()      
		init.end_process()     




