"""wxBoxSizer
Arranges elements horizontally or vertically in a single row or column.
Useful for stacking widgets in a linear fashion.
You can specify whether items expand to fill available space or remain at their default size.

wxButton – A standard clickable button.
wxTextCtrl – A text input field for user input.
wxListBox – A list of selectable items.
wxCheckBox – A checkbox for toggling options.
wxRadioButton – A radio button for selecting one option from a group.
wxSlider – A slider for selecting a value within a range.
wxComboBox – A dropdown list with selectable items.
wxStaticText – A label for displaying static text.
wxTreeCtrl – A tree view for hierarchical data.
wxNotebook
"""
from random import choices

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


        my_sizer2=wx.BoxSizer(wx.VERTICAL)
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