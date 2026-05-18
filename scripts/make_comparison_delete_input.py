from pathlib import Path
import pandas as pd
import argparse
import shutil


def parse_args():
    parser = argparse.ArgumentParser(
        description="Merge spatial comparison tables into one dataset"
    )

    parser.add_argument(
        "--input-dir",
        type=Path,
        required=True,
        help="Path to folder with experiment subfolders"
    )

    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
        help="Directory for final merged output"
    )

    return parser.parse_args()


def main():
    args = parse_args()

    # output folder
    out_dir = Path(f"../outputs/B_TASK_OUTPUT") / args.output_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    base_path = args.input_dir

    files = list(base_path.glob("*/spatial_comparison_table.csv"))

    print(f"Found files: {len(files)}")

    all_tables = []

    for f in files:
        df = pd.read_csv(f)

        folder = f.parent.name

        exp_id = int(folder.split("_")[1])
        site_id = int(folder.split("_")[3])

        df["exp_id"] = exp_id
        df["site_id"] = site_id

        all_tables.append(df)

    comparison_df = pd.concat(all_tables, ignore_index=True)

    out_file = out_dir / "spatial_comparison_ALL.csv"
    comparison_df.to_csv(out_file, index=False)

    print("Saved:", out_file)
    print("Shape:", comparison_df.shape)


    #DELETE ALL FILES INSIDE INPUT DIR
    shutil.rmtree(args.input_dir)
        


if __name__ == "__main__":
    main()