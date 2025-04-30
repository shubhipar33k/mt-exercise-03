import pandas as pd
import matplotlib.pyplot as plt

# Load the three CSVs
baseline = pd.read_csv("/Users/shubhi/Desktop/MT_Exercises/mt-exercise-03/extracted_ppls/baseline.csv")
prenorm = pd.read_csv("/Users/shubhi/Desktop/MT_Exercises/mt-exercise-03/extracted_ppls/prenorm.csv")
postnorm = pd.read_csv("/Users/shubhi/Desktop/MT_Exercises/mt-exercise-03/extracted_ppls/postnorm.csv")

# Merge based on the Step column
merged = pd.DataFrame({
    "Step": baseline["Step"],
    "Baseline": baseline["PPL"],
    "Prenorm": prenorm["PPL"],
    "Postnorm": postnorm["PPL"]
})

# Save the merged table
merged.to_csv("merged_table.csv", index=False)
print("Merged CSV saved as merged_table.csv!")

# Plot
plt.figure(figsize=(12, 8))
plt.plot(merged["Step"], merged["Baseline"], label="Baseline", marker='o')
plt.plot(merged["Step"], merged["Prenorm"], label="Prenorm", marker='x')
plt.plot(merged["Step"], merged["Postnorm"], label="Postnorm", marker='s')

plt.xlabel("Training Steps")
plt.ylabel("Validation Perplexity")
plt.title("Validation Perplexities over Training Steps")
plt.legend()
plt.grid(True)
plt.savefig("validation_ppl_plot.png")
print("Plot saved as validation_ppl_plot.png!")
plt.show()
