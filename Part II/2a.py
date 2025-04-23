import networkx as nx
import visualizer as viz
import experiments as exp

# --- Parameters ---
N = 1000
tMax = 50
nExp = 60 # Number of experiments to average over
infected = 1 # Initial number of infected nodes (Group A)
vaccinated = 0 # No initial vaccinated nodes (Group B) >>>
gamma = 2.5 # Parameter for scale-free graph
p_random = 1.5 / N # Probability for random graph edges
probabilityOfTransmission = 0.5

print(f"Starting Experiment 2a (No Vaccination): Comparing Random vs Scale-Free Dynamics")
print(f"Parameters: N={N}, tMax={tMax}, nExp={nExp}, initial_infected={infected}, initial_vaccinated={vaccinated}, p_transmission={probabilityOfTransmission}")
print("-" * 30)

# --- Generate Networks ---
print("Generating Random Graph (rG)...")
rG = nx.binomial_graph(N, p_random)
print(f"Generated rG with {rG.number_of_nodes()} nodes and {rG.number_of_edges()} edges.")

print("\nGenerating Scale-Free Graph (plG)...")
plG_raw = exp.generatePowerLawGraph(N, gamma)
plG = nx.Graph(plG_raw) # Remove parallel edges
plG.remove_edges_from(nx.selfloop_edges(plG)) # Remove self-loops
print(f"Generated plG with {plG.number_of_nodes()} nodes and {plG.number_of_edges()} edges (after removing self-loops).")
print("-" * 30)


# --- Run Simulations and Averaging ---

# 1. Random Graph
print(f"\nRunning {nExp} simulations on the Random Graph (rG)...")
# Use fullyRandomExperiment, ensuring sizeGroupB is correctly passed as 'vaccinated' (which is 0)
data_rG_repeated = exp.repeatedExperiments(exp.fullyRandomExperiment,
                                           rG,
                                           tMax,
                                           probabilityOfTransmission,
                                           infected,     # sizeGroupA
                                           vaccinated,   # sizeGroupB = 0
                                           nExp)
print(f"Finished simulations for rG.")

print("\nAveraging results for rG...")
# Tmax steps -> Tmax+1 data points (t=0 to t=Tmax)
avg_data_rG = exp.averageExperiment(data_rG_repeated, tMax + 1)
print("Averaging complete for rG.")

# 2. Scale-Free Graph
print(f"\nRunning {nExp} simulations on the Scale-Free Graph (plG)...")
# Use fullyRandomExperiment, ensuring sizeGroupB is correctly passed as 'vaccinated' (which is 0)
data_plG_repeated = exp.repeatedExperiments(exp.fullyRandomExperiment,
                                            plG,
                                            tMax,
                                            probabilityOfTransmission,
                                            infected,     # sizeGroupA
                                            vaccinated,   # sizeGroupB = 0
                                            nExp)
print(f"Finished simulations for plG.")

print("\nAveraging results for plG...")
# Tmax steps -> Tmax+1 data points (t=0 to t=Tmax)
avg_data_plG = exp.averageExperiment(data_plG_repeated, tMax + 1)
print("Averaging complete for plG.")
print("-" * 30)

# --- Visualize Averaged Results ---
# Filenames and titles for clarity
filename_rG = f"Avg_SI_Random_N{N}_p{p_random:.1e}_Inf{infected}_Vac{vaccinated}"
filename_plG = f"Avg_SI_ScaleFree_N{N}_gamma{gamma}_Inf{infected}_Vac{vaccinated}"

print(f"\nGenerating visualization for average Random Graph dynamics (No Vaccination)...")
# The visualizer function `showData` will automatically handle the 3 columns (U, A, B)
# even if B is always zero. The legend will show 'B' but the line will be flat at 0.
viz.showData(avg_data_rG, filename_rG)
print(f"Saved Random Graph dynamics plot: {filename_rG}_data.html")

print(f"\nGenerating visualization for average Scale-Free Graph dynamics (No Vaccination)...")
viz.showData(avg_data_plG, filename_plG)
print(f"Saved Scale-Free Graph dynamics plot: {filename_plG}_data.html")

print("-" * 30)
print("Experiment 2a (No Vaccination) finished. Check the generated HTML files for plots.")