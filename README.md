# Integrated Postsecondary Education Data System (IPEDS) API
This is the codebase for an IPEDS API constructed using the Django REST Framework.

The project references a database that has been populated with data from the online [IPEDS data repository](https://nces.ed.gov/ipeds/use-the-data).

To access the data at the above link, select "Complete Data Files" from the "Survey Data" dropdown.

Currently, the data is only available online through downloadable CSV and XLSX files.

**This project is meant to provide endpoints through which developers may access the data without downloading and storing in memory those spreadsheets.**