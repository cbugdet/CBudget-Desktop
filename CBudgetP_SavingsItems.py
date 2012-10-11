#Boa:Frame:SavingsItems

import wx
import time
from datetime import datetime
import CBudgetP
init = CBudgetP.initialize()
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
    return SavingsItems(parent)

[wxID_SAVINGSITEMS, wxID_SAVINGSITEMSBUTTONACCOUNTS, 
 wxID_SAVINGSITEMSBUTTONADDSAVINGSITEM, wxID_SAVINGSITEMSBUTTONADDTOEXPENSES, 
 wxID_SAVINGSITEMSBUTTONBUDGET, wxID_SAVINGSITEMSBUTTONCLOSE, 
 wxID_SAVINGSITEMSBUTTONCREDITS, wxID_SAVINGSITEMSBUTTONEDITSAVINGSITEM, 
 wxID_SAVINGSITEMSBUTTONEXPENSES, wxID_SAVINGSITEMSBUTTONEXPENSESDUE, 
 wxID_SAVINGSITEMSBUTTONHOME, wxID_SAVINGSITEMSBUTTONINCOMES, 
 wxID_SAVINGSITEMSBUTTONREMOVESAVINGSITEM, 
 wxID_SAVINGSITEMSBUTTONTRANSACTIONS, wxID_SAVINGSITEMSDATEPICKERCTRLDUEDATE, 
 wxID_SAVINGSITEMSLISTBOXSAVINGSITEMS, wxID_SAVINGSITEMSPANEL1, 
 wxID_SAVINGSITEMSSTATICTEXTAMOUNT, wxID_SAVINGSITEMSSTATICTEXTDATE, 
 wxID_SAVINGSITEMSSTATICTEXTSAVINGSITEMNAME, wxID_SAVINGSITEMSTEXTCTRLAMOUNT, 
 wxID_SAVINGSITEMSTEXTCTRLSAVINGSITEMNAME, 
] = [wx.NewId() for _init_ctrls in range(22)]

