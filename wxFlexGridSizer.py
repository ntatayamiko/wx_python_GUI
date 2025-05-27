"""wxFlexGridSizer

Similar to wxGridSizer, but allows variable row and column sizes.

You can specify which rows or columns should be growable, making it more flexible.

Useful when some elements need more space than others"""
"""wxGridSizer
Organizes elements in a grid with equal-sized cells.
You define the number of rows and columns, and each cell gets the same width and height.
Ideal for layouts where uniform spacing is required."""

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
        panel=wx.Panel(self)
        self.list_box1 = wx.ListBox(panel, pos=wx.DefaultPosition, choices=[])
        self.static_txt1 = wx.StaticText(panel, id=1, label="firstname :",pos=wx.DefaultPosition)
        self.static_txt2 = wx.StaticText(panel, id=1, label="surname :",pos=wx.DefaultPosition)
        self.static_txt3 = wx.StaticText(panel, id=1, label="nationality :", pos=wx.DefaultPosition)
        self.my_btn1 = wx.Button(panel, label="SAVE",pos=wx.DefaultPosition)
        self.radio_btn1=wx.RadioButton(panel,id=wx.ID_ANY,label="Male ",pos=wx.DefaultPosition)
        self.radio_btn2 = wx.RadioButton(panel, label="Female ",pos=wx.DefaultPosition)
        self.text_ctrl1=wx.TextCtrl(panel)
        self.text_ctrl2 = wx.TextCtrl(panel)
        choices=["Malawi", "Zambia", "Zimbabwe"]
        self.drop_down1 = wx.ComboBox(parent=panel,choices=choices,)


        my_sizer2=wx.FlexGridSizer(wx.VERTICAL)
        #my_sizer2 = wx.BoxSizer()

        my_sizer2.Add(window=self.list_box1,proportion= 0, flag=wx.ALL| wx.EXPAND, border=5)
        my_sizer2.Add(window=self.static_txt1,proportion=0,flag=wx.ALL | wx.LEFT , border=10)
        my_sizer2.Add(window=self.text_ctrl1,proportion=0,flag=wx.ALL | wx.LEFT | wx.SHAPED, border=10)
        my_sizer2.Add(window=self.static_txt2,proportion=0,flag=wx.ALL | wx.LEFT, border=10)
        my_sizer2.Add(window=self.text_ctrl2,proportion=0,flag=wx.ALL | wx.LEFT | wx.SHAPED, border=10)
        my_sizer2.Add(window=self.radio_btn1,proportion= 0, flag=wx.ALL | wx.LEFT | wx.SHAPED, border=10)
        my_sizer2.Add(window=self.radio_btn2,proportion=0, flag=wx.ALL | wx.LEFT , border=10,userData=None)
        my_sizer2.Add(window=self.static_txt3, proportion=0, flag=wx.ALL | wx.LEFT, border=10)
        my_sizer2.Add(window=self.drop_down1,proportion=0, flag=wx.ALL | wx.LEFT | wx.SHAPED, border=10)
        my_sizer2.Add(window=self.my_btn1, proportion=0,flag= wx.ALL | wx.LEFT, border=5)
        panel.SetSizer(my_sizer2)





        self.Show()




if __name__=="__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()