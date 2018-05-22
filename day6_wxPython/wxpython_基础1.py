#每个wxPYthon的程序都得有一个wx.App对象
import wx
app = wx.App(True)
frame = wx.Frame(None,-1,title='计算器',pos=(300,400),size=(400,500))
frame.Centre()#打开在屏幕中居中
frame.Show()#界面展示

print("小鸟叽叽叫")
app.MainLoop()