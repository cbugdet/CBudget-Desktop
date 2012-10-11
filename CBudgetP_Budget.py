#Boa:Frame:Budget

import wx
import CBudgetP
import os
import time
init = CBudgetP.initialize()
import CBudgetP_Home
from datetime import datetime
import CBudgetP_Accounts
import CBudgetP_Incomes
import CBudgetP_Credits
import CBudgetP_Expenses
import CBudgetP_SavingsItems
import CBudgetP_ExpensesDue
import CBudgetP_Transactions

def create(parent):
    return Budget(parent)

[wxID_BUDGET, wxID_BUDGETBUTTONACCOUNTS, wxID_BUDGETBUTTONCLOSE, 
 wxID_BUDGETBUTTONCREDITS, wxID_BUDGETBUTTONEXPENSES, 
 wxID_BUDGETBUTTONEXPENSESDUE, wxID_BUDGETBUTTONHOME, 
 wxID_BUDGETBUTTONINCOMES, wxID_BUDGETBUTTONRECORDTRANSFERS, 
 wxID_BUDGETBUTTONSAVINGSITEMS, wxID_BUDGETBUTTONTRANSACTIONS, 
 wxID_BUDGETCHOICEPAYBILLS, wxID_BUDGETCHOICESAVINGS, 
 wxID_BUDGETCHOICESPENDING, wxID_BUDGETLISTBOXINCOMES, wxID_BUDGETPANEL1, 
 wxID_BUDGETSTATICTEXTDAILYALLOWANCE, wxID_BUDGETSTATICTEXTDEBTTOINCOMERATIO, 
 wxID_BUDGETSTATICTEXTINCOMES, wxID_BUDGETSTATICTEXTLEFTOVER, 
 wxID_BUDGETSTATICTEXTMONTHLYALLOWANCE, wxID_BUDGETSTATICTEXTMONTHLYSAVINGS, 
 wxID_BUDGETSTATICTEXTSAVEAMOUNT, wxID_BUDGETSTATICTEXTSETASIDE, 
 wxID_BUDGETSTATICTEXTWEEKLYALLOWANCE, wxID_BUDGETSTATICTEXTWHEREPUTMONEY, 
 wxID_BUDGETTEXTCTRLDAILYALLOWANCE, wxID_BUDGETTEXTCTRLDEBTTOINCOMERATIO, 
 wxID_BUDGETTEXTCTRLMONTHLYALLOWANCE, wxID_BUDGETTEXTCTRLMONTHLYSAVINGS, 
 wxID_BUDGETTEXTCTRLPAYBILLS, wxID_BUDGETTEXTCTRLSAVINGS, 
 wxID_BUDGETTEXTCTRLSPENDING, wxID_BUDGETTEXTCTRLWEEKLYALLOWANCE, 
] = [wx.NewId() for _init_ctrls in range(34)]

