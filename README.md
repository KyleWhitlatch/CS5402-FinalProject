# CS5402-FinalProject
Analysis of Crime Data in the City of St. Louis.

1. Pull & Edit Data back to January 2018
- Pull All Unique CrimeID Values and Group into More Clear / Larger Categories
- Remove Data where (Last 2 Digits CodedMonth) != (First 2 Digits DateOccur)
2. Pull November 2018 as Testing Data (based on CrimeID)
3. Create Decision Tree
4. Use Functions on Decision Tree for Timeline, Counts, Geographically-based, etc.
- Predict CrimeID for October2018 (Drop Description)
- Count # of unique CrimeID per Month & All Months
- Count # of unique CrimeID per District per Month
- Timeline per District for # of Total CrimeID
5. Write Report
6. Profit


All CrimeID Categories:
- 1#### = Homicide
- 2#### = Rape
- 3#### = Robbery
- 4#### = Aggravated Assault
- 5#### = Burglary
- 6#### = Larceny
- 7#### = Vehicle Theft
- 8#### = Arson
- 9#### = Simple Assault
- Else = DROP


Time:
1 = Morning (6am - 11:59am)
2 = Afternoon (12pm - 5:59pm)
3 = Night (6pm - 5:59am)
