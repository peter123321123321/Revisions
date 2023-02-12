concrete = list()
while True:
    finish = input("Would you like to calculate your concrete?[Y or N]"
                   "\nIf no proceed to total").upper()
    if finish == "Y":
        length = int(input("What is the length of your foundation? "))
        width = int(input("What is the width for your foundation? "))
        depth = int(input("Are you measuring concrete for a Commercial or Residential building? "
                          "\nIf Commercial enter [1]"
                          "\nif Residential enter [2]"))
        if depth == 1:
            volume = length*width*0.5
            print(f"The volume of concrete required for a slab with a length of {length} and a width of {width}"
                  f" and a depth of {0.5} is {volume}")
            concrete.append(volume)
        if depth == 2:
            volume = length*width*0.25
            print(f"The volume of concrete required for a slab with a length of {length} and a width of {width}"
                  f" and a depth of {0.25} is {volume}")
            concrete.append(volume)
    else:
        print(sum(concrete))
        exit()
