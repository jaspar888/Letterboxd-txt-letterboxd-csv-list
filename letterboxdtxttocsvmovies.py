from imdb import IMDb 
import csv 
filename = input("What is the exact name of the text file you want me to read? (must be in the same direcotry as this script!): ")
ia = IMDb()

#makes the csv file blank and puts Title at the top, bc thats what letterboxd needs for it to be compatible
with open('IMPORT_THIS_TO_LETTERBOXD.csv', mode='w') as csv1:
    csv2 = csv.writer(csv1, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv2.writerow(['Title'])

#read the file then itterate thrrough all lines of the file
#encoding is special because of special foreign characters n long lists
f = open(filename, "r", encoding='utf-8')

for line in f:
    try:
        #remove cringe
        movee = line
        characters = [".", "+", "(", ")", "-", "_", "   ", "  "]
        for character in characters:
            if character in movee:
                movee = movee.replace(character, " ")
            else:
                pass
        #fucking end me, yes this is necasary and helps
        extentions = ["mp4", "mov", "mkv", "avi", "bluray", "1080p", "720p", "x264", "x.264", "h264", "X 264", "H264", "H.264", 
        "H 264", "FLAC", "1.0", "1 0", "AC3", "AAC", "2.0", "DD2", "DDP", "AVC", "DVDRip", "BDRip", "Cam", "Remux", "WEBRip", "WEBDL", "WEB-DL", 
        "DVD-R", "DVDR", "DVDs", "DVD", "BGRip", "Criterion", "VHSRip", "HDRip", "TVRip", "TV", "REPACK", "VIMEO", "AMZN", "AMAZON", "LDRip", 
        "NoAudio", "576p", "1480x1080", "James Benning", "Jean-marie Straub", "Danièle Huillet", "Straub-Huillet", "Stan Brakhage", 
        "R Bruce Elder", "David Cronenberg", "Phil Solomon", "Adam Curtis", "Andy Warhol", "Marguerite Duras", "Akira Kurosawa", 
        "Robert Beavers", "Andrei Tarkovsky", "Ion De Sosa", "John Abraham", 'Nathaniel Dorsky', "Akira Kurosawa’s", 'Cinefeel', 'Handjob', 
        'bipolar', 'epsilon', 'melite', 'Sbr', 'crtlhd', 'Bmp', 'ijia', 'usury', 'ghouls', 'deep', 'crx', 'joma', 'kesh', 'sinners', 'wise', 
        'LAA', '7sins', 'Viethd', 'Llama', 'redblade', 'yellowbird', 'mrthe', 'fgt', 'prfb', 'HPN', 'whren', 'pfa', 'zpz', 'amiable', 'HJ', 
        'Don', 'depth', 'sal', 'mfcorrea', 'antsy', 'nova', 'ibex', 'creepshow', 'CG', 'KG', 'TCO', 'Sistiaga', 'BeiTai', '900pence', 
        'collection', "remastered", "BluRay", "Criterion", "[rip]", "480p", "iBEX", "[", "]", "rip", "hd4u", "X2647SinS", "HANDJOB", "Zog", 
        "RedBlade", "YELLOWBiRD", "2 0", "FGT", "PRFB", "Critterior", "PAL", "264", "Bluray", "WHRen", "XviD", "zPZ", "X264AMIABLE", 
        "REMASTERED", "VietHD", "Restored", "AMIABLE", "SaL", "bdrip", "AHB", "WHRen", "DD5", "REMUX", "USURY", "brmp", "HiFi", "DTSMA", 
        "FAPCAVE", "DD+2", "QOQ", "XViD", "DTSHD", "BluDragon", "SbR", "DD+5", "NTSC", "0ZN", "iFT", "FrOnkY", "EXTENDED", "SUBBED", "USURY", 
        "DTS", "decibeL", "DON", "X264", "ABM", "DTSFGT", "CiNEFiLE", "SiNNERS", "traVis", "RiTALiN", "SPOOKS", "CiNEMAGROTESQUE", "COMMKESH", 
        "THORA", "GCJM", "sub", "RIYE", "MEPHiSTO786", "5 1", "KINeMA", "BRMP", "esp", "eng", "SADPANDA", "PHOBOS", "REMUXFraMeSToR", 
        "DiVULGED", "CMYK", "monkee", "DD+2", "nstr", "PBS", "pbs", "Public", "BiPOLAR", "N1C", "alfa", "psychd", "ac3", "Ctrl", 
        "T,O,U,C,H,I,N,G", "CiNEMAGROTESQUE", "VHSrip", "AquA", "KRaLiMaRKo", "3ivxPoutineKing", "Distanasia", "pirata00", "PTBar", 
        "SILENT", "DEPTH", "KinghdDOWNLOAD", "MP4", "dev0", "SADPANDA", "DD5", "5REMUX", "Short", "dps", "WebDL", "Dariush", "ExREN", 
        "5 1", "NF", "BmP", "USURY", "cinefile", "GECKOS", "spooks", "limited", "MeFecit", "4U", "KJNU", "CHD", "DD", "MPEG2", 
        "REMUXRPG", "HD", "killerhd", "GHOULS", "ZineSouce", "MAYS", " 0 ", "WHRen", "AVRS", "RUT", "WEB DL", "PRAGMA", "DIR", 
        "KESH", "0FBF0E45", "eXo", "WiSE", " X ", "7SinS", "PRAGMA", "CAM", "INTERNAL", " h ", " R ", "LIMITED", " 1 ", " EA ", 
        "x260bit", " MA ", "de42", "DXVA", "Blu Ray", "Amazon", "Frederick Wiseman", " ZN ", "CRITERION", "Ken jacobs", 
        "Kenneth Anger", "Jacques Rivette", "John Smith", "Kenneth Anger", "FraMeSToR", " SD", " 5", "DOWNLOAD", " hd ", "rovers", 
        "Rip", "Collection"]
        #remove more cringe
        for extention in extentions:
            if extention in movee:
                movee = movee.replace(extention, "")
            else:
                pass
            #search n print result then write to the csv we made earlier
        
        for year in range(1900, 2021):
            if str(year) in movee:
                
                movee = movee.replace(str(year), "")
            #else IndexError: 
                #pass
        movie = ia.search_movie(movee)
        #only prints the first search result
        print(movie[0])
        with open('IMPORT_THIS_TO_LETTERBOXD.csv', mode='a') as csv1:
            csv2 = csv.writer(csv1, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv2.writerow([movie[0]])

    except IndexError:
        #when it cant find the movie, it adds it to a text file so you know what movies you need to add manually
        print("could not find " + movee)
        cum = open("COULD_NOT_FIND_THESE_FILMS_LIST.txt", "a", encoding='utf-8')
        cum.write(line)