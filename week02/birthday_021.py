import sys
import calendar
day = int(sys.argv[1])
month= int(sys.argv[2])
year = int(sys.argv[3])
Day_of_year = calendar.weekday(year,month,day)
Day_of_week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
Poem = ["Monday's child is fair of face.","Tuesday's child is full of grace.","Wednesday's child is full of woe.","Thursday's child has far to go.","Friday's child is loving and giving.","Saturday's child works hard for a living.","Sunday's child is fair and wise and good in every way."]
poem_day_of_the_week = Day_of_week[Day_of_year]
Poem_line = Poem[Day_of_year]
print("You were born on a",poem_day_of_the_week,"and",Poem_line)