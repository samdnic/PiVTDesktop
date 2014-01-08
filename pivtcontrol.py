import logging
import asyncore
import asynchat
import socket
import shlex
import wx
import threading
from time import sleep
import re

class PiVTControl(asynchat.async_chat):
	"""Sends messages to a VT servers and handles status update responses
	
	"""
	
	playing = ""
	loaded = ""
	connected = False
	
	def __init__(self, server, conn_cb, data_cb):
		splits = server.split(':')
		self.server = server
		self.conn_cb = conn_cb
		self.data_cb = data_cb
		
		host = splits[0]
		port = int(splits[1])
		if port == "" or host == "":
			wx.MessageBox('Bad server', 'Failed to connect', 
						wx.ICON_ERROR | wx.OK)
			raise IndexError
		
		# Ok, try to connect
		self.databuffer = []
		
		try:
			asynchat.async_chat.__init__(self)
			self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
			self.connect((host, port))
		except socket.error, e:
			wx.MessageBox('Error: {0}'.format(e.message), 'Failed to connect', 
						  wx.ICON_ERROR | wx.OK)
			print "Fail!"
			raise Exception
	
	def get_info(self):
		if self.connected == True:
			self.push("i\r\n")
	
	def stop(self):
		if self.connected == True:
			self.push("s\r\n")
			self.playing = ""
			
	def play(self):
		if self.connected == True:
			if self.loaded != "":
				self.push("p\r\n")
				self.playing = self.loaded
				self.loaded = ""
			else:
				wx.MessageBox('Cannot play with nothing loaded!', 'Error',
							wx.ICON_ERROR | wx.OK)
			
	def load(self, filename):
		if self.connected == True:
			self.push('l "{0}"\r\n'.format(filename))
			self.loaded = "filename"
	
	def handle_connect(self):
		print "Connected!"
		self.connected = True
		self.set_terminator("\n")
		self.conn_cb()
		
	def collect_incoming_data(self, data):
		self.databuffer.append(data)
		
	def found_terminator(self):		
		msg = ''.join(self.databuffer)
		self.databuffer = []
		
		if msg.startswith("Welcome to PiVT"):
			return
		
		message = re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', msg)
		
		if len(message) < 1:
			return
		
		if message[0].startswith('200'):
			# Got a 200 status update
			playgroups = shlex.split(message[0])
			print(repr(playgroups))
			if playgroups[1] == "Playing":
				self.playing = playgroups[2]
			else:
				self.playing = ""
				
			loadgroups = shlex.split(message[1])
			print(repr(loadgroups))
			if loadgroups[0] == "Loaded":
				self.loaded = loadgroups[1]
			else:
				self.loaded = ""
				
			numbers = float(shlex.split(message[2])[0])
			
			self.data_cb(numbers)
			
		elif message[0].startswith('202'):
			# 202 Playing - respond with info request for accurate time
			self.get_info()
		
		elif message[0].startswith('204'):
			splits = shlex.split(message[0])
			if splits[1] == 'Stopped':
				self.playing = ""
				self.data_cb(None)
			else:
				self.playing = splits[2]
				numbers = float(splits[3])
				self.data_cb(numbers)
			
		else:
			wx.MessageBox(msg, 'Error', wx.ICON_WARNING | wx.OK)	
			
	def startup_async(self):
		self.run = True
		self.netthread = threading.Thread(target=self.runner)
		self.netthread.start()
			
	def runner(self):
		while self.run:
			asyncore.poll(0.1)