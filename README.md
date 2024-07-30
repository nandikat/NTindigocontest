This is a Web application developed as a solution for the case study provided.

The Web application has the following features:
1.	Passengers can check the current status of their flight.
2.	Every time the status of a flight is changed, all the passengers supposed to travel from that flight are notified via email.
   
Working:
The web application has the Following pages:

**1.	Check Status Page**
Through This page the users can check the current status of their flight by filling in their Departure location, Arrival Location,Flight ID and Booking Number

![image](https://github.com/user-attachments/assets/e624bcf2-2194-43f8-b08f-c3ab986ac837)
![image](https://github.com/user-attachments/assets/32ba7625-c3c1-4d86-9906-87a99433a9b7)
![image](https://github.com/user-attachments/assets/34fbc216-9273-40d5-a7f6-a77583a7b56a)



**2.	Change Status Page**
This is Used to change the status of a flight by filling in the Flight ID and selecting its new status.
After clicking the submit button The status table of the database is updated with the new status and all the passengers supposed to travel from this flight are notified via email(Using Python smtplib library)

![image](https://github.com/user-attachments/assets/a9ef7094-4648-4761-8e98-f12c8c3cf975)
![image](https://github.com/user-attachments/assets/02e869aa-c00a-4fe3-8bcd-e2d09455a3d1)
<img width="959" alt="image" src="https://github.com/user-attachments/assets/b6d52ed9-2adc-496a-abd4-4b736e683fb9">





**Tech Stack:**

Frontend: HTML,CSS

Backend:Python,Flask

RDBMS:MySQL




