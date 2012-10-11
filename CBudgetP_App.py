#!/usr/bin/env python
#Boa:App:BoaApp

import wx
import CBudgetP_Home

modules ={'CBudgetP_Home': [1, 'Main frame of Application', 'CBudgetP_Home.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = CBudgetP_Home.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
