# Starbucks Capstone Challenge

## Introduction

This data set contains simulated data that mimics my behavior on the Starbucks rewards mobile app. Once every few days, Starbucks sends out an offer to users of the mobile app. An offer can be merely an advertisement for a drink or an actual offer such as a discount or BOGO (buy one get one free). Some of us might not receive any offer during certain weeks.

Not all of us receive the same offer, and that is the challenge to solve with this data set.

My task is to combine transaction, demographic, and offer data to determine which demographic groups respond best to which offer type. This data set is a simplified version of the real Starbucks app because the underlying simulator only has one product whereas Starbucks actually sells dozens of products.

Every offer has a validity period before the offer expires. As an example, a BOGO offer might be valid for only 5 days. I will see in the data set that informational offers have a validity period even though these ads are merely providing information about a product; for example, if an informational offer has 7 days of validity, I can assume I am feeling the influence of the offer for 7 days after receiving the advertisement.

I will be given transactional data showing my purchases made on the app including the timestamp of purchase and the amount of money spent on a purchase. This transactional data also has a record for each offer that I receive as well as a record for when I actually view the offer. There are also records for when I complete an offer.

I should keep in mind as well that I might make a purchase through the app without having received an offer or seen an offer.

## Example

To give an example, I could receive a discount offer "buy 10 dollars get 2 off" on Monday. The offer is valid for 10 days from receipt. If I accumulate at least 10 dollars in purchases during the validity period, I complete the offer.

However, there are a few things to watch out for in this data set. I do not opt into the offers that I receive; in other words, I can receive an offer, never actually view the offer, and still complete the offer. For example, I might receive the "buy 10 dollars get 2 dollars off offer", but I never open the offer during the 10-day validity period. I spend 15 dollars during those ten days. There will be an offer completion record in the data set; however, I was not influenced by the offer because I never viewed the offer.



## Data Sets

The data is contained in three files:

- `portfolio.json` - containing offer ids and meta data about each offer (duration, type, etc.)
- `profile.json` - demographic data for each customer
- `transcript.json` - records for transactions, offers received, offers viewed, and offers completed

### Here is the schema and explanation of each variable in the files:

#### `portfolio.json`

- `id` (string) - offer id
- `offer_type` (string) - type of offer i.e., BOGO, discount, informational
- `difficulty` (int) - minimum required spend to complete an offer
- `reward` (int) - reward given for completing an offer
- `duration` (int) - time for offer to be open, in days
- `channels` (list of strings)

#### `profile.json`

- `age` (int) - age of the customer
- `became_member_on` (int) - date when customer created an app account
- `gender` (str) - gender of the customer (note some entries contain 'O' for other rather than M or F)
- `id` (str) - customer id
- `income` (float) - customer's income

#### `transcript.json`

- `event` (str) - record description (i.e., transaction, offer received, offer viewed, etc.)
- `person` (str) - customer id
- `time` (int) - time in hours since start of test. The data begins at time t=0
- `value` - (dict of strings) - either an offer id or transaction amount depending on the record

**The objective of this project is to integrate transaction, demographic, and offer data to ascertain which demographic segments exhibit the most favorable responses to specific types of offers. This dataset represents a streamlined version of the actual Starbucks app, as the underlying simulator is limited to a single product, whereas Starbucks' real-world inventory includes a diverse array of products.**


## Project Structure

The project is organized into the following directories and files:


### Directories and Files

- **data/**: Contains the dataset files.
  - `portfolio.json`: Contains offer ids and metadata about each offer (duration, type, etc.).
  - [`profile.json`](command:_github.copilot.openSymbolFromReferences?%5B%22profile.json%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fsubhopam%2FDocuments%2FProgramming%2FData_Science%2Fstarbucks_capstone%2Fstarbucks-capstone%2FREADME.md%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fsubhopam%2FDocuments%2FProgramming%2FData_Science%2Fstarbucks_capstone%2Fstarbucks-capstone%2FREADME.md%22%2C%22path%22%3A%22%2Fhome%2Fsubhopam%2FDocuments%2FProgramming%2FData_Science%2Fstarbucks_capstone%2Fstarbucks-capstone%2FREADME.md%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A44%2C%22character%22%3A6%7D%7D%5D%5D "Go to definition"): Contains demographic data for each customer.
  - [`transcript.json`](command:_github.copilot.openSymbolFromReferences?%5B%22transcript.json%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fsubhopam%2FDocuments%2FProgramming%2FData_Science%2Fstarbucks_capstone%2Fstarbucks-capstone%2FREADME.md%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fsubhopam%2FDocuments%2FProgramming%2FData_Science%2Fstarbucks_capstone%2Fstarbucks-capstone%2FREADME.md%22%2C%22path%22%3A%22%2Fhome%2Fsubhopam%2FDocuments%2FProgramming%2FData_Science%2Fstarbucks_capstone%2Fstarbucks-capstone%2FREADME.md%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A52%2C%22character%22%3A6%7D%7D%5D%5D "Go to definition"): Contains records for transactions, offers received, offers viewed, and offers completed.

- **notebooks/**: Contains Jupyter notebooks used for data exploration, analysis, and model development.
  - `starbucks_capstone_notebook.ipynb`: contains separate sections along with reasoning for data cleansing, exploratory data anakysis and final model training and evaluation



### Documentation

- **README.md**: Provides an overview of the project, including the objective, data description, and project structure.


This structure ensures that the project is well-organized and that each component is easily accessible for development, testing, and deployment.

