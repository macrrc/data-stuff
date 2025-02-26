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

import record_processor as rp

header_row = "First Name, Last Name, Age, Height, Sex"
test_rows = [
    "Bob, Newhart, 78, 175, M",
    "Stacy, DUNCAN, 22, 189, F",
    "marilyn, Manson,, 176, Male"
]

for row in test_rows:
    record = rp.Record(header_row, row)
    record.parse()

