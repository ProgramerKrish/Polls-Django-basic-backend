User clicks "Vote"
      ↓
Browser sends POST request
      ↓
request.POST["choice"] = "1"
      ↓
vote(request, 2)
      ↓
Fetch Question(id=2)
      ↓
Fetch Choice(id=1, question_id=2)
      ↓
votes = votes + 1
      ↓
Database updated
      ↓
Redirect to results page
      ↓
results() view renders updated data
