from django.shortcuts import render
import openai

openai.api_key = "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"

# Create your views here.
def chat(question):
        result = openai.Completion.create(engine="text-davinci-003",prompt=question,    max_tokens=1024,n=1,stop=None,temperature=0.5,)
        replay = result.choices[0].text
        return str(replay)

def home(request):
    if(request.method == 'POST'):
        res = chat(str(request.POST["question"]))

        return render(request,"index.html",{"name":res})
    else:
        return render(request,"index.html",{"name":"josh"})
    