class SavingsItems(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_SAVINGSITEMS, name='SavingsItems',
              parent=prnt, pos=wx.Point(393, 127), size=wx.Size(580, 473),
              style=wx.CAPTION, title='Savings Items')
        self.SetClientSize(wx.Size(564, 435))
        self.Center(wx.BOTH)
        self.Bind(wx.EVT_IDLE, self.OnSavingsItemsIdle)

        self.panel1 = wx.Panel(id=wxID_SAVINGSITEMSPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(564, 435),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetToolTipString('Savings Items Window')
        self.panel1.Bind(wx.EVT_MOTION, self.OnPanel1Motion)

        self.listBoxSavingsItems = wx.ListBox(choices=[],
              id=wxID_SAVINGSITEMSLISTBOXSAVINGSITEMS,
              name='listBoxSavingsItems', parent=self.panel1, pos=wx.Point(48,
              24), size=wx.Size(352, 144), style=0)
        self.listBoxSavingsItems.SetToolTipString('Savings Items List - You can add as many savings items here as you want. Just start by going to the Savings Items Name box and enter a savings items name. Click Add Savings Item if you need help')
        self.listBoxSavingsItems.Bind(wx.EVT_LISTBOX,
              self.OnListBoxSavingsItemsListbox,
              id=wxID_SAVINGSITEMSLISTBOXSAVINGSITEMS)

        self.textCtrlSavingsItemName = wx.TextCtrl(id=wxID_SAVINGSITEMSTEXTCTRLSAVINGSITEMNAME,
              name='textCtrlSavingsItemName', parent=self.panel1,
              pos=wx.Point(404, 39), size=wx.Size(108, 21), style=wx.TE_CENTER,
              value='')
        self.textCtrlSavingsItemName.SetToolTipString('Enter the savings item name')
        self.textCtrlSavingsItemName.Bind(wx.EVT_KILL_FOCUS,
              self.OnTextCtrlSavingsItemNameKillFocus)

        self.textCtrlAmount = wx.TextCtrl(id=wxID_SAVINGSITEMSTEXTCTRLAMOUNT,
              name='textCtrlAmount', parent=self.panel1, pos=wx.Point(128, 184),
              size=wx.Size(328, 21), style=wx.TE_CENTER, value='')
        self.textCtrlAmount.SetToolTipString('Enter the savings item amount here. This amount is used to calculate how much you need to save each paycheck if the item is added to your regualar expenses. The amount be changed at any time')

        self.datePickerCtrlDueDate = wx.DatePickerCtrl(id=wxID_SAVINGSITEMSDATEPICKERCTRLDUEDATE,
              name='datePickerCtrlDueDate', parent=self.panel1,
              pos=wx.Point(128, 216), size=wx.Size(328, 21),
              style=wx.DP_SHOWCENTURY)
        self.datePickerCtrlDueDate.SetToolTipString('Select the date by which you would like to have the money saved for this item. This is your target date and will determine how much you need to save each paycheck to meet the goal if this item is added to your regualar expenses. The date can be changed at any time')

        self.buttonAddSavingsItem = wx.Button(id=wxID_SAVINGSITEMSBUTTONADDSAVINGSITEM,
              label='Add Savings Item', name='buttonAddSavingsItem',
              parent=self.panel1, pos=wx.Point(404, 64), size=wx.Size(110, 23),
              style=0)
        self.buttonAddSavingsItem.Enable(True)
        self.buttonAddSavingsItem.SetToolTipString('Add a savings item to the list')
        self.buttonAddSavingsItem.Bind(wx.EVT_BUTTON,
              self.OnButtonAddSavingsItemButton,
              id=wxID_SAVINGSITEMSBUTTONADDSAVINGSITEM)

        self.buttonRemoveSavingsItem = wx.Button(id=wxID_SAVINGSITEMSBUTTONREMOVESAVINGSITEM,
              label='Remove Savings Item', name='buttonRemoveSavingsItem',
              parent=self.panel1, pos=wx.Point(404, 92), size=wx.Size(110, 23),
              style=0)
        self.buttonRemoveSavingsItem.Enable(False)
        self.buttonRemoveSavingsItem.SetToolTipString('Remove the selected savings item from the list')
        self.buttonRemoveSavingsItem.Bind(wx.EVT_BUTTON,
              self.OnButtonRemoveSavingsItemButton,
              id=wxID_SAVINGSITEMSBUTTONREMOVESAVINGSITEM)

        self.buttonEditSavingsItem = wx.Button(id=wxID_SAVINGSITEMSBUTTONEDITSAVINGSITEM,
              label='Edit Savings Item', name='buttonEditSavingsItem',
              parent=self.panel1, pos=wx.Point(404, 120), size=wx.Size(110, 23),
              style=0)
        self.buttonEditSavingsItem.Enable(False)
        self.buttonEditSavingsItem.SetToolTipString('Change values for the selected savings item')
        self.buttonEditSavingsItem.Bind(wx.EVT_BUTTON,
              self.OnButtonEditSavingsItemButton,
              id=wxID_SAVINGSITEMSBUTTONEDITSAVINGSITEM)

        self.buttonAddToExpenses = wx.Button(id=wxID_SAVINGSITEMSBUTTONADDTOEXPENSES,
              label='Add to Expenses', name='buttonAddToExpenses',
              parent=self.panel1, pos=wx.Point(404, 148), size=wx.Size(110, 23),
              style=0)
        self.buttonAddToExpenses.Enable(False)
        self.buttonAddToExpenses.SetToolTipString('Clicking this button will add the selected savings item to your expense list as a regular expense. The new expense amount will be the savings item amount divided by how many paychecks there are between now and the target date.')
        self.buttonAddToExpenses.Bind(wx.EVT_BUTTON,
              self.OnButtonAddToExpensesButton,
              id=wxID_SAVINGSITEMSBUTTONADDTOEXPENSES)

        self.buttonHome = wx.Button(id=wxID_SAVINGSITEMSBUTTONHOME,
              label='Home', name='buttonHome', parent=self.panel1,
              pos=wx.Point(90, 256), size=wx.Size(85, 48), style=0)
        self.buttonHome.SetToolTipString('Takes you back to the Home window. If you press this button you will have to enter your password again.')
        self.buttonHome.Bind(wx.EVT_BUTTON, self.OnButtonHomeButton,
              id=wxID_SAVINGSITEMSBUTTONHOME)

        self.buttonAccounts = wx.Button(id=wxID_SAVINGSITEMSBUTTONACCOUNTS,
              label='Accounts', name='buttonAccounts', parent=self.panel1,
              pos=wx.Point(190, 256), size=wx.Size(85, 48), style=0)
        self.buttonAccounts.SetToolTipString('Takes you to the Accounts window')
        self.buttonAccounts.Bind(wx.EVT_BUTTON, self.OnButtonAccountsButton,
              id=wxID_SAVINGSITEMSBUTTONACCOUNTS)

        self.buttonIncomes = wx.Button(id=wxID_SAVINGSITEMSBUTTONINCOMES,
              label='Incomes', name='buttonIncomes', parent=self.panel1,
              pos=wx.Point(290, 256), size=wx.Size(85, 48), style=0)
        self.buttonIncomes.SetToolTipString('Takes you to the Incomes window')
        self.buttonIncomes.Bind(wx.EVT_BUTTON, self.OnButtonIncomesButton,
              id=wxID_SAVINGSITEMSBUTTONINCOMES)

        self.buttonCredits = wx.Button(id=wxID_SAVINGSITEMSBUTTONCREDITS,
              label='Credits', name='buttonCredits', parent=self.panel1,
              pos=wx.Point(392, 256), size=wx.Size(85, 48), style=0)
        self.buttonCredits.SetToolTipString('Takes you to the Credits window')
        self.buttonCredits.Bind(wx.EVT_BUTTON, self.OnButtonCreditsButton,
              id=wxID_SAVINGSITEMSBUTTONCREDITS)

        self.buttonExpenses = wx.Button(id=wxID_SAVINGSITEMSBUTTONEXPENSES,
              label='Expenses', name='buttonExpenses', parent=self.panel1,
              pos=wx.Point(90, 320), size=wx.Size(85, 48), style=0)
        self.buttonExpenses.SetToolTipString('Takes you to the Expenses window')
        self.buttonExpenses.Bind(wx.EVT_BUTTON, self.OnButtonExpensesButton,
              id=wxID_SAVINGSITEMSBUTTONEXPENSES)

        self.buttonBudget = wx.Button(id=wxID_SAVINGSITEMSBUTTONBUDGET,
              label='Budget', name='buttonBudget', parent=self.panel1,
              pos=wx.Point(192, 320), size=wx.Size(85, 48), style=0)
        self.buttonBudget.SetToolTipString('Takes you to the Budget window')
        self.buttonBudget.Bind(wx.EVT_BUTTON, self.OnButtonBudgetButton,
              id=wxID_SAVINGSITEMSBUTTONBUDGET)

        self.buttonExpensesDue = wx.Button(id=wxID_SAVINGSITEMSBUTTONEXPENSESDUE,
              label='Expenses Due', name='buttonExpensesDue',
              parent=self.panel1, pos=wx.Point(290, 320), size=wx.Size(85, 48),
              style=0)
        self.buttonExpensesDue.SetToolTipString('Takes you to the Expenses Due window')
        self.buttonExpensesDue.Bind(wx.EVT_BUTTON,
              self.OnButtonExpensesDueButton,
              id=wxID_SAVINGSITEMSBUTTONEXPENSESDUE)

        self.buttonTransactions = wx.Button(id=wxID_SAVINGSITEMSBUTTONTRANSACTIONS,
              label='Transactions', name='buttonTransactions',
              parent=self.panel1, pos=wx.Point(392, 320), size=wx.Size(85, 48),
              style=0)
        self.buttonTransactions.SetToolTipString('Takes you to the Transactions window')
        self.buttonTransactions.Bind(wx.EVT_BUTTON,
              self.OnButtonTransactionsButton,
              id=wxID_SAVINGSITEMSBUTTONTRANSACTIONS)

        self.buttonClose = wx.Button(id=wxID_SAVINGSITEMSBUTTONCLOSE,
              label='Close', name='buttonClose', parent=self.panel1,
              pos=wx.Point(244, 392), size=wx.Size(75, 23), style=0)
        self.buttonClose.SetToolTipString('See you next time!')
        self.buttonClose.Bind(wx.EVT_BUTTON, self.OnButtonCloseButton,
              id=wxID_SAVINGSITEMSBUTTONCLOSE)

        self.staticTextDate = wx.StaticText(id=wxID_SAVINGSITEMSSTATICTEXTDATE,
              label='Target Date:', name='staticTextDate', parent=self.panel1,
              pos=wx.Point(60, 220), size=wx.Size(63, 13), style=0)

        self.staticTextSavingsItemName = wx.StaticText(id=wxID_SAVINGSITEMSSTATICTEXTSAVINGSITEMNAME,
              label='Savings Item Name', name='staticTextSavingsItemName',
              parent=self.panel1, pos=wx.Point(413, 24), size=wx.Size(93, 13),
              style=0)

        self.staticTextAmount = wx.StaticText(id=wxID_SAVINGSITEMSSTATICTEXTAMOUNT,
              label='Amount:', name='staticTextAmount', parent=self.panel1,
              pos=wx.Point(80, 188), size=wx.Size(42, 13), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
        init.load()
        self.user = init.userList[0]
        self.si = self.user.s._savings_items
        self.si.run_count += 1
        self.add_savings_item_message = 'Start by entering the name of your first savings item in the box below where it says \"Savings Item Name\" on the top right. ' \
                           'Then go to the box that says \"Amount\" and enter the savings item amount. After that, select the date you want to have this item saved ' \
                           'by. When you\'re all done, click \"Add Savings Item\" and the new savings item will be added to the list. Click \"Add Savings Item\" again if you need help.'
        self.message_count = 0
        if self.si.run_first_time: wx.MessageBox(self.si.welcome_message, self.si.welcome_title, wx.OK | wx.CENTRE)  
        self.listBoxSavingsItems.InsertItems([s.name for s in self.user.savingsItemList],0)   
        if self.user.expenseList == [] or self.user.incomeList == []: 
            self.buttonExpensesDue.Enabled = False       
            self.buttonBudget.Enabled = False
        self.start_time = time.time()
            
    def OnSavingsItemsIdle(self, event):
        if self.si.run_first_time and self.message_count < 1: 
            wx.MessageBox(self.add_savings_item_message, 'To add a savings item', wx.OK | wx.CENTRE) 
            self.set_backcolor_green(self.textCtrlSavingsItemName) 
            self.message_count += 1
        init.window_timeout(self, self.start_time)
        
    def OnPanel1Motion(self, event):
        self.start_time = time.time()
            
    def OnTextCtrlSavingsItemNameKillFocus(self, event):
        self.set_backcolor_white([self.textCtrlSavingsItemName])

    def OnListBoxSavingsItemsListbox(self, event):
        self.textCtrlSavingsItemName.Clear()
        self.textCtrlSavingsItemName.WriteText(str(self.user.savingsItemList[self.listBoxSavingsItems.GetSelection()].name))        
        self.textCtrlAmount.Clear()
        self.textCtrlAmount.WriteText('$'+str(round(self.user.savingsItemList[self.listBoxSavingsItems.GetSelection()].amount, 2)))
        if self.textCtrlSavingsItemName != '' and self.textCtrlAmount.GetValue() != '' and self.textCtrlSavingsItemName.GetValue() != '': self.buttonAddSavingsItem.Enabled = True
        self.buttonRemoveSavingsItem.Enabled = True
        self.buttonEditSavingsItem.Enabled = True
        self.buttonAddToExpenses.Enabled = True
        date = self.user.savingsItemList[self.listBoxSavingsItems.GetSelection()].date
        self.datePickerCtrlDueDate.SetValue(wx.DateTimeFromDMY(date.day,date.month-1,date.year))

    def OnButtonAddSavingsItemButton(self, event): 
        dt = self.datePickerCtrlDueDate.GetValue()
        date = datetime(dt.Year,dt.Month+1,dt.Day)
        if self.textCtrlSavingsItemName.GetValue() == '' and self.textCtrlAmount.GetValue() == '' and date.date() == datetime.today().date(): 
            wx.MessageBox(self.add_savings_item_message, 'To add a savings item', wx.OK | wx.CENTRE)
            self.set_backcolor_green(self.textCtrlSavingsItemName)
        elif self.textCtrlSavingsItemName.GetValue() == '' and self.textCtrlAmount.GetValue() == '': 
            wx.MessageBox('In order to add a savings item, it has to have a name. You can enter that below where it says \"Savings Item Name\".', 'Savings item has no name', wx.OK | wx.CENTRE)
            self.set_backcolor_red(self.textCtrlSavingsItemName)
        elif self.textCtrlSavingsItemName.GetValue() == '' and self.textCtrlAmount.GetValue() != '':
            wx.MessageBox('In order to add a savings item, it has to have a name. You can enter that below where it says \"Savings Item Name\".', 'Savings item has no name', wx.OK | wx.CENTRE)
            self.set_backcolor_red(self.textCtrlSavingsItemName)            
            self.set_backcolor_white([self.textCtrlAmount])
        elif self.textCtrlSavingsItemName.GetValue() != '' and self.textCtrlAmount.GetValue() == '':
            wx.MessageBox('In order to add a savings item, it has to have an amount. You can enter that next to where it says \"Amount\".', 'Savings item has no amount', wx.OK | wx.CENTRE)
            self.set_backcolor_red(self.textCtrlAmount)            
            self.set_backcolor_white([self.textCtrlSavingsItemName])
        elif self.textCtrlSavingsItemName.GetValue() != '' and self.textCtrlAmount.GetValue() != '' and date.date() == datetime.today().date(): 
            wx.MessageBox('In order to add a savings item, it has to have a target date other than today. You can change it next to where it says \"Target Date\".', 'Savings item has no target date', wx.OK | wx.CENTRE)
            self.set_backcolor_red(self.staticTextDate)
            self.set_backcolor_red(self.datePickerCtrlDueDate)
            self.set_backcolor_white([self.textCtrlSavingsItemName, self.textCtrlAmount])
        elif self.textCtrlSavingsItemName.GetValue() != '' and self.textCtrlAmount.GetValue() != '' and date.date() < datetime.today().date(): 
            wx.MessageBox('In order to add a savings item, it has to have a target date that is not in the past. You can change it next to where it says \"Target Date\".', 'Savings item has a target date in the past', wx.OK | wx.CENTRE)
            self.set_backcolor_red(self.staticTextDate)
            self.set_backcolor_white([self.textCtrlSavingsItemName, self.textCtrlAmount])
        else:
            self.set_backcolor_white([self.textCtrlSavingsItemName, self.textCtrlAmount])
            self.set_backcolor_grey(self.staticTextDate)
            if self.textCtrlSavingsItemName.GetValue() not in self.listBoxSavingsItems.GetStrings(): 
                amount = 0.0
                try: 
                    if '$' in self.textCtrlAmount.GetValue(): amount = float(self.textCtrlAmount.GetValue()[1:])
                    else: amount = float(self.textCtrlAmount.GetValue())       
                    self.user.addSavingsItem(self.textCtrlSavingsItemName.GetValue(),float(self.textCtrlAmount.GetValue()),date)
                    self.si.run_first_time = False
                    init.save()
                    self.set_backcolor_white([self.textCtrlAmount])
                    self.listBoxSavingsItems.Clear()
                    self.listBoxSavingsItems.InsertItems([s.name for s in self.user.savingsItemList],0)
                    self.textCtrlSavingsItemName.Clear()
                    self.textCtrlAmount.Clear()
                    self.listBoxSavingsItems.SetSelection(len(self.user.savingsItemList)-1)                    
                    self.textCtrlSavingsItemName.SetFocus()
                    result = wx.MessageBox('The savings item \"{0}\" has been to your savings item list. Would you like to add this savings item to your expense list?'.format(self.listBoxSavingsItems.GetStringSelection()), 'Add item to expenses?', wx.YES_NO | wx.CENTRE)
                    if result == wx.YES: self.OnButtonAddToExpensesButton(event)
                except ValueError: 
                    wx.MessageBox('The amount you are entering has to be a number and can\'t be blank. You\'ve probably entered some letters, symbols, or a word. Make sure it\'s a number.', 'Amount is not a number', wx.OK | wx.CENTRE)                                               
                    self.set_backcolor_red(self.textCtrlAmount)
            else: 
                wx.MessageBox('Sorry, you can\'t add a savings item with that name. It\'s already in the list. To add another savings item, you\'ll need to change the name.', 'Duplicate savings item', wx.OK | wx.CENTRE)                    
                self.set_backcolor_red(self.textCtrlSavingsItemName)

    def OnButtonRemoveSavingsItemButton(self, event):
        result = wx.MessageBox('You are about to remove the savings item: {0}. Is this what you really want to do?'.format(self.user.savingsItemList[self.listBoxSavingsItems.GetSelection()].name), 'Remove savings item?', wx.YES_NO | wx.CENTRE)
        if result == wx.YES:
            self.user.removeSavingsItem(self.user.savingsItemList[self.listBoxSavingsItems.GetSelection()])
            init.save()
            self.listBoxSavingsItems.Clear()
            self.listBoxSavingsItems.InsertItems([s.name for s in self.user.savingsItemList],0)
            self.textCtrlSavingsItemName.Clear()
            self.textCtrlAmount.Clear()        
            self.buttonRemoveSavingsItem.Enabled = False
            self.buttonEditSavingsItem.Enabled = False
            self.buttonAddToExpenses.Enabled = False
        
    def OnButtonEditSavingsItemButton(self, event):
        if self.textCtrlSavingsItemName.GetValue() != '': self.user.savingsItemList[self.listBoxSavingsItems.GetSelection()].name = self.textCtrlSavingsItemName.GetValue()
        amount = 0.0
        try: 
            if '$' in self.textCtrlAmount.GetValue(): amount = float(self.textCtrlAmount.GetValue()[1:])
            else: amount = float(self.textCtrlAmount.GetValue())
            self.user.savingsItemList[self.listBoxSavingsItems.GetSelection()].amount = amount
        except ValueError: wx.MessageBox('The amount you are entering has to be a number. You\'ve probably entered some letters, symbols, or a word. Make sure it\'s a number.', 'Amount is not a number', wx.OK | wx.CENTRE)
        dt = self.datePickerCtrlDueDate.GetValue()
        date = datetime(dt.Year,dt.Month+1,dt.Day)        
        self.user.savingsItemList[self.listBoxSavingsItems.GetSelection()].date = date
        init.save()
        self.buttonRemoveSavingsItem.Enabled = False
        self.buttonEditSavingsItem.Enabled = False
        self.buttonAddToExpenses.Enabled = False
        init.load()
        self.listBoxSavingsItems.Clear()
        self.listBoxSavingsItems.InsertItems([s.name for s in self.user.savingsItemList],0)

    def OnButtonAddToExpensesButton(self, event):        
        if self.user.incomeList != []: 
            success_fail = self.user.savingsItemList[self.listBoxSavingsItems.GetSelection()].add_to_expenseList(self.user)
            dt = self.datePickerCtrlDueDate.GetValue()
            date = datetime(dt.Year,dt.Month+1,dt.Day)
            if date > datetime.now():
                if success_fail == 'success':
                    self.user.s.savings_item_added = True
                    init.save()        
                    wx.MessageBox('{0} has been added as a new expense to your expense list'.format(self.listBoxSavingsItems.GetStringSelection()), 'Savings item added', wx.OK | wx.CENTRE)
                    self.OnButtonExpensesButton(event)
                    self.buttonRemoveSavingsItem.Enabled = False
                    self.buttonEditSavingsItem.Enabled = False
                    self.buttonAddToExpenses.Enabled = False
            else: wx.MessageBox('The date you selected is either today or a date in the past. This will not work to calculate a new expense. Please select a future date', 'Use a future date!', wx.OK | wx.CENTRE)
        else: 
            wx.MessageBox('You have no incomes yet. In order to add this savings item to your expense list, you must have at least one income', 'No incomes', wx.OK | wx.CENTRE)
            self.Hide()
            self.OnButtonIncomesButton(event)      
            
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
        
    def OnButtonExpensesButton(self, event):
        self.Hide()
        self.Close()
        self.main = CBudgetP_Expenses.create(None)
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
        if self.si.run_count <= 10: init.delete_install_folder()
        self.Close()
        init.end_process()
