# ece-140a-winter-2022-20aszulc
ece-140a-winter-2022-20aszulc created by GitHub Classroom

Name: Amber Szulc
PID: A16241551
### Tutorial 1
  I learned how to set up the MySQL CLI, which took a long time to download. I learned how to create and use a databse. I learned how to find what database I was on.

### Tutorial 2
In your README, please include a short description of what each of these data types and their input values represent. 

integer - medium integer. Size parameter defines maximum dsipla width

decimal- An exact fixed-point number. The total number of digits is specified in size.  

varchar - variable length string. Size parameter specifies maximum column length

I learned LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Songs_data.csv'
    -> INTO TABLE songs_data
    -> COLUMNS TERMINATED BY ','
    -> ENCLOSED BY '"'
    -> LINES TERMINATED BY '\r\n'
    -> IGNORE 1 ROWS;
This took soooo long to figure out.However, I learned that the data we collected is from the infile path. It goes into our table of our choosing. Then we seperate data by field or column and rows by \r\n and we ignore the first row since it is just headings. I know how to alter, update, delete (LOTS OF DELETING THEN RECREATING TABLES BECAUSE THE INFILE DIDNT WORK SO MANY TIMES).

### Tutorial 3
  I learned how to select values from specific columns. I learned what a basic query was like how to order based on sertain conditions. I figured out how to nest queries like selecting the average energy from the songs data base given certain parameters of who the artists could be.
