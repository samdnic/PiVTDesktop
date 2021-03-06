# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Nov  6 2013)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class CorePanel
###########################################################################

class CorePanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 667,352 ), style = wx.TAB_TRAVERSAL )
		
		mainSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		leftSizer = wx.BoxSizer( wx.VERTICAL )
		
		leftSizer.SetMinSize( wx.Size( 100,-1 ) ) 
		self.lstPlaylist = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_NO_SORT_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.LC_VRULES )
		self.lstPlaylist.SetMinSize( wx.Size( 100,-1 ) )
		
		leftSizer.Add( self.lstPlaylist, 1, wx.ALL|wx.EXPAND, 5 )
		
		plbuttonsSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnAdd = wx.Button( self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.btnAdd.Enable( False )
		
		plbuttonsSizer.Add( self.btnAdd, 0, wx.ALL, 5 )
		
		self.btnUp = wx.Button( self, wx.ID_ANY, u"Move Up", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		plbuttonsSizer.Add( self.btnUp, 0, wx.ALL, 5 )
		
		self.btnDown = wx.Button( self, wx.ID_ANY, u"Move Down", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		plbuttonsSizer.Add( self.btnDown, 0, wx.ALL, 5 )
		
		self.btnRemove = wx.Button( self, wx.ID_ANY, u"Remove", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		plbuttonsSizer.Add( self.btnRemove, 0, wx.ALL, 5 )
		
		
		leftSizer.Add( plbuttonsSizer, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		mainSizer.Add( leftSizer, 1, wx.EXPAND, 0 )
		
		rightSizer = wx.GridBagSizer( 5, 5 )
		rightSizer.SetFlexibleDirection( wx.BOTH )
		rightSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		rightSizer.SetMinSize( wx.Size( 300,-1 ) ) 
		self.btnPlay = wx.Button( self, wx.ID_ANY, u"Play", wx.DefaultPosition, wx.Size( 120,50 ), 0 )
		self.btnPlay.Enable( False )
		
		rightSizer.Add( self.btnPlay, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		self.btnStop = wx.Button( self, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.Size( 120,50 ), 0 )
		self.btnStop.Enable( False )
		
		rightSizer.Add( self.btnStop, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.chkAuto = wx.CheckBox( self, wx.ID_ANY, u"Auto-play next item", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.chkAuto.Enable( False )
		
		rightSizer.Add( self.chkAuto, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.lblCountdown = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,80 ), wx.TE_CENTRE|wx.TE_READONLY|wx.NO_BORDER )
		self.lblCountdown.SetFont( wx.Font( 60, 70, 90, 90, False, wx.EmptyString ) )
		self.lblCountdown.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
		self.lblCountdown.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.lblCountdown.SetMaxSize( wx.Size( -1,80 ) )
		
		rightSizer.Add( self.lblCountdown, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )
		
		self.lblPlayLabel = wx.StaticText( self, wx.ID_ANY, u"Now Playing:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.lblPlayLabel.Wrap( -1 )
		rightSizer.Add( self.lblPlayLabel, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.lblPlaying = wx.StaticText( self, wx.ID_ANY, u"None", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.lblPlaying.Wrap( 0 )
		rightSizer.Add( self.lblPlaying, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		self.lblLoadLabel = wx.StaticText( self, wx.ID_ANY, u"Loaded:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.lblLoadLabel.Wrap( -1 )
		rightSizer.Add( self.lblLoadLabel, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.lblLoaded = wx.StaticText( self, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblLoaded.Wrap( -1 )
		rightSizer.Add( self.lblLoaded, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
		
		self.lblConnectedLabel = wx.StaticText( self, wx.ID_ANY, u"Status:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.lblConnectedLabel.Wrap( -1 )
		rightSizer.Add( self.lblConnectedLabel, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.lblConnected = wx.StaticText( self, wx.ID_ANY, u"Not Connected", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblConnected.Wrap( -1 )
		rightSizer.Add( self.lblConnected, wx.GBPosition( 7, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
		
		
		rightSizer.AddGrowableCol( 0 )
		rightSizer.AddGrowableCol( 1 )
		rightSizer.AddGrowableCol( 2 )
		
		mainSizer.Add( rightSizer, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( mainSizer )
		self.Layout()
		
		# Connect Events
		self.lstPlaylist.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.OnPLSelect )
		self.lstPlaylist.Bind( wx.EVT_LIST_ITEM_SELECTED, self.OnPLSelect )
		self.btnAdd.Bind( wx.EVT_BUTTON, self.OnAdd )
		self.btnUp.Bind( wx.EVT_BUTTON, self.OnMoveUp )
		self.btnDown.Bind( wx.EVT_BUTTON, self.OnMoveDown )
		self.btnRemove.Bind( wx.EVT_BUTTON, self.OnRemove )
		self.btnPlay.Bind( wx.EVT_BUTTON, self.OnPlay )
		self.btnStop.Bind( wx.EVT_BUTTON, self.OnStop )
		self.chkAuto.Bind( wx.EVT_CHECKBOX, self.OnchkAutoChange )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnPLSelect( self, event ):
		event.Skip()
	
	
	def OnAdd( self, event ):
		event.Skip()
	
	def OnMoveUp( self, event ):
		event.Skip()
	
	def OnMoveDown( self, event ):
		event.Skip()
	
	def OnRemove( self, event ):
		event.Skip()
	
	def OnPlay( self, event ):
		event.Skip()
	
	def OnStop( self, event ):
		event.Skip()
	
	def OnchkAutoChange( self, event ):
		event.Skip()
	

###########################################################################
## Class dlgConnectOptions
###########################################################################

class dlgConnectOptions ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Connection Options", pos = wx.DefaultPosition, size = wx.Size( 234,130 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		Sizer = wx.GridBagSizer( 0, 0 )
		Sizer.SetFlexibleDirection( wx.BOTH )
		Sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.txtServer = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Sizer.Add( self.txtServer, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.txtPort = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Sizer.Add( self.txtPort, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.btnOk = wx.Button( self, wx.ID_OK, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		Sizer.Add( self.btnOk, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.btnCancel = wx.Button( self, wx.ID_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		Sizer.Add( self.btnCancel, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.lblHost = wx.StaticText( self, wx.ID_ANY, u"Server:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.lblHost.Wrap( -1 )
		Sizer.Add( self.lblHost, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.lblPort = wx.StaticText( self, wx.ID_ANY, u"Port:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.lblPort.Wrap( -1 )
		Sizer.Add( self.lblPort, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( Sizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class dlgAddItems
###########################################################################

class dlgAddItems ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add Video", pos = wx.DefaultPosition, size = wx.Size( 376,112 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		Sizer = wx.GridBagSizer( 5, 5 )
		Sizer.SetFlexibleDirection( wx.BOTH )
		Sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		Sizer.SetMinSize( wx.Size( 350,112 ) ) 
		ddVideoListChoices = []
		self.ddVideoList = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ddVideoListChoices, wx.CB_SORT )
		self.ddVideoList.SetSelection( 0 )
		Sizer.Add( self.ddVideoList, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.lblSelectFile = wx.StaticText( self, wx.ID_ANY, u"Select file:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblSelectFile.Wrap( -1 )
		Sizer.Add( self.lblSelectFile, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnAdd = wx.Button( self, wx.ID_OK, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		Sizer.Add( self.btnAdd, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.btnCancel = wx.Button( self, wx.ID_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		Sizer.Add( self.btnCancel, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		Sizer.AddGrowableCol( 1 )
		
		self.SetSizer( Sizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

