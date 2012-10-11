#Boa:Frame:Credits

import wx
import time
from datetime import datetime
import CBudgetP
init = CBudgetP.initialize()
import CBudgetP_Home
import CBudgetP_Accounts
import CBudgetP_Incomes
import CBudgetP_Expenses
import CBudgetP_SavingsItems
import CBudgetP_Budget
import CBudgetP_ExpensesDue
import CBudgetP_Transactions

def create(parent):
    return Credits(parent)

[wxID_CREDITS, wxID_CREDITSBUTTONACCOUNTS, wxID_CREDITSBUTTONADDCREDIT, 
 wxID_CREDITSBUTTONADDTOINCOMES, wxID_CREDITSBUTTONBUDGET, 
 wxID_CREDITSBUTTONCHANGECREDIT, wxID_CREDITSBUTTONCLOSE, 
 wxID_CREDITSBUTTONEXPENSES, wxID_CREDITSBUTTONEXPENSESDUE, 
 wxID_CREDITSBUTTONHOME, wxID_CREDITSBUTTONINCOMES, 
 wxID_CREDITSBUTTONREMOVECREDIT, wxID_CREDITSBUTTONSAVINGSITEMS, 
 wxID_CREDITSBUTTONTRANSACTIONS, wxID_CREDITSCHOICESELECTACCOUNT, 
 wxID_CREDITSLISTBOXCREDITS, wxID_CREDITSPANEL1, wxID_CREDITSSTATICTEXTAMOUNT, 
 wxID_CREDITSSTATICTEXTCONF, wxID_CREDITSSTATICTEXTCREDITNAME, 
 wxID_CREDITSSTATICTEXTNOTE, wxID_CREDITSSTATICTEXTSELECTACCOUNT, 
 wxID_CREDITSTEXTCTRLAMOUNT, wxID_CREDITSTEXTCTRLCONF, 
 wxID_CREDITSTEXTCTRLCREDITNAME, wxID_CREDITSTEXTCTRLNOTE, 
] = [wx.NewId() for _init_ctrls in range(26)]

