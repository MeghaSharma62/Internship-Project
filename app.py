from flask import Flask,render_template
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
# import histogram as hist
df=pd.read_csv(r"C:\Users\megha.ai.sharma\Desktop\HTML\Students_Performance.csv")
df.columns=map(str.lower,df.columns)
df.columns=df.columns.str.replace(" ","_")
df["total_score"]=df["reading_score"]+df["math_score"]+df["writing_score"]
df["ethnicity"]=df["ethnicity"]=df["test_preparation_course"].str.replace("none","not completed")
# df.describe(include='all')
app = Flask(__name__)
# The return type must be a string, dict, list, tuple with headers or status,
@app.route("/gen")
def gender():
    group=df.groupby(["gender"])["total_score"].sum()
    if group["male"]>group["female"]:
        return "male"
    else:
        return render_template("gender.html")
if __name__=="__main__":
    app.run(debug=True)
    