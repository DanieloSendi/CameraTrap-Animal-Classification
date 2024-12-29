from pathlib import Path
import zipfile
import typer
from loguru import logger
from tqdm import tqdm

from src.config import EXTERNAL_DATA_DIR, RAW_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = EXTERNAL_DATA_DIR / "dataset.zip",
    output_path: Path = RAW_DATA_DIR,
    # ----------------------------------------------
):
    # ---- REPLACE THIS WITH YOUR OWN CODE ----
    """
    Extracts a ZIP file from the external directory to the raw directory.
    """
    logger.info(f"Processing dataset - extracting {input_path} to {output_path}...")
    
     # Check if the ZIP file exists
    if not input_path.exists():
        logger.error(f"The file {input_path} does not exist.")
        raise FileNotFoundError(f"File {input_path} not found.")
    
    # Extract the ZIP file with progress tracking
    try:
        with zipfile.ZipFile(input_path, 'r') as zip_ref:
            files = zip_ref.namelist()  # Get a list of all files in the archive
            logger.info(f"Found {len(files)} files to extract.")

            # Use tqdm to show progress bar
            for file in tqdm(files, desc="Extracting files"):
                zip_ref.extract(file, output_path)

        logger.success(f"Extraction of {input_path} completed successfully.")
    except zipfile.BadZipFile:
        logger.error(f"The file {input_path} is not a valid ZIP archive.")
        raise
    # -----------------------------------------


if __name__ == "__main__":
    app()
    