from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import instaloader
import requests
import threading
import os

def media():
	link = 'https://www.instagram.com/p/CgXMTfvjNkt/?utm_source=ig_web_copy_link'
	if 'https://www.instagram.com/p/' in link:
		print(True)
		try :
			# Function to check the internet connection
			def connection(url='http://www.google.com/', timeout=5):
				try:
					req = requests.get(url, timeout=timeout)
					req.raise_for_status()
					return True
				except requests.HTTPError as error:
					messagebox.showerror('Error',f'Checking Internet Connection Failed, Status Code: {error.response.status_code}')
				except requests.ConnectionError:
					messagebox.showerror('Error','No Internet Connection Available.')
					return False
			print(connection())

			if connection()==True:
				print(True)
				location = filedialog.askdirectory()
				os.chdir(location)                    
				short_link = link.replace('https://www.instagram.com/p/','').replace('/?utm_source=ig_web_copy_link','')
				# short_link = 'CgXMTfvjNkt'
				L = instaloader.Instaloader()
				post = instaloader.Post.from_shortcode(L.context,short_link)
				# post = instaloader.Reel.from_shortcode(L.context,short_link)
				L.download_post(post,target=short_link)
				messagebox.showinfo('Status','Download Completed !')
		except Exception as e:
			messagebox.showerror('Error','URL Is Incorrect')
	else :
		messagebox.showerror('Error','URL Not Found')
	print('done')
# thread is a separate flow of execution. This means that our program will have two things happening at once
threading.Thread(target=media).start() 