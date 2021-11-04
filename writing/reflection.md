# Object Processing

## Kate Folkenroth

## Program Output

### Use two fenced code blocks to provide output from two different runs of `objectprocessor` with two different inputs

#### Provide the command the output for the first run of the `objectprocessor`

`poetry run objectprocessor --search-term john79 --attribute email --input-file input/people.txt --output-file output/people.txt`

```
🧮 Reading in the data from the specfied file input\people.txt

🚀 Parsing the data file and transforming it into people objects

🕵️‍♂️ Searching for the people with an email that matches the search term  'john79'

- John Johnson is a Food technologist who lives in Brazil. You can call this person at 197-728-4342 and email them at john79@example.net

✨ Saving the matching people to the file output\people.txt
```

#### Provide the command the output for the second run of the `objectprocessor`

`poetry run objectprocessor --search-term Kate --attribute name --input-file input/people.txt --output-file output/people.txt`

```
🧮 Reading in the data from the specfied file input\people.txt

🚀 Parsing the data file and transforming it into people objects

🕵️‍♂️ Searching for the people with an name that matches the search term  'Kate'

- Katelyn Johnson MD is a Financial adviser who lives in Mayotte. You can call this person at (975)411-7322 and email them at 
michaelcastro@example.com
- Katelyn Ferguson is a Production assistant, television who lives in Togo. You can call this person at (027)065-6700x864 and email them atlharrell@example.net
- Katelyn Watson is a Sales promotion account executive who lives in Canada. You can call this person at 057.132.7195x940 and email them atmperkins@example.org
- Katelyn Brewer is a Producer, television/film/video who lives in British Virgin Islands. You can call this person at (814)304-8121x2099  
and email them at hpatterson@example.com
- Katelyn Sullivan is a Teacher, secondary school who lives in Taiwan. You can call this person at +1-840-537-3916x227 and email them at   
jenniferoliver@example.org
- Katelyn Peters is a Actor who lives in Vanuatu. You can call this person at (172)297-2555x514 and email them at robert48@example.com     
- Katelyn Cannon is a Optometrist who lives in Micronesia. You can call this person at 585.119.9669x284 and email them at
lauraschaefer@example.org
- Katelyn Powers is a Optometrist who lives in Congo. You can call this person at (138)876-1958x8680 and email them at bmelton@example.com 
- Katelyn Schwartz is a Herpetologist who lives in Hungary. You can call this person at 504-199-5939x17143 and email them at
novaklinda@example.net
- Katelyn Francis is a Corporate investment banker who lives in Monaco. You can call this person at +1-158-263-6482x22826 and email them atumorris@example.org
- Katelyn Gonzales is a Retail banker who lives in Holy See (Vatican City State). You can call this person at 860-571-5889x05005 and email 
them at reevesangela@example.org
- Katelyn Smith is a Community education officer who lives in Senegal. You can call this person at 500.980.9501x18630 and email them at    
robinsontonya@example.org
- Mrs. Katelyn Miller DVM is a Teaching laboratory technician who lives in Bhutan. You can call this person at 920-553-2602x51449 and emailthem at kim51@example.net
- Katelyn Jones is a Brewing technologist who lives in Greece. You can call this person at 844.842.0452x805 and email them at
brodriguez@example.net
- Katelyn Solis is a Horticulturist, commercial who lives in Ghana. You can call this person at +1-672-040-4122x656 and email them at      
staciejohnson@example.org
- Katelyn West is a Engineer, communications who lives in Ukraine. You can call this person at 167-092-1783x88231 and email them at        
brandistewart@example.net
- Katelyn Wright is a Transport planner who lives in Argentina. You can call this person at 001-276-158-3756x91339 and email them at       
sarahjohnson@example.com
- Katelyn Sloan is a Data scientist who lives in Christmas Island. You can call this person at +1-158-844-1808x840 and email them at       
carloskim@example.net
- Katelyn Warner is a Medical illustrator who lives in Ireland. You can call this person at 0344633645 and email them at
emilyunderwood@example.org
- Dr. Katelyn Scott is a Accountant, chartered certified who lives in Finland. You can call this person at +1-762-412-0871x97055 and email 
them at fowens@example.org
- Katelyn Jackson is a Archivist who lives in Liechtenstein. You can call this person at (198)875-5133 and email them at
jessica27@example.net
- Katelyn Martin is a Air traffic controller who lives in Aruba. You can call this person at 063.547.6610x9825 and email them at
mark64@example.net

✨ Saving the matching people to the file output\people.txt
```

