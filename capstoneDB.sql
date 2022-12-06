create database capstone;

use capstone;

CREATE TABLE Faculty
(
  Name varchar(20) NOT NULL,
  Designation varchar(20) NOT NULL,
  YearsOfExperience INT NOT NULL,
  AreasOfInterest varchar(100) NOT NULL,
  Domain varchar(20) NOT NULL,
  AcceptableGrps INT NOT NULL,
  FID INT NOT NULL,
  PRIMARY KEY (FID)
);

CREATE TABLE Project
(
  GroupNumber INT NOT NULL,
  FacultyAdvisor varchar(20) NOT NULL,
  ProjectName varchar(50) NOT NULL,
  Interdisciplinary INT NOT NULL,
  FID INT NOT NULL,
  PRIMARY KEY (GroupNumber),
  FOREIGN KEY (FID) REFERENCES Faculty(FID)
);

CREATE TABLE Student
(
  Name varchar(20) NOT NULL,
  SRN varchar(13) NOT NULL,
  Section varchar(1) NOT NULL,
  YearOfGraduation INT NOT NULL,
  GroupNumber INT NOT NULL,
  PRIMARY KEY (SRN),
  FOREIGN KEY (GroupNumber) REFERENCES Project(GroupNumber)
);

/* DML statements */

Insert into Faculty values ("Anuradha","Chairperson",27,"Renewable energy,AIML,Control Systems","Spase and winc",3,1);
Insert into Faculty values ("Chandar","Professor",7,"Control Systems","SPaSe",3,2);
Insert into Faculty values ("Vamsi","Professor",10,"Edge detection,automatic vehicles","Winc",4,3);
Insert into Faculty values ("Vanamala","Associate Professor",25,"Digital image processing, ML","SPaSe",4,4);
Insert into Faculty values ("Rekha","Associate Professor",27,"hardware security ,cryptography","NiCE",3,5);
Insert into Faculty values ("Sumanth","Assistant Professor",4,"VLSI,Embedded systems","NiCE",3,6);

Insert into project values(1,"Chandar","Fire detection system",0,2);
Insert into project values(2,"Vamsi","RL on automobiles",0,3);
Insert into project values(3,"Rekhar","System on chip design",0,5);
Insert into project values(4,"Vamsi", "Edge computing for 6G", 0, 3);

Insert into Student values ("Amogh","PES1UG20EC002","A",2024,1);
Insert into Student values ("Achal","PES1UG20EC009","A",2024,2);
Insert into Student values ("Anagha","PES1UG20EC024","A",2024,1);
Insert into Student values ("Ananya","PES1UG20EC025","A",2024,1);
Insert into Student values ("Alokpunj","PES1UG19EC032","A",2024,2);
Insert into Student values ("Adith","PES1UG20EC011","A",2024,1);
Insert into Student values ("Chirag","PES1UG20EC051","A",2024,2);
Insert into Student values ("Divya","PES1UG20EC053","A",2024,3);
Insert into Student values ("Aaron","PES1UG20EC006","A",2024,3);
Insert into Student values ("Aakanksh","PES1UG20EC004","A",2024,3);
Insert into Student values ("yashaswi","PES1UG20EC001","A",2024,4);
Insert into Student values ("Abhay","PES1UG20EC008","A",2024,4);
Insert into Student values ("Aditya","PES1UG20EC012","A",2024,4);


/* Creating a procedure to insert faculty without giving FID */

DELIMITER $$
CREATE PROCEDURE InsertFaculty (IN FacultyName varchar(20),
  IN Designation varchar(20),
  IN YearsOfExperience INT,
  IN AreasOfInterest varchar(100),
  IN Domain varchar(20),
  IN AcceptableGrps INT,
  OUT result INT
)
BEGIN

  select count(*) INTO @CHECK from Faculty where name = FacultyName;
  IF @CHECK = 0 THEN

    SELECT max(FID) + 1 INTO @M from Faculty;
    INSERT INTO Faculty VALUES (FacultyName,Designation,YearsOfExperience,AreasOfInterest,Domain,AcceptableGrps,@M);
    SET result = 1;

  ELSE

    SET result = -1;

  END IF;

END $$
DELIMITER ;

/* CALL InsertFaculty("Achal MAAMA", "Assistant Professor", 4, "SpaSe", "NiCE", 3, @M); */





/* Procedure to insert a project. It checks if the number of existing projects are exceeding the number of acceptable 
projects by the prof. */

DELIMITER $$

CREATE PROCEDURE insertProject(IN facultyAdvisor VARCHAR(20),
  IN projectName VARCHAR(50),
  IN interdisciplinary INT,
  IN facultyID INT,
  OUT result INT
)

BEGIN
select count(*) into @projectcount from project where FID = facultyID;
select AcceptableGrps into @acceptableGrps from faculty where FID = facultyID;
IF @projectcount < @acceptableGrps THEN
  
  SELECT MAX(GroupNumber) + 1 INTO @newgrpno FROM project;
  INSERT INTO project VALUES(@newgrpno, facultyAdvisor, projectName, interdisciplinary, facultyID);

  SET result = 1;
ELSE
  SET result = -1;
END IF;

END $$
DELIMITER ;



/* A few commands that may be useful. This is for our purpose */

SELECT ROUTINE_NAME, ROUTINE_SCHEMA FROM INFORMATION_SCHEMA.ROUTINES WHERE ROUTINE_TYPE = 'PROCEDURE' AND ROUTINE_SCHEMA = 'capstone';

/* Lists all the procedures we have in the capstone database */
