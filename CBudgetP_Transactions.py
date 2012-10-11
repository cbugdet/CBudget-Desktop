#Boa:Frame:Transactions

import wx
import wx.lib.buttons
import wx.grid
from datetime import datetime
import time
import threading
import CBudgetP
from CBudgetP import init
import CBudgetP_Home
import CBudgetP_Accounts
import CBudgetP_Incomes
import CBudgetP_Credits
import CBudgetP_Expenses
import CBudgetP_SavingsItems
import CBudgetP_Budget
import CBudgetP_ExpensesDue

# To use the designer, comment the following code in the choices list in self.choiceSelectAccount:  a.name for a in init.userList[0].accountList


def create(parent):
	return Transactions(parent)

[wxID_TRANSACTIONS, wxID_TRANSACTIONSBUTTONACCOUNTS, 
 wxID_TRANSACTIONSBUTTONADDTRANSACTION, wxID_TRANSACTIONSBUTTONBUDGET, 
 wxID_TRANSACTIONSBUTTONCLOSE, wxID_TRANSACTIONSBUTTONCREDITS, 
 wxID_TRANSACTIONSBUTTONDATEFILTER, wxID_TRANSACTIONSBUTTONEDITTRANSACTION, 
 wxID_TRANSACTIONSBUTTONEXPENSES, wxID_TRANSACTIONSBUTTONEXPENSESDUE, 
 wxID_TRANSACTIONSBUTTONHOME, wxID_TRANSACTIONSBUTTONINCOMES, 
 wxID_TRANSACTIONSBUTTONREMOVETRANSACTION, 
 wxID_TRANSACTIONSBUTTONSAVINGSITEMS, wxID_TRANSACTIONSCHECKBOXTYPEFILTER, 
 wxID_TRANSACTIONSCHOICESELECTACCOUNT, 
 wxID_TRANSACTIONSCHOICESHOWTRANSACTIONS, wxID_TRANSACTIONSCHOICETYPE, 
 wxID_TRANSACTIONSDATEPICKERCTRLDATE, wxID_TRANSACTIONSDATEPICKERCTRLFROMDATE, 
 wxID_TRANSACTIONSDATEPICKERCTRLTODATE, wxID_TRANSACTIONSGRIDREGISTER, 
 wxID_TRANSACTIONSPANEL1, wxID_TRANSACTIONSSEARCHCTRLSEARCHTRANSACTIONS, 
 wxID_TRANSACTIONSSTATICTEXTAMOUNT, wxID_TRANSACTIONSSTATICTEXTBALANCE, 
 wxID_TRANSACTIONSSTATICTEXTCONF, wxID_TRANSACTIONSSTATICTEXTCREDITS, 
 wxID_TRANSACTIONSSTATICTEXTDATE, wxID_TRANSACTIONSSTATICTEXTDATEFILTER, 
 wxID_TRANSACTIONSSTATICTEXTDEBITS, wxID_TRANSACTIONSSTATICTEXTFROMDATE, 
 wxID_TRANSACTIONSSTATICTEXTNAME, wxID_TRANSACTIONSSTATICTEXTNOTE, 
 wxID_TRANSACTIONSSTATICTEXTSEARCH, wxID_TRANSACTIONSSTATICTEXTSELECTACCOUNT, 
 wxID_TRANSACTIONSSTATICTEXTSHOWTRANSACTIONS, 
 wxID_TRANSACTIONSSTATICTEXTTODATE, wxID_TRANSACTIONSSTATICTEXTTYPE, 
 wxID_TRANSACTIONSTEXTCTRLAMOUNT, wxID_TRANSACTIONSTEXTCTRLBALANCE, 
 wxID_TRANSACTIONSTEXTCTRLCONF, wxID_TRANSACTIONSTEXTCTRLCREDITS, 
 wxID_TRANSACTIONSTEXTCTRLDEBITS, wxID_TRANSACTIONSTEXTCTRLNAME, 
 wxID_TRANSACTIONSTEXTCTRLNOTE, 
] = [wx.NewId() for _init_ctrls in range(46)]

