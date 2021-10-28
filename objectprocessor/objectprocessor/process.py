"""Extract the data about the person from the CSV file."""

from typing import List

import csv

from objectprocessor import person

# Sample of the data set:

# Mrs. Natalie Lee,Bolivia,036-126-0340x0094,"Engineer, building services",david82@example.org
# Michael Anderson,Honduras,(627)610-9166,Writer,ryan23@example.org
# Cindy Burns,Dominican Republic,(102)481-3875,"Pharmacist, hospital",rtorres@example.org
# Jason Bailey,Falkland Islands (Malvinas),+1-552-912-2326,Leisure centre manager,daniel51@example.com
# Andrew Johnson,Portugal,733-554-3949,"Engineer, site",michael94@example.com
# Carol Poole,Isle of Man,365.529.7270,Pensions consultant,piercebrenda@example.com


def extract_person_data(data: str) -> List[person.Person]:
    """Extract a specified data column from the provided textual contents."""
    # TODO: create an empty list of the data
    # note that the data file:
    # --> contains five columns
    # --> each of which contains textual data with a different meaning
    # TODO: refer to the file called input/people.txt to learn more about
    # the format of the comma separated value (CSV) file that we must parse;
    # iterate through each line of the file and extract all relevant details
    # use the csv.reader to accomplish the task of parsing the CSV file
    for line in csv.reader(
        data.splitlines(),
        quotechar='"',
        delimiter=",",
        quoting=csv.QUOTE_ALL,
        skipinitialspace=True,
    ):
        # TODO: extract each of the attributes about a person from the line variable
        # TODO: construct a new instance of the Person class that contains all
        # of the attributes that were extracted from the CSV file
        # TODO: append the current instance of the person class to the data_list variable
    # TODO: return the list of all of the specified column


def write_person_data(file_name: str, person_data: List[person.Person]) -> None:
    """Write the person data stored in a list to the specified file."""
    # TODO: create an empty list that will store the person data as a list of strings
    # TODO: iterate through every person inside of the person_data list
        # TODO: create a list out of this person where each of the person's
        # attributes are stored inside of an index in the list
        # TODO: append this converted person list to the list called converted_person_data
    # TODO: use the csv.writer approach and the writerows function to write out
    # the list of lists of strings that contain all of the person data


def find_matching_people(
    attribute: str, match: str, person_data: List[person.Person]
) -> List[person.Person]:
    """Find people who have matching data for a specified attribute."""
    # TODO: create an empty list of people who have an attribute matching the search term in match
    # TODO: iterate through all of the people in the person_data list
        # TODO: the current person has an attribute that contains the search term in match
            # TODO: add the current person to the matching_person_list
    # TODO: return the matching_person_list


def is_matching_person(
    attribute: str, match: str, search_person: person.Person
) -> bool:
    """Determine if the person's specified attribute contains the search term in match."""
    # TODO: the attribute for matching is name
      # TODO: return True if the provided search term is in the match
      # variable appears inside of the specified attribute
    # TODO: the attribute for matching is country
      # TODO: return True if the provided search term is in the match
      # variable appears inside of the specified attribute
    # TODO: the attribute for matching is phone number
      # TODO: return True if the provided search term is in the match
      # variable appears inside of the specified attribute
    # TODO: the attribute for matching is job
      # TODO: return True if the provided search term is in the match
      # variable appears inside of the specified attribute
    # TODO: the attribute for matching is email
      # TODO: return True if the provided search term is in the match
      # variable appears inside of the specified attribute
    # return False if none of the conditions are matching
