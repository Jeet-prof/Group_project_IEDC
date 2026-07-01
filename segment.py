import re

def segment(text):

    pattern=r"(Q\d+\.)"

    parts=re.split(pattern,text)

    answers=[]

    for i in range(1,len(parts),2):

        question=parts[i]

        answer=parts[i+1].strip()

        answers.append((question,answer))

    return answers