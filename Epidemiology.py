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
def calcSpread(inputs):
    p, n, r = inputs
    dailySpread = []
    while sum(dailySpread) <= p:
        dailySpread.append(n)
        n *= r
    return dailySpread


# Return Which Day The Infection Will Be Higher Than Target Population
def dayNum(dailySpread):
    day = len(dailySpread) - 1
    return day


# Main Loop
def mainLoop():
    inputs = getInput()
    dailySpread = calcSpread(inputs)
    print(f'Day {dayNum(dailySpread)} will be the first day the number of people infected exceeds the population given')


# Replay Prompt
if __name__ == '__main__':
    while True:
        mainLoop()
        while True:
            answer = input('Calculate Again? (Y/N): ')
            if answer.upper() in ('Y', 'N'):
                break
            print('\nInvalid input\n')
        if answer.upper() == 'Y':
            continue
        else:
            break
