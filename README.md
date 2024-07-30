# NTindigocontest
This is a Web application developed as a solution for the case study provided.

The Web application has the following features:
1.	Passengers can check the current status of their flight.
2.	Every time the status of a flight is changed, all the passengers supposed to travel from that flight are notified via email.
Working:
The web application has the Following pages:
1.	Check Status Page
Through This page the users can check the current status of their flight by filling in their Departure location, Arrival Location,Flight ID and Booking Number

2.	Change Status Page
This is Used to change the status of a flight by filling in the Flight ID and selecting its new status.
After clicking the submit button The status table of the database is updated with the new status and all the passengers supposed to travel form this flight are notified via email(Using Python smtplib library)

Tech Stack:
Frontend: HTML,CSS
Backend:Python,Flask
RDBMS:MySQL




