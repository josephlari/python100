#Este es solo un programa de prueba para hacer la integracion de Git y Github

import wx

class MyFrame(wx.Frame):
    def __init__(self,parent,title):
        super(MyFrame, self).__init__(parent,title=title)



class MyApp(wx.App):
    def OnInit(self):
        self.frame=MyFrame(parent=None, title="Creo que aqui va el titulo")
        self.frame.Show()

        return True

app=MyApp()
app.MainLoop()


