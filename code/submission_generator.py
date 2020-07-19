from datetime import datetime
import pandas as pd

def generate_submission(predictions, name):
    date = datetime.now().strftime('%m-%d-%H_%M_%S')
    file = open("../submissions/" + name + "_" + date + ".csv", "w+")

    submit = pd.DataFrame()
    submit["Prediction"] = predictions
    submit["Id"] = submit.index + 1
    submit = submit[["Id", "Prediction"]]

    submit.to_csv(file, header=True, index=False, line_terminator='\n')
    