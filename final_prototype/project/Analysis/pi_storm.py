import subprocess
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz

def preprocess(data, target_column):
    """returns cleaned dataframe and targets"""
    data_clean = data.copy()
    targets = data_clean[target_column].unique()
    map_str_to_int = {name: n for n, name in enumerate(targets)}
    data_clean["Target"] = data_clean[target_column].replace(map_str_to_int)

    return (data_clean, targets)

def train_classifier(train_data, train_target):
    """returns a new model that can be used to make predictions"""
    # create a decision tree classifier
    wclf = DecisionTreeClassifier(min_samples_split=15, random_state=99)
    # train it on the training data / train classifier
    wclf.fit(train_data, train_target)

    return wclf

def visualize_tree(tree, feature_names):

    with open("visual.dot", 'w') as f:
        # writes a dot file 
        export_graphviz(tree, out_file=f, feature_names=feature_names)
    try:
        # generates a png file from the dot file above
        subprocess.check_call(["dot", "-Tpng", "visual.dot", "-o", "visual.png"])
    except:
        exit("Failed to generate a visual graph")

def display_labels(targets):
    print("0 :",targets[0])
    print("1 :",targets[1])
    print("2 :",targets[2])
    print("3 :",targets[3])

def ml():
    # import data set   
    data = pd.read_csv("weather_data.csv")
    print(data.head())

    # preprocess the data
    pp_data, targets = preprocess(data, "Weather Description")
    
    # just for visualization
    print("\n* targets *\n", targets, end="\n\n")
    features = list(pp_data.columns[:5])
    print("* features *\n", features, end="\n\n")
    print("=======preprocessed data=======\n")
    print("------------first five rows------------")
    print("* pp_data.head()", pp_data[["Target", "Weather Description"]].head(), sep="\n", end="\n\n")
    print("------------last five rows------------")
    print("* pp_data.head()", pp_data[["Target", "Weather Description"]].tail(), sep="\n", end="\n\n")

    p_target = pp_data["Target"]
    p_features = pp_data[features]

    idx_val = [1,491,5,493,7,495,9,6,498,394,500]
    # taking some data out of the dataset for testing
    test_target = p_target.loc[idx_val] 
    test_data = p_features.loc[idx_val]

    display_labels(targets)


    print("---Test Data's Target Value---")
    print("Note: row is off by two from the csv file")
    print("Row ","Target")
    print(test_target)

    # preparing data for training by removing test data
    train_target = p_target.drop(idx_val) 
    train_data = p_features.drop(idx_val)
    
    wclf = train_classifier(train_data, train_target)

    visualize_tree(wclf, features)
    # temp, humidity, pressure, blah 
    print(test_data)
    prediction = wclf.predict(test_data)
    print("\n---Actual Prediction---")
    print(prediction)


if __name__=="__main__":
    ml()


    