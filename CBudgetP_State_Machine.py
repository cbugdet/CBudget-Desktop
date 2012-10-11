from CBudgetP import *
init.load()
user=init.userList[0]
import CBudgetP_Home
import CBudgetP_Accounts
import CBudgetP_Incomes
import CBudgetP_Credits
import CBudgetP_Expenses
import CBudgetP_SavingsItems
import CBudgetP_Budget
import CBudgetP_ExpensesDue
import CBudgetP_Transactions
import os
import wx
import time
import threading
window = None

class state_machine():
	file_state = {'CHANGED': False}
	mtime1 = None # First users.cbd modified file time
	mtime2 = None # Second users.cbd modified file time
	time1 = time.time() # Initial timestamp before run loop starts
	time2 = None
	clock_pulse = 5
	module_map = {
				  'CBudgetP_Home': CBudgetP_Home,
				  'CBudgetP_Accounts': CBudgetP_Accounts,
				  'CBudgetP_Incomes': CBudgetP_Incomes,
				  'CBudgetP_Credits': CBudgetP_Credits,
				  'CBudgetP_Expenses': CBudgetP_Expenses,
				  'CBudgetP_SavingsItems': CBudgetP_SavingsItems,
				  'CBudgetP_Budget': CBudgetP_Budget,
				  'CBudgetP_ExpensesDue': CBudgetP_ExpensesDue,
				  'CBudgetP_Transactions': CBudgetP_Transactions,
				 }
	frame = None
			
	def run(self):
		self.mtime1 = os.path.getmtime(init.savedir+init.savefile)
		while True:
			print '\nrunning...\n'
			threading._sleep(self.clock_pulse)
			self.time2 = time.time()
			self.mtime2 = os.path.getmtime(init.savedir+init.savefile)
			if self.mtime1 != self.mtime2: 
				self.file_state['CHANGED'] = True
				self.mtime1 = os.path.getmtime(init.savedir+init.savefile)
				self.mtime2 = os.path.getmtime(init.savedir+init.savefile)
			else: self.file_state['CHANGED'] = False
			if self.time2 - self.time1 >= 10 and self.mtime1 == self.mtime2:
				user.states['IDLE'] = True
				self.handle_idle_state()
			if len(user.ed.expenses_due(user)) > 0: self.handle_expenses_due_state()
			if self.file_state['CHANGED']: self.refresh_data_from_file()
			
	def refresh_data_from_file(self):
		print '\nrefreshing data...\n'
		try:
			if self.file_state['CHANGED']: 
				init.load()
				user = init.userList[0]
		except EOFError as message: print message
		
	def handle_idle_state(self):
		print '\nhandling idle state...\n'
		if user.states['IDLE'] == True: 
			print '\nuser is idle...'
			#init.end_process()
			message_app = wx.App(0)
			wx.MessageBox('You have been logged out due to inactivity. To continue with CBudget, log back in.', 'User idle', wx.OK | wx.CENTRE | wx.ICON_WARNING) 
			user.s.switch_windows(user.s.active_window, CBudgetP_Home)
			
	def handle_got_paid_state(self):
		print '\nhandling got paid state...\n'
		if user.states['GOT_PAID'] == 'ask':
			i = init.userList[0].get_primary_income()
			if i.state == 'not_paid': 
				result = wx.MessageBox('Is today your payday? If so, would you like to go to Incomes and record your income payment. To do that, click \"Yes\" below.', 'Is is payday?', wx.YES_NO | wx.CENTRE)
				if result == wx.YES: switch_windows(CBudgetP_Home, CBudgetP_Incomes)
				user.states['GOT_PAID'] = False
			if i.state == 'paid': user.states['GOT_PAID'] = True
			
	def handle_expenses_due_state(self):
		print '\nhandling expenses due state...\n'
		if user.states['EXPENSES_DUE'] == 'ask': 
			if len(user.ed.expenses_due(user)) > 0:
				print 'Show some cool expenses due message box'
				user.states['EXPENSES_DUE'] = True
			else: 
				print 'No expenses are due at this time'
				user.states['EXPENSES_DUE'] = False
		


def main(module):
	app = wx.App(0)
	frame = module.create(None)
	frame.Show()
	app.MainLoop()
	
def start_main_thread():
	sm = state_machine()
	thread = threading.Thread(target=sm.run)
	thread.start()	
	return thread

if __name__ == '__main__':
	thread=start_main_thread()
	main(CBudgetP_Home)
else: sm=state_machine()