#Boa:Frame:ExpensesDue

import wx
import time
import CBudgetP
init = CBudgetP.initialize()
from datetime import datetime
import CBudgetP_Home
import CBudgetP_Accounts
import CBudgetP_Incomes
import CBudgetP_Credits
import CBudgetP_Expenses
import CBudgetP_SavingsItems
import CBudgetP_Budget
import CBudgetP_ExpensesDue
import CBudgetP_Transactions

def create(parent):
    return ExpensesDue(parent)

[wxID_EXPENSESDUE, wxID_EXPENSESDUEBUTTONACCOUNTS, 
 wxID_EXPENSESDUEBUTTONBUDGET, wxID_EXPENSESDUEBUTTONCLOSE, 
 wxID_EXPENSESDUEBUTTONCREDITS, wxID_EXPENSESDUEBUTTONEXPENSES, 
 wxID_EXPENSESDUEBUTTONHOME, wxID_EXPENSESDUEBUTTONINCOMES, 
 wxID_EXPENSESDUEBUTTONRECORDPAYMENT, wxID_EXPENSESDUEBUTTONSAVINGSITEMS, 
 wxID_EXPENSESDUEBUTTONTRANSACTIONS, wxID_EXPENSESDUECHOICESELECTACCOUNT, 
 wxID_EXPENSESDUEDATEPICKERCTRLDUEDATE, wxID_EXPENSESDUELISTBOXEXPENSESDUE, 
 wxID_EXPENSESDUEPANEL1, wxID_EXPENSESDUESTATICTEXT1, 
 wxID_EXPENSESDUESTATICTEXTACCOUNTBALANCE, 
 wxID_EXPENSESDUESTATICTEXTAMOUNTDUE, wxID_EXPENSESDUESTATICTEXTCONF, 
 wxID_EXPENSESDUESTATICTEXTDUEDATE, wxID_EXPENSESDUESTATICTEXTNOTE, 
 wxID_EXPENSESDUESTATICTEXTSELECTACCOUNT, 
 wxID_EXPENSESDUESTATICTEXTTOTALAMOUNTDUE, 
 wxID_EXPENSESDUETEXTCTRLACCOUNTBALANCE, wxID_EXPENSESDUETEXTCTRLAMOUNTDUE, 
 wxID_EXPENSESDUETEXTCTRLCONF, wxID_EXPENSESDUETEXTCTRLNOTE, 
 wxID_EXPENSESDUETEXTCTRLTOTALAMOUNTDUE, 
] = [wx.NewId() for _init_ctrls in range(28)]

