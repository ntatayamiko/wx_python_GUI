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


import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
        panel=wx.Panel(self)
        self.list_box1 = wx.ListBox(panel, pos=(5, 55), choices=["MALE", "FEMALE"])
        self.static_txt1 = wx.StaticText(panel, id=1, label="firstname :", pos=(5, 5))
        self.my_btn1 = wx.Button(panel, label="press me", pos=(5, 55))


        my_sizer1=wx.BoxSizer(wx.VERTICAL)

        my_sizer1.Add(self.list_box1, 0, wx.ALL| wx.EXPAND, 5)

        my_sizer2 = wx.BoxSizer(wx.HORIZONTAL)

        my_sizer1.Add(self.static_txt1,proportion=2)



        my_sizer2.Add(self.text_ctrl1,0)


        my_sizer2.Add(self.my_btn1,0,wx.ALL | wx.CENTER,5)
        panel.SetSizer(my_sizer2)





        self.Show()




if __name__=="__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()