#!/usr/bin/python
#-*-coding:utf-8-*-

import os
import json
import wx
import wx.grid
import wx.lib.rcsizer as rcs
import wx.lib.scrolledpanel as scrolled
import wx.lib.colourselect as csel


class TableConfigure:
    """room table configure"""
    
    def __init__(self):
        self.config = None

    def read(self,path):
        """table configure json file read"""

        try:
            fp = open(path,'r')
        except:
            print "open json file error!"
            return False
            
        with fp:
            try:
                check_bom = fp.read(3)
                if check_bom == '\xef\xbb\xbf':
                    fp.seek(3)
                else:
                    fp.seek(0)
                self.config = json.load(fp,"utf-8")
            except:
                print "json file read error!"
                return False

        return True

    def write(self,path):
        """table configure json file read"""

        if self.config == None or len(self.config) == 0:
            return False

        try:
            fp = open(path,'w')
        except:
            print "open json file error!"
            return False
            
        with fp:
            try:
                json.dump(self.config,fp,indent=4,separators=(',',': '))
            except:
                print "json file write error!"
                return False
                
        return True

class TableResource:
    """ table resource"""
    
    def __init__(self):
        self.table_fill = None
        self.table_normal = None
        self.table_playing = None
        self.table_face_back = None
        self.user_face = None
        self.ready_flag = None
        self.lock_flag = None
        
    def LoadDefaultTableResource(self):
        
        try:                
            self.table_fill = wx.Image("table\\table_fill.png").ConvertToBitmap()
            self.table_normal = wx.Image("table\\table_normal.png").ConvertToBitmap()
            self.table_playing = wx.Image("table\\table_playing.png").ConvertToBitmap()
            self.table_face_back = wx.Image("table\\table_face_back.png").ConvertToBitmap()
            self.user_face = wx.Image("table\\user_face.png").ConvertToBitmap()
            self.ready_flag = wx.Image("table\\ready.png").ConvertToBitmap()
            self.lock_flag = wx.Image("table\\lock.png").ConvertToBitmap()
        except:
            print "load default table resource image error!"
            wx.MessageBox(u"加载默认桌子配置错误！",u"错误提示",wx.OK|wx.ICON_ERROR)
            return False
            
        return True        
       
    def LoadTableResource(self, resource_dir):
               
        if os.path.exists(resource_dir) == False:
            return False
        
        image_file_path = ""
        image_file_count = 0
        try:                
            image_file_path = os.path.join(resource_dir,"table_fill.png")
            if os.path.exists(image_file_path) == True:
                self.table_fill = wx.Image(image_file_path).ConvertToBitmap()
                image_file_count += 1
        except:
            print "load table_fill.png resource image error!"
           
        try:    
            image_file_path = os.path.join(resource_dir,"table_normal.png")
            if os.path.exists(image_file_path) == True:
                self.table_normal = wx.Image(image_file_path).ConvertToBitmap()
                image_file_count += 1
        except:
            print "load table_normal.png resource image error!"
            
        try:        
            image_file_path = os.path.join(resource_dir,"table_playing.png")
            if os.path.exists(image_file_path) == True:
                self.table_playing = wx.Image(image_file_path).ConvertToBitmap()
                image_file_count += 1
        except:
            print "load table_playing.png resource image error!"
            
        try:
            image_file_path = os.path.join(resource_dir,"table_face_back.png")
            if os.path.exists(image_file_path) == True:
                self.table_face_back = wx.Image(image_file_path).ConvertToBitmap()
                image_file_count += 1
        except:
            print "load table_face_back.png resource image error!"
            
        try:
            image_file_path = os.path.join(resource_dir,"user_face.png")
            if os.path.exists(image_file_path) == True:
                self.user_face = wx.Image(image_file_path).ConvertToBitmap()
                image_file_count += 1
        except:
            print "load user_face.png resource image error!"
            
        try:
            image_file_path = os.path.join(resource_dir,"ready.png")
            if os.path.exists(image_file_path) == True:
                self.ready_flag = wx.Image(image_file_path).ConvertToBitmap()
                image_file_count += 1
        except:
            print "load ready.png resource image error!"
            
        try:    
            image_file_path = os.path.join(resource_dir,"lock.png")
            if os.path.exists(image_file_path) == True:
                self.lock_flag = wx.Image(image_file_path).ConvertToBitmap()
                image_file_count += 1
        except:
            print "load lock.png resource image error!"

        if image_file_count == 0:
            wx.MessageBox(u"没有找到可以加载的桌子图！",u"警告提示",wx.OK)
            return False
            
        return True

        

TEXT_ALIGN_RIGHT = 0x01
TEXT_ALIGN_CENTER = 0x02
TEXT_ALIGN_LEFT = 0x04

TEXT_ALIGN_TOP = 0x10
TEXT_ALIGN_MIDDLE = 0x20
TEXT_ALIGN_BOTTOM = 0x40

TEXT_MULTIPLE_LINE = 0x08
TEXT_ELLIPSIZE_END = 0x80

IMAGE_READY_WIDTH = 18
IMAGE_READY_HEIGHT = 27
IMAGE_LOCK_WIDTH = 29
IMAGE_LOCK_HEIGHT = 38
IMAGE_FACE_WIDHT = 50
IMAGE_FACE_HEIGHT = 50

TEXT_ACCOUNTS_WIDTH = 50
TEXT_ACCOUNTS_HEIGHT = 24

COLOR_DASH_LINE_FRAME = wx.WHITE 
        
class DrawChairInfo:
    """draw chair infomation"""
    
    def __init__(self):
        self.rect_chair = [0,0,IMAGE_FACE_WIDHT,IMAGE_FACE_HEIGHT]
        self.rect_accounts = [0,0,TEXT_ACCOUNTS_WIDTH,TEXT_ACCOUNTS_HEIGHT]
        self.rect_ready = [0,0,IMAGE_READY_WIDTH,IMAGE_READY_HEIGHT]
        self.align_mode = TEXT_ALIGN_CENTER|TEXT_ALIGN_MIDDLE
        self.visible = True

        
class DrawTableInfo:
    """draw table infomation"""
    

    def __init__(self):
        self.table_resource = None
        self.color_accounts = [255,255,255]
        self.color_table_info = [100,255,100]
        self.color_table_id = [128,128,128]
        self.table_info_align_mode = TEXT_ALIGN_CENTER|TEXT_ALIGN_MIDDLE
        self.table_id_align_mode = TEXT_ALIGN_CENTER|TEXT_ALIGN_MIDDLE
        self.rect_table_lock = [0,0,IMAGE_LOCK_WIDTH,IMAGE_LOCK_HEIGHT]
        self.rect_table_info = [0,0,200,24]
        self.rect_table_id = [0,0,180,24]
        self.table_chairs = [DrawChairInfo()]
        self.table_chairs_count = len(self.table_chairs)
        
    def SetTableResource(self, tabel_resource):
        self.table_resource = tabel_resource

    def LoadTableConfig(self, table_config):
        
        if table_config == None :
            return False
            
        if not isinstance(table_config,TableConfigure):
            return False
            
        if table_config.config == None:
            return False
            
        if len(table_config.config) == 0:
            return False
            
        try:
            table_colors = table_config.config["color"]
            self.color_accounts = table_colors["accounts"] 
            self.color_table_id = table_colors["table_id"] 
            
            table_positions = table_config.config["positions"]
            point_table_lock = table_positions["lock"]
            self.rect_table_lock = [point_table_lock[0]-IMAGE_LOCK_WIDTH/2,point_table_lock[1]-IMAGE_LOCK_HEIGHT/2,IMAGE_LOCK_WIDTH,IMAGE_LOCK_HEIGHT] 
            self.rect_table_id = table_positions["table_id"]
            
            table_chairs = table_positions["chairs"]
            table_chairs_count = self.table_chairs_count
            self.table_chairs_count = len(table_chairs)
            for index in range(0,len(table_chairs)):
                if index < table_chairs_count:
                    self.table_chairs[index].rect_chair = table_chairs[index]["chair"] 
                    self.table_chairs[index].rect_accounts = table_chairs[index]["accounts"] 
                    point_ready = table_chairs[index]["ready"]
                    self.table_chairs[index].rect_ready = [point_ready[0],point_ready[1],IMAGE_READY_WIDTH,IMAGE_READY_HEIGHT]
                    self.table_chairs[index].align_mode = table_chairs[index]["draw_style"]
                    self.table_chairs[index].visible = table_chairs[index]["visible"] 
                else:
                    chair_info = DrawChairInfo()
                    chair_info.rect_chair = table_chairs[index]["chair"] 
                    chair_info.rect_accounts = table_chairs[index]["accounts"] 
                    point_ready = table_chairs[index]["ready"]
                    chair_info.rect_ready = [point_ready[0],point_ready[1],IMAGE_READY_WIDTH,IMAGE_READY_HEIGHT]
                    chair_info.align_mode = table_chairs[index]["draw_style"]
                    chair_info.visible = table_chairs[index]["visible"] 
                    self.table_chairs.append(chair_info)
        except:
            print "load table configure error!"
            wx.MessageBox(u"加载桌子配置错误！",u"错误提示",wx.OK|wx.ICON_ERROR)
            return False
        
        return True
    
    def SaveTableConfig(self, table_config):
        
        if table_config == None :
            return False
            
        if not isinstance(table_config,TableConfigure):
            return False
            
        if table_config.config == None:
            return False
            
        if len(table_config.config) == 0:
            return False
            
        try:
            table_colors = table_config.config["color"]
            table_colors["accounts"] = self.color_accounts
            table_colors["table_id"] = self.color_table_id
            
            table_positions = table_config.config["positions"]
            table_positions["lock"] = [self.rect_table_lock[0]+self.rect_table_lock[2]/2,self.rect_table_lock[1]+self.rect_table_lock[3]/2] 
            table_positions["table_id"] = self.rect_table_id
            
            table_chairs = table_positions["chairs"]
            for index in range(0,self.table_chairs_count):
                if index < len(table_chairs):
                    table_chairs[index]["chair"] = self.table_chairs[index].rect_chair
                    table_chairs[index]["accounts"] = self.table_chairs[index].rect_accounts
                    table_chairs[index]["ready"] = [self.table_chairs[index].rect_ready[0],self.table_chairs[index].rect_ready[1]]
                    table_chairs[index]["draw_style"] = self.table_chairs[index].align_mode
                    table_chairs[index]["visible"] = self.table_chairs[index].visible
                else:
                    chairs_info = {
                        "chair": self.table_chairs[index].rect_chair,
                        "accounts": self.table_chairs[index].rect_accounts,
                        "ready": [self.table_chairs[index].rect_ready[0],self.table_chairs[index].rect_ready[1]],
                        "draw_style": self.table_chairs[index].align_mode,
                        "visible": self.table_chairs[index].visible
                    }
                    table_chairs.append(chairs_info)
                    
            if len(table_chairs) > self.table_chairs_count:
                if self.table_chairs_count > 0:    
                    del table_chairs[self.table_chairs_count-1:]
                else:
                    del table_chairs[0:]
        except:
            print "save table configure error!"
            wx.MessageBox(u"保存桌子配置错误！",u"错误提示",wx.OK|wx.ICON_ERROR)
            return False

        return True

