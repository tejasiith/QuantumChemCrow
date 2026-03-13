from chemcrow.agents import ChemCrow

# Initialize the agent
agent = ChemCrow(
    model="gpt-4-0613",
    temp=0.1
)

# Example query to test the Quantum Harmonic Oscillator tool
query = "Visualize benzene molecule"

result = agent.run(query)

print(result)