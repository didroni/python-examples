import wx
import random


class TotoGen(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title)

        self.UI()
        self.InitialValues()

    def UI(self):
        panel = wx.Panel(self)

        st1 = wx.StaticText(panel, label="Генератор на числа за тото", pos=(10, 10))
        bt1 = wx.Button(panel, label="Генерирай", pos=(250, 10), size=(80, 80))
        bt2 = wx.Button(panel, label="Нулиране", pos=(250, 100), size=(80, 80))
        self.chisla = wx.StaticText(panel, label="", pos=(10, 100))
        tempfont = self.chisla.GetFont()
        tempfont.SetPointSize(18)
        self.chisla.SetFont(tempfont)
        self.vidtotorb = wx.RadioBox(panel, label="Тото", pos=(10, 30), choices=["5/35", "6/49"])
        self.vidtotorb.SetSelection(1)
        self.Bind(wx.EVT_BUTTON, self.genchislo, bt1)
        self.Bind(wx.EVT_BUTTON, self.nulirane, bt2)
        self.Bind(wx.EVT_RADIOBOX, self.rb, self.vidtotorb)

    def InitialValues(self):
        self.iztegleni_chisla = []
        self.chisla.SetLabel("")
        self.rb(evt=None)

    def nulirane(self, evt):
        self.InitialValues()

    def genchislo(self, evt):
        if len(self.iztegleni_chisla) < self.maxnumbers:
            self.rc = random.randint(1, self.vidtoto+1)
            while self.rc in self.iztegleni_chisla:
                self.rc = random.randint(1, self.vidtoto+1)

            self.iztegleni_chisla.append(self.rc)

            if len(self.iztegleni_chisla) < self.maxnumbers:
                self.chisla.SetLabel(self.chisla.GetLabel() + str(self.rc) + ", ")
            else:
                self.chisla.SetLabel(self.chisla.GetLabel() + str(self.rc))


    def rb(self, evt):
        if self.vidtotorb.GetSelection() == 0:
            self.vidtoto = 35
            self.maxnumbers = 5
        else:
            self.vidtoto = 49
            self.maxnumbers = 6



app = wx.App()
totogen = TotoGen(None, "Генератор на числа за тото")
totogen.Show(True)
app.MainLoop()
