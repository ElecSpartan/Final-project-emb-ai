'''
Server using Flask 
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detection")
@app.route("/")
def render_website():
    '''
    main page
    '''
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detectorweb():
    '''
    Backend for the main function
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return " Invalid text! Please try again!."

    return (f"For the given statement, the system response is 'anger': {response['anger']}"
    f", 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']}"
    f" and 'sadness': {response['sadness']}."
    f"The dominant emotion is {response['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
