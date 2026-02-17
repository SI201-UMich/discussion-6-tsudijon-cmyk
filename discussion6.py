import unittest
import os
import csv

class HorseRaces:
    def __init__(self, filename):
        self.race_dict = self.load_results(self.process_csv(filename))

    def process_csv(self, f):
        '''
        Parameters: 
            f, name or path or CSV file: string

        Returns:
            list of lists
        '''
        table = []

        # Do not modify this code
        # This opens the CSV and saves it as a list of lists
        base_path = os.path.abspath(os.path.dirname(__file__))
        full_path = os.path.join(base_path, f)
        # Open the file to be read by Python
        with open(full_path) as file:
            # Get each of the rows in this file
            rows = file.readlines()
            for row in rows:
                # Because this is a CSV, we SPLIT the row by commas
                # We go through each line and build a list of cells
                table_row = []
                for cell in row.strip().split(','):
                    table_row.append(cell)
                # Append the list of cells to the table
                table.append(table_row)
        # print(table)
        return table

###############################################################################
##### TASK 1
###############################################################################
    def load_results(self, table):
        '''
        Given the processed CSV (as a list of lists), populate a nested dictionary with the horse information.
        '''
        race_dict = {}

        headers = table[0][1:]

        for row in table[1:]:
            horse_name = row[0]
            times = row[1:]

            race_dict[horse_name] = {}

            for i in range(len(headers)):
                race_name = headers[i]
                race_time = float(times[i])
                race_dict[horse_name][race_name] = race_time

        return race_dict

###############################################################################
##### TASK 2
###############################################################################

    def horse_fastest_race(self, horse):
        '''
        Given the name of a horse, return its fastest race and time.
        If the horse does not exist, return (None, 999.9)
        '''
        if horse not in self.race_dict:
            return (None, 999.9)

        races = self.race_dict[horse]

        fastest_race = None
        fastest_time = 999.9

        for race, time in races.items():
            if time < fastest_time:
                fastest_time = time
                fastest_race = race

        return (fastest_race, fastest_time)

###############################################################################
##### TASK 3
###############################################################################
        
    def horse_personal_best(self):
        '''
        Calculate the fastest race and time for each horse.
        '''
        personal_bests = {}

        for horse in self.race_dict:
            personal_bests[horse] = self.horse_fastest_race(horse)

        return personal_bests

###############################################################################
##### TASK 4
###############################################################################

    def get_average_time(self):
        '''
        Calculate the average race time for each horse.
        '''
        averages = {}

        for horse, races in self.race_dict.items():
            total_time = 0
            count = 0

            for time in races.values():
                total_time += time
                count += 1

            averages[horse] = total_time / count

        return averages

###############################################################################
##### DO NOT MODIFY THE UNIT TESTS BELOW!
###############################################################################
class dis7_test(unittest.TestCase):
    '''
    Unit tests to check that our functions were implemented correctly.
    '''
    def setUp(self):
        self.horse_races = HorseRaces('race_results.csv')

    def test_load_results(self):
        # Check that outer values are dictionaries
        self.assertIsInstance(self.horse_races.race_dict['Special Week'], dict)
        # Check one horse's time
        self.assertAlmostEqual(self.horse_races.race_dict['Special Week']['Tenno Sho Spring'], 16.3)

    def test_horse_fastest_race(self):
        nonexistent_horse = self.horse_races.horse_fastest_race('Bob')
        self.assertEqual(nonexistent_horse[0], None)
        fastest_horse = self.horse_races.horse_fastest_race('Symboli Rudolf')
        self.assertEqual(fastest_horse[0], 'Teio Sho')
        self.assertAlmostEqual(fastest_horse[1], 14.8)

    def test_horse_personal_best(self):
        self.assertEqual(self.horse_races.horse_personal_best()['Oguri Cap'][0], 'Tenno Sho Fall')
        self.assertAlmostEqual(self.horse_races.horse_personal_best()['Oguri Cap'][1], 16.6)

    def test_get_average_time(self):
        self.assertAlmostEqual(self.horse_races.get_average_time()['Gold Ship'], 16.5)

def main():
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
