#display the future leap year from current year to final year enterd by user
import datetime
current_year= datetime.datetime.now().year
final_year=int(input("enter the final year:"))
for year in range(current_year,final_year +1):
    if year % 4==0:
        print(year)
