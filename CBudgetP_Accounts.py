#Boa:Frame:Accounts

import wx
import wx.lib.buttons
import time
import CBudgetP
from CBudgetP import *
from datetime import datetime
import CBudgetP_Home
import CBudgetP_Incomes
import CBudgetP_Credits
import CBudgetP_Expenses
import CBudgetP_SavingsItems
import CBudgetP_Budget
import CBudgetP_ExpensesDue
import CBudgetP_Transactions

def create(parent):
	return Accounts(parent)

[wxID_ACCOUNTS, wxID_ACCOUNTSBUTTONADDACCOUNT, wxID_ACCOUNTSBUTTONBUDGET, 
 wxID_ACCOUNTSBUTTONCLOSE, wxID_ACCOUNTSBUTTONCREDITS, 
 wxID_ACCOUNTSBUTTONCURRENTACCOUNT, wxID_ACCOUNTSBUTTONEDITACCOUNT, 
 wxID_ACCOUNTSBUTTONEXPENSES, wxID_ACCOUNTSBUTTONEXPENSESDUE, 
 wxID_ACCOUNTSBUTTONHOME, wxID_ACCOUNTSBUTTONINCOMES, 
 wxID_ACCOUNTSBUTTONRECORDTRANSFER, wxID_ACCOUNTSBUTTONREMOVEACCOUNT, 
 wxID_ACCOUNTSBUTTONSAVINGSITEMS, wxID_ACCOUNTSBUTTONTRANSACTIONS, 
 wxID_ACCOUNTSCHOICEACCOUNTTYPE, wxID_ACCOUNTSCHOICEFROM, 
 wxID_ACCOUNTSCHOICETO, wxID_ACCOUNTSLISTBOXACCOUNTS, wxID_ACCOUNTSPANEL1, 
 wxID_ACCOUNTSSTATICTEXTACCOUNTNAME, wxID_ACCOUNTSSTATICTEXTBALANCE, 
 wxID_ACCOUNTSSTATICTEXTBANKNAME, wxID_ACCOUNTSSTATICTEXTCREDITLIMIT, 
 wxID_ACCOUNTSSTATICTEXTFROM, wxID_ACCOUNTSSTATICTEXTINTERESTRATE, 
 wxID_ACCOUNTSSTATICTEXTRECORDTRANSFERFUNDS, 
 wxID_ACCOUNTSSTATICTEXTSELECTACCOUNTTYPE, wxID_ACCOUNTSSTATICTEXTTO, 
 wxID_ACCOUNTSSTATICTEXTTOTALBALANCE, wxID_ACCOUNTSSTATICTEXTTRANSFERAMOUNT, 
 wxID_ACCOUNTSTEXTCTRLACCOUNTNAME, wxID_ACCOUNTSTEXTCTRLBALANCE, 
 wxID_ACCOUNTSTEXTCTRLBANKNAME, wxID_ACCOUNTSTEXTCTRLCREDITLIMIT, 
 wxID_ACCOUNTSTEXTCTRLINTERESTRATE, wxID_ACCOUNTSTEXTCTRLTOTALBALANCE, 
 wxID_ACCOUNTSTEXTCTRLTRANSFERAMOUNT, 
] = [wx.NewId() for _init_ctrls in range(38)]

