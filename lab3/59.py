def spy_game(nums):
    i=-1
    while i < len(nums)-3:
        a=bool()
        if nums[i+1]==0 and nums[i+2]==0 and nums[i+3]==7:
            a=True
            break
        else:
            a=False
        i+=1
    print(a)
nums=[9, 2, 0, 0, 7, 8] 
spy_game(nums)