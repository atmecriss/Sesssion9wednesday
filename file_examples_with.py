#lets create a virtual diary
with open("diary.txt", "a") as fp:
    while True:
        text = input("How do you feel today? (type q to quit): ")
        if text == "q":
            break
        fp.write(f"{text}\n") # this is the same as below line

