import os, pathlib, pandas as pd
out_dir = pathlib.Path.home() / r"C:\Users\20243314\OneDrive - TU Eindhoven\Desktop\Datasets For Projects\Crowd Prediction NS Utrecht-Amsterdam Dataset"
out_dir.mkdir(parents = True, exist_ok = True)
out_path = out_dir / "services-2025.csv"
files = [
    r"C:\Users\20243314\OneDrive - TU Eindhoven\Desktop\Datasets For Projects\Crowd Prediction NS Utrecht-Amsterdam Dataset\services-2025-01.csv", 
    r"C:\Users\20243314\OneDrive - TU Eindhoven\Desktop\Datasets For Projects\Crowd Prediction NS Utrecht-Amsterdam Dataset\services-2025-02.csv",
    r"C:\Users\20243314\OneDrive - TU Eindhoven\Desktop\Datasets For Projects\Crowd Prediction NS Utrecht-Amsterdam Dataset\services-2025-03.csv",
    r"C:\Users\20243314\OneDrive - TU Eindhoven\Desktop\Datasets For Projects\Crowd Prediction NS Utrecht-Amsterdam Dataset\services-2025-04.csv",
    r"C:\Users\20243314\OneDrive - TU Eindhoven\Desktop\Datasets For Projects\Crowd Prediction NS Utrecht-Amsterdam Dataset\services-2025-05.csv",
    r"C:\Users\20243314\OneDrive - TU Eindhoven\Desktop\Datasets For Projects\Crowd Prediction NS Utrecht-Amsterdam Dataset\services-2025-06.csv",
    r"C:\Users\20243314\OneDrive - TU Eindhoven\Desktop\Datasets For Projects\Crowd Prediction NS Utrecht-Amsterdam Dataset\services-2025-07.csv",
    r"C:\Users\20243314\OneDrive - TU Eindhoven\Desktop\Datasets For Projects\Crowd Prediction NS Utrecht-Amsterdam Dataset\services-2025-08.csv"

]

dfs = [pd.read_csv(f) for f in files]
out = pd.concat(dfs, ignore_index = True)

out.to_csv(out_path, index = False)
print(f"Saved to: {out_path}")