class DrawTablePanel(scrolled.ScrolledPanel):
    """draw room table panel"""    
    
    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1)
       
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

        self.delegate = None
        self.is_show_face_frame = True
        self.is_show_user_face = True
        self.is_show_user_accounts = True
        self.is_show_user_ready = True
        self.is_show_table_lock = True
        self.is_show_table_info = False
        self.is_show_table_id = True
        self.is_show_table_dash_line = False
        self.is_show_frame_dash_line = True
        self.is_show_table_normal = False

    def SetDelegate(self,delegate):
        self.delegate = delegate
                
    def SetShowFrameLine(self, show):
        self.is_show_frame_dash_line = show
        
    def SetImage(self, image):
        self.draw_image = image
        self.Refresh()


    def OnPaint(self, event):
       
        dc = wx.PaintDC(self)
        dc = wx.BufferedDC(dc)
        dc.SetBackground(wx.Brush("WHITE"))
        dc.Clear()
        
        windowsize= self.GetSizeTuple()
        dc.SetBrush(wx.Brush("GREY", wx.CROSSDIAG_HATCH))
        dc.DrawRectangle(0, 0, windowsize[0], windowsize[1])
        

        if self.delegate != None and self.delegate.draw_table_info != None:
            draw_table_info = self.delegate.draw_table_info
            table_resource = draw_table_info.table_resource
            table_chairs = draw_table_info.table_chairs
            
            if table_resource != None:
                #填充背景
                if table_resource.table_fill != None:
                    image_width,image_height = table_resource.table_fill.GetSize()
                    for y in range(0,windowsize[1],image_height):
                        for x in range(0,windowsize[0],image_width):
                            dc.DrawBitmap(table_resource.table_fill,x,y,True)
                #绘制桌子图
                if self.is_show_table_normal == True:
                    if table_resource.table_normal != None:
                        dc.DrawBitmap(table_resource.table_normal,0,0,True)
                        if self.is_show_table_dash_line == True:
                            width,height = table_resource.table_normal.GetSize()
                            rect_table = [0,0,width,height]
                            self.DrawRectDashLine(dc,rect_table,COLOR_DASH_LINE_FRAME)
                else:
                    if table_resource.table_playing != None:
                        dc.DrawBitmap(table_resource.table_playing,0,0,True)
                        if self.is_show_table_dash_line == True:
                            width,height = table_resource.table_playing.GetSize()
                            rect_table = [0,0,width,height]
                            self.DrawRectDashLine(dc,rect_table,COLOR_DASH_LINE_FRAME)
                        
                #绘制椅子、头像、名称   
                if table_chairs != None:
                    for index in range(0,draw_table_info.table_chairs_count):
                        xpos = 0
                        ypos = 0
                        
                        if table_chairs[index].visible == False:
                            continue
                        
                        #绘制椅子
                        if table_resource.table_face_back != None and self.is_show_face_frame == True:
                            rect_face_back = [
                                table_chairs[index].rect_chair[0]-1,
                                table_chairs[index].rect_chair[1]-1,
                                table_chairs[index].rect_chair[2]+2,
                                table_chairs[index].rect_chair[3]+2
                                ]
                            xpos = rect_face_back[0]
                            ypos = rect_face_back[1]
                            dc.DrawBitmap(table_resource.table_face_back,xpos,ypos,True)
                            self.DrawRectDashLine(dc,rect_face_back,COLOR_DASH_LINE_FRAME)
                            
                        #绘制头像
                        if table_resource.user_face != None and self.is_show_user_face == True:
                            rect_user_face = table_chairs[index].rect_chair
                            xpos = rect_user_face[0]
                            ypos = rect_user_face[1]
                            dc.DrawBitmap(table_resource.user_face,xpos,ypos,True)
                            self.DrawRectDashLine(dc,rect_user_face,COLOR_DASH_LINE_FRAME)
                            
                        #绘制账号
                        if self.is_show_user_accounts == True:
                            rect_accounts = table_chairs[index].rect_accounts
                            align_mode = table_chairs[index].align_mode|TEXT_MULTIPLE_LINE|TEXT_ELLIPSIZE_END
                            dc.SetTextForeground(draw_table_info.color_accounts)
                            self.DrawLabelFormat(dc,self.delegate.str_accounts,rect_accounts,align_mode)
                            self.DrawRectDashLine(dc,rect_accounts,COLOR_DASH_LINE_FRAME)
                                                
                        #绘制准备
                        if table_resource.ready_flag != None and self.is_show_user_ready == True:
                            rect_ready = table_chairs[index].rect_ready
                            xpos = rect_ready[0]
                            ypos = rect_ready[1]
                            dc.DrawBitmap(table_resource.ready_flag,xpos,ypos,True)
                            self.DrawRectDashLine(dc,rect_ready,COLOR_DASH_LINE_FRAME)
                        
                        
                #绘制桌子锁
                if table_resource.lock_flag != None and self.is_show_table_lock == True:
                    rect_table_lock = draw_table_info.rect_table_lock
                    xpos = rect_table_lock[0]
                    ypos = rect_table_lock[1]
                    dc.DrawBitmap(table_resource.lock_flag,xpos,ypos,True)
                    self.DrawRectDashLine(dc,rect_table_lock,COLOR_DASH_LINE_FRAME)
                    
                #绘制桌子信息
                if self.is_show_table_info == True:
                    rect_table_info = draw_table_info.rect_table_info
                    align_mode = draw_table_info.table_info_align_mode|TEXT_MULTIPLE_LINE|TEXT_ELLIPSIZE_END
                    dc.SetTextForeground(draw_table_info.color_table_info)
                    self.DrawLabelFormat(dc,self.delegate.str_table_info,rect_table_info,align_mode)
                    self.DrawRectDashLine(dc,rect_table_info,COLOR_DASH_LINE_FRAME)
                    
                #绘制桌子ID
                if self.is_show_table_id == True:
                    rect_table_id = draw_table_info.rect_table_id
                    align_mode = draw_table_info.table_id_align_mode|TEXT_MULTIPLE_LINE|TEXT_ELLIPSIZE_END
                    dc.SetTextForeground(draw_table_info.color_table_id)
                    self.DrawLabelFormat(dc,self.delegate.str_table_id,rect_table_id,align_mode)
                    self.DrawRectDashLine(dc,rect_table_id,COLOR_DASH_LINE_FRAME)


    def OnEraseBackground(self, event):
        pass

    def SwitchAlignMode(self, align):

        align_mode = 0
        if align&TEXT_ALIGN_RIGHT :
            align_mode |= wx.ALIGN_RIGHT
        elif align&TEXT_ALIGN_CENTER :
            align_mode |= wx.ALIGN_CENTER_HORIZONTAL
        else:
            align_mode |= wx.ALIGN_LEFT
            
        if align&TEXT_ALIGN_TOP :
            align_mode |= wx.ALIGN_TOP
        elif align&TEXT_ALIGN_MIDDLE :
            align_mode |= wx.ALIGN_CENTER_VERTICAL
        else:
            align_mode |= wx.ALIGN_BOTTOM

        return align_mode
                
    def DrawLabelFormat(self, dc, text, rect, fmt = TEXT_ALIGN_LEFT|TEXT_ALIGN_TOP):
        
        draw_text = ""
        text_ellipsize_end = "..."
        text_ellipsize_end_width = 0
        last_text = ""
        last_text_width = 0
        x = y = 0
        lines = 0
        line_index = 0
        width, height = (rect[2],rect[3])
        if not width or not height:
            return
        
        if fmt&TEXT_ELLIPSIZE_END :
            text_ellipsize_end_width = dc.GetTextExtent(text_ellipsize_end)[0]
        
        if fmt&TEXT_MULTIPLE_LINE :
            h = dc.GetCharHeight()
            if h > 0: lines = height/h
            
            for ch in text:
                if ch != '\n' and ch != '\r':
                    w, h = dc.GetTextExtent(ch)
                        
                    if y <= height and (line_index+1) < lines:
                        if (x+w) <= width:
                            x += w
                            draw_text += ch
                            continue
                        else:
                            x = 0
                            y += h
                            line_index += 1
                            draw_text += '\n'
                            if line_index < (lines-1) and y <= height and  (x+w) <= width:
                                x += w
                                draw_text += ch
                                continue

                    #最后一行
                    if y <= height and line_index < lines:
                        if text_ellipsize_end_width > 0:
                            if (x+w+text_ellipsize_end_width) <= width:
                                x += w
                                draw_text += ch
                            else:
                                last_text_width += w
                                if (x+last_text_width) <= width:
                                    last_text += ch
                                else:
                                    break
                        else:
                            if (x+w) <= width:
                                x += w
                                draw_text += ch
                            else:
                                break
                        
                else:
                    if ch == '\n': 
                        x = 0
                        h = dc.GetCharHeight()
                        if y <= height and (line_index+1) < lines:
                            y += h
                            line_index += 1
                            draw_text += ch 
                        else:
                            break
                    else:
                        draw_text += ch                        
                    
        else:
            lines = 1
            line_index = 0
            
            for ch in text:
                if ch != '\n' and ch != '\r':
                    w, h = dc.GetTextExtent(ch)
                    
                    if h > height: break
                    if y < h: y = h                        
        
                    if text_ellipsize_end_width > 0:
                        if (x+w+text_ellipsize_end_width) <= width:
                            x += w
                            draw_text += ch
                        else:
                            last_text_width += w
                            if (x+last_text_width) <= width:
                                last_text += ch
                            else:
                                break
                    else:
                        if (x+w) <= width:
                            x += w
                            draw_text += ch
                        else:
                            break
            
        if y <= height and line_index < lines and last_text_width > 0:
            if text_ellipsize_end_width > 0 and (x+last_text_width) <= width:
                draw_text += last_text
            elif text_ellipsize_end_width > 0:
                for ch in text_ellipsize_end:
                     w, h = dc.GetTextExtent(ch)
                     if (x+w) <= width:
                         x += w
                         draw_text += ch
            
        align_mode = self.SwitchAlignMode(fmt)
        dc.DrawLabel(draw_text,rect,align_mode)
            
                
    def DrawRectDashLine(self, dc, rect, color = "WHITE"):
        
        if self.is_show_frame_dash_line:
            pen = dc.GetPen()
            brush = dc.GetBrush()
            dc.SetPen(wx.Pen(color, 1, wx.DOT_DASH))
            dc.SetBrush(wx.Brush(color,wx.TRANSPARENT))
            dc.DrawRectangle(rect[0],rect[1],rect[2],rect[3])
            dc.SetPen(pen)
            dc.SetBrush(brush)
    

