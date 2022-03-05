def cellTowers(houses, radius):
    if(len(houses) == 0):
        return 0;

    towers = 0;
    # first tower placement 
    distance = houses[0] + radius;
    towers += 1;

    # find all other towers 
    for house in houses:
        if(abs(house - distance)) > radius:
            towers += 1;
            distance = house + radius;
    
    return towers;