class Transactions(wx.Frame):
	def _init_ctrls(self, prnt):
		# generated method, don't edit
		wx.Frame.__init__(self, id=wxID_TRANSACTIONS, name='Transactions',
			  parent=prnt, pos=wx.Point(278, 30), size=wx.Size(810, 667),
			  style=wx.CAPTION, title='Transactions')
		self.SetClientSize(wx.Size(794, 629))
		self.Center(wx.BOTH)
		self.Bind(wx.EVT_IDLE, self.OnTransactionsIdle)

		self.panel1 = wx.Panel(id=wxID_TRANSACTIONSPANEL1, name='panel1',
			  parent=self, pos=wx.Point(0, 0), size=wx.Size(794, 629),
			  style=wx.TAB_TRAVERSAL)
		self.panel1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
			  'Tahoma'))
		self.panel1.SetToolTipString('Transaction Window. To edit or remove a transaction, click the row number to the left of the transaction name in the grid above')
		self.panel1.Bind(wx.EVT_MOTION, self.OnPanel1Motion)

		self.choiceSelectAccount = wx.Choice(choices=[],
			  id=wxID_TRANSACTIONSCHOICESELECTACCOUNT,
			  name='choiceSelectAccount', parent=self.panel1, pos=wx.Point(616,
			  408), size=wx.Size(130, 21), style=0)
		self.choiceSelectAccount.Enable(True)
		self.choiceSelectAccount.SetToolTipString('Allows you to select which account you want to see transactions for')
		self.choiceSelectAccount.SetStringSelection('')
		self.choiceSelectAccount.Bind(wx.EVT_CHOICE,
			  self.OnChoiceSelectAccountChoice,
			  id=wxID_TRANSACTIONSCHOICESELECTACCOUNT)

		self.textCtrlName = wx.TextCtrl(id=wxID_TRANSACTIONSTEXTCTRLNAME,
			  name='textCtrlName', parent=self.panel1, pos=wx.Point(40, 288),
			  size=wx.Size(100, 21), style=wx.TE_CENTER, value='')
		self.textCtrlName.SetToolTipString('Enter the name of the transaction here')
		self.textCtrlName.Bind(wx.EVT_TEXT, self.OnTextCtrlNameText,
			  id=wxID_TRANSACTIONSTEXTCTRLNAME)
		self.textCtrlName.Bind(wx.EVT_KILL_FOCUS, self.OnTextCtrlNameKillFocus)

		self.textCtrlAmount = wx.TextCtrl(id=wxID_TRANSACTIONSTEXTCTRLAMOUNT,
			  name='textCtrlAmount', parent=self.panel1, pos=wx.Point(160, 288),
			  size=wx.Size(100, 21), style=wx.TE_CENTER, value='')
		self.textCtrlAmount.SetToolTipString('Enter the amount of the transaction here')
		self.textCtrlAmount.Bind(wx.EVT_TEXT, self.OnTextCtrlAmountText,
			  id=wxID_TRANSACTIONSTEXTCTRLAMOUNT)

		self.datePickerCtrlDate = wx.DatePickerCtrl(id=wxID_TRANSACTIONSDATEPICKERCTRLDATE,
			  name='datePickerCtrlDate', parent=self.panel1, pos=wx.Point(280,
			  288), size=wx.Size(98, 21), style=wx.DP_SHOWCENTURY)
		self.datePickerCtrlDate.SetToolTipString('Select the date of the transaction here')

		self.textCtrlConf = wx.TextCtrl(id=wxID_TRANSACTIONSTEXTCTRLCONF,
			  name='textCtrlConf', parent=self.panel1, pos=wx.Point(400, 288),
			  size=wx.Size(100, 21), style=wx.TE_CENTER, value='')
		self.textCtrlConf.SetToolTipString('Enter the confirmation number for the transaction here')

		self.textCtrlNote = wx.TextCtrl(id=wxID_TRANSACTIONSTEXTCTRLNOTE,
			  name='textCtrlNote', parent=self.panel1, pos=wx.Point(520, 288),
			  size=wx.Size(100, 21), style=wx.TE_CENTER, value='')
		self.textCtrlNote.SetToolTipString('Enter a note or memo for the transaction here')

		self.choiceType = wx.Choice(choices=['got_paid', 'expense', 'credit',
			  'debit', 'transfer credit', 'transfer debit'],
			  id=wxID_TRANSACTIONSCHOICETYPE, name='choiceType',
			  parent=self.panel1, pos=wx.Point(40, 344), size=wx.Size(130, 21),
			  style=0)
		self.choiceType.Enable(True)
		self.choiceType.SetToolTipString('Select the type of transaction here. A transaction is a credit if it increases the account balance and a debit if it decreases the balance. For credit card accounts, the opposite is true. A credit or debit must be assigned before a transaction can be added to the account')
		self.choiceType.Bind(wx.EVT_CHOICE, self.OnChoiceTypeChoice,
			  id=wxID_TRANSACTIONSCHOICETYPE)

		self.buttonAddTransaction = wx.Button(id=wxID_TRANSACTIONSBUTTONADDTRANSACTION,
			  label='Add Transaction', name='buttonAddTransaction',
			  parent=self.panel1, pos=wx.Point(640, 280), size=wx.Size(112, 23),
			  style=0)
		self.buttonAddTransaction.Enable(True)
		self.buttonAddTransaction.SetToolTipString('Add a transaction to the selected account')
		self.buttonAddTransaction.Bind(wx.EVT_BUTTON,
			  self.OnButtonAddTransactionButton,
			  id=wxID_TRANSACTIONSBUTTONADDTRANSACTION)

		self.buttonEditTransaction = wx.Button(id=wxID_TRANSACTIONSBUTTONEDITTRANSACTION,
			  label='Edit Transaction', name='buttonEditTransaction',
			  parent=self.panel1, pos=wx.Point(640, 312), size=wx.Size(112, 23),
			  style=0)
		self.buttonEditTransaction.Enable(False)
		self.buttonEditTransaction.SetToolTipString('Edit the selected transaction using the Name, Amount, Date, Confirmation #, and Note/Memo boxes')
		self.buttonEditTransaction.Bind(wx.EVT_BUTTON,
			  self.OnButtonEditTransactionButton,
			  id=wxID_TRANSACTIONSBUTTONEDITTRANSACTION)

		self.buttonRemoveTransaction = wx.Button(id=wxID_TRANSACTIONSBUTTONREMOVETRANSACTION,
			  label='Remove Transaction', name='buttonRemoveTransaction',
			  parent=self.panel1, pos=wx.Point(640, 344), size=wx.Size(112, 23),
			  style=0)
		self.buttonRemoveTransaction.Enable(False)
		self.buttonRemoveTransaction.SetToolTipString('Remove the selected transaction')
		self.buttonRemoveTransaction.Bind(wx.EVT_BUTTON,
			  self.OnButtonRemoveTransactionButton,
			  id=wxID_TRANSACTIONSBUTTONREMOVETRANSACTION)

		self.checkBoxTypeFilter = wx.CheckBox(id=wxID_TRANSACTIONSCHECKBOXTYPEFILTER,
			  label='Apply filter', name='checkBoxTypeFilter',
			  parent=self.panel1, pos=wx.Point(70, 368), size=wx.Size(82, 13),
			  style=0)
		self.checkBoxTypeFilter.SetValue(False)
		self.checkBoxTypeFilter.SetToolTipString('Clicking this check box will filter the transaction list by the type in the selector above. If no type is selected, you will be prompted to make a selection before checking this box')
		self.checkBoxTypeFilter.Bind(wx.EVT_CHECKBOX,
			  self.OnCheckBoxTypeFilterCheckbox,
			  id=wxID_TRANSACTIONSCHECKBOXTYPEFILTER)

		self.datePickerCtrlFromDate = wx.DatePickerCtrl(id=wxID_TRANSACTIONSDATEPICKERCTRLFROMDATE,
			  name='datePickerCtrlFromDate', parent=self.panel1,
			  pos=wx.Point(192, 344), size=wx.Size(96, 21),
			  style=wx.DP_SHOWCENTURY)
		self.datePickerCtrlFromDate.SetToolTipString('To filter transactions by date, use this as the starting date')
		self.datePickerCtrlFromDate.Bind(wx.EVT_DATE_CHANGED,
			  self.OnDatePickerCtrlFromDateDateChanged,
			  id=wxID_TRANSACTIONSDATEPICKERCTRLFROMDATE)

		self.datePickerCtrlToDate = wx.DatePickerCtrl(id=wxID_TRANSACTIONSDATEPICKERCTRLTODATE,
			  name='datePickerCtrlToDate', parent=self.panel1, pos=wx.Point(296,
			  344), size=wx.Size(98, 21), style=wx.DP_SHOWCENTURY)
		self.datePickerCtrlToDate.SetToolTipString('To filter transactions by date, use this as the ending date')
		self.datePickerCtrlToDate.Bind(wx.EVT_DATE_CHANGED,
			  self.OnDatePickerCtrlToDateDateChanged,
			  id=wxID_TRANSACTIONSDATEPICKERCTRLTODATE)

		self.buttonDateFilter = wx.Button(id=wxID_TRANSACTIONSBUTTONDATEFILTER,
			  label='Apply', name='buttonDateFilter', parent=self.panel1,
			  pos=wx.Point(400, 344), size=wx.Size(48, 23), style=0)
		self.buttonDateFilter.SetToolTipString('Shows only transactions that occurred between the starting and ending dates for the selected account. To bring the other transactions back, click Remove. Clicking Remove will show all transactions for the selected account. If transactions are being filtered by search, only those transactions will show for the applied date range.')
		self.buttonDateFilter.Bind(wx.EVT_BUTTON, self.OnButtonDateFilterButton,
			  id=wxID_TRANSACTIONSBUTTONDATEFILTER)

		self.searchCtrlSearchTransactions = wx.SearchCtrl(id=wxID_TRANSACTIONSSEARCHCTRLSEARCHTRANSACTIONS,
			  name='searchCtrlSearchTransactions', parent=self.panel1,
			  pos=wx.Point(464, 344), size=wx.Size(152, 21), style=0, value='')
		self.searchCtrlSearchTransactions.SetToolTipString('Shows only the transactions that match the search string for all account. All fields (name, amount, confirmation #, and note/memo) can be searched. This will show all transactions for all accounts. To see only transactions for a certain account, select that account in the Select Account drop-down box')
		self.searchCtrlSearchTransactions.Bind(wx.EVT_TEXT,
			  self.OnSearchCtrlSearchTransactionsText,
			  id=wxID_TRANSACTIONSSEARCHCTRLSEARCHTRANSACTIONS)

		self.textCtrlCredits = wx.TextCtrl(id=wxID_TRANSACTIONSTEXTCTRLCREDITS,
			  name='textCtrlCredits', parent=self.panel1, pos=wx.Point(72, 408),
			  size=wx.Size(144, 24), style=wx.TE_CENTER, value='')
		self.textCtrlCredits.SetToolTipString('Shows total credits to the selected account')

		self.textCtrlDebits = wx.TextCtrl(id=wxID_TRANSACTIONSTEXTCTRLDEBITS,
			  name='textCtrlDebits', parent=self.panel1, pos=wx.Point(256, 408),
			  size=wx.Size(144, 24), style=wx.TE_CENTER, value='')
		self.textCtrlDebits.SetToolTipString('Shows total debits to the selected account')

		self.textCtrlBalance = wx.TextCtrl(id=wxID_TRANSACTIONSTEXTCTRLBALANCE,
			  name='textCtrlBalance', parent=self.panel1, pos=wx.Point(440,
			  408), size=wx.Size(144, 24), style=wx.TE_CENTER, value='')
		self.textCtrlBalance.SetToolTipString('Shows the overall credit-debit balance of the selected account. This amount can be different from the account balance shown in the Accounts window')

		self.buttonHome = wx.Button(id=wxID_TRANSACTIONSBUTTONHOME,
			  label='Home', name='buttonHome', parent=self.panel1,
			  pos=wx.Point(200, 456), size=wx.Size(85, 48), style=0)
		self.buttonHome.SetToolTipString('Takes you back to the Home window. If you press this button you will have to enter your password again.')
		self.buttonHome.Bind(wx.EVT_BUTTON, self.OnButtonHomeButton,
			  id=wxID_TRANSACTIONSBUTTONHOME)

		self.buttonAccounts = wx.Button(id=wxID_TRANSACTIONSBUTTONACCOUNTS,
			  label='Accounts', name='buttonAccounts', parent=self.panel1,
			  pos=wx.Point(304, 456), size=wx.Size(85, 48), style=0)
		self.buttonAccounts.SetToolTipString('Takes you to the Accounts window')
		self.buttonAccounts.Bind(wx.EVT_BUTTON, self.OnButtonAccountsButton,
			  id=wxID_TRANSACTIONSBUTTONACCOUNTS)

		self.buttonIncomes = wx.Button(id=wxID_TRANSACTIONSBUTTONINCOMES,
			  label='Incomes', name='buttonIncomes', parent=self.panel1,
			  pos=wx.Point(408, 456), size=wx.Size(85, 48), style=0)
		self.buttonIncomes.SetToolTipString('Takes you to the Incomes window')
		self.buttonIncomes.Bind(wx.EVT_BUTTON, self.OnButtonIncomesButton,
			  id=wxID_TRANSACTIONSBUTTONINCOMES)

		self.buttonCredits = wx.Button(id=wxID_TRANSACTIONSBUTTONCREDITS,
			  label='Credits', name='buttonCredits', parent=self.panel1,
			  pos=wx.Point(512, 456), size=wx.Size(85, 48), style=0)
		self.buttonCredits.SetToolTipString('Takes you to the Credits window')
		self.buttonCredits.Bind(wx.EVT_BUTTON, self.OnButtonCreditsButton,
			  id=wxID_TRANSACTIONSBUTTONCREDITS)

		self.buttonExpenses = wx.Button(id=wxID_TRANSACTIONSBUTTONEXPENSES,
			  label='Expenses', name='buttonExpenses', parent=self.panel1,
			  pos=wx.Point(200, 512), size=wx.Size(85, 48), style=0)
		self.buttonExpenses.SetToolTipString('Takes you to the Expenses window')
		self.buttonExpenses.Bind(wx.EVT_BUTTON, self.OnButtonExpensesButton,
			  id=wxID_TRANSACTIONSBUTTONEXPENSES)

		self.buttonSavingsItems = wx.Button(id=wxID_TRANSACTIONSBUTTONSAVINGSITEMS,
			  label='Savings Items', name='buttonSavingsItems',
			  parent=self.panel1, pos=wx.Point(304, 512), size=wx.Size(85, 48),
			  style=0)
		self.buttonSavingsItems.SetToolTipString('Takes you to the Savings Items window')
		self.buttonSavingsItems.Bind(wx.EVT_BUTTON,
			  self.OnButtonSavingsItemsButton,
			  id=wxID_TRANSACTIONSBUTTONSAVINGSITEMS)

		self.buttonBudget = wx.Button(id=wxID_TRANSACTIONSBUTTONBUDGET,
			  label='Budget', name='buttonBudget', parent=self.panel1,
			  pos=wx.Point(408, 512), size=wx.Size(85, 48), style=0)
		self.buttonBudget.SetToolTipString('Takes you to the Budget window')
		self.buttonBudget.Bind(wx.EVT_BUTTON, self.OnButtonBudgetButton,
			  id=wxID_TRANSACTIONSBUTTONBUDGET)

		self.buttonExpensesDue = wx.Button(id=wxID_TRANSACTIONSBUTTONEXPENSESDUE,
			  label='Expenses Due', name='buttonExpensesDue',
			  parent=self.panel1, pos=wx.Point(512, 512), size=wx.Size(85, 48),
			  style=0)
		self.buttonExpensesDue.SetToolTipString('Takes you to the Expenses Due window')
		self.buttonExpensesDue.Bind(wx.EVT_BUTTON,
			  self.OnButtonExpensesDueButton,
			  id=wxID_TRANSACTIONSBUTTONEXPENSESDUE)

		self.buttonClose = wx.Button(id=wxID_TRANSACTIONSBUTTONCLOSE,
			  label='Close', name='buttonClose', parent=self.panel1,
			  pos=wx.Point(358, 582), size=wx.Size(83, 23), style=0)
		self.buttonClose.SetToolTipString('See you next time!')
		self.buttonClose.Bind(wx.EVT_BUTTON, self.OnButtonCloseButton,
			  id=wxID_TRANSACTIONSBUTTONCLOSE)

		self.gridRegister = wx.grid.Grid(id=wxID_TRANSACTIONSGRIDREGISTER,
			  name='gridRegister', parent=self.panel1, pos=wx.Point(0, 0),
			  size=wx.Size(784, 264), style=0)
		self.gridRegister.SetColLabelSize(24)
		self.gridRegister.SetDefaultColSize(150)
		self.gridRegister.SetDefaultRowSize(18)
		self.gridRegister.SetRowMinimalAcceptableHeight(15)
		self.gridRegister.SetRowLabelSize(20)
		self.gridRegister.SetToolTipString('Shows all transactions for the account selected in the Select Account drop-down box')
		self.gridRegister.Bind(wx.grid.EVT_GRID_RANGE_SELECT,
			  self.OnGridRegisterGridRangeSelect)

		self.staticTextDate = wx.StaticText(id=wxID_TRANSACTIONSSTATICTEXTDATE,
			  label='Date', name='staticTextDate', parent=self.panel1,
			  pos=wx.Point(320, 272), size=wx.Size(24, 13), style=0)

		self.staticTextAmount = wx.StaticText(id=wxID_TRANSACTIONSSTATICTEXTAMOUNT,
			  label='Amount', name='staticTextAmount', parent=self.panel1,
			  pos=wx.Point(192, 272), size=wx.Size(38, 13), style=0)

		self.staticTextConf = wx.StaticText(id=wxID_TRANSACTIONSSTATICTEXTCONF,
			  label='Confirmation #', name='staticTextConf', parent=self.panel1,
			  pos=wx.Point(416, 272), size=wx.Size(73, 13), style=0)

		self.staticTextToDate = wx.StaticText(id=wxID_TRANSACTIONSSTATICTEXTTODATE,
			  label='To Date', name='staticTextToDate', parent=self.panel1,
			  pos=wx.Point(320, 328), size=wx.Size(39, 13), style=0)

		self.staticTextFromDate = wx.StaticText(id=wxID_TRANSACTIONSSTATICTEXTFROMDATE,
			  label='From Date', name='staticTextFromDate', parent=self.panel1,
			  pos=wx.Point(216, 328), size=wx.Size(51, 13), style=0)

		self.staticTextNote = wx.StaticText(id=wxID_TRANSACTIONSSTATICTEXTNOTE,
			  label='Note/Memo', name='staticTextNote', parent=self.panel1,
			  pos=wx.Point(544, 272), size=wx.Size(56, 13), style=0)

		self.staticTextSelectAccount = wx.StaticText(id=wxID_TRANSACTIONSSTATICTEXTSELECTACCOUNT,
			  label='View Transactions For:', name='staticTextSelectAccount',
			  parent=self.panel1, pos=wx.Point(627, 392), size=wx.Size(110, 13),
			  style=0)
		self.staticTextSelectAccount.Enable(True)

		self.staticTextBalance = wx.StaticText(id=wxID_TRANSACTIONSSTATICTEXTBALANCE,
			  label='Credit-Debit Balance', name='staticTextBalance',
			  parent=self.panel1, pos=wx.Point(462, 392), size=wx.Size(99, 13),
			  style=0)

		self.staticTextDebits = wx.StaticText(id=wxID_TRANSACTIONSSTATICTEXTDEBITS,
			  label='Debits from account', name='staticTextDebits',
			  parent=self.panel1, pos=wx.Point(280, 392), size=wx.Size(97, 13),
			  style=0)

		self.staticTextCredits = wx.StaticText(id=wxID_TRANSACTIONSSTATICTEXTCREDITS,
			  label='Credits to account', name='staticTextCredits',
			  parent=self.panel1, pos=wx.Point(104, 392), size=wx.Size(89, 13),
			  style=0)

		self.staticTextSearch = wx.StaticText(id=wxID_TRANSACTIONSSTATICTEXTSEARCH,
			  label='Search transactions', name='staticTextSearch',
			  parent=self.panel1, pos=wx.Point(494, 328), size=wx.Size(96, 13),
			  style=0)

		self.staticTextType = wx.StaticText(id=wxID_TRANSACTIONSSTATICTEXTTYPE,
			  label='Transaction type', name='staticTextType',
			  parent=self.panel1, pos=wx.Point(64, 328), size=wx.Size(82, 13),
			  style=0)

		self.staticTextName = wx.StaticText(id=wxID_TRANSACTIONSSTATICTEXTNAME,
			  label='Name', name='staticTextName', parent=self.panel1,
			  pos=wx.Point(72, 272), size=wx.Size(28, 13), style=0)

		self.staticTextDateFilter = wx.StaticText(id=wxID_TRANSACTIONSSTATICTEXTDATEFILTER,
			  label='Date Filter', name='staticTextDateFilter',
			  parent=self.panel1, pos=wx.Point(400, 328), size=wx.Size(51, 13),
			  style=0)

		self.staticTextShowTransactions = wx.StaticText(id=wxID_TRANSACTIONSSTATICTEXTSHOWTRANSACTIONS,
			  label='Show # of transactions:',
			  name='staticTextShowTransactions', parent=self.panel1,
			  pos=wx.Point(47, 456), size=wx.Size(117, 13), style=0)

		self.choiceShowTransactions = wx.Choice(choices=['Last 10', 'Last 25',
			  'Last 50', 'Last 100', 'All'],
			  id=wxID_TRANSACTIONSCHOICESHOWTRANSACTIONS,
			  name='choiceShowTransactions', parent=self.panel1,
			  pos=wx.Point(40, 472), size=wx.Size(130, 21), style=0)
		self.choiceShowTransactions.Bind(wx.EVT_CHOICE,
			  self.OnChoiceShowTransactionsChoice,
			  id=wxID_TRANSACTIONSCHOICESHOWTRANSACTIONS)

	def __init__(self, parent):
		self.selected_row = -1  
		self.rows = []
		self.filtered_by_type = False
		self.filtered_by_search = False     
		self.filtered_by_date = False      
		self.filtered_transactions = []  
		self.type_filter = []
		self.search_filter = []
		self.date_filter = []        
		self.search_text_len = 0
		self._init_ctrls(parent)
		init.load()
		self.user = init.userList[0]
		self.account = self.user.get_current_account()
		self.choiceSelectAccount.Append('All')
		for a in self.user.accountList: self.choiceSelectAccount.Append(a.name)
		self.t = self.user.s._transactions
		self.t.run_count += 1
		self.add_transaction_message = 'Start by entering the name of the transaction in the box below where it says \"Name\" under the grid on the left. ' \
						   'Then go to the box that says \"Amount\" and enter the transaction amount. After that, you\'ll need to select the date if it\'s ' \
						   'different from today\'s date. Last, select what type of transaction this is. It\'s a credit transaction if it increases your ' \
						   'account balance. It\'s a debit transaction if it decreases your balance. With a credit card account, the opposite is true. A credit ' \
						   'transaction (payment) will decrease your balance and a debit transaction (charge) will increase your balance. ' \
						   'When you\'re all done, click \"Add Transaction\" and the new transaction will be added to the list. ' \
						   'Click \"Add Transaction\" again if you need help.'
		self.message_count = 0                           
		if self.t.run_first_time: wx.MessageBox(self.t.welcome_message, self.t.welcome_title, wx.OK | wx.CENTRE) 
		init.save()        
		rows = self.account.r.registerList
		self.gridRegister.CreateGrid(len(rows), 5)
		self.gridRegister.SetColLabelValue(0, 'Name')
		self.gridRegister.SetColLabelValue(1, 'Amount')
		self.gridRegister.SetColLabelValue(2, 'Date')
		self.gridRegister.SetColLabelValue(3, 'Confirmation #')
		self.gridRegister.SetColLabelValue(4, 'Note/Memo')
		self.show_grid(rows)
		self.show_transaction_totals(rows)
		try:
			if self.user.s.show_last_transactions: self.choiceShowTransactions.SetStringSelection(self.user.s.show_last_transactions)
			else: self.choiceShowTransactions.SetStringSelection('All')
			self.show_last_transactions()
		except Exception as message: print '\n',str(message.__class__)+':',str(message),'\n'
		self.choiceSelectAccount.SetStringSelection(self.account.name)                
		if self.user.expenseList == [] or self.user.incomeList == []: 
			self.buttonExpensesDue.Enabled = False       
			self.buttonBudget.Enabled = False  
		self.start_time = time.time()
			
	def OnTransactionsIdle(self, event):
		if self.t.run_first_time and self.message_count < 1: 
			wx.MessageBox(self.add_transaction_message, 'To add a transaction', wx.OK | wx.CENTRE)  
			self.set_backcolor_green(self.textCtrlName)  
			self.message_count += 1  
			self.t.run_first_time = False
			init.save()  
		init.window_timeout(self, self.start_time)
		
	def OnPanel1Motion(self, event):
		self.start_time = time.time()
			
	def OnTextCtrlNameKillFocus(self, event):
		self.set_backcolor_white([self.textCtrlName])
		
	def OnTextCtrlNameText(self, event):
		if self.choiceType.GetSelection() != -1 and self.textCtrlName.GetValue() != '' or self.textCtrlAmount.GetValue() != '' or self.textCtrlConf.GetValue() != '' or self.textCtrlNote.GetValue() != '': self.buttonAddTransaction.Enabled = True        
		self.set_forecolor_black([self.textCtrlAmount])  
		
	def OnTextCtrlAmountText(self, event):
		self.set_forecolor_black([self.textCtrlAmount])  
		
	def OnChoiceSelectAccountChoice(self, event):
		for a in self.user.accountList:
			if a.name == self.choiceSelectAccount.GetStringSelection(): 
				self.account = a
				self.buttonAddTransaction.Enabled = True
			elif self.choiceSelectAccount.GetStringSelection() == 'All': 
				self.account = CBudgetP.account(None,None,None,None,None,self.user.get_all_transactions())
				self.buttonAddTransaction.Enabled = False
				self.buttonEditTransaction.Enabled = False
				self.buttonRemoveTransaction.Enabled = False
		init.save()
		self.filtered_by_type = False
		self.choiceType.SetSelection(-1)
		self.checkBoxTypeFilter.SetValue(False)            
		self.filtered_by_search = False
		self.searchCtrlSearchTransactions.Clear()
		self.filtered_by_date = False
		self.buttonDateFilter.Label = 'Apply'
		self.checkBoxTypeFilter.Label = 'Apply filter'
		self.show_grid(self.account.r.registerList)
		self.show_transaction_totals(self.account.r.registerList)
		self.enable_ctrls(True)
		self.set_forecolor_black([self.textCtrlAmount])
		try:
			if self.user.s.show_last_transactions: self.show_last_transactions()
		except Exception as message: print '\n',str(message.__class__)+':',str(message),'\n'
		
	def OnButtonAddTransactionButton(self, event):
		dt = self.datePickerCtrlDate.GetValue()
		date = datetime(dt.Year,dt.Month+1,dt.Day)     
		if self.textCtrlName.GetValue() == '' and self.textCtrlAmount.GetValue() == '' and self.choiceType.GetSelection() == -1: 
			wx.MessageBox(self.add_transaction_message, 'To add a transaction', wx.OK | wx.CENTRE)  
			self.set_backcolor_green(self.textCtrlName)
		elif self.textCtrlName.GetValue() == '' and self.textCtrlAmount.GetValue() == '': 
			wx.MessageBox('In order to add a transaction, it has to have a name. You can enter that below where it says \"Name\".', 'Transaction has no name', wx.OK | wx.CENTRE)
			self.set_backcolor_red(self.textCtrlName)  
		elif self.textCtrlName.GetValue() == '' and self.textCtrlAmount.GetValue() != '':
			wx.MessageBox('In order to add a transaction, it has to have a name. You can enter that below where it says \"Name\".', 'Transaction has no name', wx.OK | wx.CENTRE)
			self.set_backcolor_red(self.textCtrlName)  
			self.set_backcolor_white([self.textCtrlAmount])
		elif self.textCtrlName.GetValue() != '' and self.textCtrlAmount.GetValue() == '':
			wx.MessageBox('In order to add a transaction, it has to have an amount. You can enter that below where it says \"Amount\".', 'Transaction has no amount', wx.OK | wx.CENTRE)
			self.set_backcolor_red(self.textCtrlAmount)            
			self.set_backcolor_white([self.textCtrlName])
		elif self.textCtrlName.GetValue() != '' and self.textCtrlAmount.GetValue() != '' and self.choiceType.GetSelection() == -1: 
			wx.MessageBox('In order to add a transaction, it has to have a type (credit or debit). You can enter that below where it says \"Transaction type\".', 'Transaction has no type', wx.OK | wx.CENTRE)
			self.set_backcolor_red(self.staticTextType)
			self.set_backcolor_white([self.textCtrlName, self.textCtrlAmount])
		else:
			self.set_backcolor_white([self.textCtrlName, self.textCtrlAmount])
			self.set_backcolor_grey(self.staticTextType)
			amount = 0.0
			try: 
				if '$' in self.textCtrlAmount.GetValue(): amount = float(self.textCtrlAmount.GetValue()[1:])
				else: amount = float(self.textCtrlAmount.GetValue())     
				trans = CBudgetP.transaction(self.textCtrlName.GetValue(), amount, date, self.textCtrlConf.GetValue(), self.textCtrlNote.GetValue(), self.choiceType.GetStringSelection())
				if self.choiceType.GetStringSelection() == 'debit' and self.textCtrlAmount.GetValue() != '': trans.amount *= -1
				if self.account.type == 'Credit Card': trans.amount *= -1
				if self.account.type == 'Credit Card' and (trans.amount + self.account.balance > self.account.credit_limit): wx.MessageBox('This transaction will put your balance over your credit limit.', 'Warning!', wx.OK | wx.CENTRE)        
				if self.account.type != 'Credit Card' and (trans.amount + self.account.balance < 0.0): 
					result = wx.MessageBox('This action will record an overdrawn balance for the account {0}. Do you want to continue?'.format(self.account.name), 'Insufficient funds!', wx.YES_NO | wx.CENTRE)                                        
					if result == wx.YES: self.add_transaction(trans)
				else: 
					self.add_transaction(trans)
					self.OnChoiceShowTransactionsChoice(event)
			except ValueError:
				wx.MessageBox('The amount you are entering has to be a number. You\'ve probably entered some letters, symbols, or a word. Make sure it\'s a number.', 'Amount is not a number', wx.OK | wx.CENTRE)
				self.set_backcolor_red(self.textCtrlAmount)      
				
	def add_transaction(self, trans):
		self.account.r.add_transaction(self.user, trans, self.account)
		self.rows.append(trans)
		self.t.run_first_time = False
		self.user.set_current_account(self.account)
		init.save()
		wx.MessageBox('The transaction \"{0}\" has been to your transactions list.'.format(self.textCtrlName.GetValue()), 'Transaction added', wx.OK | wx.CENTRE)                    
		self.set_backcolor_white([self.textCtrlAmount])
		row_count = self.gridRegister.GetNumberRows()
		self.gridRegister.InsertRows(row_count,1)
		self.set_cell_values(row_count,values=[trans.name,str(trans.amount),str(trans.date.date()),trans.conf,trans.note])
		self.choiceType.SetSelection(-1)
		self.clear_boxes()   
		if len(self.filtered_transactions) == 0: self.filtered_transactions = self.account.r.registerList
		self.show_transaction_totals(self.filtered_transactions)
		date = datetime.now()   
		self.datePickerCtrlDate.SetValue(wx.DateTimeFromDMY(date.day,date.month-1,date.year))
		self.textCtrlName.SetFocus()
		init.window_timeout(self, self.start_time)

	def OnButtonEditTransactionButton(self, event):
		dt = self.datePickerCtrlDate.GetValue()
		date = datetime(dt.Year,dt.Month+1,dt.Day)
		amount = None
		try: 
			if '$' in self.textCtrlAmount.GetValue(): amount = float(self.textCtrlAmount.GetValue()[1:])
			trans = CBudgetP.transaction(self.textCtrlName.GetValue(), amount, date, self.textCtrlConf.GetValue(), self.textCtrlNote.GetValue(), self.choiceType.GetStringSelection())
			if len(self.filtered_transactions) > 0 and (len(self.filtered_transactions) < len(self.account.r.registerList)): 
				self.change_trans_type(self.filtered_transactions[self.selected_row].type, trans.type, trans)
				self.change_trans_type(self.account.r.registerList[self.account.r.registerList.index(self.filtered_transactions[self.selected_row])].type, trans.type, trans)
				self.account.r.edit_transaction(self.account.r.registerList, self.account.r.registerList.index(self.filtered_transactions[self.selected_row]), trans.name, trans.amount, trans.date, trans.conf, trans.note, trans.type)
				self.filtered_transactions[self.selected_row] = trans
			else: 
				self.change_trans_type(self.rows[self.selected_row].type, trans.type, trans)
				self.change_trans_type(self.account.r.registerList[self.account.r.registerList.index(self.rows[self.selected_row])].type, trans.type, trans)
				self.account.r.edit_transaction(self.account.r.registerList, self.account.r.registerList.index(self.rows[self.selected_row]), trans.name, trans.amount, trans.date, trans.conf, trans.note, trans.type)
				self.rows[self.selected_row] = trans
			if self.account.name: self.user.set_current_account(self.account)   
			init.save()
			self.set_backcolor_white([self.textCtrlAmount])
			self.set_cell_values(self.selected_row,values=[trans.name,str(trans.amount),str(trans.date.date()),trans.conf,trans.note])
			self.buttonEditTransaction.Enabled = False
			self.choiceType.SetSelection(-1)
			self.textCtrlName.Clear()
			self.textCtrlAmount.Clear()
			self.textCtrlConf.Clear()
			self.textCtrlNote.Clear()   
			if len(self.filtered_transactions) == 0: self.filtered_transactions = self.account.r.registerList
			self.show_transaction_totals(self.filtered_transactions)
			date = datetime.now()   
			self.datePickerCtrlDate.SetValue(wx.DateTimeFromDMY(date.day,date.month-1,date.year))
			self.OnChoiceShowTransactionsChoice(event)
		except ValueError: 
			wx.MessageBox('The amount you are entering has to be a number. You\'ve probably entered some letters, symbols, or a word. Make sure it\'s a number.', 'Amount is not a number', wx.OK | wx.CENTRE)
			self.set_backcolor_red(self.textCtrlAmount)
			
	def change_trans_type(self, before, after, trans):
		if ('credit' in before or 'got_paid' in before) and ('debit' in after or 'expense' in after): trans.amount *= -1
		if ('credit' in after or 'got_paid' in after) and ('debit' in before or 'expense' in before): trans.amount *= -1

	def OnButtonRemoveTransactionButton(self, event):
		result = wx.MessageBox('You are about to remove a transaction. Is this what you really want to do?', 'Remove transaction?', wx.YES_NO | wx.CENTRE)
		if result == wx.YES:
			if len(self.filtered_transactions) > 0 and (len(self.filtered_transactions) < len(self.account.r.registerList)): self.account.r.remove_transaction(self.filtered_transactions, self.account.r.registerList.index(self.filtered_transactions[self.selected_row]))
			else:
				self.account.r.remove_transaction(self.account.r.registerList, self.account.r.registerList.index(self.rows[self.selected_row]))
				self.rows.remove(self.rows[self.selected_row])
			self.user.set_current_account(self.account)
			init.save()
			self.gridRegister.DeleteRows(self.selected_row,1)
			self.buttonRemoveTransaction.Enabled = False
			self.buttonEditTransaction.Enabled = False
			self.choiceType.SetSelection(-1)  
			self.clear_boxes()    
			if len(self.filtered_transactions) == 0: self.filtered_transactions = self.account.r.registerList
			self.show_transaction_totals(self.filtered_transactions)   
			self.OnChoiceShowTransactionsChoice(event)
		date = datetime.now()   
		self.datePickerCtrlDate.SetValue(wx.DateTimeFromDMY(date.day,date.month-1,date.year))    

	def OnGridRegisterGridRangeSelect(self, event):
		try: 
			self.selected_row = self.gridRegister.GetSelectedRows()[0]
		except Exception as message: print '\n',str(message.__class__)+':',str(message),'\n'
		if len(self.filtered_transactions) > 0 and (len(self.filtered_transactions) < len(self.account.r.registerList)) and (len(self.filtered_transactions) < len(self.account.r.registerList)): rows = self.filtered_transactions
		else: rows = self.rows
		date = rows[self.selected_row].date   
		self.clear_boxes()
		self.textCtrlName.WriteText(rows[self.selected_row].name)
		self.textCtrlAmount.WriteText('$'+str(rows[self.selected_row].amount))
		self.pos_neg_amount_forecolor(rows[self.selected_row].amount, self.textCtrlAmount)
		self.datePickerCtrlDate.SetValue(wx.DateTimeFromDMY(date.day,date.month-1,date.year))   
		self.textCtrlConf.WriteText(rows[self.selected_row].conf)
		self.textCtrlNote.WriteText(rows[self.selected_row].note)
		self.choiceType.SetStringSelection(rows[self.selected_row].type)
		if self.account.name:
			self.buttonEditTransaction.Enabled = True
			self.buttonRemoveTransaction.Enabled = True     
		
	def OnChoiceTypeChoice(self, event):   
		if self.filtered_by_type and self.checkBoxTypeFilter.IsChecked():  
			self.type_filter = self.account.r.filter_by_type(self.user, str(self.choiceType.GetStringSelection()), self.rows)    
			self.filter_transactions()
		if not self.filtered_by_type and not self.checkBoxTypeFilter.IsChecked():   
			self.type_filter = self.account.r.registerList
		self.set_backcolor_grey(self.staticTextType)
			
	def OnCheckBoxTypeFilterCheckbox(self, event):
		if self.choiceType.GetSelection() == -1 and self.checkBoxTypeFilter.IsChecked():
			wx.MessageBox('In order to filter by type, you must first select a transaction type from the Transaction type selector', 'No type selected', wx.OK | wx.CENTRE)
			self.checkBoxTypeFilter.SetValue(False)
			self.set_backcolor_red(self.staticTextType)
		else:
			if self.checkBoxTypeFilter.IsChecked(): 
				self.filtered_by_type = True                            
				self.checkBoxTypeFilter.Label = 'Remove filter'
				self.checkBoxTypeFilter.Position = wx.Point(65, 368)
			else: 
				self.filtered_by_type = False  
				self.checkBoxTypeFilter.Label = 'Apply filter'
				self.checkBoxTypeFilter.Position = wx.Point(70, 368)
				self.filter_transactions()
			self.OnChoiceTypeChoice(event)                 
			
	def OnSearchCtrlSearchTransactionsText(self, event):       
		if len(self.searchCtrlSearchTransactions.GetValue()) > 0: 
			self.search_filter = self.account.r.filter_by_search(self.user, self.searchCtrlSearchTransactions.GetValue(), self.account.r.registerList)      
			self.filtered_by_search = True
			self.filter_transactions()            
		if len(self.searchCtrlSearchTransactions.GetValue()) == 0:                      
			self.search_filter = self.account.r.registerList
			self.filtered_by_search = False  
			self.filter_transactions()           
					
	def OnButtonDateFilterButton(self, event):                   
		if self.filtered_by_date:                    
			self.date_filter = self.account.r.registerList 
			self.buttonDateFilter.Label = 'Apply' 
			self.filtered_by_date = False    
			self.filter_transactions()     
		else:         
			dt = self.datePickerCtrlFromDate.GetValue()
			dateFrom = datetime(dt.Year,dt.Month+1,dt.Day)   
			dt = self.datePickerCtrlToDate.GetValue()
			dateTo = datetime(dt.Year,dt.Month+1,dt.Day)    
			if dateFrom > dateTo: wx.MessageBox('You have have chosen a From Date that is after the To Date. Make sure the From Date is before the To Date.', 'Negative date range', wx.OK | wx.CENTRE)      
			self.date_filter = self.account.r.filter_by_date_range(self.user, dateFrom, dateTo, self.account.r.registerList)              
			self.buttonDateFilter.Label = 'Remove'    
			self.filtered_by_date = True    
			self.filter_transactions()     
		
	def filter_transactions(self):
		self.filtered_transactions = self.account.r.registerList
		if self.filtered_by_type: 
			row_count = self.gridRegister.GetNumberRows()
			if row_count != 0: self.gridRegister.DeleteRows(0,row_count) 
			self.filtered_transactions = [f for f in self.filtered_transactions if f in self.type_filter]
		if self.filtered_by_search: 
			row_count = self.gridRegister.GetNumberRows()
			if row_count != 0: self.gridRegister.DeleteRows(0,row_count)             
			self.filtered_transactions = [f for f in self.filtered_transactions if f in self.search_filter]
		if self.filtered_by_date: 
			row_count = self.gridRegister.GetNumberRows()
			if row_count != 0: self.gridRegister.DeleteRows(0,row_count) 
			self.filtered_transactions = [f for f in self.filtered_transactions if f in self.date_filter]
		self.show_filtered_rows()
		
	def OnDatePickerCtrlFromDateDateChanged(self, event):
		self.filtered_by_date = False
		self.OnButtonDateFilterButton(event)

	def OnDatePickerCtrlToDateDateChanged(self, event):
		self.filtered_by_date = False
		self.OnButtonDateFilterButton(event)
		
	def OnChoiceShowTransactionsChoice(self, event):
		self.show_last_transactions()
		self.OnChoiceSelectAccountChoice(event)
		
	def show_last_transactions(self):
		rows = []
		if self.choiceShowTransactions.GetStringSelection() == 'Last 10': rows = self.account.r.registerList[-10:]
		if self.choiceShowTransactions.GetStringSelection() == 'Last 25': rows = self.account.r.registerList[-25:]
		if self.choiceShowTransactions.GetStringSelection() == 'Last 50': rows = self.account.r.registerList[-50:]
		if self.choiceShowTransactions.GetStringSelection() == 'Last 100': rows = self.account.r.registerList[-100:]
		if self.choiceShowTransactions.GetStringSelection() == 'All': rows = self.account.r.registerList
		rows = self.user.sort_transactions_by_date(rows)
		self.rows = rows
		self.show_grid(rows)
		self.show_transaction_totals(self.account.r.registerList)
		self.user.s.show_last_transactions = self.choiceShowTransactions.GetStringSelection()
		init.save()
		
	def show_filtered_rows(self):
		rows = self.filtered_transactions
		row_count = self.gridRegister.GetNumberRows()
		if row_count != 0: self.gridRegister.DeleteRows(0,row_count)
		try:
			for i in range(len(rows)):
				self.gridRegister.InsertRows(i,1)
				self.gridRegister.SetCellValue(i,0,rows[i].name)
				self.gridRegister.SetCellValue(i,1,str(rows[i].amount))
				self.gridRegister.SetCellValue(i,2,str(rows[i].date.date()))
				self.gridRegister.SetCellValue(i,3,rows[i].conf)
				self.gridRegister.SetCellValue(i,4,rows[i].note)   
			self.show_transaction_totals(rows)
		except Exception as message: print '\n',str(message.__class__)+':',str(message),'\n'
		  
	def show_transaction_totals(self, rows):
		total_credits = 0.0
		total_debits = 0.0
		total_balance = 0.0        
		for i in range(len(rows)):
			total_credits = sum([r.amount for r in rows if r.amount >= 0])
			total_debits = sum([r.amount for r in rows if r.amount < 0])
		total_balance = sum([r.amount for r in rows])
		self.textCtrlCredits.Clear()
		self.textCtrlDebits.Clear()
		self.textCtrlBalance.Clear()
		self.textCtrlCredits.WriteText('$'+str(round(total_credits, 2)))
		self.pos_neg_amount_forecolor(total_credits, self.textCtrlCredits)
		self.textCtrlDebits.WriteText('$'+str(round(total_debits, 2)))
		self.pos_neg_amount_forecolor(total_debits, self.textCtrlDebits)
		self.textCtrlBalance.WriteText('$'+str(round(total_balance, 2))) 
		self.pos_neg_amount_forecolor(total_balance, self.textCtrlBalance) 
		if self.filtered_transactions == self.account.r.registerList: self.account.balance = total_balance
		# init.save()
		
	def show_grid(self, rows):
		row_count = self.gridRegister.GetNumberRows()
		if row_count != 0: self.gridRegister.DeleteRows(0,row_count) 
		try:
			for i in range(len(rows)):
				self.gridRegister.InsertRows(i,1)
				self.gridRegister.SetCellValue(i,0,rows[i].name)
				self.gridRegister.SetCellValue(i,1,str(rows[i].amount))
				self.gridRegister.SetCellValue(i,2,str(rows[i].date.date()))
				self.gridRegister.SetCellValue(i,3,rows[i].conf)
				self.gridRegister.SetCellValue(i,4,rows[i].note) 
			self.show_transaction_totals(rows) 
		except Exception as message: print '\n',str(message.__class__)+':',str(message),'\n'
		
	def set_cell_values(self, row_index, values):
		self.gridRegister.SetCellValue(row_index,0,values[0])
		self.gridRegister.SetCellValue(row_index,1,values[1])
		self.gridRegister.SetCellValue(row_index,2,values[2])
		self.gridRegister.SetCellValue(row_index,3,values[3])
		self.gridRegister.SetCellValue(row_index,4,values[4])
		
	def enable_ctrls(self, enabled):
		if enabled:
			self.textCtrlName.Enabled = True
			self.textCtrlAmount.Enabled = True
			self.datePickerCtrlDate.Enabled = True
			self.textCtrlConf.Enabled = True
			self.textCtrlNote.Enabled = True
			self.choiceType.Enabled = True
			self.datePickerCtrlFromDate.Enabled = True
			self.datePickerCtrlToDate.Enabled = True
			self.buttonDateFilter.Enabled = True
			self.searchCtrlSearchTransactions.Enabled = True
			self.textCtrlCredits.Enabled = True
			self.textCtrlDebits.Enabled = True
			self.textCtrlBalance.Enabled = True
			self.choiceType.Enabled = True
		else:
			self.textCtrlName.Enabled = False
			self.textCtrlAmount.Enabled = False
			self.datePickerCtrlDate.Enabled = False
			self.textCtrlConf.Enabled = False
			self.textCtrlNote.Enabled = False     
			self.buttonEditTransaction.Enabled = False
			self.buttonRemoveTransaction.Enabled = False
			self.choiceType.Enabled = False
			self.datePickerCtrlFromDate.Enabled = False
			self.datePickerCtrlToDate.Enabled = False
			self.buttonDateFilter.Enabled = False
			self.searchCtrlSearchTransactions.Enabled = False
			self.textCtrlCredits.Enabled = False
			self.textCtrlDebits.Enabled = False    
			self.textCtrlBalance.Enabled = False    
			self.choiceType.Enabled = False  
					
	def clear_boxes(self):
		self.textCtrlName.Clear()
		self.textCtrlAmount.Clear()
		self.textCtrlConf.Clear()
		self.textCtrlNote.Clear()   
		
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
		
	def pos_neg_amount_forecolor(self, amount, ctrl):
		if amount > 0:
			ctrl.SetForegroundColour(wx.Colour(0, 128, 0))
			ctrl.Refresh
		elif amount == 0:
			ctrl.SetForegroundColour(wx.Colour(0, 0, 0))
			ctrl.Refresh
		else:
			ctrl.SetForegroundColour(wx.Colour(197, 1, 31))
			ctrl.Refresh
			
	def set_forecolor_black(self, ctrls):
		for c in ctrls:
			c.SetForegroundColour(wx.Colour(0, 0, 0))
			c.Refresh()
			   
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

	def OnButtonCloseButton(self, event):
		if self.t.run_count <= 10: init.delete_install_folder()
		self.Close()
		init.end_process()
	
