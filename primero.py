#Este es solo un programa de prueba para hacer la integracion de Git y Github

import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title)
        
        # Cargar el ícono desde un archivo .ico en la misma carpeta
        icon = wx.Icon("math.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None, title="MatPlotLib con WsPython")
        self.frame.Show()
        return True

print("Esto es una presentacion limpia")
app = MyApp()
app.MainLoop()

