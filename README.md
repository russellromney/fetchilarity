# fetchilarity

"Text similarity is so fetch"

This is similarity calculator for Fetch. 

---

## To use

There are three parts: the basic program that intakes pathnames, the Flask API, and the Dash web app.

#### Basic fetchilarity program. 

This is contained in `fetchilarity.py`

```
python fetchilarity.py
```

It will ask for two pathnames and spit out the similarity score of the two texts. The function it uses is located in `utilities.py`

#### Flask API

This is a basic Flask API with three endpoints:

```
python api.py
```

`http://localhost:5000/`: returns a message describing how to use it

`http://localhost:5000/api`: a POST endpoint that accepts a JSON payload like `{'text1':'a','text2':'b'}` and returns the similarity score for the two texts

`http://localhost:5000/api/raw`: a GET endpoint that accepts a simple URL like `.../api/raw/text1 body/text2 body` and returns the similarity score for the two texts. 


#### Dash web app

This is a simple web app. You input two texts and it shows the similarity score between them. Warning: this is addictive. 

```
python webapp.py
```

Live at `http://localhost:8050`


---
