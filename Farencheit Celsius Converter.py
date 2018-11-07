import wx

class Converter (wx.Frame):

    def __init__(self, parent, title):

        wx.Frame.__init__(self, parent, -1, title, size=(700,300))

        self.UI()

    def UI(self):

        panel = wx.Panel(self)

        zaglavie = wx.StaticText(panel, label = "Конвертор между температура по Фаренхайт и Целзий")
        fonttemp = zaglavie.GetFont()
        fonttemp.SetPointSize(18)
        zaglavie.SetFont(fonttemp)
        self.name1 = wx.StaticText(panel, label = "Фаренхайт")
        fonttemp.SetPointSize(14)
        self.name1.SetFont(fonttemp)
        self.name2 = wx.StaticText(panel, label = "Целзий")
        self.name2.SetFont(fonttemp)
        self.t1e = wx.TextCtrl(panel)
        self.t2e = wx.TextCtrl(panel)
        bmp = wx.Bitmap("exchange.png")
        bmpbutton = wx.BitmapButton(panel, bitmap = bmp)
        emptybutton = wx.BitmapButton(panel)
        convertbutton = wx.Button(panel, label = "Конвертирай")

        bs = wx.BoxSizer(wx.VERTICAL)
        bs.Add(zaglavie, flag = wx.ALIGN_CENTER)
        bs.Add(0,20)

        gs = wx.GridSizer(2,3,5,5)

        gs.Add(self.name1)
        gs.Add(bmpbutton, flag = wx.ALIGN_CENTER)
        gs.Add(self.name2)

        gs.Add(self.t1e)
        gs.Add(emptybutton)
        gs.Add(self.t2e)

        bs.Add(gs, flag = wx.ALIGN_CENTER)

        bs.Add(convertbutton, flag = wx.ALIGN_CENTER)

        panel.SetSizer(bs)

        self.Bind(wx.EVT_BUTTON, self.convert, convertbutton)
        self.Bind(wx.EVT_BUTTON, self.exchange, bmpbutton)

    def far_cel(self, temp):

        tc = (temp - 32) * 5 / 9
        return tc

    def cel_far(self, temp):

        tf = temp * 9/5 + 32
        return tf

    def convert(self, evt):

        if self.name1.GetLabel() == "Фаренхайт":
            self.t2e.SetValue(str(self.far_cel(int(self.t1e.GetValue()))))
        else:
            self.t2e.SetValue(str(self.cel_far(int(self.t1e.GetValue()))))

    def exchange(self, evt):

        if self.name1.GetLabel() == "Фаренхайт":
            self.name2.SetLabel("Фаренхайт")
            self.name1.SetLabel("Целзий")
        else:
            self.name1.SetLabel("Фаренхайт")
            self.name2.SetLabel("Целзий")

app = wx.App()
convtemp = Converter(None, "Конвертор на температури")
convtemp.Show(True)
app.MainLoop()