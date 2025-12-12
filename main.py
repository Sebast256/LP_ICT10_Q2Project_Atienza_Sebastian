from pysript import document

def compute_average(event):
    englishscore = float(document.getElementById("englishscore").value)
    sciencescore = float(document.getElementById("sciencescore").value)
    mathscore = float(document.getElementById("mathscore").value)
    socialstudiescore = float(document.getElementById("socialstudiesscore").value)
    ictscore = float(document.getElementById("ictscore").value)
    tlescore = float(document.getElementById("tlescore").value)

    
    average = (englishscore + sciencescore) (mathscore + socialstudiescore) (ictscore + tlescore) / 2
    
    if average >=75:
        result = "Yes"
    else:
        result = "No"


    document.getElementById("average").innerText = str(round(average, 2))
    document.getElementById("result").innerText = result