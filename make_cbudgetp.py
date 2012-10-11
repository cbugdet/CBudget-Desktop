from os import system, environ, walk, path, makedirs, rename, remove, startfile, path
from shutil import rmtree, copytree, copy, make_archive
import zipfile
import win32com.client


while True:
	try:
		r = raw_input('Production or Archive? (p or a)')
		if r == 'p' or r == 'P':
			system('taskkill /F /IM pythonw.exe')
			system('taskkill /F /IM cbudgetp_app.exe')
			if path.exists(environ['USERPROFILE']+'\\desktop\\CBudget'): rmtree(environ['USERPROFILE']+'\\desktop\\cbudget', True)
			if path.exists(environ['USERPROFILE']+'\\desktop\\cbudget.zip'): remove(environ['USERPROFILE']+'\\desktop\\cbudget.zip')
			if path.exists(environ['USERPROFILE']+'\\desktop\\cbudget.exe'): remove(environ['USERPROFILE']+'\\desktop\\cbudget.exe')
			rmtree('build', True)
			rmtree('dist', True)
			rmtree('app', True)
			system('\"d:\python27\setup.py py2exe\"')
			rename('dist', 'app')
			# system('python setup.py bdist --formats=wininst')
			rmtree('build', True)
			rmtree('dist', True)
			rmtree('install', True)
			system('\"d:\python27\setup_install.py py2exe\"')
			rename('dist', 'install')
			copytree('d:\\python27\\app', environ['USERPROFILE']+'\\desktop\\CBudget\\app')
			copytree('d:\\python27\\install', environ['USERPROFILE']+'\\desktop\\CBudget\\install')
			shell = win32com.client.Dispatch('WScript.Shell')
			shortcut = shell.CreateShortCut('c:\\users\\cary\\desktop\\cbudget\\Install.lnk')
			shortcut.Targetpath = 'c:\\users\\cary\\desktop\\cbudget\\install\\install_cbudget.exe'
			shortcut.save()
			make_archive('c:\\users\\cary\\desktop\\CBudget', 'zip', 'c:\\users\\cary\\desktop\\CBudget')
			#if path.exists(environ['USERPROFILE']+'\\desktop\\CBudget'): rmtree(environ['USERPROFILE']+'\\desktop\\cbudget', True)
			startfile('D:\\Program Files (x86)\\NSIS\\Bin\\zip2exe.exe')
			print '\n\nDone!\n\n'

		elif r == 'a' or r == 'A':
			system('taskkill /F /IM pythonw.exe')
			system('taskkill /F /IM cbudgetp_app.exe')
			if path.exists(environ['USERPROFILE']+'\\desktop\\CBudget_Archive'): rmtree(environ['USERPROFILE']+'\\desktop\\cbudget_archive', True)
			if path.exists(environ['USERPROFILE']+'\\desktop\\cbudget_archive.zip'): remove(environ['USERPROFILE']+'\\desktop\\cbudget_archive.zip')
			if not path.exists(environ['USERPROFILE']+'\\desktop\\CBudget_Archive'): makedirs(environ['USERPROFILE']+'\\desktop\\CBudget_Archive')
			copy('C:\\Users\\Cary\\Documents\\GitHub\\CBudget-Desktop\\cbudgetp.py', environ['USERPROFILE']+'\\desktop\\CBudget_Archive')
			copy('C:\\Users\\Cary\\Documents\\GitHub\\CBudget-Desktop\\cbudgetp_accounts.py', environ['USERPROFILE']+'\\desktop\\CBudget_Archive')
			copy('C:\\Users\\Cary\\Documents\\GitHub\\CBudget-Desktop\\cbudgetp_app.py', environ['USERPROFILE']+'\\desktop\\CBudget_Archive')
			copy('C:\\Users\\Cary\\Documents\\GitHub\\CBudget-Desktop\\cbudgetp_budget.py', environ['USERPROFILE']+'\\desktop\\CBudget_Archive')
			copy('C:\\Users\\Cary\\Documents\\GitHub\\CBudget-Desktop\\cbudgetp_console.py', environ['USERPROFILE']+'\\desktop\\CBudget_Archive')
			copy('C:\\Users\\Cary\\Documents\\GitHub\\CBudget-Desktop\\cbudgetp_credits.py', environ['USERPROFILE']+'\\desktop\\CBudget_Archive')
			copy('C:\\Users\\Cary\\Documents\\GitHub\\CBudget-Desktop\\cbudgetp_expenses.py', environ['USERPROFILE']+'\\desktop\\CBudget_Archive')
			copy('C:\\Users\\Cary\\Documents\\GitHub\\CBudget-Desktop\\cbudgetp_expensesdue.py', environ['USERPROFILE']+'\\desktop\\CBudget_Archive')
			copy('C:\\Users\\Cary\\Documents\\GitHub\\CBudget-Desktop\\cbudgetp_home.py', environ['USERPROFILE']+'\\desktop\\CBudget_Archive')
			copy('C:\\Users\\Cary\\Documents\\GitHub\\CBudget-Desktop\\cbudgetp_incomes.py', environ['USERPROFILE']+'\\desktop\\CBudget_Archive')
			copy('C:\\Users\\Cary\\Documents\\GitHub\\CBudget-Desktop\\cbudgetp_savingsitems.py', environ['USERPROFILE']+'\\desktop\\CBudget_Archive')
			copy('C:\\Users\\Cary\\Documents\\GitHub\\CBudget-Desktop\\cbudgetp_transactions.py', environ['USERPROFILE']+'\\desktop\\CBudget_Archive')
			if path.exists(environ['USERPROFILE']+'\\desktop\\Finance\\users.cbp'): f = open(environ['USERPROFILE']+'\\desktop\\Finance\\users.cbp', 'r')
			if path.exists(environ['APPDATA']+'\\CBudget\\users.cbp'): 
				c = open(environ['APPDATA']+'\\CBudget\\users.cbp', 'r')
				if c and f: 
					if c > f: 
						temp = c.read()
						copy(environ['APPDATA']+'\\CBudget\\users.cbp', environ['USERPROFILE']+'\\desktop\\CBudget_Archive\\users.cbp')	
						if 'Cary' in temp: copy(environ['APPDATA']+'\\CBudget\\users.cbp', environ['USERPROFILE']+'\\desktop\\Finance\\users.cbp')	
					if f > c: copy(environ['USERPROFILE']+'\\desktop\\Finance\\users.cbp', environ['USERPROFILE']+'\\desktop\\CBudget_Archive\\users.cbp')	
			else: copy(environ['USERPROFILE']+'\\desktop\\Finance\\users.cbp', environ['USERPROFILE']+'\\desktop\\CBudget_Archive\\users.cbp')	
			make_archive('c:\\users\\cary\\desktop\\CBudget_Archive', 'zip', 'c:\\users\\cary\\desktop\\CBudget_Archive')	
			if path.exists(environ['USERPROFILE']+'\\desktop\\cbudget_archive'): rmtree(environ['USERPROFILE']+'\\desktop\\cbudget_archive', True)	
			print '\n\nDone!\n\n'
		else: break
	except Exception as message: print '\n',str(message.__class__)+':',str(message),'\n'