class MainFrame(wx.Frame):
    """window show"""

    
    def __init__(self):
        wx.Log().SetLogLevel(0)
        wx.Frame.__init__(self,parent=None,id=-1,title = u'房间桌子配置',size = (960,600))
        
        #读配置文件
        self.table_config_file_name = "table\\table_config"
        self.table_cfg = TableConfigure()
        try:
            self.table_cfg.read(self.table_config_file_name)
        except:
            print "read table configure error!"
    
        #创建子空间
        self.OnCreateWindow()
        
        self.draw_table_panel.SetDelegate(self)
        self.draw_table_info = DrawTableInfo()
        self.draw_table_info.LoadTableConfig(self.table_cfg)
        
        #加载默认资源配置
        self.table_res = TableResource()
        self.table_res.LoadDefaultTableResource()
        self.draw_table_info.SetTableResource(self.table_res)
        
        self.str_accounts = self.combo_user_accounts.GetValue()
        self.str_table_info = self.combo_table_info.GetValue()
        self.str_table_id = self.combo_table_id.GetValue()
        
        if self.draw_table_info.table_chairs_count > 0:
            self.combo_table_chairs_count.Select(self.draw_table_info.table_chairs_count-1)
            
        if self.combo_table_chairs_count.GetValue().count > 0:
            table_chairs_count = int(self.combo_table_chairs_count.GetValue())
            table_chair_index_list = []
            for item in range(0, table_chairs_count): table_chair_index_list.append(str(item))
            self.combo_table_chair_index.Set(table_chair_index_list)
            self.combo_table_chair_index.Select(0)
            select_object_index = int(self.combo_table_chair_index.GetValue())
            self.UpdateTableChairData(select_object_index)



    def __del__(self):
        #写配置
        self.draw_table_info.SaveTableConfig(self.table_cfg)
        try:
            self.table_cfg.write(self.table_config_file_name)
        except:
            print "write table configure error!"
            
            
    def OnCreateWindow(self,*arg):
        #创建控件
        panel = wx.Panel(self)
        frame_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        panel.SetSizer(frame_sizer)
        
        label_table_browse = wx.StaticBox(panel,label=u"桌子示意图:")
        self.draw_table_panel = DrawTablePanel(label_table_browse)
        
        frame_sizer1 = wx.StaticBoxSizer(label_table_browse,orient=wx.VERTICAL)
        frame_sizer1.Add(self.draw_table_panel,1,wx.ALL|wx.EXPAND,0)
        frame_sizer.Add(frame_sizer1,2,wx.ALL|wx.EXPAND,2)
        frame_sizer2 = wx.BoxSizer(orient=wx.VERTICAL)
        frame_sizer.Add(frame_sizer2,1,wx.ALL|wx.EXPAND,2)
        frame_sizer2_1 = wx.BoxSizer(orient=wx.HORIZONTAL)
        frame_sizer2.Add(frame_sizer2_1,0,wx.ALL,2)
        frame_sizer2_2 = wx.BoxSizer(orient=wx.HORIZONTAL)
        frame_sizer2.Add(frame_sizer2_2,0,wx.ALL,2)
        frame_sizer2_3 = wx.BoxSizer(orient=wx.HORIZONTAL)
        frame_sizer2.Add(frame_sizer2_3,0,wx.ALL,2)
        frame_sizer2_4 = wx.BoxSizer(orient=wx.HORIZONTAL)
        frame_sizer2.Add(frame_sizer2_4,0,wx.ALL,2)
        frame_sizer2_5 = wx.BoxSizer(orient=wx.HORIZONTAL)
        frame_sizer2.Add(frame_sizer2_5,0,wx.ALL,2)
        frame_sizer2_6 = wx.BoxSizer(orient=wx.HORIZONTAL)
        frame_sizer2.Add(frame_sizer2_6,0,wx.ALL,2)
        frame_sizer2_7 = wx.BoxSizer(orient=wx.HORIZONTAL)
        frame_sizer2.Add(frame_sizer2_7,0,wx.ALL,2)
        frame_sizer2_8 = wx.BoxSizer(orient=wx.HORIZONTAL)
        frame_sizer2.Add(frame_sizer2_8,1,wx.ALL|wx.EXPAND,2)

        btn_load_table_resource = wx.Button(panel,label=u"加载桌子资源图")
        btn_load_table_config = wx.Button(panel,label=u"加载桌子配置文件")
        btn_save_table_config = wx.Button(panel,label=u"保存桌子配置文件")
        
        frame_sizer2_1.Add(btn_load_table_resource,0,wx.TOP,2)
        frame_sizer2_1.Add(btn_load_table_config,0,wx.TOP,2)
        frame_sizer2_1.Add(btn_save_table_config,0,wx.TOP,2)
        
        label_user_accounts = wx.StaticText(panel,label=u"测试账号：")
        user_accounts_list = [u"测试账号",u"一行两行测试账号",u"一行两行三行测试账号",
        u"一行两行三行四行测试账号",u"一行两行三行四行五行测试账号",u"一行两行三行四行五行六行测试账号"]        
        self.combo_user_accounts = wx.ComboBox(panel,value=u"测试账号",choices=user_accounts_list)
        btn_use_account = wx.Button(panel,label=u"应用账号")
        
        label_table_info = wx.StaticText(panel,label=u"测试信息：")
        table_info_list = [u"限制分数：1000",u"限制分数：1万",u"限制分数：10万",
        u"坐下金币：1000",u"坐下金币：1万",u"坐下金币：1万"]        
        self.combo_table_info = wx.ComboBox(panel,value=u"限制分数：1000",choices=table_info_list)
        btn_use_table_info = wx.Button(panel,label=u"应用信息")
        
        label_table_id = wx.StaticText(panel,label=u"测试桌号：")
        table_id_list = [u"第1桌",u"第2桌",u"第3桌",u"第10桌",u"第88桌",u"第100桌"]        
        self.combo_table_id = wx.ComboBox(panel,value=u"第1桌",choices=table_id_list)
        btn_use_table_id = wx.Button(panel,label=u"应用桌号")
        
        user_accounts_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        table_info_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        table_id_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        test_context_sizer = rcs.RowColSizer()
        
        user_accounts_sizer.Add(label_user_accounts,0,wx.TOP,5)
        user_accounts_sizer.Add(self.combo_user_accounts,0,wx.TOP,2)
        user_accounts_sizer.Add(btn_use_account,0,wx.TOP,0)
        
        table_info_sizer.Add(label_table_info,0,wx.TOP,5)
        table_info_sizer.Add(self.combo_table_info,0,wx.TOP,2)
        table_info_sizer.Add(btn_use_table_info,0,wx.TOP,0)
        
        table_id_sizer.Add(label_table_id,0,wx.TOP,5)
        table_id_sizer.Add(self.combo_table_id,0,wx.TOP,2)
        table_id_sizer.Add(btn_use_table_id,0,wx.TOP,0)
           
        test_context_sizer.Add(user_accounts_sizer,0,wx.TOP,5,row=0,col=0)
        test_context_sizer.Add(table_info_sizer,0,wx.TOP,2,row=1,col=0)
        test_context_sizer.Add(table_id_sizer,0,wx.TOP,0,row=2,col=0)
        frame_sizer2_2.Add(test_context_sizer,0,wx.TOP,0)
        
        label_select_show_object = wx.StaticBox(panel,label=u"选择显示(隐藏)的对象")
        self.check_show_user_face = wx.CheckBox(panel,label=u"用户头像")
        self.check_show_user_accounts = wx.CheckBox(panel,label=u"用户账号")
        self.check_show_user_ready = wx.CheckBox(panel,label=u"用户准备")
        self.check_show_table_lock = wx.CheckBox(panel,label=u"桌子锁")
        self.check_show_table_info = wx.CheckBox(panel,label=u"桌信息")
        self.check_show_table_id = wx.CheckBox(panel,label=u"桌子号")
        self.check_show_face_frame = wx.CheckBox(panel,label=u"头像底框")
        self.check_show_table_dash_line = wx.CheckBox(panel,label=u"桌子虚线框")
        self.check_show_frame_dash_line = wx.CheckBox(panel,label=u"虚线框")
        
        self.check_show_user_face.SetValue(self.draw_table_panel.is_show_user_face)
        self.check_show_user_accounts.SetValue(self.draw_table_panel.is_show_user_accounts)
        self.check_show_user_ready.SetValue(self.draw_table_panel.is_show_user_ready)
        self.check_show_table_lock.SetValue(self.draw_table_panel.is_show_table_lock)
        self.check_show_table_info.SetValue(self.draw_table_panel.is_show_table_info)
        self.check_show_table_id.SetValue(self.draw_table_panel.is_show_table_id)
        self.check_show_face_frame.SetValue(self.draw_table_panel.is_show_face_frame)
        self.check_show_table_dash_line.SetValue(self.draw_table_panel.is_show_table_dash_line)
        self.check_show_frame_dash_line.SetValue(self.draw_table_panel.is_show_frame_dash_line)
        
        select_show_object_sizer = wx.StaticBoxSizer(label_select_show_object,orient=wx.VERTICAL)
        select_show_object_sizer1 = wx.BoxSizer(orient=wx.HORIZONTAL)
        select_show_object_sizer2 = wx.BoxSizer(orient=wx.HORIZONTAL)
        
        select_show_object_sizer1.Add(self.check_show_user_face,0,wx.TOP,2)
        select_show_object_sizer1.Add(self.check_show_user_accounts,0,wx.TOP,2)
        select_show_object_sizer1.Add(self.check_show_user_ready,0,wx.TOP,2)
        select_show_object_sizer1.Add(self.check_show_table_lock,0,wx.TOP,2)
        select_show_object_sizer1.Add(self.check_show_table_info,0,wx.TOP,2)
        select_show_object_sizer1.Add(self.check_show_table_id,0,wx.TOP,2)
        select_show_object_sizer2.Add(self.check_show_face_frame,0,wx.TOP,2)
        select_show_object_sizer2.Add(self.check_show_table_dash_line,0,wx.TOP,2)
        select_show_object_sizer2.Add(self.check_show_frame_dash_line,0,wx.TOP,2)
        select_show_object_sizer.Add(select_show_object_sizer1,1,wx.ALL|wx.EXPAND,0)
        select_show_object_sizer.Add(select_show_object_sizer2,1,wx.ALL|wx.EXPAND,0)
        frame_sizer2_3.Add(select_show_object_sizer,1,wx.TOP|wx.EXPAND,2)
        
        label_select_object = wx.StaticBox(panel,label=u"选择调整的对象")
        select_object_sizer = wx.StaticBoxSizer(label_select_object,orient=wx.HORIZONTAL)
        self.radio_select_user_face = wx.RadioButton(panel,label=u"头像",style=wx.RB_GROUP)
        self.radio_select_user_accounts = wx.RadioButton(panel,label=u"账号")
        self.radio_select_user_ready = wx.RadioButton(panel,label=u"准备")
        self.radio_select_table_lock = wx.RadioButton(panel,label=u"桌子锁")
        self.radio_select_table_info = wx.RadioButton(panel,label=u"桌信息")
        self.radio_select_table_id = wx.RadioButton(panel,label=u"桌子号")
        
        select_object_sizer.Add(self.radio_select_user_face,0,wx.Top,2)
        select_object_sizer.Add(self.radio_select_user_accounts,0,wx.Top,2)
        select_object_sizer.Add(self.radio_select_user_ready,0,wx.Top,2)
        select_object_sizer.Add(self.radio_select_table_lock,0,wx.Top,2)
        select_object_sizer.Add(self.radio_select_table_info,0,wx.Top,2)
        select_object_sizer.Add(self.radio_select_table_id,0,wx.Top,2)
        frame_sizer2_4.Add(select_object_sizer,1,wx.TOP|wx.EXPAND,2)
        
        label1= wx.StaticText(panel,label=u"椅子数目：")
        chairs_list = []        
        for item in range(1,101):
            chairs_list.append(str(item))
        self.combo_table_chairs_count = wx.ComboBox(panel,value="2",choices=chairs_list,style=wx.CB_READONLY,size=(50,-1))
        self.btn_table_chairs_reverse = wx.Button(panel,label=u"反转桌子椅子顺序")
        
        frame_sizer2_5.Add(label1,0,wx.TOP,5)
        frame_sizer2_5.Add(self.combo_table_chairs_count,0,wx.TOP,2)
        frame_sizer2_5.AddSpacer(18)
        frame_sizer2_5.Add(self.btn_table_chairs_reverse,0,wx.TOP,2)
        
        label3 = wx.StaticText(panel,label=u"选择索引：")
        chair_index_list = []
        for item in range(0,int(self.combo_table_chairs_count.GetValue())):
            chair_index_list.append(str(item))
        self.combo_table_chair_index = wx.ComboBox(panel,value="0",choices=chair_index_list,style=wx.CB_READONLY,size=(50,-1))
        self.check_table_chair_visible = wx.CheckBox(panel,label=u"显示椅子信息")       
        
        frame_sizer2_6.Add(label3,0,wx.TOP,5)
        frame_sizer2_6.Add(self.combo_table_chair_index,0,wx.TOP,2)
        frame_sizer2_6.Add(self.check_table_chair_visible,0,wx.LEFT|wx.ALIGN_CENTER_VERTICAL,18)
        
        label_text_set = wx.StaticBox(panel,label=u"文本设置")
        self.radio_text_align_h1 = wx.RadioButton(panel,label=u"左边对齐",style=wx.RB_GROUP)
        self.radio_text_align_h2 = wx.RadioButton(panel,label=u"水平居中")
        self.radio_text_align_h3 = wx.RadioButton(panel,label=u"右边对齐")
        self.radio_text_align_v1 = wx.RadioButton(panel,label=u"上边对齐",style=wx.RB_GROUP)
        self.radio_text_align_v2 = wx.RadioButton(panel,label=u"垂直居中")
        self.radio_text_align_v3 = wx.RadioButton(panel,label=u"下边对齐")
        
        label_color_r = wx.StaticText(panel,label=u"R:")
        label_color_g = wx.StaticText(panel,label=u"G:")
        label_color_b = wx.StaticText(panel,label=u"B:")
        self.text_color_r = wx.SpinCtrl(panel,size =(48, 24))
        self.text_color_g = wx.SpinCtrl(panel,size =(48, 24))
        self.text_color_b = wx.SpinCtrl(panel,size =(48, 24))
        self.btn_text_color_select = csel.ColourSelect(panel,label=u"用户账号颜色",colour=(255,255,255))
        self.btn_info_color_select = csel.ColourSelect(panel,label=u"桌子信息颜色",colour=(0,255,200))
        self.btn_table_color_select = csel.ColourSelect(panel,label=u"桌子ID号颜色",colour=(128,128,128))
        
        self.text_color_r.SetRange(0,255)
        self.text_color_g.SetRange(0,255)
        self.text_color_b.SetRange(0,255)
        self.text_color_r.SetValue(255)
        self.text_color_g.SetValue(255)
        self.text_color_b.SetValue(255)
        
        text_set_box_sizer = wx.StaticBoxSizer(label_text_set,orient=wx.HORIZONTAL)
        text_set_sizer = rcs.RowColSizer()
        text_color_r_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        text_color_g_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        text_color_b_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        
        text_set_sizer.Add(self.radio_text_align_h1,0,wx.LEFT,8,row=0,col=1)
        text_set_sizer.Add(self.radio_text_align_h2,0,wx.LEFT,8,row=1,col=1)
        text_set_sizer.Add(self.radio_text_align_h3,0,wx.LEFT,8,row=2,col=1)
        text_set_sizer.Add(self.radio_text_align_v1,0,wx.LEFT,2,row=0,col=2)
        text_set_sizer.Add(self.radio_text_align_v2,0,wx.LEFT,2,row=1,col=2)
        text_set_sizer.Add(self.radio_text_align_v3,0,wx.LEFT,2,row=2,col=2)
        
        text_color_r_sizer.Add(label_color_r,0,wx.TOP,5)
        text_color_r_sizer.Add(self.text_color_r,0,wx.TOP,2)
        text_color_g_sizer.Add(label_color_g,0,wx.TOP,5)
        text_color_g_sizer.Add(self.text_color_g,0,wx.TOP,2)
        text_color_b_sizer.Add(label_color_b,0,wx.TOP,5)
        text_color_b_sizer.Add(self.text_color_b,0,wx.TOP,2)      
        
        text_set_sizer.Add(text_color_r_sizer,0,wx.LEFT,8,row=0,col=3)
        text_set_sizer.Add(text_color_g_sizer,0,wx.LEFT,8,row=1,col=3)
        text_set_sizer.Add(text_color_b_sizer,0,wx.LEFT,8,row=2,col=3)
    
        text_set_sizer.Add(self.btn_text_color_select,0,wx.LEFT,8,row=0,col=4)
        text_set_sizer.Add(self.btn_info_color_select,0,wx.LEFT,8,row=1,col=4)
        text_set_sizer.Add(self.btn_table_color_select,0,wx.LEFT,8,row=2,col=4)
        
        text_set_box_sizer.Add(text_set_sizer,0,wx.TOP,2)
        frame_sizer2_7.Add(text_set_box_sizer,1,wx.TOP|wx.EXPAND,2)
    
        #位置区域
        label_area_set = wx.StaticBox(panel,label=u"对象区域设置")
        
        self.btn_left_arrow = wx.Button(panel,label=u"左",size=(40,30))
        self.btn_right_arrow = wx.Button(panel,label=u"右",size=(40,30))
        self.btn_up_arrow = wx.Button(panel,label=u"上",size=(40,30))
        self.btn_down_arrow = wx.Button(panel,label=u"下",size=(40,30))

        label_set_position_x = wx.StaticText(panel,label=u"X位置：")
        label_set_position_y = wx.StaticText(panel,label=u"Y位置：")
        self.spin_set_position_x = wx.SpinCtrl(panel,value="40",size=(60,-1))
        self.spin_set_position_y = wx.SpinCtrl(panel,value="20",size=(60,-1))
        
        label_set_width = wx.StaticText(panel,label=u"宽度：")
        label_set_height = wx.StaticText(panel,label=u"高度：")
        self.spin_set_width = wx.SpinCtrl(panel,value="40",size=(60,-1))
        self.spin_set_height = wx.SpinCtrl(panel,value="20",size=(60,-1))

        self.spin_set_position_x.SetRange(0,10000)
        self.spin_set_position_x.SetValue(0)
        self.spin_set_position_y.SetRange(0,10000)
        self.spin_set_position_y.SetValue(0)
        
        self.spin_set_width.SetRange(0,10000)
        self.spin_set_width.SetValue(40)
        self.spin_set_height.SetRange(0,10000)
        self.spin_set_height.SetValue(20)
        
        area_set_box_sizer = wx.StaticBoxSizer(label_area_set,orient=wx.HORIZONTAL)
        object_position_sizer = rcs.RowColSizer()
        object_positionxy_sizer = wx.BoxSizer(orient=wx.VERTICAL)
        object_positionx_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        object_positiony_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        object_size_sizer = wx.BoxSizer(orient=wx.VERTICAL)
        object_width_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        object_height_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        
        object_position_sizer.Add(self.btn_left_arrow,0,wx.TOP,2,row=1,col=0)
        object_position_sizer.Add(self.btn_right_arrow,0,wx.TOP,2,row=1,col=2)
        object_position_sizer.Add(self.btn_up_arrow,0,wx.TOP,2,row=0,col=1)
        object_position_sizer.Add(self.btn_down_arrow,0,wx.TOP,2,row=2,col=1)

        object_positionx_sizer.Add(label_set_position_x,0,wx.TOP,5)
        object_positionx_sizer.Add(self.spin_set_position_x,0,wx.TOP,2)
        object_positiony_sizer.Add(label_set_position_y,0,wx.TOP,5)
        object_positiony_sizer.Add(self.spin_set_position_y,0,wx.TOP,2)
        object_positionxy_sizer.Add(object_positionx_sizer,0,wx.TOP,2)
        object_positionxy_sizer.Add(object_positiony_sizer,0,wx.TOP,2)
                
        object_width_sizer.Add(label_set_width,0,wx.TOP,5)
        object_width_sizer.Add(self.spin_set_width,0,wx.TOP,2)
        object_height_sizer.Add(label_set_height,0,wx.TOP,5)
        object_height_sizer.Add(self.spin_set_height,0,wx.TOP,2)
        object_size_sizer.Add(object_width_sizer,0,wx.TOP,2)
        object_size_sizer.Add(object_height_sizer,0,wx.TOP,2)
        
        area_set_box_sizer.Add(object_position_sizer,0,wx.LEFT|wx.ALIGN_CENTER_VERTICAL,36)
        area_set_box_sizer.Add(object_positionxy_sizer,0,wx.LEFT|wx.ALIGN_CENTER_VERTICAL,36)
        area_set_box_sizer.Add(object_size_sizer,0,wx.LEFT|wx.ALIGN_CENTER_VERTICAL,16)
        frame_sizer2_8.Add(area_set_box_sizer,1,wx.TOP,0)        
        
        #事件绑定
        self.Bind(wx.EVT_BUTTON,self.OnClickedLoadTableResource, btn_load_table_resource)
        self.Bind(wx.EVT_BUTTON,self.OnClickedLoadTableConfig, btn_load_table_config)
        self.Bind(wx.EVT_BUTTON,self.OnClickedSaveTableConfig, btn_save_table_config)
        
        self.Bind(wx.EVT_TEXT, self.OnComboBoxAccountsTextChange, self.combo_user_accounts)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnComboBoxAccountsTextEnter, self.combo_user_accounts)
        self.Bind(wx.EVT_COMBOBOX, self.OnComboBoxAccountsSelected, self.combo_user_accounts)
        self.Bind(wx.EVT_BUTTON,self.OnClickedUseAccounts, btn_use_account)
        
        self.Bind(wx.EVT_TEXT, self.OnComboBoxTableInfoTextChange, self.combo_table_info)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnComboBoxTableInfoTextEnter, self.combo_table_info)
        self.Bind(wx.EVT_COMBOBOX, self.OnComboBoxTableInfoSelected, self.combo_table_info)
        self.Bind(wx.EVT_BUTTON,self.OnClickedUseTableInfo, btn_use_table_info)
        
        self.Bind(wx.EVT_TEXT, self.OnComboBoxTableIDTextChange, self.combo_table_id)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnComboBoxTableIDTextEnter, self.combo_table_id)
        self.Bind(wx.EVT_COMBOBOX, self.OnComboBoxTableIDSelected, self.combo_table_id)
        self.Bind(wx.EVT_BUTTON,self.OnClickedUseTableID, btn_use_table_id)
        
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckBoxClickedShowObjects, self.check_show_user_face)
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckBoxClickedShowObjects, self.check_show_user_accounts)
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckBoxClickedShowObjects, self.check_show_user_ready)
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckBoxClickedShowObjects, self.check_show_table_lock)
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckBoxClickedShowObjects, self.check_show_table_info)
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckBoxClickedShowObjects, self.check_show_table_id)
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckBoxClickedShowObjects, self.check_show_face_frame)
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckBoxClickedShowObjects, self.check_show_table_dash_line)
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckBoxClickedShowObjects, self.check_show_frame_dash_line)
        
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadioClickedSelectObject, self.radio_select_user_face)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadioClickedSelectObject, self.radio_select_user_accounts)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadioClickedSelectObject, self.radio_select_user_ready)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadioClickedSelectObject, self.radio_select_table_lock)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadioClickedSelectObject, self.radio_select_table_info)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadioClickedSelectObject, self.radio_select_table_id)
        
        self.Bind(wx.EVT_COMBOBOX, self.OnComboBoxChairCountSelected, self.combo_table_chairs_count)
        self.Bind(wx.EVT_BUTTON, self.OnClickedTableChairsReverse, self.btn_table_chairs_reverse)
        self.Bind(wx.EVT_COMBOBOX, self.OnComboBoxTableChairIndexSelected, self.combo_table_chair_index)
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckBoxClickedTableVisible, self.check_table_chair_visible)
        
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadioClickedSelectTextAlignH, self.radio_text_align_h1)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadioClickedSelectTextAlignH, self.radio_text_align_h2)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadioClickedSelectTextAlignH, self.radio_text_align_h3)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadioClickedSelectTextAlignV, self.radio_text_align_v1)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadioClickedSelectTextAlignV, self.radio_text_align_v2)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadioClickedSelectTextAlignV, self.radio_text_align_v3)
        
        self.Bind(wx.EVT_SPINCTRL, self.OnSpinColorRGBSelected, self.text_color_r)
        self.Bind(wx.EVT_TEXT, self.OnSpinColorRGBChange, self.text_color_r)
        self.Bind(wx.EVT_SPINCTRL, self.OnSpinColorRGBSelected, self.text_color_g)
        self.Bind(wx.EVT_TEXT, self.OnSpinColorRGBChange, self.text_color_g)
        self.Bind(wx.EVT_SPINCTRL, self.OnSpinColorRGBSelected, self.text_color_b)
        self.Bind(wx.EVT_TEXT, self.OnSpinColorRGBChange, self.text_color_b)
        self.btn_text_color_select.Bind(csel.EVT_COLOURSELECT, self.OnColourSelectedTextColor)
        self.btn_info_color_select.Bind(csel.EVT_COLOURSELECT, self.OnColourSelectedTextColor)
        self.btn_table_color_select.Bind(csel.EVT_COLOURSELECT, self.OnColourSelectedTextColor)
        
        self.Bind(wx.EVT_BUTTON, self.OnClickedPositionMove, self.btn_left_arrow)
        self.Bind(wx.EVT_BUTTON, self.OnClickedPositionMove, self.btn_right_arrow)
        self.Bind(wx.EVT_BUTTON, self.OnClickedPositionMove, self.btn_up_arrow)
        self.Bind(wx.EVT_BUTTON, self.OnClickedPositionMove, self.btn_down_arrow)

        self.Bind(wx.EVT_SPINCTRL, self.OnSpinSetPositionSelected, self.spin_set_position_x)
        self.Bind(wx.EVT_TEXT, self.OnSpinSetPositionChange, self.spin_set_position_x)
        self.Bind(wx.EVT_SPINCTRL, self.OnSpinSetPositionSelected, self.spin_set_position_y)
        self.Bind(wx.EVT_TEXT, self.OnSpinSetPositionChange, self.spin_set_position_y)
        
        self.Bind(wx.EVT_SPINCTRL, self.OnSpinSetSizeSelected, self.spin_set_width)
        self.Bind(wx.EVT_TEXT, self.OnSpinSetSizeChange, self.spin_set_width)
        self.Bind(wx.EVT_SPINCTRL, self.OnSpinSetSizeSelected, self.spin_set_height)
        self.Bind(wx.EVT_TEXT, self.OnSpinSetSizeChange, self.spin_set_height)
        
        self.draw_table_panel.Bind(wx.EVT_KEY_DOWN,self.OnKeyDown) 
            

    def OnQuit(self, event):
        self.Close()
        
    def OnClickedLoadTableResource(self, event):
        
        dlg = wx.DirDialog(self,u"请选择房间桌子图资源目录：",style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            if len(dlg.GetPath()) > 0:
                self.table_res.LoadTableResource(dlg.GetPath())
                self.draw_table_panel.Refresh()
            
        dlg.Destroy()
        
    def OnClickedLoadTableConfig(self, event):
        
        dlg = wx.FileDialog(self,u"请选择房间桌子配置文件：",style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            if len(dlg.GetPath()) > 0:
                self.table_cfg.read(dlg.GetPath())
                self.draw_table_info.LoadTableConfig(self.table_cfg)
                if self.draw_table_info.table_chairs_count > 0:
                    self.combo_table_chairs_count.Select(self.draw_table_info.table_chairs_count-1)
            
                if self.combo_table_chairs_count.GetValue().count > 0:
                    table_chairs_count = int(self.combo_table_chairs_count.GetValue())
                    table_chair_index_list = []
                    for item in range(0, table_chairs_count): table_chair_index_list.append(str(item))
                    self.combo_table_chair_index.Set(table_chair_index_list)
                    self.combo_table_chair_index.Select(0)
                    select_object_index = int(self.combo_table_chair_index.GetValue())
                    self.UpdateTableChairData(select_object_index)
                    
                self.draw_table_panel.Refresh()
            
        dlg.Destroy()
        
    def OnClickedSaveTableConfig(self, event):
        
        dlg = wx.FileDialog(self,u"保存房间桌子配置文件：",style=wx.DD_DEFAULT_STYLE|wx.SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            if len(dlg.GetPath()) > 0:
                self.draw_table_info.SaveTableConfig(self.table_cfg)
                self.table_cfg.write(dlg.GetPath())
            
        dlg.Destroy()
        
        
    def OnComboBoxAccountsSelected(self, event):
        self.str_accounts = event.GetString()
        self.draw_table_panel.Refresh()
        
    def OnComboBoxAccountsTextChange(self, event):
        self.str_accounts = event.GetString()
        self.draw_table_panel.Refresh()
    
    def OnComboBoxAccountsTextEnter(self, event):
        self.str_accounts = event.GetString()
        self.draw_table_panel.Refresh()
    
    def OnClickedUseAccounts(self, event):
        self.draw_table_panel.Refresh()
    
    def OnComboBoxTableInfoSelected(self, event):
        self.str_table_info = event.GetString()
        self.draw_table_panel.Refresh()
        
    def OnComboBoxTableInfoTextChange(self, event):
        self.str_table_info = event.GetString()
        self.draw_table_panel.Refresh()
    
    def OnComboBoxTableInfoTextEnter(self, event):
        self.str_table_info = event.GetString() 
        self.draw_table_panel.Refresh()
    
    def OnClickedUseTableInfo(self, event): 
        self.draw_table_panel.Refresh()
    
    def OnComboBoxTableIDSelected(self, event):
        self.str_table_id = event.GetString()
        self.draw_table_panel.Refresh()
        
    def OnComboBoxTableIDTextChange(self, event):
        self.str_table_id = event.GetString()
        self.draw_table_panel.Refresh()
    
    def OnComboBoxTableIDTextEnter(self, event):
        self.str_table_id = event.GetString()
        self.draw_table_panel.Refresh()
    
    def OnClickedUseTableID(self, event):
        self.draw_table_panel.Refresh()
        
    def OnCheckBoxClickedShowObjects(self, event):
        
        self.draw_table_panel.is_show_face_frame = self.check_show_face_frame.GetValue()
        self.draw_table_panel.is_show_user_face = self.check_show_user_face.GetValue()
        self.draw_table_panel.is_show_user_accounts = self.check_show_user_accounts.GetValue()
        self.draw_table_panel.is_show_user_ready = self.check_show_user_ready.GetValue()
        self.draw_table_panel.is_show_table_lock = self.check_show_table_lock.GetValue()
        self.draw_table_panel.is_show_table_info = self.check_show_table_info.GetValue()
        self.draw_table_panel.is_show_table_id = self.check_show_table_id.GetValue()
        self.draw_table_panel.is_show_table_dash_line = self.check_show_table_dash_line.GetValue()
        self.draw_table_panel.is_show_frame_dash_line = self.check_show_frame_dash_line.GetValue()
        
        self.draw_table_panel.Refresh()
       
    
    def OnRadioClickedSelectObject(self, event):

        select_object_index = int(self.combo_table_chair_index.GetValue())
        self.UpdateTableChairData(select_object_index)
    
    def OnComboBoxChairCountSelected(self, event):

        if self.combo_table_chairs_count.GetValue().count > 0:
            table_chairs_count = int(self.combo_table_chairs_count.GetValue())
            self.UpdateTableChairCount(table_chairs_count)
            
    def OnClickedTableChairsReverse(self, event):
        
        table_info = self.draw_table_info
        if table_info == None:
            return
            
        table_chairs = []
        table_chairs_count = len(table_info.table_chairs)
        for index in range(0,table_chairs_count):
            table_chairs.append(table_info.table_chairs[table_chairs_count-1-index])
            
        table_info.table_chairs = table_chairs
        
        self.draw_table_panel.Refresh()
    
    def OnComboBoxTableChairIndexSelected(self, event):

        select_object_index = int(self.combo_table_chair_index.GetValue())
        self.UpdateTableChairData(select_object_index)
    
    def OnCheckBoxClickedTableVisible(self, event):
        
        visible = self.check_table_chair_visible.GetValue()
        self.UpdateTableShowChair(visible)
            
    def OnRadioClickedSelectTextAlignH(self, event):

        align = None

        if self.radio_text_align_h1.GetValue() :
            align = TEXT_ALIGN_LEFT
        elif self.radio_text_align_h2.GetValue() :
            align = TEXT_ALIGN_CENTER
        elif self.radio_text_align_h3.GetValue() :
            align = TEXT_ALIGN_RIGHT
        else:
            pass
        
        if align != None:
            self.UpdateTextAlignMode(align_h=align)
    
    def OnRadioClickedSelectTextAlignV(self, event):

        align = None

        if self.radio_text_align_v1.GetValue() :
            align = TEXT_ALIGN_TOP
        elif self.radio_text_align_v2.GetValue() :
            align = TEXT_ALIGN_MIDDLE
        elif self.radio_text_align_v3.GetValue() :
            align = TEXT_ALIGN_BOTTOM
        else:
            pass
        
        if align != None:
            self.UpdateTextAlignMode(align_v=align)
    
    def OnSpinColorRGBSelected(self, event):
        pass
    
    def OnSpinColorRGBChange(self, event):
        pass
    
    def OnColourSelectedTextColor(self, event):
        
        obj = event.GetEventObject()
        table_info = self.draw_table_info
        if table_info == None:
            return
        
        colorRGBA = None
        if obj is self.btn_text_color_select:
            colorRGBA = self.btn_text_color_select.GetColour()
            table_info.color_accounts[0] = colorRGBA[0]
            table_info.color_accounts[1] = colorRGBA[1]
            table_info.color_accounts[2] = colorRGBA[2]
        elif obj is self.btn_info_color_select:
            colorRGBA = self.btn_info_color_select.GetColour()
            table_info.color_table_info[0] = colorRGBA[0]
            table_info.color_table_info[1] = colorRGBA[1]
            table_info.color_table_info[2] = colorRGBA[2]
        elif obj is self.btn_table_color_select: 
            colorRGBA = self.btn_table_color_select.GetColour()
            table_info.color_table_id[0] = colorRGBA[0]
            table_info.color_table_id[1] = colorRGBA[1]
            table_info.color_table_id[2] = colorRGBA[2]
        else:
            pass
        
        if colorRGBA != None:
            self.text_color_r.SetValue(colorRGBA[0])
            self.text_color_g.SetValue(colorRGBA[1])
            self.text_color_b.SetValue(colorRGBA[2])
        
        self.draw_table_panel.Refresh()
    
    def OnClickedPositionMove(self, event):
        
        obj = event.GetEventObject()
        
        if obj is self.btn_left_arrow:
            self.UpdateTableObjectPostion(-1,0)
        elif obj is self.btn_right_arrow:
            self.UpdateTableObjectPostion(1,0)
        elif obj is self.btn_up_arrow:
            self.UpdateTableObjectPostion(0,-1)
        elif obj is self.btn_down_arrow:
            self.UpdateTableObjectPostion(0,1)
        else:
            pass

    def OnSpinSetPositionSelected(self, event):
        
        spin = event.GetEventObject()

        if spin is self.spin_set_position_x:
            self.UpdateTableObjectPostionXY(position_x=spin.GetValue())
        elif spin is self.spin_set_position_y:
            self.UpdateTableObjectPostionXY(position_y=spin.GetValue())
        else:
            pass
        
    def OnSpinSetPositionChange(self, event):

        spin = event.GetEventObject()

        if spin is self.spin_set_position_x:
            self.UpdateTableObjectPostionXY(position_x=spin.GetValue())
        elif spin is self.spin_set_position_y:
            self.UpdateTableObjectPostionXY(position_y=spin.GetValue())
        else:
            pass
        
    def OnSpinSetSizeSelected(self, event):
        
        spin = event.GetEventObject()

        if spin is self.spin_set_width:
            self.UpdateTableObjectSize(spin.GetValue(),0,True,False)
        elif spin is self.spin_set_height:
            self.UpdateTableObjectSize(0,spin.GetValue(),False,True)
        else:
            pass
        
    def OnSpinSetSizeChange(self, event):
        
        spin = event.GetEventObject()

        if spin is self.spin_set_width:
            self.UpdateTableObjectSize(spin.GetValue(),0,True,False)
        elif spin is self.spin_set_height:
            self.UpdateTableObjectSize(0,spin.GetValue(),False,True)
        else:
            pass
        
    def OnKeyDown(self, event):

        key_code = event.GetKeyCode()        
        if key_code == wx.WXK_LEFT:
            self.UpdateTableObjectPostion(-1,0)
        elif key_code == wx.WXK_RIGHT:
            self.UpdateTableObjectPostion(1,0)
        elif key_code == wx.WXK_UP:
            self.UpdateTableObjectPostion(0,-1)
        elif key_code == wx.WXK_DOWN:
            self.UpdateTableObjectPostion(0,1)
        else:
            pass

    def UpdateTableChairCount(self, table_chairs_count):

        table_info = self.draw_table_info
        if table_info == None:
            return
        
        if table_chairs_count <= 0 or table_chairs_count == self.draw_table_info.table_chairs_count:
            return
        
        if table_chairs_count < table_info.table_chairs_count:
            table_info.table_chairs_count = table_chairs_count
            table_chair_index_list = []
            for item in range(0, table_chairs_count): table_chair_index_list.append(str(item))
            select_index = self.combo_table_chair_index.GetSelection()
            self.combo_table_chair_index.Set(table_chair_index_list)
            
            if select_index < self.combo_table_chair_index.GetCount():
                self.combo_table_chair_index.Select(select_index)
                self.UpdateTableChairData(select_index)
            else:
                self.combo_table_chair_index.Select(0)
                self.UpdateTableChairData(0)
        
        else:
            
            table_info.table_chairs_count = table_chairs_count
            if len(table_info.table_chairs) < table_chairs_count:
                for item in range(0,table_chairs_count-len(table_info.table_chairs)):
                    table_info.table_chairs.append(DrawChairInfo())
            
            table_chair_index_list = []
            for item in range(0, table_chairs_count): table_chair_index_list.append(str(item))
            select_index = self.combo_table_chair_index.GetSelection()
            self.combo_table_chair_index.Set(table_chair_index_list)
            
            if select_index < self.combo_table_chair_index.GetCount():
                self.combo_table_chair_index.Select(select_index)
                self.UpdateTableChairData(select_index)
            else:
                self.combo_table_chair_index.Select(0)
                self.UpdateTableChairData(0)

        self.draw_table_panel.Refresh()
        

    def UpdateTableChairData(self, select_chair_index):
        
        table_info = self.draw_table_info
        if table_info == None:
            return
        
        if select_chair_index < table_info.table_chairs_count:
            table_chair = table_info.table_chairs[select_chair_index]
            
            if table_chair != None:

                self.check_table_chair_visible.SetValue(table_chair.visible)
                
                if self.radio_select_user_face.GetValue() :
                    self.spin_set_position_x.SetValue(table_chair.rect_chair[0])
                    self.spin_set_position_y.SetValue(table_chair.rect_chair[1])
                    self.spin_set_width.SetValue(table_chair.rect_chair[2])
                    self.spin_set_height.SetValue(table_chair.rect_chair[3])
                
                if self.radio_select_user_accounts.GetValue() :
                    self.spin_set_position_x.SetValue(table_chair.rect_accounts[0])
                    self.spin_set_position_y.SetValue(table_chair.rect_accounts[1])
                    self.spin_set_width.SetValue(table_chair.rect_accounts[2])
                    self.spin_set_height.SetValue(table_chair.rect_accounts[3])
                    self.radio_text_align_h1.SetValue(table_chair.align_mode&TEXT_ALIGN_LEFT)
                    self.radio_text_align_h2.SetValue(table_chair.align_mode&TEXT_ALIGN_CENTER)
                    self.radio_text_align_h3.SetValue(table_chair.align_mode&TEXT_ALIGN_RIGHT)
                    self.radio_text_align_v1.SetValue(table_chair.align_mode&TEXT_ALIGN_TOP)
                    self.radio_text_align_v2.SetValue(table_chair.align_mode&TEXT_ALIGN_MIDDLE)
                    self.radio_text_align_v3.SetValue(table_chair.align_mode&TEXT_ALIGN_BOTTOM)
                    self.text_color_r.SetValue(table_info.color_accounts[0])
                    self.text_color_g.SetValue(table_info.color_accounts[1])
                    self.text_color_b.SetValue(table_info.color_accounts[2])
                    rgb_color = wx.Colour(table_info.color_accounts[0], table_info.color_accounts[1], table_info.color_accounts[2], 255)
                    self.btn_text_color_select.SetColour(rgb_color)
                
                if self.radio_select_user_ready.GetValue() :
                    self.spin_set_position_x.SetValue(table_chair.rect_ready[0])
                    self.spin_set_position_y.SetValue(table_chair.rect_ready[1])
                    self.spin_set_width.SetValue(table_chair.rect_ready[2])
                    self.spin_set_height.SetValue(table_chair.rect_ready[3])
                
        if self.radio_select_table_lock.GetValue() :
            self.spin_set_position_x.SetValue(table_info.rect_table_lock[0])
            self.spin_set_position_y.SetValue(table_info.rect_table_lock[1])
            self.spin_set_width.SetValue(table_info.rect_table_lock[2])
            self.spin_set_height.SetValue(table_info.rect_table_lock[3])
            
        if self.radio_select_table_info.GetValue() :
            self.spin_set_position_x.SetValue(table_info.rect_table_info[0])
            self.spin_set_position_y.SetValue(table_info.rect_table_info[1])
            self.spin_set_width.SetValue(table_info.rect_table_info[2])
            self.spin_set_height.SetValue(table_info.rect_table_info[3])
            self.radio_text_align_h1.SetValue(table_info.table_info_align_mode&TEXT_ALIGN_LEFT)
            self.radio_text_align_h2.SetValue(table_info.table_info_align_mode&TEXT_ALIGN_CENTER)
            self.radio_text_align_h3.SetValue(table_info.table_info_align_mode&TEXT_ALIGN_RIGHT)
            self.radio_text_align_v1.SetValue(table_info.table_info_align_mode&TEXT_ALIGN_TOP)
            self.radio_text_align_v2.SetValue(table_info.table_info_align_mode&TEXT_ALIGN_MIDDLE)
            self.radio_text_align_v3.SetValue(table_info.table_info_align_mode&TEXT_ALIGN_BOTTOM)
            self.text_color_r.SetValue(table_info.color_table_info[0])
            self.text_color_g.SetValue(table_info.color_table_info[1])
            self.text_color_b.SetValue(table_info.color_table_info[2])
            rgb_color = wx.Colour(table_info.color_table_info[0], table_info.color_table_info[1], table_info.color_table_info[2], 255)
            self.btn_info_color_select.SetColour(rgb_color)
            
        if self.radio_select_table_id.GetValue() :
            self.spin_set_position_x.SetValue(table_info.rect_table_id[0])
            self.spin_set_position_y.SetValue(table_info.rect_table_id[1])
            self.spin_set_width.SetValue(table_info.rect_table_id[2])
            self.spin_set_height.SetValue(table_info.rect_table_id[3])
            self.radio_text_align_h1.SetValue(table_info.table_id_align_mode&TEXT_ALIGN_LEFT)
            self.radio_text_align_h2.SetValue(table_info.table_id_align_mode&TEXT_ALIGN_CENTER)
            self.radio_text_align_h3.SetValue(table_info.table_id_align_mode&TEXT_ALIGN_RIGHT)
            self.radio_text_align_v1.SetValue(table_info.table_id_align_mode&TEXT_ALIGN_TOP)
            self.radio_text_align_v2.SetValue(table_info.table_id_align_mode&TEXT_ALIGN_MIDDLE)
            self.radio_text_align_v3.SetValue(table_info.table_id_align_mode&TEXT_ALIGN_BOTTOM)
            self.text_color_r.SetValue(table_info.color_table_id[0])
            self.text_color_g.SetValue(table_info.color_table_id[1])
            self.text_color_b.SetValue(table_info.color_table_id[2])
            rgb_color = wx.Colour(table_info.color_table_id[0], table_info.color_table_id[1], table_info.color_table_id[2], 255)
            self.btn_table_color_select.SetColour(rgb_color)

        rgb_color = wx.Colour(table_info.color_accounts[0], table_info.color_accounts[1], table_info.color_accounts[2], 255)
        self.btn_text_color_select.SetColour(rgb_color)
        rgb_color = wx.Colour(table_info.color_table_info[0], table_info.color_table_info[1], table_info.color_table_info[2], 255)
        self.btn_info_color_select.SetColour(rgb_color)
        rgb_color = wx.Colour(table_info.color_table_id[0], table_info.color_table_id[1], table_info.color_table_id[2], 255)
        self.btn_table_color_select.SetColour(rgb_color)
            

    def UpdateTableObjectPostion(self, delta_x, delta_y):
        
        select_object_index = int(self.combo_table_chair_index.GetValue())
        table_info = self.draw_table_info
        if table_info == None:
            return
        
        if select_object_index < table_info.table_chairs_count:
            table_chair = table_info.table_chairs[select_object_index]
            
            if table_chair != None:
                if self.radio_select_user_face.GetValue() :
                    table_chair.rect_chair[0] += delta_x
                    table_chair.rect_chair[1] += delta_y
                    self.spin_set_position_x.SetValue(table_chair.rect_chair[0])
                    self.spin_set_position_y.SetValue(table_chair.rect_chair[1])
                
                if self.radio_select_user_accounts.GetValue() :
                    table_chair.rect_accounts[0] += delta_x
                    table_chair.rect_accounts[1] += delta_y
                    self.spin_set_position_x.SetValue(table_chair.rect_accounts[0])
                    self.spin_set_position_y.SetValue(table_chair.rect_accounts[1])
                
                if self.radio_select_user_ready.GetValue() :
                    table_chair.rect_ready[0] += delta_x
                    table_chair.rect_ready[1] += delta_y
                    self.spin_set_position_x.SetValue(table_chair.rect_ready[0])
                    self.spin_set_position_y.SetValue(table_chair.rect_ready[1])
                
        if self.radio_select_table_lock.GetValue() :
            table_info.rect_table_lock[0] += delta_x
            table_info.rect_table_lock[1] += delta_y
            self.spin_set_position_x.SetValue(table_info.rect_table_lock[0])
            self.spin_set_position_y.SetValue(table_info.rect_table_lock[1])
            
        if self.radio_select_table_info.GetValue() :
            table_info.rect_table_info[0] += delta_x
            table_info.rect_table_info[1] += delta_y
            self.spin_set_position_x.SetValue(table_info.rect_table_info[0])
            self.spin_set_position_y.SetValue(table_info.rect_table_info[1])
            
        if self.radio_select_table_id.GetValue() :
            table_info.rect_table_id[0] += delta_x
            table_info.rect_table_id[1] += delta_y
            self.spin_set_position_x.SetValue(table_info.rect_table_id[0])
            self.spin_set_position_y.SetValue(table_info.rect_table_id[1])
            
        self.draw_table_panel.Refresh()

    def UpdateTableObjectPostionXY(self, position_x = None, position_y = None):
        
        select_object_index = int(self.combo_table_chair_index.GetValue())
        table_info = self.draw_table_info
        if table_info == None:
            return
        
        if select_object_index < table_info.table_chairs_count:
            table_chair = table_info.table_chairs[select_object_index]
            
            if table_chair != None:
                if self.radio_select_user_face.GetValue() :
                    if position_x != None: table_chair.rect_chair[0] = position_x
                    if position_y != None: table_chair.rect_chair[1] = position_y
                
                if self.radio_select_user_accounts.GetValue() :
                    if position_x != None: table_chair.rect_accounts[0] = position_x
                    if position_y != None: table_chair.rect_accounts[1] = position_y
                
                if self.radio_select_user_ready.GetValue() :
                    if position_x != None: table_chair.rect_ready[0] = position_x
                    if position_y != None: table_chair.rect_ready[1] = position_y
                
        if self.radio_select_table_lock.GetValue() :
            if position_x != None: table_info.rect_table_lock[0] = position_x
            if position_y != None: table_info.rect_table_lock[1] = position_y
            
        if self.radio_select_table_info.GetValue() :
            if position_x != None: table_info.rect_table_info[0] = position_x
            if position_y != None: table_info.rect_table_info[1] = position_y
            
        if self.radio_select_table_id.GetValue() :
            if position_x != None: table_info.rect_table_id[0] = position_x
            if position_y != None: table_info.rect_table_id[1] = position_y
            
        self.draw_table_panel.Refresh()

        
    
    def UpdateTableObjectSize(self, width, height, change_width = True, change_height = True):
        
        select_object_index = int(self.combo_table_chair_index.GetValue())
        table_info = self.draw_table_info
        if table_info == None:
            return
        
        if select_object_index < table_info.table_chairs_count:
            table_chair = table_info.table_chairs[select_object_index]
            
            if table_chair != None:
                if self.radio_select_user_face.GetValue() :
                    if change_width == True : table_chair.rect_chair[2] = width
                    if change_height == True: table_chair.rect_chair[3] = height
                
                if self.radio_select_user_accounts.GetValue() :
                    if change_width == True : table_chair.rect_accounts[2] = width
                    if change_height == True: table_chair.rect_accounts[3] = height
                
                if self.radio_select_user_ready.GetValue() :
                    if change_width == True : table_chair.rect_ready[2] = width
                    if change_height == True: table_chair.rect_ready[3] = height
                
        if self.radio_select_table_lock.GetValue() :
            if change_width == True : table_info.rect_table_lock[2] = width
            if change_height == True: table_info.rect_table_lock[3] = height
            
        if self.radio_select_table_info.GetValue() :
            if change_width == True : table_info.rect_table_info[2] = width
            if change_height == True: table_info.rect_table_info[3] = height
            
        if self.radio_select_table_id.GetValue() :
            if change_width == True : table_info.rect_table_id[2] = width
            if change_height == True: table_info.rect_table_id[3] = height
            
        self.draw_table_panel.Refresh()


    def UpdateTextAlignMode(self, align_h = None, align_v = None):

        select_object_index = int(self.combo_table_chair_index.GetValue())
        table_info = self.draw_table_info
        if table_info == None:
            return
        
        if select_object_index < table_info.table_chairs_count:
            table_chair = table_info.table_chairs[select_object_index]
            
            if table_chair != None:
                if self.radio_select_user_accounts.GetValue() :
                    if align_h != None : table_chair.align_mode = ((table_chair.align_mode&(~0x0F))|align_h)
                    if align_v != None : table_chair.align_mode = ((table_chair.align_mode&(~0xF0))|align_v)
                    self.draw_table_panel.Refresh()
            
        if self.radio_select_table_info.GetValue() :
            if align_h != None : table_info.table_info_align_mode = ((table_info.table_info_align_mode&(~0x0F))|align_h)
            if align_v != None : table_info.table_info_align_mode = ((table_info.table_info_align_mode&(~0xF0))|align_v)
            self.draw_table_panel.Refresh()
            
        if self.radio_select_table_id.GetValue() :
            if align_h != None : table_info.table_id_align_mode = ((table_info.table_id_align_mode&(~0x0F))|align_h)
            if align_v != None : table_info.table_id_align_mode = ((table_info.table_id_align_mode&(~0xF0))|align_v)
            self.draw_table_panel.Refresh()
            
            
    def UpdateTableShowChair(self, visible):
        select_object_index = int(self.combo_table_chair_index.GetValue())
        table_info = self.draw_table_info
        if table_info == None:
            return
        
        if select_object_index < table_info.table_chairs_count:
            table_chair = table_info.table_chairs[select_object_index]
            
            if table_chair != None and table_chair.visible != visible:
                table_chair.visible = visible
                self.draw_table_panel.Refresh()
            
            
        

class RoomTableConfigureApp(wx.App):  

    def OnInit(self):
        frame = MainFrame()
        frame.Show(True)
        return True


def main():
    """software start runing """
    
    app = RoomTableConfigureApp()  
    app.MainLoop()
    
    return

									
if __name__ == '__main__':
    main()

        