## Source Code

### Describe in detail how the provided source code works

```
person_index = create_constants(
    "person", Name=0, Country=1, Phone_Number=2, Job=3, Email=4
)
```

This piece of code initializes the constant of person index for the class Person. This helps label where the pieces of information in each line of the person. As name is with 0 and country is with 1, these numbers represent the location in the index where the respective piece of information is.

### Describe in detail how the provided source code works

```
person_attribute = create_constants(
    "person",
    Name="name",
    Country="country",
    Phone_Number="phone_number",
    Job="job",
    Email="email",
)
```

This piece of code also initializes a constant. This section creates the person attribute constant for the class Person. This connects the variables like "name" and "phone_number" to the attribute labels of Name and Phone_Number for example. This is important for the Person class to call for it's functions in the process.py file.

### Describe in detail how the provided source code works

```
def __init__(
    self, name: str, country: str, phone_number: str, job: str, email: str
) -> None:
    """Define the constructor for a person."""
    self.name = name
    self.country = country
    self.phone_number = phone_number
    self.job = job
    self.email = email
```

This segment of code is a the double underscore (dunder) init function of the class Person. This function will run defaultly when the class Person is called. The function take in itself and 5 strings (one for name, country, phone number, job, and email) as input.  This acts as the constructor of the class. It label each of these actual parameters as its own attributes. This functions similarly to dictionaries. When we refer to a specific person, it has these attributes that we can search for within itself by calling its job or phone number.

### Describe in detail how the provided source code works

```
def __repr__(self) -> str:
    """Return a textual representation of the person."""
      return f"{self.name} is a {self.job} who lives in {self.country}. You can call this person at {self.phone_number} and email them {self.email}."
```

This segment of code is the double underscore (dunder) repr function of the class Person. This funtion is called when the class Person is being displayed or represented in a string format. The function only needs itself (specifically its attributes from the dunder init function) as input and outputs a string representation of itself. This function just has an f string as its return which calls the attributes of itself to fill in the bracketed sections in the sentence.

## Professional Development

### What are the benefits and drawbacks of object-oriented programming in Python?

There are many benefits and costs of object-oriented programming in Python. One of the drawbacks is the complexity of the code. It takes longer to code and understand. However, object-oriented programming is also beneficial because of the complexity. It is thoughtful code and can be reused more easily. It can also allow for more modular testing.

### What was the greatest challenge that you faced when completing this assignment?

The greatest challenge in this assignment was working with the csv package. I have only had experience with these types of files and readers in the R programming language. I was very confused how to implement the reader and writers, especially when implementing them to work with the code segments provided by the instructor. This challenge was not impossible to overcome but brought frustration with the lack of diverse documentation on the content.

### Leveraging your response to the previous question, how did you overcome the challenge?

This challenge was definitely overcome by multiple courses of action. I sat with the lab and worked on it a little everyday as I sifted through documentation. I utilized a new method of temporary testing as I printed out steps of my code and deleted them along the way. However, as usual, I heavily relied on my collegues to surmount this challenge. I also was fortunate to have the opportunity to ask working professionals about their experiences with coding and csv files. Two of these professionals were also excited to lend an ear and recommend possible solutions or tests to run with my program. In the end, my peers helped me to find the last errors in my code and help it run.