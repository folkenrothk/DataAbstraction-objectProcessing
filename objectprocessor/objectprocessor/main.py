"""Input and process objects about people."""

from pathlib import Path

from typing import List

import typer
import csv

from rich.console import Console

from objectprocessor import process
from objectprocessor import person

# create a Typer object to support the command-line interface
cli = typer.Typer()

# create a console for display of rich text
console = Console()


def prepare_person_list_for_display(person_list: List[person.Person]) -> str:
    """Process the list of people for display in the console."""
    # create an empty string that will contain all of the text
    workString = ""
    # iterate through each of the people in the person_list and
    # add all of their textual details to a string; making sure to
#    for currentPerson in person_list:

#///
#person_list_text = ""
#    for current_person in person_list:
#      person_list_text +=
#        "- " + str(current_person) + "\n"
#    return person_list_text

    
    # TODO: preface each entry with a "-" and add a newline
    # TODO: return the list of generated text for each person
#    workString = person.Person.__repr__(currentPerson)
    return workString


@cli.command()
def main(
    search_term: str = typer.Option(...),
    attribute: str = typer.Option(...),
    input_file: Path = typer.Option(...),
    output_file: Path = typer.Option(...),
):
    """Input data about a person and then analyze and save it."""
    # display details about the file provided on the command line
    data_text = ""
    # the file was not specified so we cannot continue using program
    if input_file is None:
        console.print("No data file specified!")
        raise typer.Abort()
    # the file was specified and it is valid so we should read and check it
    if input_file.is_file():
        # read in the data from the specified file containing information about people
   #     inFile = open(input_file, "r")
   #     readInFile = csv.reader(inFile)
   #     inFileData = list(readInFile)
   #     mainList = []
        # transform the data in the CSV file (now in a string) into a list of instances of the Person class
   #     for row in readInFile:
   #         currentPerson = process.extract_person_data(str(inFileData))
   #         mainList.append(currentPerson)
        # search for the people with an attribute that matches the search term
   #     matchList = process.find_matching_people(attribute, search_term, mainList)
   #     print(matchList)
        # display the details about the matching people to the console
        
        # make sure to use the prepare_person_list_for_display function for creating a suitable display
        
        # save the details about the matching people to the file system in the specified output directory