class Budget(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_BUDGET, name='Budget', parent=prnt,
              pos=wx.Point(344, 103), size=wx.Size(678, 521), style=wx.CAPTION,
              title='Budget')
        self.SetClientSize(wx.Size(662, 483))
        self.Center(wx.BOTH)
        self.Bind(wx.EVT_IDLE, self.OnBudgetIdle)

        self.panel1 = wx.Panel(id=wxID_BUDGETPANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(662, 483),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetToolTipString('Budget Window')
        self.panel1.Bind(wx.EVT_MOTION, self.OnPanel1Motion)

        self.listBoxIncomes = wx.ListBox(choices=[],
              id=wxID_BUDGETLISTBOXINCOMES, name='listBoxIncomes',
              parent=self.panel1, pos=wx.Point(224, 40), size=wx.Size(368, 100),
              style=0)
        self.listBoxIncomes.SetToolTipString('Shows your incomes. Select an income to view suggested amounts to be set aside for bills, savings, and left over for spending')
        self.listBoxIncomes.Bind(wx.EVT_LISTBOX, self.OnListBoxIncomesListbox,
              id=wxID_BUDGETLISTBOXINCOMES)

        self.textCtrlDebtToIncomeRatio = wx.TextCtrl(id=wxID_BUDGETTEXTCTRLDEBTTOINCOMERATIO,
              name='textCtrlDebtToIncomeRatio', parent=self.panel1,
              pos=wx.Point(64, 40), size=wx.Size(100, 21), style=wx.TE_CENTER,
              value='')
        self.textCtrlDebtToIncomeRatio.SetToolTipString('Using the ratio of your total expenses to total income, CBudget calculates a suggested amount for you to save each paycheck with a formual that uses this percentage')

        self.textCtrlMonthlySavings = wx.TextCtrl(id=wxID_BUDGETTEXTCTRLMONTHLYSAVINGS,
              name='textCtrlMonthlySavings', parent=self.panel1,
              pos=wx.Point(64, 92), size=wx.Size(100, 21), style=wx.TE_CENTER,
              value='')
        self.textCtrlMonthlySavings.SetToolTipString('This is the amount you would be saving each month if you are setting aside the suggested amount to save per paycheck')

        self.textCtrlDailyAllowance = wx.TextCtrl(id=wxID_BUDGETTEXTCTRLDAILYALLOWANCE,
              name='textCtrlDailyAllowance', parent=self.panel1,
              pos=wx.Point(64, 144), size=wx.Size(100, 21), style=wx.TE_CENTER,
              value='')
        self.textCtrlDailyAllowance.SetToolTipString('This is just so you know how much you could get away with spending each day to keep from going over the amount left over for spending')

        self.textCtrlWeeklyAllowance = wx.TextCtrl(id=wxID_BUDGETTEXTCTRLWEEKLYALLOWANCE,
              name='textCtrlWeeklyAllowance', parent=self.panel1,
              pos=wx.Point(64, 200), size=wx.Size(100, 21), style=wx.TE_CENTER,
              value='')
        self.textCtrlWeeklyAllowance.SetToolTipString('This is just so you know how much you could get away with spending each week to keep from going over the amount left over for spending')

        self.textCtrlMonthlyAllowance = wx.TextCtrl(id=wxID_BUDGETTEXTCTRLMONTHLYALLOWANCE,
              name='textCtrlMonthlyAllowance', parent=self.panel1,
              pos=wx.Point(64, 256), size=wx.Size(100, 21), style=wx.TE_CENTER,
              value='')
        self.textCtrlMonthlyAllowance.SetToolTipString('This is just so you know how much you could get away with spending each month to keep from going over the amount left over for spending')

        self.textCtrlPayBills = wx.TextCtrl(id=wxID_BUDGETTEXTCTRLPAYBILLS,
              name='textCtrlPayBills', parent=self.panel1, pos=wx.Point(224,
              200), size=wx.Size(100, 21), style=wx.TE_CENTER, value='')
        self.textCtrlPayBills.SetToolTipString('When you get paid, put this amount into a seperate account "pool" so you will always have enough money to pay bills when they are due')

        self.choicePayBills = wx.Choice(choices=[],
              id=wxID_BUDGETCHOICEPAYBILLS, name='choicePayBills',
              parent=self.panel1, pos=wx.Point(224, 224), size=wx.Size(100, 21),
              style=0)
        self.choicePayBills.SetToolTipString('Use this selector to choose the account you would like to transfer funds to for paying bills')
        self.choicePayBills.Bind(wx.EVT_CHOICE, self.OnChoicePayBillsChoice,
              id=wxID_BUDGETCHOICEPAYBILLS)

        self.textCtrlSavings = wx.TextCtrl(id=wxID_BUDGETTEXTCTRLSAVINGS,
              name='textCtrlSavings', parent=self.panel1, pos=wx.Point(360,
              200), size=wx.Size(100, 21), style=wx.TE_CENTER, value='')
        self.textCtrlSavings.SetToolTipString('When you get paid, put this amount into a seperate savings account \"pool\" so you can start building up a savings for emergencies')

        self.choiceSavings = wx.Choice(choices=[], id=wxID_BUDGETCHOICESAVINGS,
              name='choiceSavings', parent=self.panel1, pos=wx.Point(360, 224),
              size=wx.Size(100, 21), style=0)
        self.choiceSavings.SetToolTipString('Use this selector to choose the account you would like to transfer funds to for saving money')
        self.choiceSavings.Bind(wx.EVT_CHOICE, self.OnChoiceSavingsChoice,
              id=wxID_BUDGETCHOICESAVINGS)

        self.textCtrlSpending = wx.TextCtrl(id=wxID_BUDGETTEXTCTRLSPENDING,
              name='textCtrlSpending', parent=self.panel1, pos=wx.Point(496,
              200), size=wx.Size(100, 21), style=wx.TE_CENTER, value='')
        self.textCtrlSpending.SetToolTipString('When you get paid, this amount is left over so you can have some spending cash. You can transfer this amount to a seperate account for spending money or just leave it in the account your paycheck went into')

        self.choiceSpending = wx.Choice(choices=[],
              id=wxID_BUDGETCHOICESPENDING, name='choiceSpending',
              parent=self.panel1, pos=wx.Point(496, 224), size=wx.Size(100, 21),
              style=0)
        self.choiceSpending.SetToolTipString('Use this selector to choose the account you would like to transfer funds to for spending money')
        self.choiceSpending.Bind(wx.EVT_CHOICE, self.OnChoiceSpendingChoice,
              id=wxID_BUDGETCHOICESPENDING)

        self.buttonRecordTransfers = wx.Button(id=wxID_BUDGETBUTTONRECORDTRANSFERS,
              label='Record Transfers', name='buttonRecordTransfers',
              parent=self.panel1, pos=wx.Point(335, 256), size=wx.Size(150, 32),
              style=0)
        self.buttonRecordTransfers.SetToolTipString('Records transfers of the above amounts. Use the account selectors above to choose which accounts to record transfers to')
        self.buttonRecordTransfers.Bind(wx.EVT_BUTTON,
              self.OnButtonRecordTransfersButton,
              id=wxID_BUDGETBUTTONRECORDTRANSFERS)

        self.buttonHome = wx.Button(id=wxID_BUDGETBUTTONHOME, label='Home',
              name='buttonHome', parent=self.panel1, pos=wx.Point(144, 312),
              size=wx.Size(85, 48), style=0)
        self.buttonHome.SetToolTipString('Takes you back to the Home window. If you press this button you will have to enter your password again.')
        self.buttonHome.Bind(wx.EVT_BUTTON, self.OnButtonHomeButton,
              id=wxID_BUDGETBUTTONHOME)

        self.buttonAccounts = wx.Button(id=wxID_BUDGETBUTTONACCOUNTS,
              label='Accounts', name='buttonAccounts', parent=self.panel1,
              pos=wx.Point(240, 312), size=wx.Size(85, 48), style=0)
        self.buttonAccounts.SetToolTipString('Takes you to the Accounts window')
        self.buttonAccounts.Bind(wx.EVT_BUTTON, self.OnButtonAccountsButton,
              id=wxID_BUDGETBUTTONACCOUNTS)

        self.buttonIncomes = wx.Button(id=wxID_BUDGETBUTTONINCOMES,
              label='Incomes', name='buttonIncomes', parent=self.panel1,
              pos=wx.Point(336, 312), size=wx.Size(85, 48), style=0)
        self.buttonIncomes.SetToolTipString('Takes you to the Incomes window')
        self.buttonIncomes.Bind(wx.EVT_BUTTON, self.OnButtonIncomesButton,
              id=wxID_BUDGETBUTTONINCOMES)

        self.buttonCredits = wx.Button(id=wxID_BUDGETBUTTONCREDITS,
              label='Credits', name='buttonCredits', parent=self.panel1,
              pos=wx.Point(432, 312), size=wx.Size(85, 48), style=0)
        self.buttonCredits.SetToolTipString('Takes you to the Credits window')
        self.buttonCredits.Bind(wx.EVT_BUTTON, self.OnButtonCreditsButton,
              id=wxID_BUDGETBUTTONCREDITS)

        self.buttonExpenses = wx.Button(id=wxID_BUDGETBUTTONEXPENSES,
              label='Expenses', name='buttonExpenses', parent=self.panel1,
              pos=wx.Point(144, 368), size=wx.Size(85, 48), style=0)
        self.buttonExpenses.SetToolTipString('Takes you to the Expenses window')
        self.buttonExpenses.Bind(wx.EVT_BUTTON, self.OnButtonExpensesButton,
              id=wxID_BUDGETBUTTONEXPENSES)

        self.buttonSavingsItems = wx.Button(id=wxID_BUDGETBUTTONSAVINGSITEMS,
              label='Savings Items', name='buttonSavingsItems',
              parent=self.panel1, pos=wx.Point(240, 368), size=wx.Size(85, 48),
              style=0)
        self.buttonSavingsItems.SetToolTipString('Takes you to the Savings Items window')
        self.buttonSavingsItems.Bind(wx.EVT_BUTTON,
              self.OnButtonSavingsItemsButton,
              id=wxID_BUDGETBUTTONSAVINGSITEMS)

        self.buttonExpensesDue = wx.Button(id=wxID_BUDGETBUTTONEXPENSESDUE,
              label='Expenses Due', name='buttonExpensesDue',
              parent=self.panel1, pos=wx.Point(336, 368), size=wx.Size(85, 48),
              style=0)
        self.buttonExpensesDue.SetToolTipString('Takes you to the Expenses Due window')
        self.buttonExpensesDue.Bind(wx.EVT_BUTTON,
              self.OnButtonExpensesDueButton, id=wxID_BUDGETBUTTONEXPENSESDUE)

        self.buttonClose = wx.Button(id=wxID_BUDGETBUTTONCLOSE, label='Close',
              name='buttonClose', parent=self.panel1, pos=wx.Point(295, 440),
              size=wx.Size(75, 23), style=0)
        self.buttonClose.Bind(wx.EVT_BUTTON, self.OnButtonCloseButton,
              id=wxID_BUDGETBUTTONCLOSE)

        self.staticTextDailyAllowance = wx.StaticText(id=wxID_BUDGETSTATICTEXTDAILYALLOWANCE,
              label='Daily Allowance', name='staticTextDailyAllowance',
              parent=self.panel1, pos=wx.Point(78, 128), size=wx.Size(75, 13),
              style=0)

        self.staticTextWeeklyAllowance = wx.StaticText(id=wxID_BUDGETSTATICTEXTWEEKLYALLOWANCE,
              label='Weekly Allowance', name='staticTextWeeklyAllowance',
              parent=self.panel1, pos=wx.Point(72, 184), size=wx.Size(87, 13),
              style=0)

        self.staticTextMonthlyAllowance = wx.StaticText(id=wxID_BUDGETSTATICTEXTMONTHLYALLOWANCE,
              label='Monthly Allowance', name='staticTextMonthlyAllowance',
              parent=self.panel1, pos=wx.Point(71, 240), size=wx.Size(90, 13),
              style=0)

        self.staticTextIncomes = wx.StaticText(id=wxID_BUDGETSTATICTEXTINCOMES,
              label='Incomes', name='staticTextIncomes', parent=self.panel1,
              pos=wx.Point(384, 24), size=wx.Size(41, 13), style=0)

        self.staticTextSetAside = wx.StaticText(id=wxID_BUDGETSTATICTEXTSETASIDE,
              label='Set aside to pay bills', name='staticTextSetAside',
              parent=self.panel1, pos=wx.Point(226, 184), size=wx.Size(99, 13),
              style=0)

        self.staticTextSaveAmount = wx.StaticText(id=wxID_BUDGETSTATICTEXTSAVEAMOUNT,
              label='Put in savings', name='staticTextSaveAmount',
              parent=self.panel1, pos=wx.Point(377, 184), size=wx.Size(67, 13),
              style=0)

        self.staticTextLeftOver = wx.StaticText(id=wxID_BUDGETSTATICTEXTLEFTOVER,
              label='Left over for spending', name='staticTextLeftOver',
              parent=self.panel1, pos=wx.Point(494, 184), size=wx.Size(108, 13),
              style=0)

        self.staticTextMonthlySavings = wx.StaticText(id=wxID_BUDGETSTATICTEXTMONTHLYSAVINGS,
              label='Monthly Savings', name='staticTextMonthlySavings',
              parent=self.panel1, pos=wx.Point(74, 76), size=wx.Size(79, 16),
              style=0)

        self.staticTextDebtToIncomeRatio = wx.StaticText(id=wxID_BUDGETSTATICTEXTDEBTTOINCOMERATIO,
              label='Savings Percentage', name='staticTextDebtToIncomeRatio',
              parent=self.panel1, pos=wx.Point(67, 24), size=wx.Size(96, 13),
              style=0)

        self.buttonTransactions = wx.Button(id=wxID_BUDGETBUTTONTRANSACTIONS,
              label='Transactions', name='buttonTransactions',
              parent=self.panel1, pos=wx.Point(432, 368), size=wx.Size(85, 48),
              style=0)
        self.buttonTransactions.SetToolTipString('Takes you to the Transactions window')
        self.buttonTransactions.Bind(wx.EVT_BUTTON,
              self.OnButtonTransactionsButton,
              id=wxID_BUDGETBUTTONTRANSACTIONS)

        self.staticTextWherePutMoney = wx.StaticText(id=wxID_BUDGETSTATICTEXTWHEREPUTMONEY,
              label='Where to put your money on payday:',
              name='staticTextWherePutMoney', parent=self.panel1,
              pos=wx.Point(286, 152), size=wx.Size(250, 18), style=0)
        self.staticTextWherePutMoney.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, 'Tahoma'))
        self.staticTextWherePutMoney.SetToolTipString('Click on an income in the Incomes list to see suggestions')

    def __init__(self, parent):
        self._init_ctrls(parent)
        init.load()
        self.user = init.userList[0]
        self.b = self.user.s._budget
        if self.b.run_first_time: wx.MessageBox(self.b.welcome_message, self.b.welcome_title, wx.OK | wx.CENTRE) 
        self.b.run_first_time = False
        self.b.run_count += 1
        init.save()
        self.textCtrlDebtToIncomeRatio.WriteText(str(self.user.b.save_percent(self.user)*100)+'%')
        self.textCtrlMonthlySavings.WriteText('$'+str(self.user.b.monthly_savings(self.user)))
        self.pos_neg_amount_forecolor(self.user.b.monthly_savings(self.user), self.textCtrlMonthlySavings)
        self.textCtrlDailyAllowance.WriteText('$'+str(self.user.b.daily_allowance(self.user)))
        self.pos_neg_amount_forecolor(self.user.b.daily_allowance(self.user), self.textCtrlDailyAllowance)
        self.textCtrlWeeklyAllowance.WriteText('$'+str(self.user.b.weekly_allowance(self.user)))
        self.pos_neg_amount_forecolor(self.user.b.weekly_allowance(self.user), self.textCtrlWeeklyAllowance)
        self.textCtrlMonthlyAllowance.WriteText('$'+str(self.user.b.monthly_allowance(self.user)))
        self.pos_neg_amount_forecolor(self.user.b.monthly_allowance(self.user), self.textCtrlMonthlyAllowance)
        self.listBoxIncomes.InsertItems([i.name for i in self.user.incomeList],0)
        self.listBoxIncomes.SetStringSelection(self.user.get_primary_income().name)
        self.textCtrlPayBills.WriteText('$'+str(self.user.b.set_aside(self.user, self.user.incomeList[self.listBoxIncomes.GetSelection()])))
        self.textCtrlSavings.WriteText('$'+str(self.user.b.save_amount(self.user, self.user.incomeList[self.listBoxIncomes.GetSelection()])))
        self.textCtrlSpending.WriteText('$'+str(self.user.b.left_after_save_amount(self.user, self.user.incomeList[self.listBoxIncomes.GetSelection()])))
        self.choicePayBills.Append('')
        for a in self.user.accountList: 
            if a != self.user.account_paid_into: self.choicePayBills.Append(a.name)
        self.choiceSavings.Append('')
        for a in self.user.accountList: 
            if a != self.user.account_paid_into: self.choiceSavings.Append(a.name)
        self.choiceSpending.Append('')
        for a in self.user.accountList: 
            if a != self.user.account_paid_into: self.choiceSpending.Append(a.name)        
        if len(self.user.accountList) < 2: 
            self.choicePayBills.Enabled = False
            self.choiceSavings.Enabled = False
            self.choiceSpending.Enabled = False
            self.buttonRecordTransfers.Enabled = False
        if self.user.expenseList == [] or self.user.incomeList == []: self.buttonExpensesDue.Enabled = False
        self.start_time = time.time()
        
    def OnBudgetIdle(self, event):
        init.window_timeout(self, self.start_time)
        
    def OnPanel1Motion(self, event):
        self.start_time = time.time()

    def OnListBoxIncomesListbox(self, event):
        self.textCtrlPayBills.Clear()
        self.textCtrlSavings.Clear()
        self.textCtrlSpending.Clear()
        self.textCtrlPayBills.WriteText('$'+str(self.user.b.set_aside(self.user, self.user.incomeList[self.listBoxIncomes.GetSelection()])))
        self.textCtrlSavings.WriteText('$'+str(self.user.b.save_amount(self.user, self.user.incomeList[self.listBoxIncomes.GetSelection()])))
        self.textCtrlSpending.WriteText('$'+str(self.user.b.left_after_save_amount(self.user, self.user.incomeList[self.listBoxIncomes.GetSelection()])))
        
    def OnButtonRecordTransfersButton(self, event):
        pay_bills = 0.0
        pay_bills_before_message = ''
        pay_bills_after_message = ''
        savings = 0.0
        savings_before_message = ''
        savings_after_message = ''
        spending = 0.0   
        spending_before_message = ''     
        spending_after_message = ''     
        from_account = self.user.account_paid_into
        pay_bills_to_account = None
        savings_to_account = None
        spending_to_account = None
        if self.choicePayBills.GetSelection() != -1:
            pay_bills = float(self.textCtrlPayBills.GetValue()[1:])
            for a in self.user.accountList:
                if a.name == self.choicePayBills.GetStringSelection(): pay_bills_to_account = a
            pay_bills_trans_from = CBudgetP.transaction('account transfer', pay_bills*-1, datetime.now(), 'budgeted amount', 'to '+pay_bills_to_account.name, 'transfer debit')            
            pay_bills_trans_to = CBudgetP.transaction('account transfer', pay_bills, datetime.now(), 'budgeted amount', 'from '+from_account.name, 'transfer credit')      
            pay_bills_before_message = '$'+str(pay_bills)+ ' will be transferred from '+from_account.name+' to '+pay_bills_to_account.name+':'
            pay_bills_after_message = '$'+str(pay_bills)+ ' was transferred from '+from_account.name+' to '+pay_bills_to_account.name+':'
        if self.choiceSavings.GetSelection() != -1:
            savings = float(self.textCtrlSavings.GetValue()[1:])
            for a in self.user.accountList:
                if a.name == self.choiceSavings.GetStringSelection(): savings_to_account = a
            savings_trans_from = CBudgetP.transaction('account transfer', savings*-1, datetime.now(), 'budgeted amount', 'to '+savings_to_account.name, 'transfer debit')            
            savings_trans_to = CBudgetP.transaction('account transfer', savings, datetime.now(), 'budgeted amount', 'from '+from_account.name, 'transfer credit')            
            savings_before_message = '$'+str(savings)+ ' will be transferred from '+from_account.name+' to '+savings_to_account.name+':'
            savings_after_message = '$'+str(savings)+ ' was transferred from '+from_account.name+' to '+savings_to_account.name+':'
        if self.choiceSpending.GetSelection() != -1:
            spending = float(self.textCtrlSpending.GetValue()[1:])
            for a in self.user.accountList:
                if a.name == self.choiceSpending.GetStringSelection(): spending_to_account = a
            spending_trans_from = CBudgetP.transaction('account transfer', spending*-1, datetime.now(), 'budgeted amount', 'to '+spending_to_account.name, 'transfer debit')            
            spending_trans_to = CBudgetP.transaction('account transfer', spending, datetime.now(), 'budgeted amount', 'from '+from_account.name, 'transfer credit')
            spending_before_message = '$'+str(spending)+ ' will be transferred from '+from_account.name+' to '+spending_to_account.name+':'
            spending_after_message = '$'+str(spending)+ ' was transferred from '+from_account.name+' to '+spending_to_account.name+':'
        if self.choicePayBills.GetSelection() == -1 and self.choiceSavings.GetSelection() == -1 and self.choiceSpending.GetSelection() == -1:
            wx.MessageBox('You have not selected any accounts to record funds transfers to. You must select at least one account', 'No accounts selected', wx.OK | wx.CENTRE)
        if pay_bills_before_message != '' or savings_before_message != '' or spending_before_message != '': 
            first_result = wx.MessageBox('You are about to record the following transfers: \n\n{0}\n{1}\n{2}\n\nIs this correct?'.format(pay_bills_before_message, savings_before_message, spending_before_message), 'Record transfers?', wx.YES_NO | wx.CENTRE)
            if first_result == wx.YES:
                if pay_bills_to_account and pay_bills_trans_from.amount != 0: from_account.r.add_transaction(self.user, pay_bills_trans_from, from_account)                
                if savings_to_account and savings_trans_from.amount != 0: from_account.r.add_transaction(self.user, savings_trans_from, from_account)
                if spending_to_account and spending_trans_from.amount != 0: from_account.r.add_transaction(self.user, spending_trans_from, from_account)
                for a in self.user.accountList:
                    if a.name == self.choicePayBills.GetStringSelection(): 
                        try: pay_bills_to_account.r.add_transaction(self.user, pay_bills_trans_to, pay_bills_to_account) 
                        except Exception as message: print message
                    if a.name == self.choiceSavings.GetStringSelection(): 
                        try: savings_to_account.r.add_transaction(self.user, savings_trans_to, savings_to_account) 
                        except Exception as message: print message  
                    if a.name == self.choiceSpending.GetStringSelection():
                        try: spending_to_account.r.add_transaction(self.user, spending_trans_to, spending_to_account)   
                        except Exception as message: print message
                init.save()                
                second_result = wx.MessageBox('You have recorded the following transfers: \n\n{0}\n{1}\n{2}\n\nNow that you have transferred funds, would you like to go to the Expenses Due window ' \
                                'to see if there are any bills that need to be paid?'.format(pay_bills_after_message, savings_after_message, spending_after_message), 'Transfers recorded', wx.YES_NO | wx.CENTRE)            
                if second_result == wx.YES: self.OnButtonExpensesDueButton(event)
                self.choicePayBills.SetSelection(-1)
                self.choiceSavings.SetSelection(-1)
                self.choiceSpending.SetSelection(-1)
            else: wx.MessageBox('Make sure you have selected the correct accounts for funds transfers to be recorded', 'Make corrections', wx.OK | wx.CENTRE)            
            
    def OnChoicePayBillsChoice(self, event):
        if self.choicePayBills.GetStringSelection() == '': self.choicePayBills.SetSelection(-1)

    def OnChoiceSavingsChoice(self, event):
        if self.choiceSavings.GetStringSelection() == '': self.choiceSavings.SetSelection(-1)

    def OnChoiceSpendingChoice(self, event):
        if self.choiceSpending.GetStringSelection() == '': self.choiceSpending.SetSelection(-1)
        
    def OnBitmapButtonCalculatorButton(self, event):
        os.startfile('calc.exe')
        
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
        if self.b.run_count <= 10: init.delete_install_folder()
        self.Close()      
        init.end_process()