class ExpensesDue(wx.Frame):    
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_EXPENSESDUE, name='ExpensesDue',
              parent=prnt, pos=wx.Point(430, 70), size=wx.Size(506, 587),
              style=wx.CAPTION, title='Expenses Due')
        self.SetClientSize(wx.Size(490, 549))
        self.Center(wx.BOTH)
        self.Bind(wx.EVT_IDLE, self.OnExpensesDueIdle)

        self.panel1 = wx.Panel(id=wxID_EXPENSESDUEPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(490, 549),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetToolTipString('Expenses Due Window')
        self.panel1.Bind(wx.EVT_MOTION, self.OnPanel1Motion)

        self.listBoxExpensesDue = wx.ListBox(choices=[],
              id=wxID_EXPENSESDUELISTBOXEXPENSESDUE, name='listBoxExpensesDue',
              parent=self.panel1, pos=wx.Point(72, 40), size=wx.Size(344, 136),
              style=wx.LB_MULTIPLE)
        self.listBoxExpensesDue.SetToolTipString('Show all bills due in the pay cycle for the primary income. You can change the primary income in the Incomes window. You can also select more than one item in this list to see the total amount due for only the selected items. Just select or unselect the items you want in the list by clicking on them. To record a payment for an item, make sure only that item is selected.')
        self.listBoxExpensesDue.Bind(wx.EVT_LISTBOX,
              self.OnListBoxExpensesDueListbox,
              id=wxID_EXPENSESDUELISTBOXEXPENSESDUE)

        self.textCtrlAmountDue = wx.TextCtrl(id=wxID_EXPENSESDUETEXTCTRLAMOUNTDUE,
              name='textCtrlAmountDue', parent=self.panel1, pos=wx.Point(72,
              200), size=wx.Size(160, 21), style=wx.TE_CENTER, value='')
        self.textCtrlAmountDue.SetToolTipString("Shows the amount due for the selected expense. This can be changed to record a different amount when you click the 'Record Payment' button")

        self.datePickerCtrlDueDate = wx.DatePickerCtrl(id=wxID_EXPENSESDUEDATEPICKERCTRLDUEDATE,
              name='datePickerCtrlDueDate', parent=self.panel1,
              pos=wx.Point(264, 200), size=wx.Size(154, 21),
              style=wx.DP_SHOWCENTURY)
        self.datePickerCtrlDueDate.SetToolTipString("Shows the due date for the selected expense. This can be changed to record a payment date other than the due date when you click the 'Record Payment' button")
        self.datePickerCtrlDueDate.SetLabel('')
        self.datePickerCtrlDueDate.SetValue(wx.DateTimeFromDMY(5, 9, 2011, 0, 0,
              0))
        self.datePickerCtrlDueDate.Enable(False)
        self.datePickerCtrlDueDate.SetHelpText('')

        self.textCtrlTotalAmountDue = wx.TextCtrl(id=wxID_EXPENSESDUETEXTCTRLTOTALAMOUNTDUE,
              name='textCtrlTotalAmountDue', parent=self.panel1,
              pos=wx.Point(72, 248), size=wx.Size(160, 21), style=wx.TE_CENTER,
              value='')
        self.textCtrlTotalAmountDue.SetToolTipString('Shows the total amount due for all expenses in the above list. This amount cannot be changed')
        self.textCtrlTotalAmountDue.Enable(False)
        self.textCtrlTotalAmountDue.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL,
              wx.BOLD, False, 'Tahoma'))

        self.textCtrlConf = wx.TextCtrl(id=wxID_EXPENSESDUETEXTCTRLCONF,
              name='textCtrlConf', parent=self.panel1, pos=wx.Point(72, 296),
              size=wx.Size(160, 21), style=wx.TE_CENTER, value='')
        self.textCtrlConf.SetToolTipString("If there is a confirmation number associated with this payment, enter it here before clicking the 'Record Payment' button")

        self.textCtrlNote = wx.TextCtrl(id=wxID_EXPENSESDUETEXTCTRLNOTE,
              name='textCtrlNote', parent=self.panel1, pos=wx.Point(264, 296),
              size=wx.Size(148, 21), style=wx.TE_CENTER, value='')
        self.textCtrlNote.SetToolTipString("If there is a note or memo you would like to record along with this payment, enter it here before clicking the 'Record Payment' button")

        self.buttonRecordPayment = wx.Button(id=wxID_EXPENSESDUEBUTTONRECORDPAYMENT,
              label='Record Payment', name='buttonRecordPayment',
              parent=self.panel1, pos=wx.Point(264, 232), size=wx.Size(152, 39),
              style=0)
        self.buttonRecordPayment.Enable(False)
        self.buttonRecordPayment.SetToolTipString("Click this button after changing the selected expense values (or leave them as they are) to record that you made this payment in your transaction register. Note: clicking this button does not make any payments to a creditor or change a balance in any of your accounts online. It's just for keeping track")
        self.buttonRecordPayment.Bind(wx.EVT_BUTTON,
              self.OnButtonRecordPaymentButton,
              id=wxID_EXPENSESDUEBUTTONRECORDPAYMENT)

        self.choiceSelectAccount = wx.Choice(choices=[],
              id=wxID_EXPENSESDUECHOICESELECTACCOUNT,
              name='choiceSelectAccount', parent=self.panel1, pos=wx.Point(72,
              344), size=wx.Size(160, 21), style=0)
        self.choiceSelectAccount.SetToolTipString(' Using this drop-down box, you can select which account you want to record this payment to. When you first come to Expenses Due window, the account that will be shown is the one selected as current in the Accounts window')
        self.choiceSelectAccount.Bind(wx.EVT_CHOICE,
              self.OnChoiceSelectAccountChoice,
              id=wxID_EXPENSESDUECHOICESELECTACCOUNT)

        self.textCtrlAccountBalance = wx.TextCtrl(id=wxID_EXPENSESDUETEXTCTRLACCOUNTBALANCE,
              name='textCtrlAccountBalance', parent=self.panel1,
              pos=wx.Point(264, 344), size=wx.Size(148, 21), style=wx.TE_CENTER,
              value='')
        self.textCtrlAccountBalance.SetToolTipString('Shows the account balance for the selected account from the drop-down box on the left')

        self.buttonHome = wx.Button(id=wxID_EXPENSESDUEBUTTONHOME, label='Home',
              name='buttonHome', parent=self.panel1, pos=wx.Point(56, 384),
              size=wx.Size(85, 48), style=0)
        self.buttonHome.SetToolTipString('Takes you back to the Home window. If you press this button you will have to enter your password again.')
        self.buttonHome.Bind(wx.EVT_BUTTON, self.OnButtonHomeButton,
              id=wxID_EXPENSESDUEBUTTONHOME)

        self.buttonAccounts = wx.Button(id=wxID_EXPENSESDUEBUTTONACCOUNTS,
              label='Accounts', name='buttonAccounts', parent=self.panel1,
              pos=wx.Point(152, 384), size=wx.Size(85, 48), style=0)
        self.buttonAccounts.SetToolTipString('Takes you to the Accounts window')
        self.buttonAccounts.Bind(wx.EVT_BUTTON, self.OnButtonAccountsButton,
              id=wxID_EXPENSESDUEBUTTONACCOUNTS)

        self.buttonIncomes = wx.Button(id=wxID_EXPENSESDUEBUTTONINCOMES,
              label='Incomes', name='buttonIncomes', parent=self.panel1,
              pos=wx.Point(248, 384), size=wx.Size(85, 48), style=0)
        self.buttonIncomes.SetToolTipString('Takes you to the Incomes window')
        self.buttonIncomes.Bind(wx.EVT_BUTTON, self.OnButtonIncomesButton,
              id=wxID_EXPENSESDUEBUTTONINCOMES)

        self.buttonCredits = wx.Button(id=wxID_EXPENSESDUEBUTTONCREDITS,
              label='Credits', name='buttonCredits', parent=self.panel1,
              pos=wx.Point(344, 384), size=wx.Size(85, 48), style=0)
        self.buttonCredits.SetToolTipString('Takes you to the Credits window')
        self.buttonCredits.Bind(wx.EVT_BUTTON, self.OnButtonCreditsButton,
              id=wxID_EXPENSESDUEBUTTONCREDITS)

        self.buttonExpenses = wx.Button(id=wxID_EXPENSESDUEBUTTONEXPENSES,
              label='Expenses', name='buttonExpenses', parent=self.panel1,
              pos=wx.Point(56, 440), size=wx.Size(85, 48), style=0)
        self.buttonExpenses.SetToolTipString('Takes you to the Expenses window')
        self.buttonExpenses.Bind(wx.EVT_BUTTON, self.OnButtonExpensesButton,
              id=wxID_EXPENSESDUEBUTTONEXPENSES)

        self.buttonSavingsItems = wx.Button(id=wxID_EXPENSESDUEBUTTONSAVINGSITEMS,
              label='Savings Items', name='buttonSavingsItems',
              parent=self.panel1, pos=wx.Point(152, 440), size=wx.Size(85, 48),
              style=0)
        self.buttonSavingsItems.SetToolTipString('Takes you to the Savings Items window')
        self.buttonSavingsItems.Bind(wx.EVT_BUTTON,
              self.OnButtonSavingsItemsButton,
              id=wxID_EXPENSESDUEBUTTONSAVINGSITEMS)

        self.buttonBudget = wx.Button(id=wxID_EXPENSESDUEBUTTONBUDGET,
              label='Budget', name='buttonBudget', parent=self.panel1,
              pos=wx.Point(248, 440), size=wx.Size(85, 48), style=0)
        self.buttonBudget.SetToolTipString('Takes you to the Budget window')
        self.buttonBudget.Bind(wx.EVT_BUTTON, self.OnButtonBudgetButton,
              id=wxID_EXPENSESDUEBUTTONBUDGET)

        self.buttonTransactions = wx.Button(id=wxID_EXPENSESDUEBUTTONTRANSACTIONS,
              label='Transactions', name='buttonTransactions',
              parent=self.panel1, pos=wx.Point(344, 440), size=wx.Size(85, 48),
              style=0)
        self.buttonTransactions.SetToolTipString('Takes you to the Transactions window')
        self.buttonTransactions.Bind(wx.EVT_BUTTON,
              self.OnButtonTransactionsButton,
              id=wxID_EXPENSESDUEBUTTONTRANSACTIONS)

        self.buttonClose = wx.Button(id=wxID_EXPENSESDUEBUTTONCLOSE,
              label='Close', name='buttonClose', parent=self.panel1,
              pos=wx.Point(206, 508), size=wx.Size(75, 23), style=0)
        self.buttonClose.SetToolTipString('See you next time!')
        self.buttonClose.Bind(wx.EVT_BUTTON, self.OnButtonCloseButton,
              id=wxID_EXPENSESDUEBUTTONCLOSE)

        self.staticTextDueDate = wx.StaticText(id=wxID_EXPENSESDUESTATICTEXTDUEDATE,
              label='Due Date', name='staticTextDueDate', parent=self.panel1,
              pos=wx.Point(312, 184), size=wx.Size(46, 13), style=0)

        self.staticTextAmountDue = wx.StaticText(id=wxID_EXPENSESDUESTATICTEXTAMOUNTDUE,
              label='Amount Due', name='staticTextAmountDue',
              parent=self.panel1, pos=wx.Point(128, 184), size=wx.Size(60, 13),
              style=0)

        self.staticTextNote = wx.StaticText(id=wxID_EXPENSESDUESTATICTEXTNOTE,
              label='Note/Memo', name='staticTextNote', parent=self.panel1,
              pos=wx.Point(312, 280), size=wx.Size(56, 13), style=0)

        self.staticTextConf = wx.StaticText(id=wxID_EXPENSESDUESTATICTEXTCONF,
              label='Confirmation #', name='staticTextConf', parent=self.panel1,
              pos=wx.Point(120, 280), size=wx.Size(73, 13), style=0)

        self.staticTextTotalAmountDue = wx.StaticText(id=wxID_EXPENSESDUESTATICTEXTTOTALAMOUNTDUE,
              label='Total Amount Due', name='staticTextTotalAmountDue',
              parent=self.panel1, pos=wx.Point(112, 232), size=wx.Size(87, 13),
              style=0)

        self.staticTextSelectAccount = wx.StaticText(id=wxID_EXPENSESDUESTATICTEXTSELECTACCOUNT,
              label='Account To Pay Bills From:',
              name='staticTextSelectAccount', parent=self.panel1,
              pos=wx.Point(89, 328), size=wx.Size(127, 13), style=0)

        self.staticTextAccountBalance = wx.StaticText(id=wxID_EXPENSESDUESTATICTEXTACCOUNTBALANCE,
              label='Account Balance', name='staticTextAccountBalance',
              parent=self.panel1, pos=wx.Point(304, 328), size=wx.Size(80, 13),
              style=0)

        self.staticText1 = wx.StaticText(id=wxID_EXPENSESDUESTATICTEXT1,
              label='Expenses that are due between now and your next paycheck:',
              name='staticText1', parent=self.panel1, pos=wx.Point(94, 24),
              size=wx.Size(301, 13), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)        
        init.load()
        self.user = init.userList[0]
        self.account = self.user.get_most_frequent_expense_payment_account()
        for a in self.user.accountList: self.choiceSelectAccount.Append(a.name)
        for i in range(len(self.user.accountList)):
            if self.user.accountList[i].name == self.account.name:
                self.choiceSelectAccount.SetSelection(i)
                self.textCtrlAccountBalance.WriteText('$'+str(round(self.account.balance, 2)))
                self.pos_neg_amount_forecolor(round(self.account.balance, 2), self.textCtrlAccountBalance, self.account)
        self.ed = self.user.s._expenses_due
        if self.user.s.show_expenses_due and self.ed.run_first_time: wx.MessageBox(self.ed.welcome_message, self.ed.welcome_title, wx.OK | wx.CENTRE) 
        self.ed.run_first_time = False
        self.ed.run_count += 1
        init.save()
        self.ed_dict = self.user.ed.expenses_due(self.user)
        if self.ed_dict == {} and self.user.s.show_expenses_due: wx.MessageBox('You have no expenses due at this time', 'Nothing is due!', wx.OK | wx.CENTRE)
        else:
            self.listBoxExpensesDue.InsertItems([k for k in
             self.ed_dict.keys()],0)
            self.textCtrlTotalAmountDue.WriteText('$'+str(sum([v[0] for v in self.ed_dict.values()])))
        date = datetime.now().date()
        self.datePickerCtrlDueDate.SetValue(wx.DateTimeFromDMY(date.day,date.month-1,date.year))  
        self.multiple_selections = []
        self.start_time = time.time()
        
    def OnExpensesDueIdle(self, event):
        init.window_timeout(self, self.start_time) 
        
    def OnPanel1Motion(self, event):
        self.start_time = time.time()           
        
    def OnListBoxExpensesDueListbox(self, event):
        self.multiple_selections = []
        selections = [self.listBoxExpensesDue.GetStrings(), range(len(self.listBoxExpensesDue.GetStrings()))]
        temp = [[],[]]
        for i in self.listBoxExpensesDue.GetSelections(): 
            if i in selections[1]: 
                temp[0].append(selections[0][i])
                temp[1].append(selections[1][i])
        selections = temp
        for s in selections[0]: self.multiple_selections.append(self.ed_dict[s])
        if len(self.multiple_selections) == 0: 
            self.buttonRecordPayment.Enabled = False
            self.datePickerCtrlDueDate.Enabled = False
            today = datetime.today()
            self.datePickerCtrlDueDate.SetValue(wx.DateTimeFromDMY(today.day,today.month-1,today.year))  
            self.textCtrlAmountDue.Clear()
        elif len(self.multiple_selections) > 1:            
            self.textCtrlAmountDue.Clear()   
            self.textCtrlTotalAmountDue.Clear()
            self.textCtrlTotalAmountDue.WriteText('$'+str(sum([m[0] for m in self.multiple_selections])))
            self.buttonRecordPayment.Enabled = False
            self.datePickerCtrlDueDate.Enabled = False
        else:
            self.textCtrlAmountDue.Clear()
            self.textCtrlAmountDue.WriteText('$'+str(self.multiple_selections[0][0]))
            if self.ed_dict != {}: 
                date = self.multiple_selections[0][1]
                self.datePickerCtrlDueDate.SetValue(wx.DateTimeFromDMY(date.day,date.month-1,date.year))  
            self.textCtrlTotalAmountDue.Clear()
            self.textCtrlTotalAmountDue.WriteText('$'+str(sum([v[0] for v in self.ed_dict.values()])))
            self.buttonRecordPayment.Enabled = True
            self.datePickerCtrlDueDate.Enabled = True
        
    def OnButtonRecordPaymentButton(self, event):
        amount = 0.0
        try: 
            if '$' in self.textCtrlAmountDue.GetValue(): amount = float(self.textCtrlAmountDue.GetValue()[1:])
            else: amount = float(self.textCtrlAmountDue.GetValue())    
            if self.account.balance >= amount:
                result = wx.MessageBox('This payment will show as deducted from your {0} account. Is this correct?'.format(self.account.name), 'Correct account?', wx.YES_NO | wx.CENTRE)
                if result == wx.YES: 
                    self.record_payment()
                    self.set_backcolor_white([self.textCtrlAmountDue])
                elif result == wx.NO: wx.MessageBox('Please use Select Account to select the account you want this payment to be shown as paid from.', 'Change account', wx.OK | wx.CENTRE)
            else: 
                result = wx.MessageBox('This action will record an overdrawn balance for the account {0}. Do you want to continue?'.format(self.account.name), 'Insufficient funds!', wx.YES_NO | wx.CENTRE)
                if result == wx.YES: 
                    self.record_payment()
                    self.set_backcolor_white([self.textCtrlAmountDue])
        except ValueError: 
            wx.MessageBox('The amount you are entering has to be a number. You\'ve probably entered some letters, symbols, or a word. Make sure it\'s a number.', 'Amount is not a number', wx.OK | wx.CENTRE)
            self.set_backcolor_red(self.textCtrlAmountDue)
            
    def record_payment(self):
        self.multiple_selections = []
        selections = [self.listBoxExpensesDue.GetStrings(), range(len(self.listBoxExpensesDue.GetStrings()))]
        temp = [[],[]]
        for i in self.listBoxExpensesDue.GetSelections(): 
            if i in selections[1]: 
                temp[0].append(selections[0][i])
                temp[1].append(selections[1][i])
        selections = temp
        amount_paid = self.ed_dict[selections[0][0]][0]
        amount = 0.0
        try: 
            if '$' in self.textCtrlAmountDue.GetValue(): amount = float(self.textCtrlAmountDue.GetValue()[1:])
            else: amount = float(self.textCtrlAmountDue.GetValue()) 
