<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo_name, twitter_handle, email, project_title, project_description
-->

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/jaspar888/Letterboxd-txt-letterboxd-csv-list/">
   
  </a>

  <h3 align="center">txt to Letterboxd csv</h3>

  <p align="center">
    Turn your txt for installed movies into a Letterboxd compatible .csv file
    <br />
  </p>
</p>

<!-- ABOUT THE PROJECT -->
## About The Project

This is a basic python script that will turn the .txt file of all the movies you have on your harddrive into a letterboxd compatible .csv file that you can import when making a "to watch list" or something of the sort. 

This exists because Letterboxd struggles with file names of downloaded movies, so instead this python script runs it through imdb's search instead, because it is much better than Letterboxd's. 

Any movie that imdb cannot find will be put into a seperate .txt file called "COULD_NOT_FIND_THESE_FILMS_LIST.txt", you will have to add these movies to your letterboxd list manually.

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these steps. 
MAKE SURE YOUR TXT LIST IS CALLED "torrents.txt" OTHERWISE THE SCRIPT WILL NOT WORK

### Prerequisites

These are the things you are going to need to have installed for this script to work.
* Python and pip

* imdb py (api for imdb)
  ```sh
  pip install imdbpy
  ```

* csv (comes with python)

* regex (comes with python)
### Installation

1. Download the script

2. Make sure you dont have any files named "IMPORT_THIS_TO_LETTERBOXD.csv" or "COULD_NOT_FIND_THESE_FILMS_LIST.txt"

3. Run the script
   and make sure you have a good internet connection and time, python isnt known for its efficiency. 


<!-- CONTACT -->
## Contact

Jaspar C (jaspar7077@gmail.com)
Discord (Jazzie#8323)
My Discord server (https://discord.gg/QMzHC6q9vR)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/github_username