class Credits(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_CREDITS, name='Credits', parent=prnt,
              pos=wx.Point(392, 137), size=wx.Size(582, 453), style=wx.CAPTION,
              title='Credits')
        self.SetClientSize(wx.Size(566, 415))
        self.Center(wx.BOTH)
        self.Bind(wx.EVT_IDLE, self.OnCreditsIdle)

        self.panel1 = wx.Panel(id=wxID_CREDITSPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(566, 415),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetToolTipString('Credits Window')
        self.panel1.Bind(wx.EVT_MOTION, self.OnPanel1Motion)

        self.listBoxCredits = wx.ListBox(choices=[],
              id=wxID_CREDITSLISTBOXCREDITS, name='listBoxCredits',
              parent=self.panel1, pos=wx.Point(48, 24), size=wx.Size(352, 128),
              style=0)
        self.listBoxCredits.SetToolTipString('Credit List - You can add as many credits here as you want. Just start by going to the Credit Name box and enter a credit name. Click Add Credit if you need help')
        self.listBoxCredits.SetStringSelection('')
        self.listBoxCredits.Bind(wx.EVT_LISTBOX, self.OnListBoxCreditsListbox,
              id=wxID_CREDITSLISTBOXCREDITS)

        self.textCtrlCreditName = wx.TextCtrl(id=wxID_CREDITSTEXTCTRLCREDITNAME,
              name='textCtrlCreditName', parent=self.panel1, pos=wx.Point(404,
              39), size=wx.Size(108, 21), style=wx.TE_CENTER, value='')
        self.textCtrlCreditName.SetToolTipString('Enter the credit name here')
        self.textCtrlCreditName.Bind(wx.EVT_KILL_FOCUS,
              self.OnTextCtrlCreditNameKillFocus)

        self.textCtrlAmount = wx.TextCtrl(id=wxID_CREDITSTEXTCTRLAMOUNT,
              name='textCtrlAmount', parent=self.panel1, pos=wx.Point(96, 160),
              size=wx.Size(152, 21), style=wx.TE_CENTER, value='')
        self.textCtrlAmount.SetToolTipString('Enter the credit amount here')

        self.textCtrlConf = wx.TextCtrl(id=wxID_CREDITSTEXTCTRLCONF,
              name='textCtrlConf', parent=self.panel1, pos=wx.Point(80, 216),
              size=wx.Size(184, 21), style=wx.TE_CENTER, value='')
        self.textCtrlConf.SetToolTipString('If there is a confirmation number associated with this payment, enter it here before clicking the Add Credit button')

        self.textCtrlNote = wx.TextCtrl(id=wxID_CREDITSTEXTCTRLNOTE,
              name='textCtrlNote', parent=self.panel1, pos=wx.Point(296, 216),
              size=wx.Size(180, 21), style=wx.TE_CENTER, value='')
        self.textCtrlNote.SetToolTipString('If there is a note or memo you would like to record along with this payment, enter it here before clicking the Add Credit button')

        self.choiceSelectAccount = wx.Choice(choices=[],
              id=wxID_CREDITSCHOICESELECTACCOUNT, name='choiceSelectAccount',
              parent=self.panel1, pos=wx.Point(264, 160), size=wx.Size(130, 21),
              style=0)
        self.choiceSelectAccount.Bind(wx.EVT_CHOICE,
              self.OnChoiceSelectAccountChoice,
              id=wxID_CREDITSCHOICESELECTACCOUNT)

        self.buttonAddCredit = wx.Button(id=wxID_CREDITSBUTTONADDCREDIT,
              label='Add Credit', name='buttonAddCredit', parent=self.panel1,
              pos=wx.Point(404, 64), size=wx.Size(110, 23), style=0)
        self.buttonAddCredit.Enable(True)
        self.buttonAddCredit.SetToolTipString('Add a credit to the list')
        self.buttonAddCredit.Bind(wx.EVT_BUTTON, self.OnButtonAddCreditButton,
              id=wxID_CREDITSBUTTONADDCREDIT)

        self.buttonRemoveCredit = wx.Button(id=wxID_CREDITSBUTTONREMOVECREDIT,
              label='Remove Credit', name='buttonRemoveCredit',
              parent=self.panel1, pos=wx.Point(404, 96), size=wx.Size(110, 23),
              style=0)
        self.buttonRemoveCredit.Enable(False)
        self.buttonRemoveCredit.SetToolTipString('Remove the selected credit from the list')
        self.buttonRemoveCredit.Bind(wx.EVT_BUTTON,
              self.OnButtonRemoveCreditButton,
              id=wxID_CREDITSBUTTONREMOVECREDIT)

        self.buttonChangeCredit = wx.Button(id=wxID_CREDITSBUTTONCHANGECREDIT,
              label='Change Credit', name='buttonChangeCredit',
              parent=self.panel1, pos=wx.Point(404, 128), size=wx.Size(110, 23),
              style=0)
        self.buttonChangeCredit.Enable(False)
        self.buttonChangeCredit.SetToolTipString('Change values for the selected credit')
        self.buttonChangeCredit.Bind(wx.EVT_BUTTON,
              self.OnButtonChangeCreditButton,
              id=wxID_CREDITSBUTTONCHANGECREDIT)

        self.buttonAddToIncomes = wx.Button(id=wxID_CREDITSBUTTONADDTOINCOMES,
              label='Add to Incomes', name='buttonAddToIncomes',
              parent=self.panel1, pos=wx.Point(404, 158), size=wx.Size(110, 23),
              style=0)
        self.buttonAddToIncomes.Enable(False)
        self.buttonAddToIncomes.SetToolTipString('Add the selected credit to your income list as a regular income. Each credit in the list with the same name as the selected one will be used to get an average amount and pay interval for the new income')
        self.buttonAddToIncomes.Bind(wx.EVT_BUTTON,
              self.OnButtonAddToIncomesButton,
              id=wxID_CREDITSBUTTONADDTOINCOMES)

        self.buttonHome = wx.Button(id=wxID_CREDITSBUTTONHOME, label='Home',
              name='buttonHome', parent=self.panel1, pos=wx.Point(80, 256),
              size=wx.Size(85, 48), style=0)
        self.buttonHome.SetToolTipString('Takes you back to the Home window. If you press this button you will have ')
        self.buttonHome.Bind(wx.EVT_BUTTON, self.OnButtonHomeButton,
              id=wxID_CREDITSBUTTONHOME)

        self.buttonAccounts = wx.Button(id=wxID_CREDITSBUTTONACCOUNTS,
              label='Accounts', name='buttonAccounts', parent=self.panel1,
              pos=wx.Point(184, 256), size=wx.Size(85, 48), style=0)
        self.buttonAccounts.SetToolTipString('Takes you to the Accounts window')
        self.buttonAccounts.Bind(wx.EVT_BUTTON, self.OnButtonAccountsButton,
              id=wxID_CREDITSBUTTONACCOUNTS)

        self.buttonIncomes = wx.Button(id=wxID_CREDITSBUTTONINCOMES,
              label='Incomes', name='buttonIncomes', parent=self.panel1,
              pos=wx.Point(288, 256), size=wx.Size(85, 48), style=0)
        self.buttonIncomes.SetToolTipString('Takes you to the Income window')
        self.buttonIncomes.Bind(wx.EVT_BUTTON, self.OnButtonIncomesButton,
              id=wxID_CREDITSBUTTONINCOMES)

        self.buttonExpenses = wx.Button(id=wxID_CREDITSBUTTONEXPENSES,
              label='Expenses', name='buttonExpenses', parent=self.panel1,
              pos=wx.Point(390, 256), size=wx.Size(85, 48), style=0)
        self.buttonExpenses.SetToolTipString('Takes you to the Expenses window')
        self.buttonExpenses.Bind(wx.EVT_BUTTON, self.OnButtonExpensesButton,
              id=wxID_CREDITSBUTTONEXPENSES)

        self.buttonSavingsItems = wx.Button(id=wxID_CREDITSBUTTONSAVINGSITEMS,
              label='Savings Items', name='buttonSavingsItems',
              parent=self.panel1, pos=wx.Point(80, 312), size=wx.Size(85, 48),
              style=0)
        self.buttonSavingsItems.SetToolTipString('Takes you to the Savings Items window')
        self.buttonSavingsItems.Bind(wx.EVT_BUTTON,
              self.OnButtonSavingsItemsButton,
              id=wxID_CREDITSBUTTONSAVINGSITEMS)

        self.buttonBudget = wx.Button(id=wxID_CREDITSBUTTONBUDGET,
              label='Budget', name='buttonBudget', parent=self.panel1,
              pos=wx.Point(184, 312), size=wx.Size(85, 48), style=0)
        self.buttonBudget.SetToolTipString('Takes you to the Budget window')
        self.buttonBudget.Bind(wx.EVT_BUTTON, self.OnButtonBudgetButton,
              id=wxID_CREDITSBUTTONBUDGET)

        self.buttonExpensesDue = wx.Button(id=wxID_CREDITSBUTTONEXPENSESDUE,
              label='Expenses Due', name='buttonExpensesDue',
              parent=self.panel1, pos=wx.Point(288, 312), size=wx.Size(85, 48),
              style=0)
        self.buttonExpensesDue.SetToolTipString('Takes you to the Expenses Due window')
        self.buttonExpensesDue.Bind(wx.EVT_BUTTON,
              self.OnButtonExpensesDueButton, id=wxID_CREDITSBUTTONEXPENSESDUE)

        self.buttonTransactions = wx.Button(id=wxID_CREDITSBUTTONTRANSACTIONS,
              label='Transactions', name='buttonTransactions',
              parent=self.panel1, pos=wx.Point(390, 312), size=wx.Size(85, 48),
              style=0)
        self.buttonTransactions.SetToolTipString('Takes you to the Transactions window')
        self.buttonTransactions.Bind(wx.EVT_BUTTON,
              self.OnButtonTransactionsButton,
              id=wxID_CREDITSBUTTONTRANSACTIONS)

        self.buttonClose = wx.Button(id=wxID_CREDITSBUTTONCLOSE, label='Close',
              name='buttonClose', parent=self.panel1, pos=wx.Point(244, 376),
              size=wx.Size(75, 23), style=0)
        self.buttonClose.SetToolTipString('See you next time!')
        self.buttonClose.Bind(wx.EVT_BUTTON, self.OnButtonCloseButton,
              id=wxID_CREDITSBUTTONCLOSE)

        self.staticTextCreditName = wx.StaticText(id=wxID_CREDITSSTATICTEXTCREDITNAME,
              label='Credit Name', name='staticTextCreditName',
              parent=self.panel1, pos=wx.Point(429, 24), size=wx.Size(60, 13),
              style=0)

        self.staticTextAmount = wx.StaticText(id=wxID_CREDITSSTATICTEXTAMOUNT,
              label='Amount:', name='staticTextAmount', parent=self.panel1,
              pos=wx.Point(48, 164), size=wx.Size(42, 13), style=0)

        self.staticTextConf = wx.StaticText(id=wxID_CREDITSSTATICTEXTCONF,
              label='Confirmation #', name='staticTextConf', parent=self.panel1,
              pos=wx.Point(136, 200), size=wx.Size(73, 13), style=0)

        self.staticTextNote = wx.StaticText(id=wxID_CREDITSSTATICTEXTNOTE,
              label='Note/Memo', name='staticTextNote', parent=self.panel1,
              pos=wx.Point(360, 200), size=wx.Size(56, 13), style=0)

        self.staticTextSelectAccount = wx.StaticText(id=wxID_CREDITSSTATICTEXTSELECTACCOUNT,
              label='Account To Receive Credit', name='staticTextSelectAccount',
              parent=self.panel1, pos=wx.Point(266, 184), size=wx.Size(128, 13),
              style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
        init.load()
        self.user = init.userList[0]
        self.account = self.user.get_current_account()        
        self.c = self.user.s._credits
        self.c.run_count += 1
        init.userList[0].s.active_frame = str(self)._formatter_field_name_split()[0][1:]
        init.save()
        self.add_credit_message = 'Start by entering the name of your first credit in the box below where it says \"Credit Name\" on the top right. ' \
                           'Then go to the box that says \"Amount\" and enter the credit amount. After that, if there is one, you can enter a ' \
                           'confirmation number in the box where it says \"Confirmation #\", or if you have a note or memo you want to attach ' \
                           'to this credit, you can enter it in the box where it says \"Note/Memo\". When you\'re all done, click \"Add Credit\" ' \
                           'and the new credit will be added to the list. Click \"Add Credit\" again if you need help.'
        self.message_count = 0
        if self.c.run_first_time: wx.MessageBox(self.c.welcome_message, self.c.welcome_title, wx.OK | wx.CENTRE)  
        self.listBoxCredits.InsertItems([c.name for c in self.user.creditList],0) 
        for a in self.user.accountList: self.choiceSelectAccount.Append(a.name)
        for i in range(len(self.user.accountList)):
            if self.user.accountList[i].name == self.account.name:
                self.choiceSelectAccount.SetSelection(i)  
        if self.user.expenseList == [] or self.user.incomeList == []: 
            self.buttonExpensesDue.Enabled = False       
            self.buttonBudget.Enabled = False
        self.start_time = time.time()
            
    def OnCreditsIdle(self, event):
        if self.c.run_first_time and self.message_count < 1: 
            wx.MessageBox(self.add_credit_message, 'To add a credit', wx.OK | wx.CENTRE) 
            self.set_backcolor_green(self.textCtrlCreditName) 
            self.message_count += 1
        init.window_timeout(self, self.start_time)
        
    def OnPanel1Motion(self, event):
        self.start_time = time.time()
            
    def OnTextCtrlCreditNameKillFocus(self, event):
        self.set_backcolor_white([self.textCtrlCreditName])

    def OnListBoxCreditsListbox(self, event):
        self.textCtrlCreditName.Clear()
        self.textCtrlCreditName.WriteText(str(self.user.creditList[self.listBoxCredits.GetSelection()].name))        
        self.textCtrlAmount.Clear()
        self.textCtrlAmount.WriteText('$'+str(self.user.creditList[self.listBoxCredits.GetSelection()].amount))  
        if self.textCtrlCreditName != '' and self.textCtrlAmount.GetValue() != '' and self.textCtrlCreditName.GetValue() != '': self.buttonAddCredit.Enabled = True
        self.buttonRemoveCredit.Enabled = True
        self.buttonChangeCredit.Enabled = True
        self.buttonAddToIncomes.Enabled = True        

    def OnButtonAddCreditButton(self, event): 
        if self.textCtrlCreditName.GetValue() == '' and self.textCtrlAmount.GetValue() == '': 
            wx.MessageBox(self.add_credit_message, 'To add an credit', wx.OK | wx.CENTRE)
            self.set_backcolor_green(self.textCtrlCreditName)
        elif self.textCtrlCreditName.GetValue() == '' and self.textCtrlAmount.GetValue() == '': 
            wx.MessageBox('In order to add a credit, it has to have a name. You can enter that below where it says \"Credit Name\".', 'Credit has no name', wx.OK | wx.CENTRE)
            self.set_backcolor_red(self.textCtrlCreditName)
        elif self.textCtrlCreditName.GetValue() == '' and self.textCtrlAmount.GetValue() != '': 
            wx.MessageBox('In order to add a credit, it has to have a name. You can enter that below where it says \"Credit Name\".', 'Credit has no name', wx.OK | wx.CENTRE)
            self.set_backcolor_red(self.textCtrlCreditName)            
            self.set_backcolor_white([self.textCtrlAmount])
        elif self.textCtrlCreditName.GetValue() != '' and self.textCtrlAmount.GetValue() == '':
            wx.MessageBox('In order to add a credit, it has to have an amount. You can enter that below where it says \"Amount\".', 'Credit has no amount', wx.OK | wx.CENTRE)
            self.set_backcolor_red(self.textCtrlAmount)            
            self.set_backcolor_white([self.textCtrlCreditName])
        else:
            self.set_backcolor_white([self.textCtrlCreditName, self.textCtrlAmount])
            amount = 0.0
            try: 
                if '$' in self.textCtrlAmount.GetValue(): amount = float(self.textCtrlAmount.GetValue()[1:])
                else: amount = float(self.textCtrlAmount.GetValue())                                    
                result = wx.MessageBox('These funds will be shown as being credited to your {0} account. Is this correct?'.format(self.user.get_current_account().name), 'Correct account?', wx.YES_NO | wx.CENTRE)
                if result == wx.YES:   
                    trans = CBudgetP.transaction(self.textCtrlCreditName.GetValue(), amount, datetime.now(), self.textCtrlConf.GetValue(), self.textCtrlNote.GetValue(), 'credit')
                    self.user.addCredit(trans.name, trans.amount, trans.date, trans.conf, trans.note)
                    self.c.run_first_time = False                
                    self.user.get_current_account().r.add_transaction(self.user, trans, self.user.get_current_account())
                    init.save()
                    wx.MessageBox('The credit \"{0}\" has been to your credits list.'.format(trans.name), 'Credit added', wx.OK | wx.CENTRE)                    
                    self.set_backcolor_white([self.textCtrlAmount])
                    self.listBoxCredits.Clear()
                    self.listBoxCredits.InsertItems([c.name for c in self.user.creditList],0)
                    self.buttonAddCredit.Enabled = False
                    self.textCtrlCreditName.Clear()
                    self.textCtrlAmount.Clear()  
                    self.textCtrlCreditName.SetFocus()
                else: 
                    wx.MessageBox('Please use Select Account to change the current account to the account you want these funds to be shown as credited to', 'Change account', wx.OK | wx.CENTRE)        
                    self.set_backcolor_red(self.staticTextSelectAccount) 
            except ValueError: 
                wx.MessageBox('The amount you are entering has to be a number and can\'t be blank. You\'ve probably entered some letters, symbols, or a word. Make sure it\'s a number.', 'Amount is not a number', wx.OK | wx.CENTRE)                                               
                self.set_backcolor_red(self.textCtrlAmount)    

    def OnButtonRemoveCreditButton(self, event):
        result = wx.MessageBox('You are about to remove the credit: {0}. Is this what you really want to do?'.format(self.user.creditList[self.listBoxCredits.GetSelection()].name), 'Remove credit?', wx.YES_NO | wx.CENTRE)
        if result == wx.YES:
            self.user.removeCredit(self.user.creditList[self.listBoxCredits.GetSelection()])
            init.save()
            self.listBoxCredits.Clear()
            self.listBoxCredits.InsertItems([c.name for c in self.user.creditList],0)
            self.textCtrlCreditName.Clear()
            self.textCtrlAmount.Clear()        
            self.buttonAddCredit.Enabled = False
            self.buttonRemoveCredit.Enabled = False
            self.buttonChangeCredit.Enabled = False
            self.buttonAddToIncomes.Enabled = False
        
    def OnButtonChangeCreditButton(self, event):
        if self.textCtrlCreditName.GetValue() != '': self.user.creditList[self.listBoxCredits.GetSelection()].name = self.textCtrlCreditName.GetValue()
        amount = 0.0
        try: 
            if '$' in self.textCtrlAmount.GetValue(): amount = float(self.textCtrlAmount.GetValue()[1:])
            else: amount = float(self.textCtrlAmount.GetValue())
            self.user.CreditList[self.listBoxCredits.GetSelection()].amount = amount
        except ValueError: wx.MessageBox('The amount you are entering has to be a number. You\'ve probably entered some letters, symbols, or a word. Make sure it\'s a number.', 'Amount is not a number', wx.OK | wx.CENTRE)
        if self.textCtrlConf.GetValue() != '': self.user.creditList[self.listBoxCredits.GetSelection()].conf = self.textCtrlConf.GetValue()
        if self.textCtrlNote.GetValue() != '': self.user.creditList[self.listBoxCredits.GetSelection()].note = self.textCtrlNote.GetValue()
        init.save()
        self.buttonAddCredit.Enabled = False
        self.buttonRemoveCredit.Enabled = False
        self.buttonChangeCredit.Enabled = False
        self.buttonAddToIncomes.Enabled = False
        init.load()
        self.listBoxCredits.Clear()
        self.listBoxCredits.InsertItems([c.name for c in self.user.creditList],0)

    def OnButtonAddToIncomesButton(self, event): 
        success__fail = None
        c = CBudgetP.credit(self.user.creditList[self.listBoxCredits.GetSelection()].name, self.user.creditList[self.listBoxCredits.GetSelection()].amount, self.user.creditList[self.listBoxCredits.GetSelection()].date, self.user.creditList[self.listBoxCredits.GetSelection()].conf, self.user.creditList[self.listBoxCredits.GetSelection()].note)
        success_fail = self.user.creditList[self.listBoxCredits.GetSelection()].add_to_incomeList(self.user, c)
        if success_fail == 'success': 
            self.user.s.credit_added = True            
            init.save()            
            wx.MessageBox('{0} has been added as a new income to your income list'.format(self.listBoxCredits.GetStringSelection()), 'Credit added', wx.OK | wx.CENTRE)
            self.OnButtonIncomesButton(event)
        if success_fail == 'fail': wx.MessageBox('You can only add a credit to the income list if you have 3 or more credits with the same name that were not all added on the same day', 'Need more credits!', wx.OK | wx.CENTRE)
        
    def OnChoiceSelectAccountChoice(self, event):
        for a in self.user.accountList:
            if a.name == self.choiceSelectAccount.GetStringSelection(): 
                self.account = a
                self.user.set_current_account(a)
                self.set_backcolor_grey(self.staticTextSelectAccount) 
                
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
        if self.c.run_count <= 10: init.delete_install_folder()
        self.Close()
        init.end_process()

