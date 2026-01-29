from pyscript import document

def compute_average(event):
    # Get the input values and convert to float
    score1 = float(document.getElementById("score1").value)
    score2 = float(document.getElementById("score2").value)
    score3 = float(document.getElementById("score3").value)
    score4 = float(document.getElementById("score4").value)

    # Compute average
    average = (score1 + score2 + score3 + score4) / 4

    # Determine pass/fail
    if average >= 75:
        result = "Yes"
    else:
        result = "No"

    # Display results
    document.getElementById("average").innerText = str(round(average, 2))
    document.getElementById("result").innerText = result

