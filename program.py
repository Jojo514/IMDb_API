#
# Description: Finding the title and year of a movie if available via IMDB and the OMDb API
# Link to OMDb API: www.omdbapi.com
#
# To run program, enter following command in command line where movie_name = argument:
#   python program.py movie_name
#
# SAMPLE USAGE SESSION(S):
#   batman:
#       python program.py batman
#   avengers:
#       python program.py avengers

import sys
import json, requests

def main(argv):
    movie_Name = argv[0]
    base_url = "http://www.omdbapi.com/?t="
    url = base_url + movie_Name
    response = requests.get(url)
    movie_dict = json.loads(response.text)
    if(movie_dict.get("Response") == "True"):
        print("Title :" + movie_dict.get("Title"))
        print("Year: "  + movie_dict.get("Year"))
    else:
        print("ERROR: " + movie_dict.get("Error"))
    return

if __name__ == "__main__":
    main(sys.argv[1:])

