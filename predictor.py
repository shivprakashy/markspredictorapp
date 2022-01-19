import pickle, NumPy as np

def main():
    pass

def get_predicted_marks(hrs):
    model = None
    result = None
    with open("predictor_pickle", "rb") as f:
        model = pickle.load(f)
    result = model.predict([[hrs]])
    return int(result[0])

if __name__ == "__main__":
    main()
