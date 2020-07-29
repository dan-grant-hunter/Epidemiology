# -----------------------------------------------------------------------------
# Epidemiology
# -----------------------------------------------------------------------------

# Get Input Population (P), Number of People Infected on Day 0 (N) and Infection Rate (R)
def getInput():
    inputs = []
    print("Enter the population, initial infections, and infection rate:")
    for n in range(3):
        inputs.append(int(input()))
    return inputs
