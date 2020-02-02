# in_day="11/19/2019"
in_day = "May 19,2019"
month={"January":"1","February":"2","March":"3","April":"4","May":"5","June":"6","July":"7","August":"8","Semptember":"9","October":"10","November":"11","December":"12"}
in_day=in_day.replace("/"," ")
in_day=in_day.replace(","," ")
word_list=in_day.split(" ")


if word_list[0].isalpha():
    mm=month[word_list[0]]

else:
    mm=word_list[0]

out = word_list[1] + '/' + mm + '/' + word_list[2]
print(out)