from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Questions,Choice
from django.http import Http404
from django.template import loader
from django.urls import reverse
from django.db.models import F

def index(request):
    latest_question_list=Questions.objects.order_by("-pub_date")[:5]
    
    template=loader.get_template("polls/index.html")
    context={"latest_question_list":latest_question_list}
    """ return HttpResponse(template.render(context,request)) """
    return render(request,"polls/index.html",context)


def detail(request,question_id):
    """ try:
       question=Questions.objects.get(pk=question_id)
    except Questions.DoesNotExist:
       raise Http404("question does not exist") """
    question=get_object_or_404(Questions, pk=question_id)
    
    return render(request,"polls/details.html",{"question":question})


def results(request,question_id):
    """     reponse="you're loking at the result of question %s."
    return HttpResponse(reponse % question_id) """
    question=get_object_or_404(Questions,pk=question_id)
    return render(request,"polls/results.html",{"question":question})


def vote(request,question_id):
    question=get_object_or_404(Questions,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST["choice"])
    except (KeyError,Choice.DoesNotExist):
        return render(
            request,
            "polls/details.html",
            {
                "question":question,
                "error_message":"you didn't select a choice"
            },
        )
    else:
        selected_choice.votes=F("votes")+1
        selected_choice.save()
        

        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