##            set_new_amount = None
            for e in self.user.expenseList:
##                if selections[0][0] == e.name''' and not e.partial_paid''':
##                    set_new_amount = wx.MessageBox('Your payment of ${0} has been recorded in {1} account transactions. Select [Yes] to keep ${0} as the new or same payment amount. Select [No] if this is a partial payment and you intend to pay the rest later or if you are catching up on a late payment.'.format(amount, self.account.name), 'Payment recorded', wx.YES_NO | wx.CENTRE)
##                    if set_new_amount == wx.YES: new_amount = True
##                    else: set_new_amount = False
                if selections[0][0] == e.name: wx.MessageBox('Your payment of ${0} has been recorded in {1} account transactions. You can view this payment in the Transactions window'.format(amount, self.account.name), 'Payment recorded', wx.OK | wx.CENTRE)            
            self.user.ed.record_payment(self.user, selections[0][0], amount, datetime.now(), self.textCtrlConf.GetValue(), \
                self.textCtrlNote.GetValue(), self.account)  
            self.user.set_current_account(self.account)
            init.save()     
            self.ed_dict = self.user.ed.expenses_due(self.user)
            self.listBoxExpensesDue.Clear()
            self.listBoxExpensesDue.InsertItems([k for k in self.ed_dict.keys()],0)
            self.textCtrlAmountDue.Clear()            
            self.textCtrlTotalAmountDue.Clear()
            self.textCtrlTotalAmountDue.WriteText(str(sum([v[0] for v in self.ed_dict.values()])))
            date = datetime.min
            self.datePickerCtrlDueDate.SetValue(wx.DateTimeFromDMY(date.day,date.month-1,date.year))
            self.textCtrlAccountBalance.Clear()
            self.textCtrlAccountBalance.WriteText('$'+str(round(self.account.balance, 2)))
            self.pos_neg_amount_forecolor(round(self.account.balance, 2), self.textCtrlAccountBalance, self.account)
            self.textCtrlConf.Clear()
            self.textCtrlNote.Clear()
            self.buttonRecordPayment.Enabled = False
            if self.ed_dict == {}: wx.MessageBox('You have no expenses due at this time', 'Nothing is due!', wx.OK | wx.CENTRE)
        except ValueError: wx.MessageBox('The amount you are entering has to be a number. You\'ve probably entered some letters, symbols, or a word. Make sure it\'s a number.', 'Amount is not a number', wx.OK | wx.CENTRE)            

    def OnChoiceSelectAccountChoice(self, event):
        for a in self.user.accountList:
            if a.name == self.choiceSelectAccount.GetStringSelection(): self.account = a
        self.textCtrlAccountBalance.Clear()
        self.textCtrlAccountBalance.WriteText('$'+str(round(self.account.balance, 2)))
        self.pos_neg_amount_forecolor(round(self.account.balance, 2), self.textCtrlAccountBalance, self.account)
        
    def set_backcolor_red(self, ctrl):
        ctrl.SetBackgroundColour(wx.Colour(255, 128, 128))
        ctrl.Refresh()
        ctrl.SetFocus()
        if 'TextCtrl' in str(ctrl.__str__):
            ctrl.SetSelection(0,-1)
        
    def set_backcolor_white(self, ctrls):
        for c in ctrls:
            c.SetBackgroundColour(wx.Colour(255, 255, 255))
            c.Refresh()
        
    def set_backcolor_grey(self, ctrl):
        ctrl.SetBackgroundColour(wx.Colour(240, 240, 240))
        ctrl.Refresh()   
        
    def pos_neg_amount_forecolor(self, amount, ctrl, account):
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

    def OnButtonTransactionsButton(self, event):
        self.Hide()
        self.Close()
        self.main = CBudgetP_Transactions.create(None)
        self.main.Show()  

    def OnButtonCloseButton(self, event):
        if self.ed.run_count <= 10: init.delete_install_folder()
        self.Close()      
        init.end_process()
