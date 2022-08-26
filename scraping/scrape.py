from tkinter import messagebox
from tkinter import filedialog
import instaloader
import requests
import threading
import os

def media(link):
    
	if 'https://www.instagram.com/reel/' in link:
        
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
				print('connected!')
			                   
				short_link = link.replace('https://www.instagram.com/reel/','').replace('/?utm_source=ig_web_copy_link','')
				L = instaloader.Instaloader()
				L.dirname_pattern = fr'instagram_videos\{short_link}'
				print('login...')
				print(short_link)
				try:
					L.login('apptest78', 'z9x8y7')
				except:
					print('failed to login')
					
				print('logged in!')
			

				post = instaloader.Post.from_shortcode(L.context,short_link)
				L.download_post(post,target=short_link)

                

                
				
		except Exception as e:
			print(e)
			messagebox.showerror('Error','No Connection')
	else :
		messagebox.showerror('Error','URL Not Found')
	print('done')



