# day32_100
I am currently engaged in a 100-day Python Bootcamp, which I am documenting and sharing my progress on GitHub. The boot camp is designed to progressively intensify, allowing me to deepen my understanding and proficiency in Python programming.

Additionally, I have chosen to include the beginner, intermediate and advanced in my documentation to provide a valuable reference for my future growth and development.

------------------
# Lessons Learned from the SMTP Automated Birthday Wishes Project

**Overview**
This project was a fantastic journey into the world of email automation using Python. The primary objective was to send automated birthday wishes to family members by leveraging the Simple Mail Transfer Protocol (SMTP). Here are some key takeaways from this project:

**Key Learnings**

1. __SMTP Protocol and Email Automation:__
  - Gained practical experience with the SMTP protocol for sending emails programmatically.
  - Learned how to securely connect to an SMTP server using Python's smtplib library.
  - Understood the importance of using secure connections with starttls() to encrypt the email content.
    
2. __Working with Dates and Times:__
  - Utilized the datetime module to fetch the current date and time.
  - Learned how to extract and compare specific date components (month and day) to trigger birthday reminders.

3. __Handling CSV Files:__
  - Explored reading and processing CSV files using the pandas library.
  - Gained proficiency in creating dictionaries from CSV data for quick lookups.
    
4. __Dynamic Content Generation:__
  - Implemented dynamic content generation by replacing placeholders in email templates with actual names.
  - Utilised randomization to select different email templates, adding variety to the birthday messages.

5. __Email Encoding with MIMEText:__
  - Learned how to handle email content encoding using the email.mime.text.MIMEText class.
  - Ensured proper handling of non-ASCII characters in email messages.
    
6. __Running Code in the Cloud:__
  - Configured the script to run in the cloud such as using PythonAnywhere, ensuring continuous operation without relying on a local machine by setting up a scheduler run.
    
## Project Highlights

- __Automated Birthday Reminders:__
The project sends personalized birthday wishes to family members on their special day, ensuring no birthday is missed.

- __Email Template Variety:__
Implemented multiple email templates to keep the messages fresh and engaging.

- __Secure Email Transmission:__
Used secure methods to connect and send emails, maintaining privacy and security.

## Future Improvements
__Improve Error Handling:__
Implement more robust error handling to manage cases where the email fails to send or the CSV file is not accessible.
