from __future__ import print_function

import requests

CPI_DATA_URL = 'http://research.stlouisfed.org/fred2/data/CPIAUCSL.txt'
class CPIDATA(object):
    """Abstraction of the CPI data provided by FRED
    This stores internally only one value per year
    """

    def __init__(self):
        #Each year available to the dataset will end up as a simple key-value
        #pair within this dict. We don't really need any order here so going
        #with a plain old dictionary is the best approach
        self.year_cpi = {}

        #Later on we will also remember the first and the last year we
        #have found in the dataset to handle years prior or after the
        #documented time span
        self.last_year = None
        self.first_year = None

    def load_from_url(self, url, save_as_file=None):
        """Loads data from a given url.

        The downloaded file can also be saved into a location for later
        re-use with the "save_as_file" parameter specifying a filename

        After fetching the file this implementation uses load_from_file
        internally
        """

    def load_from_file(self, fp):
        """Loads CPI data from a given file-like object."""

    def get_adjusted_price(self, price, year, current_year=None):
        """Returns the adapted price from a given year compared to what current
        year has been specified

        """


def main():
    """This function handles the actual logic of this script"""

    #Grap CPI/Inflation data

    #Grab API/game platform data

    #Figure out the current price of each platform
    #This will require looping through each game platform we received, and
    #calculat the adjusted price based on the CPI data we also received
    #During this point, we should also validate our data so we do not skew
    #our results

    #Generate a plot/bar graph for the adjusted price data

    #Generate a CSV file to save for the adjusted price data
