def farm(heads, legs):
    rabbits=-legs*1/2+heads*2
    chickens=heads-rabbits
    return(rabbits, chickens)
print(farm(int(input()), int(input())))