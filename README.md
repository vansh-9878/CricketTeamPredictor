# CricketTeamPredictor

CricketTeamPredictor is a Python-based project designed to predict the playing XI of a cricket team based on a squad's performance data. The project uses web scraping, data processing, and a trained machine learning model to provide recommendations for team composition. The user provides a squad link from [www.espncricinfo.com](https://www.espncricinfo.com), and the program predicts the optimal combination of batters, bowlers, and allrounders.

---

## Features
- **Web Scraping**: Automatically scrapes squad details (batters, bowlers, allrounders) from an ESPN Cricinfo squad page.
- **Data Storage**: Stores player data in three separate CSV files: `batters.csv`, `bowlers.csv`, and `allrounders.csv`.
- **Player Ranking**: Calculates weighted scores for each player based on their statistics and assigns ranks.
- **Machine Learning**: A trained RandomForestClassifier model predicts the number of batters, bowlers, and allrounders needed in the playing XI.
- **Playing XI Recommendation**: Combines the prediction and ranking system to recommend the optimal playing XI.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vansh-9878/CricketTeamPredictor
   cd CricketTeamPredictor
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Run the main script:
   ```bash
   python main.py
   ```

2. When prompted, enter the squad link. Ensure the link is from (https://www.espncricinfo.com).

3. The program will:
   - Scrape the squad data from the provided link.
   - Store the data in three CSV files: `batters.csv`, `bowlers.csv`, and `allrounders.csv`.
   - Use the data to calculate weighted scores and ranks for each player.
   - Predict the optimal number of batters, bowlers, and all-rounders in the playing XI.
   - Recommend the final playing XI.

---

## Example Workflow

1. Provide a valid ESPN Cricinfo squad link:
   ```
   Enter the link for the squad: https://www.espncricinfo.com/series/australia-vs-india-2024-25-1426547/india-2nd-3rd-4th-and-5th-test-squad-1460697/series-squads
   ```

2. Output will include:
   - CSV files for player data.
   - Predicted team composition.
   - Suggested playing XI.

---

## Prerequisites
- Python 3.7 or higher
- Required libraries: BeautifulSoup, pandas, scikit-learn, numpy, requests

---

## Limitations
- The squad link must be valid and from ESPN Cricinfo.
- Predictions are based on the trained model and may not account for external factors like player injuries or weather conditions.

---

## Future Enhancements
- Support for format-specific predictions.
- Enhanced scraping for more detailed player statistics (Scraping data of the latest matches).
- Increased Accuracy for the ForestClassifier Model
- Improving user access by going beyond the ESPN link 

---

## License
This project is licensed under the GNU License. See the LICENSE file for details.

---

## Author
Vansh Arora (https://github.com/vansh-9878)

