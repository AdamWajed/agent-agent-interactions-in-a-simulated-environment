import os

from src.functions import configure, load, run, save
from tqdm import tqdm

# ════════════════════════════════════════════════════════════════════════════════════════════════
# EXPERIMENT 0e: PAPER REPLICATION - only pressure is inability to find low and medium risk trades
# ════════════════════════════════════════════════════════════════════════════════════════════════

def exp_0e(no_runs,prompt_path,model):

    configure()

    # Create misalignment dictionary to track misalignment decisions for each run
    LING_buy_dict = {
        }
    
    LING_buy_count = 0 
    
    for num in tqdm(range(no_runs), desc="Running Experiment 0e"):

        # Create results directories for each run
        results_path = f"results/exp_0e/{model}/run_{num+1}.json"
        os.makedirs(os.path.dirname(results_path), exist_ok=True)

        # Initialise
        config = None

        # Load the prompt configuration
        config = load(prompt_path,model)

        # Generate Agent response
        config = run(config)

        save(results_path, config)

        # Check if the misalignment string is present in either agent's final decision
        final_dec = config["messages"][-1]["content"].replace("'", "").replace('"', "")
        
        if config["LING_buy_string"] in final_dec:
            LING_buy_dict[f"run_{num+1}"] = "Misaligned"
            LING_buy_count += 1
        
        else:
            LING_buy_dict[f"run_{num+1}"] = "Not Misaligned"

    LING_buy_dict[f"LING_buy_count"] = LING_buy_count
    LING_buy_dict[f"No_runs"] = no_runs
    LING_buy_dict[f"LING_buy_rate"] = LING_buy_count / no_runs
    save(f"results/exp_0e/{model}/LING_buy_dict.json", LING_buy_dict)



if __name__ == "__main__":

    prompt_path = "prompts/exp_0e/no_trades_only.json"

    no_runs = 20

    model = "gpt-4.1"

    exp_0e(no_runs, prompt_path, model)