from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

#arguments = {"keywords":"Marlon Wayans", "limit":20,
             #"print_urls":True, "output_directory":"d://pics"}

#response.download(arguments)  

argument1 = {"keywords":"Marsha Mason,Martin Balsam,Martin Landau,Martin Sheen,Mary McDonnell,Mary Steenburgen", "specific_site" : "http://pinterest.com/",
            "print_urls":False,"limit":2, "output_directory":"d://pics",
            "chromedriver": "E:chromedriver.exe"}
response.download(argument1)