class Accounts(wx.Frame):
	def _init_ctrls(self, prnt):
		# generated method, don't edit
		wx.Frame.__init__(self, id=wxID_ACCOUNTS, name='Accounts', parent=prnt,
			  pos=wx.Point(394, 73), size=wx.Size(578, 582), style=wx.CAPTION,
			  title='Accounts')
		self.SetClientSize(wx.Size(562, 544))
		self.Center(wx.BOTH)
		self.Bind(wx.EVT_IDLE, self.OnAccountsIdle)

		self.panel1 = wx.Panel(id=wxID_ACCOUNTSPANEL1, name='panel1',
			  parent=self, pos=wx.Point(0, 0), size=wx.Size(562, 544),
			  style=wx.TAB_TRAVERSAL)
		self.panel1.SetToolTipString('Accounts Window')
		self.panel1.Bind(wx.EVT_MOTION, self.OnPanel1Motion)

		self.listBoxAccounts = wx.ListBox(choices=[],
			  id=wxID_ACCOUNTSLISTBOXACCOUNTS, name='listBoxAccounts',
			  parent=self.panel1, pos=wx.Point(48, 24), size=wx.Size(352, 160),
			  style=0)
		self.listBoxAccounts.SetToolTipString('Account List - You can add as many accounts here as you want. Just start by going to the account Name box and enter a account name. Click Add Account if you need help')
		self.listBoxAccounts.SetStringSelection('')
		self.listBoxAccounts.Bind(wx.EVT_LISTBOX, self.OnListBoxAccountsListbox,
			  id=wxID_ACCOUNTSLISTBOXACCOUNTS)

		self.textCtrlAccountName = wx.TextCtrl(id=wxID_ACCOUNTSTEXTCTRLACCOUNTNAME,
			  name='textCtrlAccountName', parent=self.panel1, pos=wx.Point(404,
			  42), size=wx.Size(108, 21), style=wx.TE_CENTER, value='')
		self.textCtrlAccountName.SetToolTipString('Enter account name here')
		self.textCtrlAccountName.Bind(wx.EVT_KILL_FOCUS,
			  self.OnTextCtrlAccountNameKillFocus)
		self.textCtrlAccountName.Bind(wx.EVT_TEXT,
			  self.OnTextCtrlAccountNameText,
			  id=wxID_ACCOUNTSTEXTCTRLACCOUNTNAME)

		self.textCtrlBalance = wx.TextCtrl(id=wxID_ACCOUNTSTEXTCTRLBALANCE,
			  name='textCtrlBalance', parent=self.panel1, pos=wx.Point(48, 208),
			  size=wx.Size(140, 21), style=wx.TE_CENTER, value='')
		self.textCtrlBalance.SetToolTipString('Enter the account balance here')
		self.textCtrlBalance.Bind(wx.EVT_TEXT, self.OnTextCtrlBalanceText,
			  id=wxID_ACCOUNTSTEXTCTRLBALANCE)

		self.textCtrlTotalBalance = wx.TextCtrl(id=wxID_ACCOUNTSTEXTCTRLTOTALBALANCE,
			  name='textCtrlTotalBalance', parent=self.panel1, pos=wx.Point(208,
			  208), size=wx.Size(145, 21), style=wx.TE_CENTER, value='')
		self.textCtrlTotalBalance.SetToolTipString('Shows the total balance for all accounts')
		self.textCtrlTotalBalance.Enable(False)
		self.textCtrlTotalBalance.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL,
			  wx.BOLD, False, 'Tahoma'))

		self.textCtrlBankName = wx.TextCtrl(id=wxID_ACCOUNTSTEXTCTRLBANKNAME,
			  name='textCtrlBankName', parent=self.panel1, pos=wx.Point(376,
			  208), size=wx.Size(140, 21), style=wx.TE_CENTER, value='')
		self.textCtrlBankName.SetToolTipString('Enter the name of the financial institution this account belongs to (optional)')

		self.choiceAccountType = wx.Choice(choices=['Checking', 'Savings',
			  'Credit Card'], id=wxID_ACCOUNTSCHOICEACCOUNTTYPE,
			  name='choiceAccountType', parent=self.panel1, pos=wx.Point(404,
			  164), size=wx.Size(110, 21), style=0)
		self.choiceAccountType.SetToolTipString('Select the account type')
		self.choiceAccountType.Bind(wx.EVT_CHOICE,
			  self.OnChoiceAccountTypeChoice,
			  id=wxID_ACCOUNTSCHOICEACCOUNTTYPE)

		self.textCtrlCreditLimit = wx.TextCtrl(id=wxID_ACCOUNTSTEXTCTRLCREDITLIMIT,
			  name='textCtrlCreditLimit', parent=self.panel1, pos=wx.Point(48,
			  256), size=wx.Size(124, 21), style=wx.TE_CENTER, value='')
		self.textCtrlCreditLimit.Enable(False)
		self.textCtrlCreditLimit.SetToolTipString('If this account is a credit card, you can enter the credit limit here (optional)')

		self.textCtrlInterestRate = wx.TextCtrl(id=wxID_ACCOUNTSTEXTCTRLINTERESTRATE,
			  name='textCtrlInterestRate', parent=self.panel1, pos=wx.Point(396,
			  256), size=wx.Size(120, 21), style=wx.TE_CENTER, value='')
		self.textCtrlInterestRate.Show(True)
		self.textCtrlInterestRate.Enable(False)
		self.textCtrlInterestRate.SetToolTipString('If the account is a credit card, you can enter the interest rate here (optional)')

		self.buttonAddAccount = wx.Button(id=wxID_ACCOUNTSBUTTONADDACCOUNT,
			  label='Add Account', name='buttonAddAccount', parent=self.panel1,
			  pos=wx.Point(404, 64), size=wx.Size(110, 23), style=0)
		self.buttonAddAccount.Enable(True)
		self.buttonAddAccount.SetToolTipString('Add an account to the list')
		self.buttonAddAccount.Bind(wx.EVT_BUTTON, self.OnButtonAddAccountButton,
			  id=wxID_ACCOUNTSBUTTONADDACCOUNT)

		self.buttonRemoveAccount = wx.Button(id=wxID_ACCOUNTSBUTTONREMOVEACCOUNT,
			  label='Remove Account', name='buttonRemoveAccount',
			  parent=self.panel1, pos=wx.Point(404, 92), size=wx.Size(110, 23),
			  style=0)
		self.buttonRemoveAccount.Enable(False)
		self.buttonRemoveAccount.SetToolTipString('Remove the selected account from the list')
		self.buttonRemoveAccount.Bind(wx.EVT_BUTTON,
			  self.OnButtonRemoveAccountButton,
			  id=wxID_ACCOUNTSBUTTONREMOVEACCOUNT)

		self.buttonEditAccount = wx.Button(id=wxID_ACCOUNTSBUTTONEDITACCOUNT,
			  label='Edit Account', name='buttonEditAccount',
			  parent=self.panel1, pos=wx.Point(404, 120), size=wx.Size(110, 23),
			  style=0)
		self.buttonEditAccount.Enable(False)
		self.buttonEditAccount.SetToolTipString('Change information for the selected account')
		self.buttonEditAccount.Bind(wx.EVT_BUTTON,
			  self.OnButtonEditAccountButton,
			  id=wxID_ACCOUNTSBUTTONEDITACCOUNT)

		self.buttonCurrentAccount = wx.Button(id=wxID_ACCOUNTSBUTTONCURRENTACCOUNT,
			  label='Current Account', name='buttonCurrentAccount',
			  parent=self.panel1, pos=wx.Point(200, 238), size=wx.Size(168, 34),
			  style=0)
		self.buttonCurrentAccount.SetToolTipString('Set, view, or change the current account. The current account is the one that will be shown when you press the Transactions button')
		self.buttonCurrentAccount.Bind(wx.EVT_BUTTON,
			  self.OnButtonCurrentAccountButton,
			  id=wxID_ACCOUNTSBUTTONCURRENTACCOUNT)

		self.buttonRecordTransfer = wx.Button(id=wxID_ACCOUNTSBUTTONRECORDTRANSFER,
			  label='Record Transfer', name='buttonRecordTransfer',
			  parent=self.panel1, pos=wx.Point(412, 306), size=wx.Size(96, 28),
			  style=0)
		self.buttonRecordTransfer.Enable(False)
		self.buttonRecordTransfer.Bind(wx.EVT_BUTTON,
			  self.OnButtonRecordTransferButton,
			  id=wxID_ACCOUNTSBUTTONRECORDTRANSFER)

		self.choiceFrom = wx.Choice(choices=[], id=wxID_ACCOUNTSCHOICEFROM,
			  name='choiceFrom', parent=self.panel1, pos=wx.Point(88, 310),
			  size=wx.Size(130, 21), style=0)
		self.choiceFrom.Enable(False)
		self.choiceFrom.Bind(wx.EVT_CHOICE, self.OnChoiceFromChoice,
			  id=wxID_ACCOUNTSCHOICEFROM)

		self.choiceTo = wx.Choice(choices=[], id=wxID_ACCOUNTSCHOICETO,
			  name='choiceTo', parent=self.panel1, pos=wx.Point(264, 310),
			  size=wx.Size(130, 21), style=0)
		self.choiceTo.Enable(False)
		self.choiceTo.Bind(wx.EVT_CHOICE, self.OnChoiceToChoice,
			  id=wxID_ACCOUNTSCHOICETO)

		self.textCtrlTransferAmount = wx.TextCtrl(id=wxID_ACCOUNTSTEXTCTRLTRANSFERAMOUNT,
			  name='textCtrlTransferAmount', parent=self.panel1,
			  pos=wx.Point(176, 336), size=wx.Size(216, 21), style=wx.TE_CENTER,
			  value='')
		self.textCtrlTransferAmount.Enable(False)

		self.buttonHome = wx.Button(id=wxID_ACCOUNTSBUTTONHOME, label='Home',
			  name='buttonHome', parent=self.panel1, pos=wx.Point(88, 384),
			  size=wx.Size(85, 48), style=0)
		self.buttonHome.Bind(wx.EVT_BUTTON, self.OnButtonHomeButton,
			  id=wxID_ACCOUNTSBUTTONHOME)

		self.buttonIncomes = wx.Button(id=wxID_ACCOUNTSBUTTONINCOMES,
			  label='Incomes', name='buttonIncomes', parent=self.panel1,
			  pos=wx.Point(187, 384), size=wx.Size(85, 48), style=0)
		self.buttonIncomes.Bind(wx.EVT_BUTTON, self.OnButtonIncomesButton,
			  id=wxID_ACCOUNTSBUTTONINCOMES)

		self.buttonCredits = wx.Button(id=wxID_ACCOUNTSBUTTONCREDITS,
			  label='Credits', name='buttonCredits', parent=self.panel1,
			  pos=wx.Point(286, 384), size=wx.Size(85, 48), style=0)
		self.buttonCredits.SetToolTipString('Takes you to the Credits window')
		self.buttonCredits.Bind(wx.EVT_BUTTON, self.OnButtonCreditsButton,
			  id=wxID_ACCOUNTSBUTTONCREDITS)

		self.buttonExpenses = wx.Button(id=wxID_ACCOUNTSBUTTONEXPENSES,
			  label='Expenses', name='buttonExpenses', parent=self.panel1,
			  pos=wx.Point(384, 384), size=wx.Size(85, 48), style=0)
		self.buttonExpenses.SetToolTipString('Takes you to the Expenses window')
		self.buttonExpenses.Bind(wx.EVT_BUTTON, self.OnButtonExpensesButton,
			  id=wxID_ACCOUNTSBUTTONEXPENSES)

		self.buttonSavingsItems = wx.Button(id=wxID_ACCOUNTSBUTTONSAVINGSITEMS,
			  label='Savings Items', name='buttonSavingsItems',
			  parent=self.panel1, pos=wx.Point(88, 440), size=wx.Size(85, 48),
			  style=0)
		self.buttonSavingsItems.SetToolTipString('Takes you to the Savings Items window')
		self.buttonSavingsItems.Bind(wx.EVT_BUTTON,
			  self.OnButtonSavingsItemsButton,
			  id=wxID_ACCOUNTSBUTTONSAVINGSITEMS)

		self.buttonBudget = wx.Button(id=wxID_ACCOUNTSBUTTONBUDGET,
			  label='Budget', name='buttonBudget', parent=self.panel1,
			  pos=wx.Point(187, 440), size=wx.Size(85, 48), style=0)
		self.buttonBudget.SetToolTipString('Takes you to the Budget window')
		self.buttonBudget.Bind(wx.EVT_BUTTON, self.OnButtonBudgetButton,
			  id=wxID_ACCOUNTSBUTTONBUDGET)

		self.buttonExpensesDue = wx.Button(id=wxID_ACCOUNTSBUTTONEXPENSESDUE,
			  label='Expenses Due', name='buttonExpensesDue',
			  parent=self.panel1, pos=wx.Point(286, 440), size=wx.Size(85, 48),
			  style=0)
		self.buttonExpensesDue.SetToolTipString('Takes you to the Expenses Due window')
		self.buttonExpensesDue.Bind(wx.EVT_BUTTON,
			  self.OnButtonExpensesDueButton,
			  id=wxID_ACCOUNTSBUTTONEXPENSESDUE)

		self.buttonTransactions = wx.Button(id=wxID_ACCOUNTSBUTTONTRANSACTIONS,
			  label='Transactions', name='buttonTransactions',
			  parent=self.panel1, pos=wx.Point(384, 440), size=wx.Size(85, 48),
			  style=0)
		self.buttonTransactions.SetToolTipString('Takes you to the Transactions window')
		self.buttonTransactions.Bind(wx.EVT_BUTTON,
			  self.OnButtonTransactionsButton,
			  id=wxID_ACCOUNTSBUTTONTRANSACTIONS)

		self.buttonClose = wx.Button(id=wxID_ACCOUNTSBUTTONCLOSE, label='Close',
			  name='buttonClose', parent=self.panel1, pos=wx.Point(242, 504),
			  size=wx.Size(78, 23), style=0)
		self.buttonClose.SetToolTipString('See you next time!')
		self.buttonClose.Bind(wx.EVT_BUTTON, self.OnButtonCloseButton,
			  id=wxID_ACCOUNTSBUTTONCLOSE)

		self.staticTextAccountName = wx.StaticText(id=wxID_ACCOUNTSSTATICTEXTACCOUNTNAME,
			  label='Account Name', name='staticTextAccountName',
			  parent=self.panel1, pos=wx.Point(424, 24), size=wx.Size(70, 13),
			  style=0)

		self.staticTextTotalBalance = wx.StaticText(id=wxID_ACCOUNTSSTATICTEXTTOTALBALANCE,
			  label='Total Balance', name='staticTextTotalBalance',
			  parent=self.panel1, pos=wx.Point(248, 192), size=wx.Size(65, 13),
			  style=0)

		self.staticTextBalance = wx.StaticText(id=wxID_ACCOUNTSSTATICTEXTBALANCE,
			  label='Balance', name='staticTextBalance', parent=self.panel1,
			  pos=wx.Point(104, 192), size=wx.Size(38, 13), style=0)

		self.staticTextTransferAmount = wx.StaticText(id=wxID_ACCOUNTSSTATICTEXTTRANSFERAMOUNT,
			  label='Transfer Amount:', name='staticTextTransferAmount',
			  parent=self.panel1, pos=wx.Point(88, 340), size=wx.Size(86, 13),
			  style=0)
		self.staticTextTransferAmount.Enable(False)
		self.staticTextTransferAmount.SetToolTipString('staticTextAmount')

		self.staticTextBankName = wx.StaticText(id=wxID_ACCOUNTSSTATICTEXTBANKNAME,
			  label='Bank Name', name='staticTextBankName', parent=self.panel1,
			  pos=wx.Point(424, 192), size=wx.Size(54, 13), style=0)

		self.staticTextInterestRate = wx.StaticText(id=wxID_ACCOUNTSSTATICTEXTINTERESTRATE,
			  label='Interest Rate', name='staticTextInterestRate',
			  parent=self.panel1, pos=wx.Point(424, 240), size=wx.Size(66, 13),
			  style=0)
		self.staticTextInterestRate.Enable(False)

		self.staticTextSelectAccountType = wx.StaticText(id=wxID_ACCOUNTSSTATICTEXTSELECTACCOUNTTYPE,
			  label='Account Type', name='staticTextSelectAccountType',
			  parent=self.panel1, pos=wx.Point(424, 148), size=wx.Size(67, 13),
			  style=0)

		self.staticTextCreditLimit = wx.StaticText(id=wxID_ACCOUNTSSTATICTEXTCREDITLIMIT,
			  label='Credit Limit', name='staticTextCreditLimit',
			  parent=self.panel1, pos=wx.Point(88, 240), size=wx.Size(54, 13),
			  style=0)
		self.staticTextCreditLimit.Enable(False)

		self.staticTextRecordTransferFunds = wx.StaticText(id=wxID_ACCOUNTSSTATICTEXTRECORDTRANSFERFUNDS,
			  label='Record Transfer of Funds',
			  name='staticTextRecordTransferFunds', parent=self.panel1,
			  pos=wx.Point(176, 288), size=wx.Size(141, 13), style=0)
		self.staticTextRecordTransferFunds.SetFont(wx.Font(8, wx.SWISS,
			  wx.NORMAL, wx.BOLD, False, 'Tahoma'))
		self.staticTextRecordTransferFunds.Enable(False)

		self.staticTextFrom = wx.StaticText(id=wxID_ACCOUNTSSTATICTEXTFROM,
			  label='From:', name='staticTextFrom', parent=self.panel1,
			  pos=wx.Point(56, 312), size=wx.Size(29, 13), style=0)
		self.staticTextFrom.Enable(False)

		self.staticTextTo = wx.StaticText(id=wxID_ACCOUNTSSTATICTEXTTO,
			  label='To:', name='staticTextTo', parent=self.panel1,
			  pos=wx.Point(240, 312), size=wx.Size(17, 13), style=0)
		self.staticTextTo.Enable(False)

	def __init__(self, parent):
		self._init_ctrls(parent)  
		init.load()                
		self.user = init.userList[0]
		self.a = self.user.s._accounts
		self.add_account_message = 'Start by entering the name of your first account in the box below where it says \"Account Name\" on the top right. ' \
						   'Then go to the box that says \"Balance\" and enter the balance for the account. After that, enter the name of your bank. ' \
						   'Next, select what type of account you\'re adding (Checking, Savings, or Credit Card). If the account is a credit card, you\'ll ' \
						   'see the additional boxes for credit limit and interest rate become active. For a credit card, you have to put a credit limit, ' \
						   'but interest rate is optional and is just there so you can keep track of it. Once you\'re done with all that, click \"Add Account\" ' \
						   'and the new account will be added to the list. Click \"Add Account\" again if you need help.'        
		self.message_count = 0
		if self.a.run_first_time: wx.MessageBox(self.a.welcome_message, self.a.welcome_title, wx.OK | wx.CENTRE) 
		self.a.run_count += 1    
		self.listBoxAccounts.InsertItems([a.name for a in self.user.accountList],0)
		if self.user.accountList == []: self.enable_main_buttons(False)
		else: 
			self.enable_main_buttons(True)
			if len(self.user.accountList) > 1: self.enable_transfer_ctrls(True)
		for a in self.user.accountList: self.choiceFrom.Append(a.name)
		for a in self.user.accountList: self.choiceTo.Append(a.name)
		self.enable_ctrls(False)
		if self.user.accountList != []:
			self.listBoxAccounts.SetStringSelection(self.user.get_current_account().name)
			self.textCtrlAccountName.WriteText(str(self.user.accountList[self.listBoxAccounts.GetSelection()].name))
			self.textCtrlBalance.WriteText('$'+str(round(self.user.accountList[self.listBoxAccounts.GetSelection()].balance, 2)))    
			self.pos_neg_amount_forecolor(round(self.user.accountList[self.listBoxAccounts.GetSelection()].balance, 2), self.textCtrlBalance)    
			self.textCtrlTotalBalance.WriteText('$'+str(round(self.user.get_total_accounts_balance(), 2)))
			self.pos_neg_amount_forecolor_total(round(self.user.get_total_accounts_balance(), 2), self.textCtrlTotalBalance) 
			self.textCtrlBankName.WriteText(self.user.accountList[self.listBoxAccounts.GetSelection()].bank_name)    
			if self.user.accountList[self.listBoxAccounts.GetSelection()].type == 'Credit Card':
				self.textCtrlCreditLimit.WriteText(str(self.user.accountList[self.listBoxAccounts.GetSelection()].credit_limit))
				if str(self.user.accountList[self.listBoxAccounts.GetSelection()].interest_rate) != '': 
					self.textCtrlInterestRate.WriteText(str(self.user.accountList[self.listBoxAccounts.GetSelection()].interest_rate)+'%')
				self.textCtrlCreditLimit.Enabled = True
				self.textCtrlInterestRate.Enabled = True
				self.staticTextCreditLimit.Enabled = True
				self.staticTextInterestRate.Enabled = True
			self.choiceAccountType.SetStringSelection(self.user.get_current_account().type)
			self.enable_ctrls(True)
			init.userList[0].s.active_frame = str(self)._formatter_field_name_split()[0][1:]
		self.goto_incomes = None
		if self.user.expenseList == [] or self.user.incomeList == []: self.buttonExpensesDue.Enabled = False   
		if self.user.expenseList == [] or self.user.incomeList == []: self.buttonBudget.Enabled = False     
		self.start_time = time.time()
		if self.user.accountList != []: self.goto_incomes = True  
		
	def OnAccountsIdle(self, event):
		if self.a.run_first_time and self.message_count < 1: 
			wx.MessageBox(self.add_account_message, 'To add an account', wx.OK | wx.CENTRE)  
			self.set_backcolor_green(self.textCtrlAccountName)
			self.message_count += 1
		if self.goto_incomes:     
			if self.user.incomeList == [] and len(self.user.accountList) == 1:
				result = wx.MessageBox('You have an account, but it might be a good idea to go to the Incomes window and enter some income information, or you can stay here and add more accounts. Would you like to enter some incomes now?', 'Enter incomes?', wx.YES_NO | wx.CENTRE)
				if result == wx.YES: self.OnButtonIncomesButton(event)
			if self.user.incomeList == [] and len(self.user.accountList) > 1:
				result = wx.MessageBox('You have some accounts, but now it might be a good idea to go to the Incomes window and enter some income information, or you can stay here and add more accounts. Would you like to enter some incomes now?', 'Enter incomes?', wx.YES_NO | wx.CENTRE)
				if result == wx.YES: self.OnButtonIncomesButton(event)  
			self.goto_incomes = False      
		init.window_timeout(self, self.start_time)
		
	def OnPanel1Motion(self, event):
		self.start_time = time.time()
			
	def OnTextCtrlAccountNameKillFocus(self, event):
		self.set_backcolor_white([self.textCtrlAccountName])

	def OnListBoxAccountsListbox(self, event):
		self.clear_boxes()
		self.textCtrlAccountName.WriteText(str(self.user.accountList[self.listBoxAccounts.GetSelection()].name))        
		self.textCtrlBalance.WriteText('$'+str(round(self.user.accountList[self.listBoxAccounts.GetSelection()].balance, 2)))    
		self.pos_neg_amount_forecolor(round(self.user.accountList[self.listBoxAccounts.GetSelection()].balance, 2), self.textCtrlBalance)    
		self.textCtrlTotalBalance.WriteText('$'+str(round(self.user.get_total_accounts_balance(), 2)))
		self.pos_neg_amount_forecolor_total(round(self.user.get_total_accounts_balance(), 2), self.textCtrlTotalBalance)  
		self.textCtrlBankName.WriteText(self.user.accountList[self.listBoxAccounts.GetSelection()].bank_name)
		self.textCtrlCreditLimit.Enabled = False
		self.textCtrlInterestRate.Enabled = False
		self.staticTextCreditLimit.Enabled = False
		self.staticTextInterestRate.Enabled = False
		if self.user.accountList[self.listBoxAccounts.GetSelection()].type == 'Credit Card':
			self.textCtrlCreditLimit.WriteText('$'+str(self.user.accountList[self.listBoxAccounts.GetSelection()].credit_limit))
			if str(self.user.accountList[self.listBoxAccounts.GetSelection()].interest_rate) != '': 
				self.textCtrlInterestRate.WriteText(str(self.user.accountList[self.listBoxAccounts.GetSelection()].interest_rate)+'%')
			self.textCtrlCreditLimit.Enabled = True
			self.textCtrlInterestRate.Enabled = True
			self.staticTextCreditLimit.Enabled = True
			self.staticTextInterestRate.Enabled = True
		self.buttonEditAccount.Enabled = True        
		self.buttonRemoveAccount.Enabled = True        
		if len(self.user.accountList) > 1: self.buttonCurrentAccount.Enabled = True
		self.choiceAccountType.SetStringSelection(self.user.accountList[self.listBoxAccounts.GetSelection()].type)
		
	def OnTextCtrlAccountNameText(self, event):
		self.set_forecolor_black([self.textCtrlBalance])
		
	def OnTextCtrlBalanceText(self, event):
		self.choiceAccountType.Enabled = True        
		self.set_forecolor_black([self.textCtrlBalance])

	def OnButtonAddAccountButton(self, event):            
		if self.textCtrlAccountName.GetValue() == '' and self.textCtrlBalance.GetValue() == '' and self.choiceAccountType.GetSelection() == -1:
			wx.MessageBox(self.add_account_message, 'To add an account', wx.OK | wx.CENTRE)
			self.set_backcolor_green(self.textCtrlAccountName)
		elif self.textCtrlAccountName.GetValue() == '' and self.textCtrlBalance.GetValue() == '': 
			wx.MessageBox('In order to add an account, it has to have a name. You can enter that below where it says \"Account Name\".', 'Account has no name', wx.OK | wx.CENTRE)
			self.set_backcolor_red(self.textCtrlAccountName)
		elif self.textCtrlAccountName.GetValue() == '' and self.textCtrlBalance.GetValue() != '': 
			wx.MessageBox('In order to add an account, it has to have a name. You can enter that below where it says \"Account Name\".', 'Account has no name', wx.OK | wx.CENTRE)
			self.set_backcolor_red(self.textCtrlAccountName)      
			self.set_backcolor_white([self.textCtrlBalance])
		elif self.textCtrlAccountName.GetValue() != '' and self.textCtrlBalance.GetValue() == '': 
			wx.MessageBox('In order to add an account, it has to have an balance. You can set the balance to $0 or even give it a negative balance if your account is overdrawn. You can enter that below where it says \"Balance\".', 'Account has no balance', wx.OK | wx.CENTRE)
			self.set_backcolor_red(self.textCtrlBalance)            
			self.set_backcolor_white([self.textCtrlAccountName])
		elif self.textCtrlAccountName.GetValue() != '' and self.textCtrlBalance.GetValue() != '' and self.choiceAccountType.GetSelection() == -1: 
			wx.MessageBox('In order to add an account, Cbudget needs to know if it\'s a Checking, Savings, or Credit Card account. You can select that below where it says \"Account Type\".', 'Account has no type', wx.OK | wx.CENTRE)
			self.set_backcolor_red(self.staticTextSelectAccountType)
			self.set_backcolor_white([self.textCtrlAccountName, self.textCtrlBalance])
		elif self.choiceAccountType.GetSelection() == 2 and self.textCtrlCreditLimit.GetValue() == '': 
			wx.MessageBox('In order to add a credit card account, it has to have a credit limit. You can enter that below where it says \"Credit Limit\".', 'Credit card account has no credit limit', wx.OK | wx.CENTRE) 
			self.set_backcolor_red(self.textCtrlCreditLimit)
			self.set_backcolor_white([self.textCtrlAccountName, self.textCtrlBalance])
		else:
			self.set_backcolor_white([self.textCtrlAccountName, self.textCtrlBalance, self.textCtrlCreditLimit])
			self.set_backcolor_grey(self.staticTextSelectAccountType)
			balance = 0.0
			try: 
				if '$' in self.textCtrlBalance.GetValue(): balance = float(self.textCtrlBalance.GetValue()[1:])
				else: balance = float(self.textCtrlBalance.GetValue())                        
				if self.textCtrlAccountName.GetValue() not in self.listBoxAccounts.GetStrings(): 
					if self.choiceAccountType.GetStringSelection() == 'Checking': 
						self.user.addCheckingAccount(self.textCtrlAccountName.GetValue(), 0.0, '', self.textCtrlBankName.GetValue(), self.choiceAccountType.GetStringSelection())
						trans = CBudgetP.transaction(self.textCtrlAccountName.GetValue(), balance, datetime.now(), '', 'starting balance', 'account_creation')
						if len(self.user.accountList[-1].r.registerList) == 0: self.user.accountList[-1].r.add_transaction(self.user, trans, self.user.accountList[-1])
						self.add_account(event)
					if self.choiceAccountType.GetStringSelection() == 'Savings': 
						self.user.addSavingsAccount(self.textCtrlAccountName.GetValue(), 0.0, '', self.textCtrlBankName.GetValue(), self.choiceAccountType.GetStringSelection())
						trans = CBudgetP.transaction(self.textCtrlAccountName.GetValue(), balance, datetime.now(), '', 'starting balance', 'account_creation')
						if len(self.user.accountList[-1].r.registerList) == 0: self.user.accountList[-1].r.add_transaction(self.user, trans, self.user.accountList[-1])
						self.add_account(event)
					if self.choiceAccountType.GetStringSelection() == 'Credit Card':
						self.user.addCreditCardAccount(self.textCtrlAccountName.GetValue(), 0.0, '', self.textCtrlBankName.GetValue(),self.textCtrlInterestRate.GetValue(), float(self.textCtrlCreditLimit.GetValue()), self.choiceAccountType.GetStringSelection())
						trans = CBudgetP.transaction(self.textCtrlAccountName.GetValue(), balance, datetime.now(), '', 'starting balance', 'account_creation')
						if len(self.user.accountList[-1].r.registerList) == 0: self.user.accountList[-1].r.add_transaction(self.user, trans, self.user.accountList[-1])
						self.add_account(event)
				else: 
					wx.MessageBox('Sorry, you can\'t add an account with that name. It\'s already in the list. To add another account, you\'ll need to change the name.', 'Duplicate account', wx.OK | wx.CENTRE)                    
					self.set_backcolor_red(self.textCtrlAccountName)
			except ValueError:                 
				wx.MessageBox('The balance you are entering has to be a number and can\'t be blank. You\'ve probably entered some letters, symbols, or a word. Make sure it\'s a number.', 'Balance is not a number', wx.OK | wx.CENTRE)
				self.set_backcolor_red(self.textCtrlBalance)
		self.enable_ctrls(False)     
						
	def add_account(self, event):
		self.listBoxAccounts.Clear()
		self.listBoxAccounts.InsertItems([a.name for a in self.user.accountList],0)        
		self.enable_ctrls(False)
		if self.choiceAccountType.GetStringSelection() == 'Credit Card':
			self.textCtrlInterestRate.Enabled = True
			self.staticTextInterestRate.Enabled = True
		self.enable_main_buttons(True)
		if len(self.user.accountList) > 1: self.enable_transfer_ctrls(True)
		if self.user.expenseList == [] or self.user.incomeList == []: 
			self.buttonExpensesDue.Enabled = False       
			self.buttonBudget.Enabled = False
		self.a.run_first_time = False        
		self.user.set_current_account(self.user.accountList[-1])
		init.save()
		wx.MessageBox('The {0} account \"{1}\" has been to your accounts list.'.format(self.choiceAccountType.GetStringSelection().lower(), self.textCtrlAccountName.GetValue()), 'Account added', wx.OK | wx.CENTRE)                    
		self.clear_boxes()
		self.set_backcolor_white([self.textCtrlAccountName, self.textCtrlBalance, self.textCtrlCreditLimit, self.textCtrlInterestRate])
		self.choiceFrom.Clear()
		self.choiceTo.Clear()
		for a in self.user.accountList: self.choiceFrom.Append(a.name)
		for a in self.user.accountList: self.choiceTo.Append(a.name)
		self.textCtrlAccountName.SetFocus()
		if self.user.incomeList == [] and len(self.user.accountList) == 1:
			result = wx.MessageBox('Now that you have an account, it would be a good idea to go to the Incomes window and enter some income information, or you can stay here and add more accounts. Would you like to enter some incomes now?', 'Enter incomes?', wx.YES_NO | wx.CENTRE)
			if result == wx.YES: self.OnButtonIncomesButton(event)
		if self.user.incomeList == [] and len(self.user.accountList) > 1:
			result = wx.MessageBox('Now that you have some accounts, it would be a good idea to go to the Incomes window and enter some income information, or you can stay here and add more accounts. Would you like to enter some incomes now?', 'Enter incomes?', wx.YES_NO | wx.CENTRE)
			if result == wx.YES: self.OnButtonIncomesButton(event)        

		
	def OnButtonRemoveAccountButton(self, event):
		result = wx.MessageBox('You are about to remove the account: {0}. Is this what you really want to do?'.format(self.user.accountList[self.listBoxAccounts.GetSelection()].name), 'Remove account?', wx.YES_NO | wx.CENTRE)
		if result == wx.YES:
			temp = self.user.get_current_account()
			if self.user.removeAccount(self.user.accountList[self.listBoxAccounts.GetSelection()]) == 'success':
				wx.MessageBox("Because your previous current account, {0}, was removed. Your new current account has been set to {1}. To change it, select an account from the list and click 'Change Current Account'".format(temp.name, self.user.accountList[0].name), 'Primary account changed!', wx.OK | wx.CENTRE) 
			init.save()
			self.listBoxAccounts.Clear()
			self.listBoxAccounts.InsertItems([a.name for a in self.user.accountList],0)
			self.clear_boxes()
			self.enable_ctrls(False)
			self.enable_transfer_ctrls(False)
			if self.user.accountList == []: self.enable_main_buttons(False)
		
	def OnButtonEditAccountButton(self, event):
		if self.textCtrlAccountName.GetValue() != '': self.user.accountList[self.listBoxAccounts.GetSelection()].name = self.textCtrlAccountName.GetValue()        
		if self.textCtrlBalance.GetValue() != '':
			balance = 0.0
			try: 
				if '$' in self.textCtrlBalance.GetValue(): balance = float(self.textCtrlBalance.GetValue()[1:])
				else: balance = float(self.textCtrlBalance.GetValue())        
				self.user.accountList[self.listBoxAccounts.GetSelection()].balance = balance
			except ValueError: wx.MessageBox('The balance you are entering has to be a number. You\'ve probably entered some letters, symbols, or a word. Make sure it\'s a number.', 'Balance is not a number', wx.OK | wx.CENTRE)
		if self.textCtrlBankName.GetValue() != '': self.user.accountList[self.listBoxAccounts.GetSelection()].bank_name = self.textCtrlBankName.GetValue()
		if self.choiceAccountType.GetSelection() != -1: self.user.accountList[self.listBoxAccounts.GetSelection()].type = self.choiceAccountType.GetStringSelection()
		if self.choiceAccountType.GetSelection() == 2:
			if self.textCtrlCreditLimit.GetValue() != '':
				credit_limit = 0.0
				try: 
					if '$' in self.textCtrlCreditLimit.GetValue(): credit_limit = float(self.textCtrlCreditLimit.GetValue()[1:])
					else: credit_limit = float(self.textCtrlCreditLimit.GetValue())        
					self.user.accountList[self.listBoxAccounts.GetSelection()].credit_limit = credit_limit
					init.save()
					self.set_backcolor_white([self.textCtrlCreditLimit])
				except ValueError: 
					wx.MessageBox('The credit limit you are entering has to be a number. You\'ve probably entered some letters, symbols, or a word. Make sure it\'s a number.', 'Credit limit is not a number', wx.OK | wx.CENTRE)        
					self.set_backcolor_red(self.textCtrlCreditLimit)
			if self.textCtrlInterestRate.GetValue() != '':
				interest_rate = 0.0
				try: 
					if '%' in self.textCtrlInterestRate.GetValue(): interest_rate = float(self.textCtrlInterestRate.GetValue()[:-1])
					else: interest_rate = float(self.textCtrlInterestRate.GetValue())        
					self.user.accountList[self.listBoxAccounts.GetSelection()].interest_rate = interest_rate
					init.save()
					self.set_backcolor_white([self.textCtrlInterestRate])
				except ValueError: 
					wx.MessageBox('The interest rate you are entering has to be a number. You\'ve probably entered some letters, symbols, or a word. Make sure it\'s a number.', 'Interest rate is not a number', wx.OK | wx.CENTRE)                            
					self.set_backcolor_red(self.textCtrlCreditLimit)
		init.save()       
		self.enable_ctrls(False)
		self.listBoxAccounts.Clear()
		self.listBoxAccounts.InsertItems([a.name for a in self.user.accountList],0)    
	
	def OnChoiceAccountTypeChoice(self, event):
		self.buttonAddAccount.Enabled = True
		if self.choiceAccountType.GetStringSelection() == 'Credit Card': 
			self.textCtrlInterestRate.Enabled = True
			self.staticTextInterestRate.Enabled = True
			self.textCtrlCreditLimit.Enabled = True
			self.staticTextCreditLimit.Enabled = True
		else: 
			self.textCtrlInterestRate.Enabled = False
			self.staticTextInterestRate.Enabled = False  
			self.textCtrlCreditLimit.Enabled = False
			self.staticTextCreditLimit.Enabled = False
		
	def OnButtonCurrentAccountButton(self, event):
		if self.user.get_current_account().name != self.textCtrlAccountName.GetValue(): 
			result = wx.MessageBox('Your current account is {0}. You are changing it to {1}. Is this correct?'.format(self.user.get_current_account().name, self.user.accountList[self.listBoxAccounts.GetSelection()].name), 'Change current account?', wx.YES_NO | wx.CENTRE)        
			if result == wx.YES: 
				self.user.set_current_account(self.user.accountList[self.listBoxAccounts.GetSelection()])
				init.save()
				wx.MessageBox('Your current account is now: {0}'.format(self.user.get_current_account().name), 'Current account', wx.OK | wx.CENTRE)        
		else: wx.MessageBox('Your current account is {0}. You can change it by selecting a different account from the list above and clicking the [Current Account] button again.'.format(self.textCtrlAccountName.GetValue()), 'Current account', wx.OK | wx.CENTRE)  
		
	def OnButtonRecordTransferButton(self, event):
		for a in self.user.accountList:
			if self.choiceFrom.GetStringSelection() == a.name: from_account = a
			if self.choiceTo.GetStringSelection() == a.name: to_account = a
		if self.choiceFrom.GetStringSelection() != '' and self.choiceTo.GetStringSelection() != '':
			if self.textCtrlTransferAmount.GetValue() != '': 
				if self.choiceFrom.GetStringSelection() != self.choiceTo.GetStringSelection():
					amount = 0.0
					try: 
						if '$' in self.textCtrlTransferAmount.GetValue(): amount = float(self.textCtrlTransferAmount.GetValue()[1:])
						else: amount = float(self.textCtrlTransferAmount.GetValue())     
						if amount > from_account.balance: 
							result = wx.MessageBox('This action will record an overdrawn balance for the account {0}. Do you want to continue?'.format(from_account.name), 'Insufficient funds!', wx.YES_NO | wx.CENTRE)
							if result == wx.YES:
								subresult = wx.MessageBox('You are recording a transfer of ${0} from {1} to {2}. Is this correct?'.format(self.textCtrlTransferAmount.GetValue(), self.choiceFrom.GetStringSelection(), self.choiceTo.GetStringSelection()), 'Record funds transfer?', wx.YES_NO | wx.CENTRE)        
								if subresult == wx.YES:    
									from_account.r.add_transaction(self.user, CBudgetP.transaction('account transfer', amount*-1, datetime.now(), '', 'to '+self.choiceTo.GetStringSelection(), 'transfer debit'), from_account)
									to_account.r.add_transaction(self.user, CBudgetP.transaction('account transfer', amount, datetime.now(), '', 'from '+self.choiceFrom.GetStringSelection(), 'transfer credit'), to_account)
									wx.MessageBox('Your transfer of ${0} from {1} to {2} has been recorded in the transaction register. You can view this activity in the Transaction window'.format(float(self.textCtrlTransferAmount.GetValue()), self.choiceFrom.GetStringSelection(), self.choiceTo.GetStringSelection()), 'Success', wx.OK | wx.CENTRE)                     
									init.save()
									self.set_backcolor_white([self.textCtrlTransferAmount])
									self.choiceFrom.SetSelection(-1)
									self.choiceTo.SetSelection(-1)
									self.textCtrlTransferAmount.Clear()
									self.textCtrlBalance.Clear()
									self.textCtrlTotalBalance.Clear()
									self.textCtrlBalance.WriteText('$'+str(round(self.user.accountList[self.listBoxAccounts.GetSelection()].balance, 2)))    
									self.pos_neg_amount_forecolor(round(self.user.accountList[self.listBoxAccounts.GetSelection()].balance, 2), self.textCtrlBalance)    
									self.textCtrlTotalBalance.WriteText('$'+str(round(self.user.get_total_accounts_balance(), 2)))
									self.pos_neg_amount_forecolor_total(round(self.user.get_total_accounts_balance(), 2), self.textCtrlTotalBalance) 
						else: 
							subresult = wx.MessageBox('You are recording a transfer of ${0} from {1} to {2}. Is this correct?'.format(self.textCtrlTransferAmount.GetValue(), self.choiceFrom.GetStringSelection(), self.choiceTo.GetStringSelection()), 'Record funds transfer?', wx.YES_NO | wx.CENTRE)        
							if subresult == wx.YES:    
								from_account.r.add_transaction(self.user, CBudgetP.transaction('account transfer', amount*-1, datetime.now(), '', 'to '+self.choiceTo.GetStringSelection(), 'transfer debit'), from_account)
								to_account.r.add_transaction(self.user, CBudgetP.transaction('account transfer', amount, datetime.now(), '', 'from '+self.choiceFrom.GetStringSelection(), 'transfer credit'), to_account)
								wx.MessageBox('Your transfer of ${0} from {1} to {2} has been recorded in the transaction register. You can view this activity in the Transaction window'.format(float(self.textCtrlTransferAmount.GetValue()), self.choiceFrom.GetStringSelection(), self.choiceTo.GetStringSelection()), 'Success', wx.OK | wx.CENTRE)                     
								init.save()
								self.set_backcolor_white([self.textCtrlTransferAmount])
								self.choiceFrom.SetSelection(-1)
								self.choiceTo.SetSelection(-1)
								self.textCtrlTransferAmount.Clear()
								self.textCtrlBalance.Clear()
								self.textCtrlTotalBalance.Clear()
								self.textCtrlBalance.WriteText('$'+str(round(self.user.accountList[self.listBoxAccounts.GetSelection()].balance, 2)))    
								self.pos_neg_amount_forecolor(round(self.user.accountList[self.listBoxAccounts.GetSelection()].balance, 2), self.textCtrlBalance)    
								self.textCtrlTotalBalance.WriteText('$'+str(round(self.user.get_total_accounts_balance(), 2)))
								self.pos_neg_amount_forecolor_total(round(self.user.get_total_accounts_balance(), 2), self.textCtrlTotalBalance)                                 
					except ValueError:                 
						wx.MessageBox('The transfer amount you are entering has to be a number. You\'ve probably entered some letters, symbols, or a word. Make sure it\'s a number.', 'Transfer amount is not a number', wx.OK | wx.CENTRE)
						self.set_backcolor_red(self.textCtrlTransferAmount)
						self.OnListBoxAccountsListbox(event)
				else: 
					wx.MessageBox('You are trying to record a transfer from an account to itsself. Make sure the From and To accounts are different', 'Transfer to same account', wx.OK | wx.CENTRE)                                        
					self.OnListBoxAccountsListbox(event)
			else: 
				wx.MessageBox('You must enter a transfer amount to transfer funds', 'Enter an amount', wx.OK | wx.CENTRE)                     
				self.set_backcolor_red(self.textCtrlTransferAmount)
				self.OnListBoxAccountsListbox(event)
		else: wx.MessageBox('You must select both from and to accounts in order to transfer funds', 'Select transfer accounts', wx.OK | wx.CENTRE)                     
		
	def OnChoiceFromChoice(self, event):
		for a in self.user.accountList: 
			if a.name == self.choiceFrom.GetStringSelection(): 
				self.textCtrlBalance.Clear()
				self.textCtrlBalance.WriteText('$'+str(round(a.balance, 2)))    
				self.pos_neg_amount_forecolor(round(a.balance, 2), self.textCtrlBalance)    

	def OnChoiceToChoice(self, event):
		for a in self.user.accountList: 
			if a.name == self.choiceTo.GetStringSelection(): 
				self.textCtrlBalance.Clear()
				self.textCtrlBalance.WriteText('$'+str(a.balance))
				self.pos_neg_amount_forecolor_total(a.balance, self.textCtrlBalance)
				
	def enable_ctrls(self, enable):
		if enable:
			self.buttonRemoveAccount.Enabled = True
			self.buttonEditAccount.Enabled = True
			self.buttonCurrentAccount.Enabled = True
		else:
			self.buttonRemoveAccount.Enabled =  False
			self.buttonEditAccount.Enabled = False            
			self.buttonCurrentAccount.Enabled = False       
			
	def enable_transfer_ctrls(self, enable):
		if enable:
			self.staticTextRecordTransferFunds.Enabled = True
			self.staticTextRecordTransferFunds.Enabled = True
			self.staticTextFrom.Enabled = True
			self.staticTextTo.Enabled = True
			self.choiceFrom.Enabled = True
			self.choiceTo.Enabled = True
			self.buttonRecordTransfer.Enabled = True
			self.staticTextTransferAmount.Enabled = True
			self.textCtrlTransferAmount.Enabled = True   
		else:
			self.staticTextRecordTransferFunds.Enabled = False
			self.staticTextFrom.Enabled = False
			self.staticTextTo.Enabled = False         
			self.choiceFrom.Enabled = False
			self.choiceTo.Enabled = False
			self.buttonRecordTransfer.Enabled = False
			self.staticTextTransferAmount.Enabled = False
			self.textCtrlTransferAmount.Enabled = False
			
	def enable_main_buttons(self, enable):
		if enable:
			self.buttonIncomes.Enabled = True
			self.buttonCredits.Enabled = True
			self.buttonExpenses.Enabled = True
			self.buttonSavingsItems.Enabled = True
			self.buttonBudget.Enabled = True
			self.buttonExpensesDue.Enabled = True
			self.buttonTransactions.Enabled = True
		else:
			self.buttonIncomes.Enabled = False
			self.buttonCredits.Enabled = False
			self.buttonExpenses.Enabled = False
			self.buttonSavingsItems.Enabled = False
			self.buttonBudget.Enabled = False
			self.buttonExpensesDue.Enabled = False
			self.buttonTransactions.Enabled = False
			
	def clear_boxes(self):
		self.textCtrlAccountName.Clear()
		self.textCtrlBalance.Clear()     
		self.textCtrlTotalBalance.Clear()             
		self.textCtrlBankName.Clear()    
		self.textCtrlCreditLimit.Clear()
		self.textCtrlInterestRate.Clear()       
			
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
		account = self.user.accountList[self.listBoxAccounts.GetSelection()]
		if account.type == 'Credit Card': amount *= -1
		if amount > 0:
			ctrl.SetForegroundColour(wx.Colour(0, 128, 0))
			ctrl.Refresh
		elif amount == 0:
			ctrl.SetForegroundColour(wx.Colour(0, 0, 0))
			ctrl.Refresh
		else:
			ctrl.SetForegroundColour(wx.Colour(197, 1, 31))
			ctrl.Refresh
			
	def pos_neg_amount_forecolor_total(self, amount, ctrl):
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
		
	def OnBitmapButtonHomeButton(self, event):
		self.Hide()
		self.Close()
		self.main = CBudgetP_Home.create(None)
		self.main.Show()
		
	def OnButtonIncomesButton(self, event):
		init.userList[0].s.show_incomes = True
		init.save()
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

	def OnButtonTransactionsButton(self, event):
		self.user.s.show_transactions = True
		init.save()        
		self.Hide()
		self.Close()
		self.main = CBudgetP_Transactions.create(None)
		self.main.Show()
		
	def OnButtonCloseButton(self, event):        
		if self.a.run_count <= 10: init.delete_install_folder()
		self.Close()
		init.end_process()

