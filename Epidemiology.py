# -----------------------------------------------------------------------------
# Epidemiology
# -----------------------------------------------------------------------------

# Get Input Population (p), Number of People Infected on Day 0 (n) and Infection Rate (r)
def getInput():
    inputs = []
    print("Enter the population, initial infections, and infection rate:")
    for n in range(3):
        inputs.append(int(input()))
    return inputs


# Calculate Spread of Infection
def calcSpread():
    p, n, r = inputs
    dailySpread = []
    while max(dailySpread) < p:
        infected = n * r
        dailySpread.append(infected)
        n = infected
    return dailySpread



# Return Which Day The Infection Will Be Higher Than Target Population
def dayNum():
    pass



# Main Loop
def mainLoop():
    pass




# Replay Prompt

