from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

#arguments = {"keywords":"Marlon Wayans", "limit":20,
             #"print_urls":True, "output_directory":"d://pics"}

#response.download(arguments)  

arguments = {"keywords":"Marlon Wayans","keywords":" ali","specific_site" : "https://www.pinterest.com/",
             "limit":100, "print_urls":True, "output_directory":"d://pics",}
response.download(arguments)