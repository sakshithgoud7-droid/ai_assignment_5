from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Bayesian Network:
# Rain and Accident both affect Traffic

network = DiscreteBayesianNetwork([
    ("Rain", "Traffic"),
    ("Accident", "Traffic")
])

# Probability of Rain
rain_cpd = TabularCPD(
    variable="Rain",
    variable_card=2,
    values=[[0.7], [0.3]]
)

# Probability of Accident
accident_cpd = TabularCPD(
    variable="Accident",
    variable_card=2,
    values=[[0.8], [0.2]]
)

# Probability of Traffic depending on Rain and Accident
traffic_cpd = TabularCPD(
    variable="Traffic",
    variable_card=2,
    values=[
        [0.9, 0.6, 0.7, 0.1],
        [0.1, 0.4, 0.3, 0.9]
    ],
    evidence=["Rain", "Accident"],
    evidence_card=[2, 2]
)

network.add_cpds(rain_cpd, accident_cpd, traffic_cpd)

print("Is the model correct?", network.check_model())

# Finding probability of Traffic when Rain is true
infer = VariableElimination(network)

answer = infer.query(
    variables=["Traffic"],
    evidence={"Rain": 1}
)

print("\nProbability of Traffic when it is raining:")
print(answer)
