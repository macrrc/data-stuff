# Script to process data records
## validate
## - for correct data type
## - valid range
## - complete data
## clean
## - Normalize case
## Creates a new list of records
## Invalid and uncleanable records are skipped and logged
## 


header_record = "First Name, Last Name, Age, Height, Sex"
test_records = [
    "Bob, Newhart, 78, 175, M",
    "Stacy, DUNCAN, 22, 189, F",
    "marilyn, Manson,, 176, Male"
]

for record in test_records:
    # run validate on each
    pass

