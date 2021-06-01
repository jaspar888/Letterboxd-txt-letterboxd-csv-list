from imdb import IMDb 
import csv 

#Todo, read a file, get rid of junk, get imbd to search for the movie names induvidually, add those to .csv
ia = IMDb()
#makes the csv file blank and puts Title at the top, bc thats what letterboxd needs for it to be compatible
with open('employee_file.csv', mode='w') as csv1:
    csv2 = csv.writer(csv1, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv2.writerow(['Title'])
#read the file then itterate thrrough all lines of the file
f = open("torrents.txt", "r", encoding='utf-8')
for line in f:
    try:
        movee = line.replace(".", " ")
        movie = ia.search_movie(movee)
        #only prints the first search result
        print(movie[0])
        with open('IMPORT_THIS_TO_LETTERBOXD.csv', mode='a') as csv1:
            csv2 = csv.writer(csv1, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv2.writerow([movie[0]])
    except IndexError:
        #when it cant find the movie, it adds it to a text file so you know what movies you need to add manually
        print("could not find " + line)
        c = open("COULD_NOT_FIND_THESE_FILMS_LIST.txt", "a", encoding='utf-8')
        c.write(line)
    except:
        #catches all errors, your guess is as good as mine, but check that you have all the files, cause maybe your firewall is blocking the script from making files?
        print("something went very wrong")